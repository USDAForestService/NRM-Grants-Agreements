type AbChoices = '----' | '01' | '02';

type BooleanChoices = 'Y' | 'N';

type FedIdRegionChoices =
  | '1'
  | '2'
  | '3'
  | '4'
  | '5'
  | '6'
  | '7'
  | '8'
  | '9'
  | '10'
  | '11'
  | '12'
  | '13'
  | '15'
  | '16'
  | '22'
  | '23'
  | '24'
  | '25'
  | '26'
  | '27'
  | '33'
  | '42';

type FedIdTypeChoices =
  | 'CA'
  | 'CO'
  | 'CR'
  | 'CS'
  | 'DG'
  | 'DP'
  | 'FA'
  | 'FI'
  | 'FO'
  | 'FP'
  | 'GN'
  | 'IA'
  | 'IC'
  | 'IG'
  | 'IJ'
  | 'JV'
  | 'LE'
  | 'LI'
  | 'MU'
  | 'OR'
  | 'PA'
  | 'RD'
  | 'RO'
  | 'RU'
  | 'SA'
  | 'SU'
  | 'TR';

type ApplicationTypeChoices =
  | 'Initial'
  | 'NEW'
  | 'CONTINUATION'
  | 'REVISION A-INCREASE AWARD'
  | 'REVISION B-DECREASE AWARD'
  | 'REVISION C-INCREASE AWARD'
  | 'REVISION D-DECREASE AWARD'
  | 'OTHER';

type ApplicationSubmissionTypeChoices =
  | 'NEW'
  | 'Application'
  | 'Preapplication'
  | 'NON-CONSTRUCTION PRE-APPLICATION'
  | 'NON-CONSTRUCTION APPLICATION'
  | 'CONSTRUCTION PRE-APPLICATION'
  | 'CONSTRUCTION APPLICATION'
  | 'MOU'
  | 'OTHER'
  | '8/1/2004NON-CONSTRUCTION APPLICATION'
  | '5/1/2005NON-CONSTRUCTION APPLICATION'
  | "Non-construction'"
  | "NON-Construction'"
  | '%';

type CfdaChoices =
  | '10.652'
  | '10.664'
  | '10.665'
  | '10.666'
  | '10.67'
  | '10.671'
  | '10.672'
  | '10.673'
  | '10.674'
  | '10.675'
  | '10.676'
  | '10.677'
  | '10.678'
  | '10.679'
  | '10.681'
  | '10.682'
  | '10.683'
  | '10.684'
  | '10.685'
  | '10.686'
  | '10.689'
  | '10.69'
  | '10.691'
  | '10.692'
  | '10.693'
  | '10.694';

type NoteTypeChoices =
  | 'AGREEMENT'
  | 'COMMITMENT'
  | 'OBLIGATION'
  | 'PAYMENT'
  | 'MODIFICATION'
  | 'OTHER';

type ProgramResponsibilityTypeChoices =
  | 'INCOMING FUNDING AGREEMENT'
  | 'NON-CASH AGREEMENT'
  | 'OUTGOING FUNDING AGREEMENT';

type ResearchTypeChoices = 'A' | 'B' | 'D' | 'N';

type RwuChoices =
  | 'None'
  | 'FPL-4501'
  | 'FPL-4502'
  | 'FPL-4701'
  | 'FPL-4703'
  | 'FPL-4706'
  | 'FPL-4707'
  | 'FPL-4709'
  | 'FPL-4710'
  | 'FPL-4712'
  | 'FPL-4714'
  | 'FPL-4716'
  | 'FPL-4719'
  | 'FPL-4722'
  | 'FPL-4723'
  | 'FPL-4724'
  | 'FPL-4725'
  | 'FPL-4851'
  | 'IITF-4151'
  | 'INT-4151'
  | 'INT-4153'
  | 'INT-4154'
  | 'INT-5201'
  | 'INT-4202'
  | 'INT-4203'
  | 'INT-4251'
  | 'INT-4252'
  | 'INT-4301'
  | 'INT-4302'
  | 'INT-4401'
  | 'INT-4403'
  | 'INT-4404'
  | 'INT-4501'
  | 'INT-4551'
  | 'INT-4702'
  | 'INT-4801'
  | 'INT-4802'
  | 'INT-4901'
  | 'NC-4108'
  | 'NC-4152'
  | 'NC-4153'
  | 'NC-4154'
  | 'NC-4155'
  | ''
  | 'NC-4157'
  | 'NC-4158'
  | 'NC-4159'
  | 'NC-4351'
  | 'NC-4401'
  | 'NC-4455'
  | 'NC-4501'
  | 'NC-4502'
  | 'NC-4509'
  | 'NC-4702'
  | 'NC-4801'
  | 'NC-4803'
  | 'NC-4804'
  | 'NC-4902'
  | 'NE-4103'
  | 'NE-4104'
  | 'NE-4152'
  | 'NE-4153'
  | 'NE-4155'
  | 'NE-4251'
  | 'NE-4252'
  | 'NE-4352'
  | 'NE-4353'
  | 'NE-4454'
  | 'NE-4455'
  | 'NE-450'
  | 'NE-4501'
  | 'NE-4502'
  | 'NE-4505'
  | 'NE-4557'
  | 'NE-4558'
  | 'NE-4701'
  | 'NE-4751'
  | 'NE-4801'
  | 'NE-4803'
  | 'NE-4805'
  | 'NE-4952'
  | 'RM-4151'
  | 'RM-4152'
  | 'RM-4201'
  | 'RM-4251'
  | 'RM-4252'
  | 'RM-4301'
  | 'RM-4302'
  | 'RM-4351'
  | 'RM-4352'
  | 'RM-4451'
  | 'RM-4452'
  | 'RM-4551'
  | 'RM-4651'
  | 'RM-4652'
  | 'RM-4653'
  | 'RM-4802'
  | 'RM-4803'
  | 'RM-4851'
  | 'RM-4852'
  | 'RM-4853'
  | 'RMRS-4151'
  | 'RMRS-4152'
  | 'RMRS-4155'
  | 'RMRS-4156'
  | 'RMRS-4201'
  | 'RMRS-4251'
  | 'RMRS-4252'
  | 'RMRS-4254'
  | 'RMRS-4301'
  | 'RMRS-4302'
  | 'RMRS-4351'
  | 'RMRS-4352'
  | 'RMRS-4353'
  | 'RMRS-4401'
  | 'RMRS-4403'
  | 'RMRS-4404'
  | 'RMRS-4451'
  | 'RMRS-4501'
  | 'RMRS-4551'
  | 'RMRS-4552'
  | 'RMRS-4651'
  | 'RMRS-4652'
  | 'RMRS-4653'
  | 'RMRS-4654'
  | 'RMRS-4655'
  | 'RMRS-4702'
  | 'RMRS-4801'
  | 'RMRS-4802'
  | 'RMRS-4804'
  | 'RMRS-4851'
  | 'RMRS-4852'
  | 'RMRS-4853'
  | 'RMRS-4901'
  | 'PNW-64'
  | 'PNW-4163'
  | 'PNW-4166'
  | 'PNW-4261'
  | 'PNW-4362'
  | 'PNW-4577'
  | 'PNW-4865'
  | 'PNW-4869'
  | 'PNW-4103'
  | 'PSW-4154'
  | 'PSW-4155'
  | 'PSW-4202'
  | 'PSW-4251'
  | 'PSW-4351'
  | 'PSW-4401'
  | 'PSW-4402'
  | 'PSW-4403'
  | 'PSW-4451'
  | 'PSW-4502'
  | 'PSW-4651'
  | ''
  | 'PSW-4902'
  | 'PSW-4952'
  | 'SRS-4101'
  | 'SRS-4103'
  | 'SRS-4104'
  | 'SRS-4105'
  | 'SRS-4106'
  | 'SRS-4111'
  | 'SRS-4153'
  | 'SRS-4154'
  | 'SRS-4155'
  | 'SRS-420'
  | 'SRS-4201'
  | 'SRS-4202'
  | 'SRS-4251'
  | 'SRS-4351'
  | 'SRS-4501'
  | 'SRS-4502'
  | 'SRS-4505'
  | 'SRS-4701'
  | 'SRS-4702'
  | 'SRS-4703'
  | 'SRS-4801'
  | 'SRS-4802'
  | 'SRS-4803'
  | 'SRS-4851'
  | 'SRS-4852'
  | 'SRS-4901'
  | 'SRS-4901';

type ScienceCodeChoices =
  | '12'
  | '21'
  | '22'
  | '31'
  | '32'
  | '43'
  | '49'
  | '51'
  | '54'
  | '55'
  | '71'
  | '72'
  | '76'
  | '79';

type StatusChoices =
  | 'AGREEMENT-ACTION'
  | 'NEW-APPLICATION'
  | 'APP-ACCEPTED'
  | 'APP-APPROVED'
  | 'APP-PGM REJECTED'
  | 'APP-RECEIVED'
  | 'APP-REJECTED'
  | 'GA-CANCELLED'
  | 'GA-EXECUTED'
  | 'GA-PENDING'
  | 'GA-TERMINATED';

type WpapStatusChoices =
  | 'Awaiting Documentation'
  | 'Executed- Active'
  | 'G&A Closed'
  | 'G&A Closeout in process'
  | 'G&A Reviewing'
  | 'New'
  | 'Out for Signature'
  | 'Pending ASC Action';

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
