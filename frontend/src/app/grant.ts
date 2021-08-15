type AbChoices = '----' | '01' | '02';
type ApplicationTypeChoices =
  | 'New'
  | 'Continuation'
  | 'Revision A - Increase Award'
  | 'Revision B - Decrease Award'
  | 'Revision C - Increase Duration'
  | 'Revision D - Decrease Duration'
  | 'Other';
type ApplicationSubmissionTypeChoices =
  | 'New'
  | 'Application'
  | 'Pre-application'
  | 'Non-construction Pre-application'
  | 'Non-construction Application'
  | 'Construction Pre-application'
  | 'Construction Application'
  | 'Mou'
  | 'Other'
  | '8/1/2004NON-CONSTRUCTION APPLICATION'
  | '5/1/2005NON-CONSTRUCTION APPLICATION';
type BooleanChoices = 'Y' | 'N';
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

export interface Grant {
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
