import { Sequelize, Model, DataTypes, Optional } from "sequelize";
import sequelizeNoUpdateAttributes from "sequelize-noupdate-attributes";

const sequelize = new Sequelize(process.env.DATABASE_URL);
/**
 * @todo Fix this, the model should be allowing noUpdate attributes.
 */
sequelizeNoUpdateAttributes(sequelize);

type AbChoices = "----" | "01" | "02";
type ApplicationTypeChoices =
  | "New"
  | "Continuation"
  | "Revision A - Increase Award"
  | "Revision B - Decrease Award"
  | "Revision C - Increase Duration"
  | "Revision D - Decrease Duration"
  | "Other";
type ApplicationSubmissionTypeChoices =
  | "New"
  | "Application"
  | "Pre-application"
  | "Non-construction Pre-application"
  | "Non-construction Application"
  | "Construction Pre-application"
  | "Construction Application"
  | "Mou"
  | "Other"
  | "8/1/2004NON-CONSTRUCTION APPLICATION"
  | "5/1/2005NON-CONSTRUCTION APPLICATION";
type BooleanChoices = "Y" | "N";
type StatusChoices =
  | "AGREEMENT-ACTION"
  | "NEW-APPLICATION"
  | "APP-ACCEPTED"
  | "APP-APPROVED"
  | "APP-PGM REJECTED"
  | "APP-RECEIVED"
  | "APP-REJECTED"
  | "GA-CANCELLED"
  | "GA-EXECUTED"
  | "GA-PENDING"
  | "GA-TERMINATED";

interface GrantAttributes {
  cn: string;
  projTitle: string;
  projStatus: AbChoices;
  applicationId: string;
  applicationType: ApplicationTypeChoices;
  appSubmissionType: ApplicationSubmissionTypeChoices;
  appSubmitDate: Date;
  appReceivedDate: Date;
  hhsPaymentInd: BooleanChoices;
  proposedStartDate: Date;
  proposedEndDate: Date;
  lockedInd: BooleanChoices;
  status: StatusChoices;
  statusDate: Date;
  createdBy: string;
  createdDate: Date;
  createdInInstance: number;
  modifiedBy: string;
  modifiedDate: Date;
  modifiedInInstance: number;
}

interface GrantCreationAttributes extends Optional<Grant, "cn"> {}

class Grant
  extends Model<GrantAttributes, GrantCreationAttributes>
  implements GrantAttributes
{
  public cn!: string;
  public projTitle!: string;
  public projStatus!: AbChoices | null;
  public applicationId!: string;
  public applicationType!: ApplicationTypeChoices;
  public appSubmissionType!: ApplicationSubmissionTypeChoices;
  public appSubmitDate!: Date;
  public appReceivedDate!: Date;
  public hhsPaymentInd!: BooleanChoices;
  public proposedStartDate!: Date;
  public proposedEndDate!: Date;
  public lockedInd!: BooleanChoices;
  public status!: StatusChoices;
  public statusDate!: Date;
  public createdBy!: string;
  public createdDate!: Date;
  public createdInInstance!: number;
  public modifiedBy!: string;
  public modifiedDate!: Date;
  public modifiedInInstance!: number;
}

/**
 * When copying from the spreadsheet, remember to:
 * - [ ] Comment out "noUpdate" lines (need to fix this, noUpdate blocks should be working)
 * - [ ] Remove all `auto_now*` and `choices` lines.
 */
Grant.init(
  {
    cn: {
      type: new DataTypes.STRING(34),
      allowNull: false,
      // noUpdate: { readOnly: true },
      validate: { notEmpty: true },
      autoIncrement: true,
      primaryKey: true,
    },
    projTitle: {
      type: new DataTypes.STRING(200),
      allowNull: false,
      validate: { notEmpty: true },
    },
    projStatus: {
      type: new DataTypes.STRING(15),
    },
    applicationId: {
      type: new DataTypes.STRING(34),
      allowNull: false,
      // noUpdate: { readOnly: true },
      validate: { notEmpty: true },
    },
    applicationType: {
      type: new DataTypes.STRING(30),
      allowNull: false,
      validate: { notEmpty: true },
    },
    appSubmissionType: {
      type: new DataTypes.STRING(100),
      allowNull: false,
      validate: { notEmpty: true },
    },
    appSubmitDate: {
      type: new DataTypes.DATE(),
      allowNull: false,
      validate: { notEmpty: true },
    },
    appReceivedDate: {
      type: new DataTypes.DATE(),
      allowNull: false,
      validate: { notEmpty: true },
    },
    hhsPaymentInd: {
      type: new DataTypes.STRING(1),
      allowNull: false,
      // noUpdate: { readOnly: true },
      validate: { notEmpty: true },
    },
    proposedStartDate: {
      type: new DataTypes.DATE(),
      allowNull: false,
      validate: { notEmpty: true },
    },
    proposedEndDate: {
      type: new DataTypes.DATE(),
      allowNull: false,
      validate: { notEmpty: true },
    },
    lockedInd: {
      type: new DataTypes.STRING(1),
      allowNull: false,
      // noUpdate: { readOnly: true },
      validate: { notEmpty: true },
    },
    status: {
      type: new DataTypes.STRING(40),
      allowNull: false,
      // noUpdate: { readOnly: true },
      validate: { notEmpty: true },
    },
    statusDate: {
      type: new DataTypes.DATE(),
      allowNull: false,
      validate: { notEmpty: true },
    },
    createdBy: {
      type: new DataTypes.STRING(30),
      allowNull: false,
      // noUpdate: { readOnly: true },
      validate: { notEmpty: true },
    },
    createdDate: {
      type: new DataTypes.DATE(),
      allowNull: false,
      validate: { notEmpty: true },
    },
    createdInInstance: {
      type: new DataTypes.DECIMAL(6, 0),
      allowNull: false,
      // noUpdate: { readOnly: true },
      validate: { notEmpty: true },
    },
    modifiedBy: {
      type: new DataTypes.STRING(30),
    },
    modifiedDate: {
      type: new DataTypes.DATE(),
    },
    modifiedInInstance: {
      type: new DataTypes.DECIMAL(6, 0),
      // noUpdate: { readOnly: true },
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
