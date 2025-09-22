# residency-match-sankey

![interactive Sankey diagram showing US residency match rates](https://github.com/nickmmark/residency-match-sankey/blob/main/residency_applicants_figure.jpg)


### 📊 Purpose
An interactive Sankey diagram visualizing US residency applicants and outcomes from the 2025 NRMP Main Match.

* Applicants (U.S. MD, U.S. DO, U.S.-citizen IMGs, non-U.S. IMGs, others)
* Outcomes (Matched, Unfilled positions, Unmatched)
* PGY-1 positions offered/filled (40,041 total; 37,667 filled, 2,374 unfilled)

Tooltips display match rates for each applicant group and the percent/absolute counts of positions filled.


### 🏃 How to run
Either click [here](https://nickmmark.github.io/residency-match-sankey/) to load the page or do the following:
1. Clone/download this repo
2. Install dependencies
```bash
pip install pandas plotly
```   
4. Run the python script
```bash
python generate_sankey.py
```
6. Open the generated HTML file
```
us_residency_applicants_2025_sankey.html
```

### 📖 Source data 
* Data is from the National Residency Matching Program (NRMP) for 2025
* Overall data

| Applicant Group            | Applicants | Matched | Unmatched | Match Rate |
|----------------------------|------------|---------|-----------|------------|
| U.S. MD seniors            | 20,368     | 19,044  | 1,324     | 93.5%      |
| U.S. DO seniors            | 8,392      | 7,773   | 619       | 92.6%      |
| U.S.-citizen IMGs          | 4,587      | 3,108   | 1,479     | 67.8%      |
| Non-U.S.-citizen IMGs      | 11,465     | 6,653   | 4,812     | 58.0%      |
| **Subtotal (above)**       | 44,812     | 36,578  | 8,234     | 81.6%      |
| Other applicants (matched) | –          | 1,089   | –         | –          |
| **Totals**                 | –          | 37,667  | 8,234     | –          |

| PGY-1 Positions | Count  | Percent |
|-----------------|--------|---------|
| Offered         | 40,041 | 100%    |
| Filled          | 37,667 | 94.1%   |
| Unfilled        | 2,374  | 5.9%    |


| Specialty                             |   Applicants_US_MD |   Matches_US_MD |   Applicants_US_DO |   Matches_US_DO |   Applicants_US_IMG |   Matches_US_IMG |   Applicants_NonUS_IMG |   Matches_NonUS_IMG |   Unfilled |
|:--------------------------------------|-------------------:|----------------:|-------------------:|----------------:|--------------------:|-----------------:|-----------------------:|--------------------:|-----------:|
| Anesthesiology                        |               1784 |            1301 |                480 |             308 |                 177 |               47 |                    221 |                  84 |          1 |
| Child Neurology                       |                136 |             118 |                 41 |              32 |                  19 |                5 |                     84 |                  28 |         10 |
| Dermatology                           |                240 |              24 |                 43 |              30 |                   1 |                0 |                      0 |                   0 |          0 |
| Emergency Medicine                    |               1514 |            1377 |               1231 |            1078 |                 467 |              315 |                    336 |                 131 |         65 |
| Emergency Med-Anesthesiology          |                 11 |               1 |                  1 |               0 |                   1 |                0 |                      1 |                   0 |          0 |
| Emergency Med-Family Med              |                 16 |               4 |                  6 |               3 |                   2 |                0 |                      0 |                   0 |          0 |
| Family Medicine                       |               1739 |            1501 |               1907 |            1482 |                1277 |              626 |                   2123 |                 801 |        805 |
| Family Med-Preventive Med             |                  6 |               1 |                  3 |               1 |                   0 |                0 |                      1 |                   0 |          0 |
| Internal Medicine (Categorical)       |               4522 |            3782 |               2396 |            1882 |                2099 |             1145 |                   7630 |                3573 |        357 |
| Medicine-Dermatology                  |                 35 |               7 |                  0 |               0 |                   0 |                0 |                      6 |                   1 |          0 |
| Medicine-Emergency Med                |                 50 |              20 |                 22 |               5 |                  19 |               12 |                     14 |                   1 |          0 |
| Medicine-Medical Genetics             |                  9 |               4 |                  0 |               0 |                   0 |                0 |                      6 |                   5 |          0 |
| Medicine-Pediatrics                   |                386 |             319 |                 67 |              42 |                  30 |               12 |                    110 |                  16 |          3 |
| Medicine-Preliminary (PGY-1 Only)     |               3824 |            1108 |                816 |             137 |                 297 |               52 |                    900 |                 139 |        145 |
| Medicine-Preventive Med               |                 29 |               4 |                 11 |               0 |                   0 |                0 |                     64 |                   4 |          0 |
| Medicine-Primary                      |                807 |             232 |                320 |              48 |                 226 |               24 |                    718 |                  82 |         11 |
| Medicine-Psychiatry                   |                 57 |              19 |                 10 |               2 |                   7 |                1 |                     11 |                   1 |          2 |
| Interventional Radiology (Integrated) |                202 |              39 |                 36 |               4 |                   9 |                0 |                     27 |                   7 |          0 |
| Neurodevelopmental Disabilities       |                 13 |               1 |                  4 |               0 |                   3 |                2 |                      7 |                   0 |          4 |
| Neurological Surgery                  |                331 |             228 |                 22 |               5 |                  13 |                2 |                     52 |                  16 |          3 |
| Neurology                             |                721 |             492 |                247 |             154 |                 135 |               46 |                    627 |                 223 |          7 |
| Obstetrics-Gynecology                 |               1310 |            1109 |                472 |             314 |                 129 |               50 |                    127 |                  44 |          1 |
| OB/GYN-Preliminary (PGY-1 Only)       |                194 |               4 |                 20 |               1 |                   4 |                1 |                     17 |                   2 |          9 |
| Orthopaedic Surgery                   |               1045 |             724 |                295 |             131 |                  48 |                8 |                     29 |                  14 |          0 |
| Osteo Neuromusculoskeletal Med        |                  0 |               0 |                 14 |               0 |                  25 |                0 |                      1 |                   0 |         14 |
| Otolaryngology                        |                447 |             351 |                138 |              24 |                  12 |                2 |                     21 |                   5 |          1 |
| Pathology                             |                295 |             263 |                130 |             104 |                 136 |               57 |                    405 |                 168 |          3 |
| Pediatrics (Categorical)              |               1676 |            1476 |                717 |             519 |                 376 |              251 |                   1174 |                 590 |        147 |
| Pediatrics-Anesthesiology             |                 24 |               7 |                  6 |               3 |                   0 |                0 |                      0 |                   0 |          0 |
| Pediatrics-Emergency Med              |                 24 |               5 |                  6 |               3 |                   0 |                0 |                      0 |                   0 |          0 |
| Pediatrics-Medical Genetics           |                 49 |              17 |                  6 |               5 |                   0 |                0 |                     21 |                   5 |          1 |
| Pediatrics-PM & R                     |                 18 |               4 |                  7 |               1 |                   0 |                0 |                      1 |                   0 |          0 |
| Pediatrics-Preliminary                |                117 |              19 |                 18 |               1 |                   4 |                3 |                     28 |                   2 |          2 |
| Pediatrics-Primary                    |                180 |              18 |                 67 |               4 |                  49 |                3 |                    299 |                  30 |          3 |
| Peds/Psych/Child Psych                |                 68 |              27 |                  5 |               1 |                   5 |                1 |                      0 |                   0 |          0 |
| Physical Medicine & Rehab             |                346 |             126 |                322 |              90 |                  39 |               10 |                     29 |                   9 |          0 |
| Plastic Surgery (Integrated)          |                295 |             197 |                 14 |               2 |                  15 |                2 |                     30 |                   4 |          0 |
| Psychiatry                            |               1705 |            1433 |                694 |             542 |                 329 |              153 |                    409 |                 190 |          8 |
| Psychiatry-Family Medicine            |                 50 |              13 |                  8 |               1 |                   3 |                0 |                      2 |                   0 |          0 |
| Psychiatry-Neurology                  |                 18 |               5 |                  4 |               0 |                   2 |                0 |                      1 |                   0 |          0 |
| Radiation Oncology                    |                 98 |               9 |                 15 |               1 |                   6 |                1 |                     33 |                   1 |          0 |
| Radiology-Diagnostic                  |                703 |              86 |                198 |              35 |                  43 |                7 |                     96 |                   9 |          4 |
| Surgery (Categorical)                 |               1496 |            1114 |                445 |             261 |                 343 |              100 |                    533 |                 114 |          4 |
| Surgery-Preliminary (PGY-1 Only)      |               1065 |             267 |                235 |              64 |                 246 |               88 |                    584 |                 240 |        521 |
| Thoracic Surgery                      |                 94 |              50 |                  9 |               2 |                  19 |                0 |                     19 |                   2 |          0 |
| Transitional (PGY-1 Only)             |               3193 |            1054 |                992 |             346 |                 338 |               89 |                    549 |                 106 |        243 |
| Vascular Surgery                      |                109 |              84 |                  9 |               2 |                   7 |                2 |                     31 |                   9 |          0 |



### References
* [National Residency Matching Program (NRMP) Data 2025](https://www.nrmp.org/wp-content/uploads/2025/03/Advance_Data_Tables_2025.pdf)
