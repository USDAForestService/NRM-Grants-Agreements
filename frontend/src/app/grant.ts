enum Status {
  None = '---',
  One = '01',
  Two = '02',
}

enum AppSubmissionType {
  New = 'NEW',
  Application = 'Application',
  Preapplication = 'Preapplication',
  NonConstructionApplication = 'NON-CONSTRUCTION APPLICATION',
  NonConstructionPreApplication = 'NON-CONSTRUCTION PRE-APPLICATION',
}

export interface Grant {
  cn: string;
  projTitle: string;
  projStatus: Status;
  appSubmissionType: AppSubmissionType;
}
