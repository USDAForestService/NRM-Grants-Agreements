import { Sequelize, Model, DataTypes, Optional } from "sequelize";
import sequelizeNoUpdateAttributes from "sequelize-noupdate-attributes";

const sequelize = new Sequelize(process.env.DATABASE_URL);
sequelizeNoUpdateAttributes(sequelize);

enum Status {
  None = "---",
  One = "01",
  Two = "02",
}

enum AppSubmissionType {
  New = "NEW",
  Application = "Application",
  Preapplication = "Preapplication",
  NonConstructionApplication = "NON-CONSTRUCTION APPLICATION",
  NonConstructionPreApplication = "NON-CONSTRUCTION PRE-APPLICATION",
}

interface GrantAttributes {
  cn: string;
  projTitle: string;
  projStatus: Status;
  appSubmissionType: AppSubmissionType;
}

interface GrantCreationAttributes extends Optional<Grant, "cn"> {}

class Grant
  extends Model<GrantAttributes, GrantCreationAttributes>
  implements GrantAttributes
{
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
);

export default Grant;
