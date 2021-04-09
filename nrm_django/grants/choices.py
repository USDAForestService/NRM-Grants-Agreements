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
    # ("Initial", "Initial"), # Not in use per the user guide
    ("NEW", "New"),
    ("CONTINUATION", "Continuation"),
    ("REVISION A-INCREASE AWARD", "Revision A - Increase Award"),
    ("REVISION B-DECREASE AWARD", "Revision B - Decrease Award"),
    ("REVISION C-INCREASE AWARD", "Revision C - Increase Duration"),
    ("REVISION D-DECREASE AWARD", "Revision D - Decrease Duration"),
    ("OTHER", "Other"),
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

CFDA_CHOICES = (
    ("10.652", "10.652 - Research and Development Forest Research"),
    ("10.664", "10.664 - S/PF Cooperative Forestry Assistance"),
    ("10.665", "10.665 - Schools and Roads, Payments to States"),
    ("10.666", "10.666 - Schools and Roads, Payments to Counties"),
    ("10.670", "10.670 - S/ PF National Forest Dependent Rural Communities"),
    ("10.671", "10.671 - S/ PF Region 10, Southeast Alaska Economic Disaster Fund"),
    ("10.672", "10.672 - Rural Development, Forestry and Communities"),
    ("10.673", "10.673 - Wood in Transportation Program"),
    ("10.674", "10.674 - Technology Marketing Unit"),
    ("10.675", "10.675 - Urban and Community Forestry Program"),
    ("10.676", "10.676 - Forest Legacy Program"),
    ("10.677", "10.677 - Forest Land Enhancement Program"),
    ("10.678", "10.678 - Forest Stewardship Program"),
    ("10.679", "10.679 - Collaborative Forest Restoration"),
    ("10.681", "10.681 - Wood Education and Resource Center (WERC)"),
    ("10.682", "10.682 - National Forest Foundation"),
    ("10.683", "10.683 - National Fish and Wildlife Foundation"),
    ("10.684", "10.684 - International Forestry Programs"),
    ("10.685", "10.685 - Recovery Act of 2009: Capital Improvement and Maintenance"),
    ("10.686", "10.686 - Recovery Act of 2009: Wildland Fire Management"),
    ("10.689", "10.689 - Community Forest and Open Space Conservation Program"),
    ("10.690", "10.690 - Lake Tahoe Erosion Control Program"),
    ("10.691", "10.691 - Good Neighbor Program"),
    (
        "10.692",
        "10.692 - Secure Rural Schools and Community Self Determination Program (RAC)",
    ),
    ("10.693", "10.693 - Watershed Restoration and Enhancement (Wyden)"),
    ("10.694", "10.694 - Southwest Forest Health and Wildfire Prevention"),
)

NOTE_TYPE_CHOICES = (
    ("AGREEMENT", "Agreement"),  # About the instrument.
    ("COMMITMENT", "Commitment"),  # About the instrument's commitments.
    ("OBLIGATION", "Obligation"),  # About the instrument's obligations.
    ("PAYMENT", "Payment"),  # About the instrument's payments.
    ("MODIFICATION", "Modification"),  # About the instrument's modifications.
    ("OTHER", "Other"),  # Other notes or comments about the instrument.
)

PROGRAM_RESPONSIBILITY_TYPE_CHOICES = (
    ("INCOMING FUNDING AGREEMENT", "Incoming funding agreement"),
    ("NON-CASH AGREEMENT", "Non-cash agreement"),
    ("OUTGOING FUNDING AGREEMENT", "Outgoing funding agreement"),
)

RESEARCH_TYPE_CHOICES = (
    ("A", "Applied"),
    ("B", "Basic"),
    ("D", "Developmental"),
    ("N", "None"),
)

# TO-DO: Double check these choices. There are several empty values and they may not be accurate.
RWU_CHOICES = (
    (" ", "None"),
    ("FPL-4501", "Center for Forest Mycology Research"),
    ("FPL-4502", "Biodeterioration of Wood"),
    ("FPL-4701", "Center for Wood Anatomy Research"),
    ("FPL-4703", "Wood Adhesives Science and Technology"),
    ("FPL-4706", "Performance- Designed Composites"),
    ("FPL-4707", "Wood Surface Chemistry"),
    ("FPL-4709", "Chemistry and Pulping"),
    ("FPL-4710", "Fiber Processing and paper Performance"),
    ("FPL-4712", "Institute of Microbial and Biochemical Technology"),
    ("FPL-4714", "Engineering Materials and Structures"),
    ("FPL-4716", "Building Moisture and Durability"),
    ("FPL-4719", "Structure Condition Assessment and Rehabilitation"),
    ("FPL-4722", "Modified Lignocellulosic Material"),
    ("FPL-4723", "Wood Preservation"),
    ("FPL-4724", "Statistical Methods in Wood and Fiber Research"),
    ("FPL-4725", "Fire Safety"),
    ("FPL-4851", "Timber Demand and Technology Assessment Research"),
    ("IITF-4151", "Tropical American Forest Management"),
    ("INT-4151", "Ecology and Management of Northern Rocky Mountain Forest"),
    ("INT-4153", "Silviculture and Genetics of Rocky Mountain Forest Ecosystems"),
    (
        "INT-4154",
        "Quantitative Analysis of Forest Resource Responses for Planning, Management, and Control",
    ),
    ("INT-5201", "Wildlife Habitats in the Northern Rockies"),
    ("INT-4202", "Riparian Stream Ecology and Mangement"),
    ("INT-4203", "Enhancing Fish Habitats"),
    ("INT-4251", "Shrubland Biology and Restoration"),
    ("INT-4252", "Ecology Paleoecology and Management of Great Basin Pinyon-Juniper"),
    ("INT-4301", "Reclamation of Disturbed Lands"),
    (
        "INT-4302",
        "Watershed Disturbance and Channel Conditions in the Northern Rocky Mountains",
    ),
    ("INT-4401", "Fire Behavior: Fundamentals and Systems Development"),
    ("INT-4403", "Fire Effects: Prescribed Fire and Wildfiee"),
    ("INT-4404", "Fire Chemistry and Emission Characteristics"),
    ("INT-4501", "Mountain Pine Beetle Population Dynamics"),
    ("INT-4551", "Microbial Processes as Ecosystem Regulators in Western Forests"),
    ("INT-4702", "Soil and Water Engineering"),
    (
        "INT-4801",
        "Interior West Resource Inventory, Monitoring, and Evaluation Program",
    ),
    ("INT-4802", "Economic Aspects of Ecosystem Management on Forest Lands"),
    ("INT-4901", "Wilderness Management Research"),
    ("NC-4108", "Ecology and Culture of the Northern Lake States Forests"),
    ("NC-4152", "Ecosystem Processes"),
    (
        "NC-4153",
        "Physiological Mechanisms of Growth, Multiple-Stress Responses in Northern Forest Trees",
    ),
    ("NC-4154", "Principles of Landscape Ecology for Managing Temperate Ecosystems"),
    ("NC-4155", "Silviculture and Ecology of Upland Central Hardwood Forests"),
    (" ", "Genetic and Molecular Base of Forest Tree Stress Tolerances"),
    ("NC-4157", "Hardwood Tree Improvement & Regeneration"),
    ("NC-4158", "Genetic & Silvicultural Systems for Sustainable Intensive Forestry"),
    ("NC-4159", "Ecosystem Processes"),
    ("NC-4351", "Ecology and Management of Riparian/ Aquatic Ecosystems"),
    ("NC-4401", "Atmospheric and Socioeconomic Relationships with Wildland Fire"),
    ("NC-4455", "Global Change"),
    ("NC-4501", "Stress Effects on Tree-Insect-Natural Enemy interaction"),
    (
        "NC-4502",
        "Rapid Systems for Disease Resistance and Control of Diseases in Nurseries, Forests, Plantations, and Christmas Tree Plantings",
    ),
    (
        "NC-4509",
        "Genetics and Management of Invasive Forest Insect Pests, Diseases, and Beneficial Fungi",
    ),
    ("NC-4702", "Engineering Technology for Managing Forest Ecosystems"),
    (
        "NC-4801",
        "Forest Inventory and Analysis for the North Central and Northern Great Plains State",
    ),
    ("NC-4803", "Social and Economic Dimensions of Ecosystem Management"),
    ("NC-4804", "Economics of Alternate Forest Management Choices in the North"),
    ("NC-4902", "Managing Forest Environments for Urban Populations"),
    ("NE-4103", "The Role of Environmental Stress on Tree Growth and Development"),
    ("NE-4104", "Forest Carbon Dynamics and Estimation for Sustainable Management"),
    (
        "NE-4152",
        "Research to Develop Guidelines and Indicators for Sustaining Forest Ecosystems of Pennsylvania and the Adjacent Allegheny Plateau Region",
    ),
    (
        "NE-4153",
        "Quantitate Methods for Modeling and Monitoring Response of Northeastern Forest Ecosystems to Management and Environmental Stresses",
    ),
    ("NE-4155", "Ecology and Management of Northern Forest Ecosystems"),
    (
        "NE-4251",
        "Wildlife and Fish Habitat Relationships and Recreation in New England Forests",
    ),
    ("NE-4252", "Atlantic Salmon Habitat Restoration, Ecology and Management"),
    (
        "NE-4352",
        "Ecological Process: A Basic for Managing Forest and Protecting Water in New England",
    ),
    ("NE-4353", "Sustaining the Diversity and Productivity of Appalachian Forests"),
    (
        "NE-4454",
        "Integrating Social and Biophysical Sciences for Natural Resource Management",
    ),
    ("NE-4455", "Northern Global Changes Research Program"),
    (
        "NE-450",
        "Development of Biologically Based Controls for Forest Insect Pests and Diseases through Molecular Technologies",
    ),
    ("NE-4501", "Forest Insect Biology and Biocontrol"),
    (
        "NE-4502",
        "Pathology and Microbial Control of Insects that Impact the Health of Eastern Forest Trees",
    ),
    (
        "NE-4505",
        "Forest Sustainability and Tress Response to Injury, Infection, and Environmental Change",
    ),
    ("NE-4557", "Disturbance Ecology and Management of Oak Dominated Forest"),
    (
        "NE-4558",
        "Multiple Stress Interactions and their Effects on Forest Health and Sustainability",
    ),
    ("NE-4701", "Efficient Use of the Northern Forest Resource"),
    (
        "NE-4751",
        "Integration of Forest Operations into Eastern Hardwood Intermediate Cuttings and Structural Retention Treatments",
    ),
    ("NE-4801", "Forest Inventory and Analysis"),
    ("NE-4803", "Eastern Forest Use in a Global Economy"),
    (
        "NE-4805",
        "The influence of Markets on Sustainability of Eastern Hardwood Forests",
    ),
    (
        "NE-4952",
        "Effects of Urban Forests and their Management on Human Health and Environmental Quality",
    ),
    (
        "RM-4151",
        "Research on Sustainable Multi-Resource Management of Forest and Woodland Ecological Systems in Central and Rocky Mountain",
    ),
    (
        "RM-4152",
        "Ecological Roles of Insects and Pathogens in Coniferous Forests of the Interior West",
    ),
    ("RM-4201", "Wildlife Habitat Relationship in Central Rocky Mountains"),
    (
        "RM-4251",
        "Sustainability of Southwestern Forest and Woodland Terrestrial Ecological Systems",
    ),
    (
        "RM-4252",
        "Management for Sustainable Ecological Systems of the Northern and Central Great Plains",
    ),
    (
        "RM-4301",
        "Research on Sustaining Fish and Watershed Components of Aquatic and Riparian Ecological Systems in Central and Southern Rocky Mountain",
    ),
    (
        "RM-4302",
        "Sustainability of Riparian Ecological Systems in Southwestern Forests and Woodlands",
    ),
    (
        "RM-4351",
        "Ecology, Recovery, and Sustainability of Southwestern Grassland and Associated Riparian Ecosystems and Wildlife",
    ),
    (
        "RM-4352",
        "Research on Sustaining Fish and Watershed Components of Aquatic and Riparian Ecosystems in the Central Rocky Mountains and Northern Great Plains",
    ),
    (
        "RM-4451",
        "Sustaining Alpine and Forest Ecosystems under Atmospheric and Terrestrial Disturbances",
    ),
    ("RM-4452", "Effects of Atmospheric Change on Alphine and Subalpine Ecosystems"),
    ("RM-4551", "Improvement of Stress-Pest Resistance of Great Plains Tree Species"),
    ("RM-4651", "Ecological Basic for Research of Borderlands of Southern U.S."),
    (
        "RM-4652",
        "Ecology, Diversity, and Sustainability of Soil, Plant, Animal and Human Resources of the Rio Grande Basin",
    ),
    (
        "RM-4653",
        "Research on Sustaining Social, Biological, and Physical Components of CO Front Range Ecosystems",
    ),
    ("RM-4802", "Multi- Resource Inventory Techniques"),
    (
        "RM-4803",
        "Advanced Research in Economics and Optimization for Forest Service Planning",
    ),
    ("RM-4851", "Identification and Valuation of Wildland Resource Benefits"),
    ("RM-4852", "Natural Resource Assessment Ecology and Management Science Research"),
    ("RM-4853", "Cultural Heritage Research"),
    ("RMRS-4151", "Ecology and Management of Northern Rocky Mountain Forests"),
    (
        "RMRS-4152",
        "Ecological Roles of Insects and Pathogens in Coniferous Forests of the Interior West",
    ),
    (
        "RMRS-4155",
        "Effects of Environmental Variability and Forest Management on Ecosystem Processes that Regulate Forest Dynamics in the Interior West",
    ),
    (
        "RMRS-4156",
        "South Western Wildland-Urban Interface Fuels Management and Forest Health Restoration",
    ),
    ("RMRS-4201", "Wildlife Ecology in Rocky Mountain Landscapes"),
    (
        "RMRS-4251",
        "Ecology and Conservation of Terrestrial Wildlife and Habitats of the Interior West",
    ),
    ("RMRS-4252", "Ecology, Paleoecology, and Restoration of Great Basin Watersheds"),
    (
        "RMRS-4254",
        "Management of Sustainable Ecological Systems of Northern and Central Great Plains",
    ),
    ("RMRS-4301", "Restoration of Disturbed Ecosystems"),
    (
        "RMRS-4302",
        "Watersheds and Riparian Ecosystems of Forests and Woodlands in the Semi-Arid West",
    ),
    (
        "RMRS-4351",
        "Ecology, Recovery, and Sustainability of Southwestern Grassland and Associated Riparian Ecosystems and Wildlife",
    ),
    (
        "RMRS-4352",
        "Sustaining Fish and Watershed Components of Aquatic and Riparian Ecological Systems in Central Rocky Mountains and Northern Great Plains",
    ),
    ("RMRS-4353", "Shrubland Biology and Restoration"),
    ("RMRS-4401", "Fire Behavior Fundamentals and Systems Development"),
    ("RMRS-4403", "Fire Effects: Prescribed Fire and Wildfire"),
    ("RMRS-4404", "Fire Chemistry"),
    (
        "RMRS-4451",
        "Sustaining Alpine and Forest Ecosystems under Atmospheric and Terrestrial Disturbances",
    ),
    (
        "RMRS-4501",
        "Disturbances Ecology in the Interior West: Bark Beetle Disturbance in Conifer Forests",
    ),
    (
        "RMRS-4551",
        "Tree- Based Buffer Technologies for Sustainable Land Use in the Central U.S.",
    ),
    ("RMRS-4552", "Microbial Processes as Ecosystem Regulators in Western Forests"),
    ("RMRS-4651", "Southwestern Borderlands Ecosystem Mangement"),
    (
        "RMRS-4652",
        "Ecology, Diversity, and Sustainability of Soil, Plant, Animal and Human Resources of the Rio Grande Basin",
    ),
    (
        "RMRS-4653",
        "Sustaining Social, Biological, and Physcial Components of Colorado Front Range Ecosystems Management Project",
    ),
    ("RMRS-4654", "Bitterroot Ecosystem Management Research Proejct"),
    ("RMRS-4655", "Interdisciplinary Ecosystem Management Project"),
    ("RMRS-4702", "Soil and Water Engineering"),
    (
        "RMRS-4801",
        "Interior West Resource Inventory, Monitoring, and Evaluation Program",
    ),
    ("RMRS-4802", "Economic Aspects of Forest Management on Public Lands"),
    ("RMRS-4804", "Forest Inventory and Monitoring Environmetrics"),
    ("RMRS-4851", "Identification and Valuation of Wildland Resource Benefits"),
    ("RMRS-4852", "Natural Resource Assessment Ecology and Management Science"),
    ("RMRS-4853", "Cultural Heritage Research"),
    ("RMRS-4901", "Wilderness Management Research"),
    ("PNW-64", "Administration"),
    ("PNW-4163", "Resource Management and Productivity"),
    ("PNW-4166", "Focus Science Delivery"),
    ("PNW-4261", "Aquatic and Land Interaction Research Programs"),
    ("PNW-4362", "Ecosystem Processes"),
    ("PNW-4577", "Managing Natural Disturbance to Sustain Forest Health"),
    ("PNW-4865", "Social and Economic Values Research Programs"),
    (
        "PNW-4869",
        "Pacific Resource Inventory Monitoring and Evaluation Research, Development and Application Program",
    ),
    ("PNW-4103", "People and Natural Resources"),
    (
        "PSW-4154",
        "National Forest Genetic Electrophoresis Laboratory (Placerville, CA)",
    ),
    ("PSW-4155", "Institute of Pacific Islands Forestry"),
    (
        "PSW-4202",
        "Ecology and Management of Western Forests Influences by Mediterranean Climate",
    ),
    ("PSW-4251", "Forestry Sciences Laboratory (Fresno, CA)"),
    (
        "PSW-4351",
        "Wildlife Habitats in Mature and Old Growth Forests of Northern California",
    ),
    (
        "PSW-4401",
        "Cumulative Effects of Forest Management on Hillslope Processes, Fishery Resources and Downstream Environments",
    ),
    ("PSW-4402", "Fire Meteorology"),
    ("PSW-4403", "Wildland Fire Management Research, Development, and Application"),
    ("PSW-4451", "Prescribed Fire and Fire Effects"),
    ("PSW-4502", "Atmospheric Deposition Effects on Western Forest Ecosystems"),
    ("PSW-4651", "Chemical Ecology of Forest Insects"),
    (" ", "Pacific Northwest Forest Plan"),
    ("PSW-4902", "Wildland Recreation and Urban Cultures"),
    ("PSW-4952", "Center for Urban Forest Research"),
    ("SRS-4101", "Ecology and Management of Southern Appalachian Hardwoods"),
    ("SRS-4103", "Center for Forested Wetlands Research"),
    ("SRS-4104", "Disturbance and Management of Southern Pine Ecosystem"),
    (
        "SRS-4105",
        "Integrated Vegetation Management for Sustaining Southern Forests and Longleaf Pine Ecosystems",
    ),
    ("SRS-4106", "Managing Upland Forest Ecosystems in the Midsouth"),
    ("SRS-4111", "Ecology and Management of Even-Aged Southern Pine Forest"),
    ("SRS-4153", "Southern Institute of Forest Genetics"),
    (
        "SRS-4154",
        "Biological Foundations of Southern Forest Productivity and Sustainability",
    ),
    ("SRS-4155", "Center for Bottomland Hardwoods Research"),
    ("SRS-420", "Coldwater Streams and Trout Habitat in the Southern Appalachians"),
    (
        "SRS-4201",
        "Endangered, Threatened and Sensitive Wildlife and Plants in Southern Forests",
    ),
    ("SRS-4202", "Coldwater Streams and Trout Habitat in the Southern Appalachians"),
    ("SRS-4251", "Integrated Management of Wildlife Habitat and Timber Resources"),
    (
        "SRS-4351",
        "Evaluation of Watershed Ecosystem Responses to Natural, Management, and other Human Disturbances of Southern Forests",
    ),
    ("SRS-4501", "Bark Beetles and Invasive Insects"),
    ("SRS-4502", "Wood Products Insect Research"),
    ("SRS-4505", "Insects and Diseases of Southern Forests"),
    ("SRS-4701", "Utilization of Southern Forest Resources"),
    ("SRS-4702", "Forest Products Conservation"),
    ("SRS-4703", "Forest Operations Research to Achieve Sustainable Management"),
    ("SRS-4801", "Forest Inventory and Analysis"),
    (
        "SRS-4802",
        "Evaluation of Legal, Tax, and Economic Influences on Forest Resource Management",
    ),
    ("SRS-4803", "Forest Health Monitoring"),
    ("SRS-4851", "Economics of Forest Protection and Management"),
    ("SRS-4852", "Southern Global Change Program"),
    (
        "SRS-4901",
        "Recreation, Wilderness, Urban Forest and Demographic Trends Research",
    ),
    (
        "SRS-4901",
        "Assessing Trends, Values and Rural Community Benefits from Outdoor Recreation and Wilderness in Forest Ecosystems",
    ),
)

SCIENCE_CODE_CHOICES = (
    ("12", "Chemistry"),
    ("21", "Mathematics"),
    ("22", "Computer Sciences"),
    ("31", "Atmospheric Sciences"),
    ("32", "Earth Science"),
    ("43", "Chemical"),
    ("49", "Engineering, n.o.c."),
    ("51", "Biological"),
    ("54", "Environmental Biology"),
    ("55", "Agricultural Sciences"),
    ("71", "Anthropology"),
    ("72", "Economics"),
    ("76", "Sociology"),
    ("79", "Social Sciences"),
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

WPAP_STATUS_CHOICES = (
    ("Awaiting Documentation", "Awaiting Documentation"),
    ("Executed- Active", "Executed - Active"),
    ("G&A Closed", "G&A Closed"),
    ("G&A Closeout in process", "G&A Closeout in process"),
    ("G&A Reviewing", "G&A Reviewing"),
    ("New", "New"),
    ("Out for Signature", "Out for Signature"),
    ("Pending ASC Action", "Pending ASC Action"),
)

# Output a list of years starting at 1949 (the earliest currently in the DB)
# And always up-to-date with today's year (plus one, to handle any late-year weirdness).
YEAR_CHOICES = sorted(
    [(str(y), str(y)) for y in range(1949, datetime.date.today().year + 1)],
    reverse=True,
)
