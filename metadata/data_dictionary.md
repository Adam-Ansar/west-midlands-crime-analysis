# Data Dictionary – West Midlands Crime Dataset

**Source:** [data.police.uk](https://data.police.uk/data/), downloaded Sep 2025  
**Coverage:** June 2024 – July 2025, West Midlands Police Force

### Columns
- **Crime ID**: Unique identifier for each crime. Missing in ~9% of rows.  
- **Month**: Date (YYYY-MM) of crime record. Converted to datetime in processing.  
- **Reported by**: Police force reporting the crime.  
- **Falls within**: Policing area (always West Midlands Police here).  
- **Longitude / Latitude**: Approximate location, anonymised to protect privacy.  
- **Location**: Public reference point (e.g., "On or near Supermarket").  
- **LSOA code / name**: Lower Layer Super Output Area, a small UK statistical geography.  
- **Crime type**: Broad crime category (e.g., "Violence and sexual offences").  
- **Last outcome category**: Investigative outcome. Missing for ~9%.  
- **Year / MonthName / MonthNum / Season**: Derived helper columns for time-based analysis.
