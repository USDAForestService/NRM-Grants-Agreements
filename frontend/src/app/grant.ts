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

type CdfaChoices = string | null;
type FedIdRegionChoices = string | null;
type FedIdTypeChoices = string | null;
type ProgramResponsibilityTypeChoices = string | null;
type ResearchTypeChoices = string | null;
type RwuChoices = string | null;
type ScienceCodeChoices = string | null;
type WpapStatusChoices = string | null;
type YearChoices = string | null;

export interface Grant {
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
  fedIdFy: YearChoices | null;
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
  projCfdaNo: CdfaChoices | null;
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
