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

