# recreating paper

## The paper

[A station-keeping maneuver detection method of non-cooperative geosynchronous satellites
By Fen Li a, Yufei Zhao b,⇑, Jingyu Zhang a, Ziqiang Zhang a, Di Wu a](https://doi.org/10.1016/j.asr.2023.10.009)

## 1. data collection

1. collect tle
2. tle to six classical orbital elements
   1. semi-major axis (a), -> "SEMIMAJOR_AXIS"
   2. eccentricity (e), -> "ECCENTRICITY"
   3. inclination (i), -> "INCLINATION"
   4. Right Ascension of the Ascending Node (X), -> "RA_OF_ASC_NODE"
   5. the argument of perigee (x), -> "ARG_OF_PERICENTER"
   6. mean anomaly (M). -> "MEAN_ANOMALY"

## 2. data preprocessing

1. data deduplication
2. window slicing
3. normalization
4. one-hot encoding
   - "EW": [1, 0, 0], # East-West station-keeping maneuver
   - "EW-NS": [0, 1, 0], # East-West and North-South station-keeping maneuver
   - "NM": [0, 0, 1] # no maneuver

## 3. setup 2dcnn model

1. 80% training, 20% testing
2. input
   - input(20 x 6 x 1) => (256@ 4x2)
   - conv1(17 x 5 x 128) => (256@ 4x2)
   - conv2(14 x 4 x 128) => maxpool(2x2)
   - pool1(7 x 2 x 128)
   - fc3(192 x 1)
   - fc4(89 x 1)
   - output(3 x 1)
