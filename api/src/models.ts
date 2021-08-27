import { Sequelize, Model, DataTypes, Optional } from "sequelize";
import sequelizeNoUpdateAttributes from "sequelize-noupdate-attributes";

import {
  AbChoices,
  BooleanChoices,
  FedIdRegionChoices,
  FedIdTypeChoices,
  ApplicationTypeChoices,
  ApplicationSubmissionTypeChoices,
  CfdaChoices,
  NoteTypeChoices,
  ProgramResponsibilityTypeChoices,
  ResearchTypeChoices,
  RwuChoices,
  ScienceCodeChoices,
  StatusChoices,
  WpapStatusChoices,
} from "./choices";

const sequelize = new Sequelize(process.env.DATABASE_URL, { logging: false });
/**
 * @todo Fix this, the model should be allowing noUpdate attributes.
 */
sequelizeNoUpdateAttributes(sequelize);

interface GrantAttributes {
  cn: string;
  projTitle: string;
  projStatus: AbChoices | null;
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
  fedIdFy: number | null;
  fedIdType: FedIdTypeChoices | null;
  fedIdAgency: string;
  fedIdRegion: FedIdRegionChoices | null;
  fedIdUnit: string;
  fedIdSubunit: string;
  fedIdSeq: number;
  projType: AbChoices | null;
  projDesc: string;
  projReceivedDt: Date;
  projExecutionDt: Date;
  projStartDt: Date;
  projObligationDt: Date;
  projExpirationDt: Date;
  projCloseDt: Date;
  projCancellationDt: Date;
  projRwu: RwuChoices | null;
  projCfdaNo: CfdaChoices | null;
  projScienceCd: ScienceCodeChoices | null;
  projectCongressionalDistrict: string;
  dateMailed: Date;
  dateSigned: Date;
  comments: string;
  extramuralInd: BooleanChoices | null;
  researchType: ResearchTypeChoices | null;
  journalInd: string;
  modNumber: number;
  origFedId: string;
  masterFedId: string;
  aopInd: BooleanChoices | null;
  geoType: string;
  managingStateCounty: string;
  areasAffected: string;
  ffin: string;
  stateIdentifier: string;
  stateEoCode: BooleanChoices | null;
  stateEoDate: Date;
  fedEstFund: number;
  applicantEstFund: number;
  stateEstFund: number;
  localEstFund: number;
  piEstFund: number;
  othEstFund: number;
  rerouteFrom: string;
  rerouteDate: Date;
  certificationDate: Date;
  ffisDocId: string;
  applicantName: string;
  internationalActInd: BooleanChoices | null;
  advanceAllowedInd: BooleanChoices | null;
  authorityApproval: BooleanChoices | null;
  authority: BooleanChoices | null;
  format: BooleanChoices | null;
  otherApproval: BooleanChoices | null;
  masterAgreementInd: BooleanChoices | null;
  programResponsibilityType: ProgramResponsibilityTypeChoices | null;
  wpapStatus: WpapStatusChoices | null;
  wpapStatusDate: Date;
  cooperatorAgreementNumber: string;
  gid: string;
  adminOpen: string;
  lastUpdate: Date;
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
  public fedIdFy!: number | null;
  public fedIdType!: FedIdTypeChoices | null;
  public fedIdAgency!: string;
  public fedIdRegion!: FedIdRegionChoices | null;
  public fedIdUnit!: string;
  public fedIdSubunit!: string;
  public fedIdSeq!: number;
  public projType!: AbChoices | null;
  public projDesc!: string;
  public projReceivedDt!: Date;
  public projExecutionDt!: Date;
  public projStartDt!: Date;
  public projObligationDt!: Date;
  public projExpirationDt!: Date;
  public projCloseDt!: Date;
  public projCancellationDt!: Date;
  public projRwu!: RwuChoices | null;
  public projCfdaNo!: CfdaChoices | null;
  public projScienceCd!: ScienceCodeChoices | null;
  public projectCongressionalDistrict!: string;
  public dateMailed!: Date;
  public dateSigned!: Date;
  public comments!: string;
  public extramuralInd!: BooleanChoices | null;
  public researchType!: ResearchTypeChoices | null;
  public journalInd!: string;
  public modNumber!: number;
  public origFedId!: string;
  public masterFedId!: string;
  public aopInd!: BooleanChoices | null;
  public geoType!: string;
  public managingStateCounty!: string;
  public areasAffected!: string;
  public ffin!: string;
  public stateIdentifier!: string;
  public stateEoCode!: BooleanChoices | null;
  public stateEoDate!: Date;
  public fedEstFund!: number;
  public applicantEstFund!: number;
  public stateEstFund!: number;
  public localEstFund!: number;
  public piEstFund!: number;
  public othEstFund!: number;
  public rerouteFrom!: string;
  public rerouteDate!: Date;
  public certificationDate!: Date;
  public ffisDocId!: string;
  public applicantName!: string;
  public internationalActInd!: BooleanChoices | null;
  public advanceAllowedInd!: BooleanChoices | null;
  public authorityApproval!: BooleanChoices | null;
  public authority!: BooleanChoices | null;
  public format!: BooleanChoices | null;
  public otherApproval!: BooleanChoices | null;
  public masterAgreementInd!: BooleanChoices | null;
  public programResponsibilityType!: ProgramResponsibilityTypeChoices | null;
  public wpapStatus!: WpapStatusChoices | null;
  public wpapStatusDate!: Date;
  public cooperatorAgreementNumber!: string;
  public gid!: string;
  public adminOpen!: string;
  public lastUpdate!: Date;
}

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
      defaultValue: "Other",
    },
    appSubmissionType: {
      type: new DataTypes.STRING(100),
      allowNull: false,
      validate: { notEmpty: true },
      defaultValue: "Other",
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
      defaultValue: "N",
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
      defaultValue: "N",
    },
    status: {
      type: new DataTypes.STRING(40),
      allowNull: false,
      // noUpdate: { readOnly: true },
      validate: { notEmpty: true },
      defaultValue: "New-Application",
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
    fedIdFy: {
      type: new DataTypes.STRING(4),
      validate: { min: 1949, max: new Date().getFullYear() + 1 },
    },
    fedIdType: {
      type: new DataTypes.STRING(2),
    },
    fedIdAgency: {
      type: new DataTypes.STRING(2),
      defaultValue: "11",
    },
    fedIdRegion: {
      type: new DataTypes.STRING(2),
    },
    fedIdUnit: {
      type: new DataTypes.STRING(2),
    },
    fedIdSubunit: {
      type: new DataTypes.STRING(2),
    },
    fedIdSeq: {
      type: new DataTypes.DECIMAL(3, 0),
    },
    projType: {
      type: new DataTypes.STRING(3),
    },
    projDesc: {
      type: new DataTypes.STRING(2000),
    },
    projReceivedDt: {
      type: new DataTypes.DATE(),
    },
    projExecutionDt: {
      type: new DataTypes.DATE(),
    },
    projStartDt: {
      type: new DataTypes.DATE(),
    },
    projObligationDt: {
      type: new DataTypes.DATE(),
    },
    projExpirationDt: {
      type: new DataTypes.DATE(),
    },
    projCloseDt: {
      type: new DataTypes.DATE(),
    },
    projCancellationDt: {
      type: new DataTypes.DATE(),
    },
    projRwu: {
      type: new DataTypes.STRING(10),
    },
    projCfdaNo: {
      type: new DataTypes.STRING(40),
    },
    projScienceCd: {
      type: new DataTypes.STRING(3),
    },
    projectCongressionalDistrict: {
      type: new DataTypes.STRING(40),
    },
    dateMailed: {
      type: new DataTypes.DATE(),
    },
    dateSigned: {
      type: new DataTypes.DATE(),
    },
    comments: {
      type: new DataTypes.STRING(2000),
    },
    extramuralInd: {
      type: new DataTypes.STRING(1),
      validate: { notEmpty: true },
      defaultValue: "N",
    },
    researchType: {
      type: new DataTypes.STRING(1),
    },
    journalInd: {
      type: new DataTypes.STRING(1),
    },
    modNumber: {
      type: new DataTypes.DECIMAL(3, 0),
    },
    origFedId: {
      type: new DataTypes.STRING(120),
      allowNull: false,
      validate: { notEmpty: true },
    },
    masterFedId: {
      type: new DataTypes.STRING(120),
    },
    aopInd: {
      type: new DataTypes.STRING(1),
      validate: { notEmpty: true },
      defaultValue: "N",
    },
    geoType: {
      type: new DataTypes.STRING(2),
    },
    managingStateCounty: {
      type: new DataTypes.STRING(240),
    },
    areasAffected: {
      type: new DataTypes.STRING(200),
      field: "areas_effected",
    },
    ffin: {
      type: new DataTypes.STRING(40),
    },
    stateIdentifier: {
      type: new DataTypes.STRING(40),
    },
    stateEoCode: {
      type: new DataTypes.STRING(1),
      defaultValue: "N",
    },
    stateEoDate: {
      type: new DataTypes.DATE(),
    },
    fedEstFund: {
      type: new DataTypes.DECIMAL(12, 2),
    },
    applicantEstFund: {
      type: new DataTypes.DECIMAL(12, 2),
    },
    stateEstFund: {
      type: new DataTypes.DECIMAL(12, 2),
    },
    localEstFund: {
      type: new DataTypes.DECIMAL(12, 2),
    },
    piEstFund: {
      type: new DataTypes.DECIMAL(12, 2),
    },
    othEstFund: {
      type: new DataTypes.DECIMAL(12, 2),
    },
    rerouteFrom: {
      type: new DataTypes.STRING(10),
    },
    rerouteDate: {
      type: new DataTypes.DATE(),
    },
    certificationDate: {
      type: new DataTypes.DATE(),
      field: "certificaion_date",
    },
    ffisDocId: {
      type: new DataTypes.STRING(11),
    },
    applicantName: {
      type: new DataTypes.STRING(200),
    },
    internationalActInd: {
      type: new DataTypes.STRING(1),
      validate: { notEmpty: true },
      defaultValue: "N",
    },
    advanceAllowedInd: {
      type: new DataTypes.STRING(1),
      validate: { notEmpty: true },
      defaultValue: "N",
    },
    authorityApproval: {
      type: new DataTypes.STRING(1),
      defaultValue: "N",
    },
    authority: {
      type: new DataTypes.STRING(1),
      defaultValue: "N",
    },
    format: {
      type: new DataTypes.STRING(1),
      defaultValue: "N",
    },
    otherApproval: {
      type: new DataTypes.STRING(1),
      defaultValue: "N",
    },
    masterAgreementInd: {
      type: new DataTypes.STRING(1),
      // noUpdate: { readOnly: true },
      defaultValue: "N",
    },
    programResponsibilityType: {
      type: new DataTypes.STRING(30),
      field: "progrm_responsibility_type",
      validate: { notEmpty: true },
    },
    wpapStatus: {
      type: new DataTypes.STRING(40),
      field: "wppp_status",
      // noUpdate: { readOnly: true },
    },
    wpapStatusDate: {
      type: new DataTypes.DATE(),
      field: "wppp_status_date",
      // noUpdate: { readOnly: true },
    },
    cooperatorAgreementNumber: {
      type: new DataTypes.STRING(34),
    },
    gid: {
      type: new DataTypes.STRING(),
    },
    adminOpen: {
      type: new DataTypes.STRING(1),
    },
    /**
     * @todo Determine why there is both a modifiedDate and lastUpdate column,
     *       and set both appropriately.
     */
    lastUpdate: {
      type: new DataTypes.DATE(),
      allowNull: false,
      validate: { notEmpty: true },
    },
  },
  {
    sequelize,
    underscored: true,
    timestamps: true,
    createdAt: "createdDate",
    updatedAt: "modifiedDate",
    // updatedAt: 'lastUpdate',
    tableName: "ii_grants",
  }
);

export default Grant;
