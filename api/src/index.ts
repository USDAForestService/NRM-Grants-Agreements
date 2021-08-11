import express, { Request, Response, NextFunction } from 'express';
import {
  Sequelize,
  Model,
  DataTypes,
  Optional,
} from 'sequelize';
import dotenv from 'dotenv';

dotenv.config()


console.log("----- DATABASE_URL -----")
console.log(process.env.DATABASE_URL)

const sequelize = new Sequelize(process.env.DATABASE_URL);

const app  = express();
const port = 3000;

/**
 * @todo Set using environment variables for security hardening.
 */
app.use(function(req, res, next) {
  res.setHeader('Access-Control-Allow-Origin',  '*')
  res.setHeader('Access-Control-Allow-Methods', '*')
  res.setHeader('Access-Control-Allow-Headers', '*')
  next();
});

enum Status {
  None = "---",
  One = "01",
  Two = "02",
}

enum AppSubmissionType {
  New = 'NEW',
  Application = 'Application',
  Preapplication = 'Preapplication',
  NonConstructionApplication = 'NON-CONSTRUCTION APPLICATION',
  NonConstructionPreApplication = 'NON-CONSTRUCTION PRE-APPLICATION',
}

interface GrantAttributes {
  cn: string;
  projTitle: string;
  projStatus: Status;
  appSubmissionType: AppSubmissionType;
}

interface GrantCreationAttributes extends Optional<Grant, "cn">{}

class Grant extends Model<GrantAttributes, GrantCreationAttributes>
  implements GrantAttributes {

  public cn!: string;
  public projTitle!: string;
  public projStatus!: Status | null;
  public appSubmissionType!: AppSubmissionType;
}

Grant.init(
  {
    /**
      Proposal ID,
      editable=False,
      db_index=True,
      help_text="A system-generated number used to identify the proposal before an agreement number is assigned or the instrument is executed.",
    */
    cn: {
      type: new DataTypes.STRING(34),
      autoIncrement: true,
      primaryKey: true,
    },
    projTitle: {
      type: new DataTypes.STRING(200),
      allowNull: false,
    },
    projStatus: {
      type: new DataTypes.STRING(15),
      allowNull: true,
    },
    appSubmissionType: {
      type: new DataTypes.STRING(30),
      allowNull: false,
    },
  },
  {
    sequelize,
    underscored: true,
    timestamps: false,
    tableName: "ii_grants",
  }
)

const awaitErrorHandlerFactory = (middleware: any) => {
  return async (request: Request, response: Response, next: NextFunction) => {
    try {
      await middleware(request, response, next);
    } catch (err) {
      next(err);
    }
  }
}

/**
* @todo Set the JSON to be { data: grants } and have Angular read the data
*/
app.get(
  '/grants',
  awaitErrorHandlerFactory(async (request: Request, response: Response, next: NextFunction) => {
    let grants: Grant[] = await Grant.findAll({ limit: 10 });
    return response.status(200).json(grants);
  })
);

/**
 * @environment development
 * When deployed, the lambda.js file only uses the exported app and
 * doesn't run app.listen.
 */
app.listen(port, () => {
  console.log(`NRM G&A API running on port ${port}.`)
});

module.exports = app;
