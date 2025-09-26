# 📌 Overview

This project analyzes street-level crime data for the West Midlands from **June 2024 to July 2025**.

**Objectives:**
- Clean and prepare raw police data
- Explore crime patterns by time, type, and location
- Use visualizations and statistical tests to highlight key trends
- Try a simple forecasting model to predict future crime volumes

The analysis demonstrates how open police data can be explored and communicated, while building my skills as a junior data analyst.

---

## 📁 Project Structure

```
west-midlands-crime-analysis/
├── data/
│   ├── raw/                # Original monthly CSVs from West Midlands Police
│   └── processed/          # Cleaned and combined datasets
├── notebooks/
│   ├── data_cleaning.ipynb         # Data preparation and cleaning
│   ├── eda.ipynb                   # Exploratory Data Analysis
│   ├── visualisations.ipynb        # Visual summaries of key findings
│   ├── Key_findings_and_insights.ipynb  # Main insights and conclusions
│   ├── predictive_modelling.ipynb  # Time series forecasting
│   └── limitations.ipynb           # Dataset limitations and caveats
├── scripts/
│   └── make_sample.py              # Utility script for sampling data
└── README.md
```

Each notebook builds on the previous one, starting with raw data cleaning and ending with predictive modelling and limitations.

---

## 🛠️ Workflow

1. **Data Cleaning**
    - Combined 12+ monthly CSV files into a single dataset
    - Removed duplicates and handled missing values (e.g., “Outcome not recorded”)
    - Created extra columns for year, month, and season to aid analysis

2. **Exploratory Data Analysis (EDA)**
    - Examined dataset size, structure, and missing values
    - Summarized crime counts by type, location, and time
    - Identified patterns (e.g., summer peaks)

3. **Visualization**
    - Built charts to clarify findings:
      - Line charts for crime trends
      - Bar charts for crime types and locations
      - Heatmaps for outcomes
      - Donut chart for solved vs unsolved crimes

4. **Statistical Testing**
    - **ANOVA:** Confirmed seasonal differences in crime are statistically significant
    - **Chi-square:** Showed outcomes differ by crime type
    - **Spearman correlation:** Identified trends over time (e.g., drug-related crime rising)
    - **Z-test for proportions:** Showed shoplifting is disproportionately in supermarkets

5. **Predictive Modelling**
    - Tried a simple ARIMA model (and Holt-Winters for comparison) to forecast monthly crime counts
    - Evaluated with Mean Absolute Error (MAE)
    - ARIMA gave the better baseline forecast

6. **Insights & Limitations**
    - Summarized findings in plain language
    - Documented dataset limitations (missing outcomes, vague locations, lack of demographics)

---

## 📊 Main Findings

- **Seasonality:** Crime peaks in summer (July highest), drops in winter (February lowest)
- **Crime Types:** Violence and sexual offences are most common; drug-related crime is rising
- **Geographic Hotspots:** Urban centres (Birmingham, Walsall, Coventry) have highest volumes; supermarkets and parking areas are high-risk
- **Outcomes:** Over 96% of crimes unresolved; few lead to caution or charge
- **Location Risks:** Shoplifting heavily concentrated in supermarkets (confirmed by statistical testing)
- **Forecasting:** ARIMA produced a reasonable short-term forecast, limited by dataset length

---

## ⚠️ Limitations

This analysis is based on open police data, which has several constraints:

- Many outcomes are missing or unresolved at release
- Not all crimes are reported (some types underrepresented)
- Locations are anonymized (“On or near…”) for privacy
- No demographic information (victim/suspect) or wider context (weather, socio-economic)
- Only 13 months of data (limits advanced forecasting)

👉 Full discussion is in `limitations.ipynb`
---

## 🚀 How to Run

1. **Clone this repository:**
    ```bash
    git clone https://github.com/your-username/west-midlands-crime-analysis.git
    cd west-midlands-crime-analysis
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 📂 Data

All required raw CSV files are provided in the [`data/raw/`](data/raw/) directory of this repository.  
You do **not** need to download any additional data to run the analysis.


4. **Run the notebooks in this order:**
    1. `data_cleaning.ipynb`
    2. `eda.ipynb`
    3. `visualisations.ipynb`
    4. `Key_findings_and_insights.ipynb`
    5. `predictive_modelling.ipynb`
    6. `limitations.ipynb`

---

## 📦 Requirements

- Python 3.8+
- pandas, numpy, matplotlib, seaborn, statsmodels, scikit-learn, scipy  
  *(see `requirements.txt` for full details)*

---

## 🙌 Credits

- **Data:** West Midlands Police Open Data
- **Analysis & code:** Adam Ansar, and CoPilot.
