import datetime

# These could use a better name
AB_CHOICES = (("", "----"), ("01", "01"), ("02", "02"))

# Since the legacy DB didn't treat booleans as booleans,
# we're trying to clean up. Really, they need to be updated/migrated.
BOOL_CHOICES = (("Y", "Yes"), ("N", "No"))

regions = [
    " ",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "15",
    "16",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "33",
    "42",
]
FED_ID_REGION_CHOICES = [(r, r) for r in regions]

FED_ID_TYPE_CHOICES = (
    (" ", " "),
    ("CA", "CA"),
    ("CO", "CO"),
    ("CR", "CR"),
    ("CS", "CS"),
    ("DG", "DG"),
    ("DP", "DP"),
    ("FA", "FA"),
    ("FI", "FI"),
    ("FO", "FO"),
    ("FP", "FP"),
    ("GN", "GN"),
    ("IA", "IA"),
    ("IC", "IC"),
    ("IG", "IG"),
    ("IJ", "IJ"),
    ("JV", "JV"),
    ("LE", "LE"),
    ("LI", "LI"),
    ("MU", "MU"),
    ("OR", "OR"),
    ("PA", "PA"),
    ("RD", "RD"),
    ("RO", "RO"),
    ("RU", "RU"),
    ("SA", "SA"),
    ("SU", "SU"),
    ("TR", "TR"),
)
APPLICATION_TYPE_CHOICES = (
    ("Initial", "Initial"),
    ("CONTINUATION", "Continuation"),
    ("NEW", "New"),
    ("OTHER", "Other"),
    ("REVISION A-INCREASE AWARD", "Revision A - Increase Award"),
    ("REVISION C-INCREASE AWARD", "Revision C - Increase Duration"),
)

APP_SUBMISSION_TYPE_CHOICES = (
    ("NEW", "New"),
    ("Application", "Application"),
    ("Preapplication", "Pre-application"),
    ("NON-CONSTRUCTION PRE-APPLICATION", "Non-construction Pre-application"),
    ("NON-CONSTRUCTION APPLICATION", "Non-construction Application"),
    # ('Non-construction', "Non-Construction"), # In the DB, but probably needs to be normalized with the above.
    # ('NON-Construction', "Non-Construction"), # In the DB, but probably needs to be normalized with the above.
    ("CONSTRUCTION PRE-APPLICATION", "Construction Pre-application"),
    ("CONSTRUCTION APPLICATION", "Construction Application"),
    ("MOU", "Mou"),
    ("OTHER", "Other"),
    (
        "8/1/2004NON-CONSTRUCTION APPLICATION",
        "8/1/2004NON-CONSTRUCTION APPLICATION",
    ),  # In the database, but probably not valid
    (
        "5/1/2005NON-CONSTRUCTION APPLICATION",
        "5/1/2005NON-CONSTRUCTION APPLICATION",
    ),  # In the database, but probably not valid
    # ("%", "%") # In the database, but probably not valid
)

STATUS_CHOICES = (
    ("AGREEMENT-ACTION", "Agreement action"),
    ("NEW-APPLICATION", "New application"),
    ("APP-ACCEPTED", "App accepted"),
    ("APP-APPROVED", "App approved"),
    ("APP-PGM REJECTED", "App PGM rejected"),
    ("APP-RECEIVED", "App received"),
    ("APP-REJECTED", "App rejected"),
    ("GA-CANCELLED", "GA closed"),
    ("GA-EXECUTED", "GA executed"),
    ("GA-PENDING", "GA pending"),
    ("GA-TERMINATED", "GA terminated"),
)

# Output a list of years starting at 1949 (the earliest currently in the DB)
# And always up-to-date with today's year (plus one, to handle any late-year weirdness).
YEAR_CHOICES = sorted(
    [(str(y), str(y)) for y in range(1949, datetime.date.today().year + 1)],
    reverse=True,
)
