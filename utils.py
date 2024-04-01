KEPLERIAN_ELEMENTS = [
    "SEMIMAJOR_AXIS",
    "ECCENTRICITY",
    "INCLINATION",
    "RA_OF_ASC_NODE",
    "ARG_OF_PERICENTER",
    "MEAN_ANOMALY"
]

TIME_SERIES_COLUMNS = [
    "NORAD_CAT_ID",
    "EPOCH",
]

TS_KE_ELEMENTS = TIME_SERIES_COLUMNS + KEPLERIAN_ELEMENTS

ONE_HOT_ENCODED_COLUMNS = {
    "EW": [1, 0, 0],        # East-West station-keeping maneuver
    "EW-NS": [0, 1, 0],     # East-West and North-South station-keeping maneuver
    "NM": [0, 0, 1]         # no maneuver
}