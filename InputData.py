# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate
DELTA_T = 1       # years

# transition matrix
TRANS_MATRIX = [
    [0.75, 0.15, 0.0, 0.1],  # Well
    [0, 0.0, 1.0, 0.0],  # Stroke
    [0, 0.25, 0.55, 0.2],  # Post-Stroke
    [0.0, 0.0, 0.0, 1.0],  # Dead
]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,   # Well
    5000,   # Stroke
    200,    # Post-Stroke
    0.0      # Dead
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.0,   # Well
    0.8865,   # Stroke
    0.9,   # Post-Stroke
    0.0     # Dead
    ]

# annual drug costs
Anticoagulation_COST = 2000
NoDrug_COST = 0

# treatment relative risk
TREATMENT_RR = 0.509
TREATMENT_RR_CI = 0.365, 0.71  # lower 95% CI, upper 95% CI
