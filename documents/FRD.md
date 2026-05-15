# Functional Requirements Document (FRD)

## Project Title
Carbon Emission Impact Analysis & Sustainability Intelligence Platform

---

## 1. Introduction
This Functional Requirements Document (FRD) defines the technical and functional behavior of the Carbon Emission Impact Analysis system. The platform is designed to analyze environmental sustainability data, generate business insights, support predictive forecasting, and provide interactive visual dashboards for decision-making.

---

## 2. System Overview
The system will provide an analytics platform that:

- processes environmental and economic datasets
- performs data transformation and integration
- generates sustainability KPIs
- supports SQL-based analysis
- provides predictive forecasting
- offers interactive dashboard visualizations
- delivers business insights and recommendations

---

## 3. Functional Requirements

# 3.1 Data Ingestion Module

### Description
The system shall load raw datasets from local storage.

### Functional Requirements
- Load CSV datasets
- Read structured environmental and economic datasets
- Support multiple dataset sources
- Validate file format compatibility

### Input
- CSV files

### Output
- Loaded pandas DataFrames

---

# 3.2 Data Cleaning Module

### Description
The system shall clean and preprocess datasets before analysis.

### Functional Requirements
- Handle missing values
- Remove duplicate records
- Standardize column names
- Convert datatypes
- Validate numerical columns
- Remove invalid records

### Input
- Raw datasets

### Output
- Clean datasets

---

# 3.3 Data Integration Module

### Description
The system shall merge datasets into a centralized analytical dataset.

### Functional Requirements
- Merge datasets using:
  - country
  - country_code
  - year

- Support left joins
- Handle mismatched country names
- Validate merged dataset consistency

### Input
- Clean datasets

### Output
- Final integrated dataset

---

# 3.4 SQL Analytics Module

### Description
The system shall support SQL-based business analysis.

### Functional Requirements
- Load processed dataset into SQLite
- Execute SQL queries
- Generate ranking reports
- Perform grouped aggregations
- Support sustainability filtering

### Example Queries
- Top emitting countries
- Sustainability leaders
- Energy consumption trends
- GDP analysis

### Output
- Query result tables

---

# 3.5 KPI Engineering Module

### Description
The system shall generate business KPIs.

### Functional Requirements
Calculate:

- Average CO₂ emissions
- Renewable energy percentage
- Average GDP
- Average energy consumption
- Carbon intensity
- Sustainability indicators

### Output
- KPI metrics

---

# 3.6 Dashboard Module

### Description
The system shall provide interactive dashboard visualization.

### Functional Requirements
- Show CO₂ trends
- Show renewable energy trends
- Compare GDP vs emissions
- Display energy consumption analysis
- Show global emission maps
- Display sustainability leaders

### User Features
- Filter by country
- Filter by year
- Select all countries
- Download filtered data

### Output
- Interactive Streamlit dashboard

---

# 3.7 Forecasting Module

### Description
The system shall predict future carbon emissions.

### Functional Requirements
- Train machine learning models
- Evaluate model performance
- Compare algorithms
- Save trained models

### Supported Models
- Linear Regression
- Random Forest
- XGBoost
- ARIMA (optional)

### Evaluation Metrics
- MAE
- RMSE
- R² Score

### Output
- predictions
- model comparison
- saved model files

---

# 3.8 Reporting Module

### Description
The system shall generate business insights and documentation.

### Functional Requirements
- Provide analytical findings
- Summarize business recommendations
- Generate sustainability conclusions

### Output
- reports
- markdown documents
- dashboard insights

---

## 4. Non-Functional Requirements

### Performance
- Dashboard should load efficiently
- Queries should execute within reasonable time

### Scalability
- System should support larger datasets

### Maintainability
- Modular folder structure
- readable code
- reusable notebooks

### Usability
- intuitive dashboard interface
- clear visualization labels
- simple filters

### Reliability
- consistent analytical outputs
- reproducible workflows

### Portability
- runnable on Linux
- deployable via Streamlit
- Docker support

---

## 5. System Architecture

Workflow:

Raw Data
→ Data Cleaning
→ Data Integration
→ SQL Analysis
→ KPI Engineering
→ Dashboard
→ Forecasting
→ Business Reporting

---

## 6. Input Data Sources

The system accepts:

- Carbon emissions dataset
- GDP dataset
- Population dataset
- Renewable energy dataset
- Energy consumption dataset
- Temperature dataset (optional)

---

## 7. Output Deliverables

The system produces:

- final_dataset.csv
- carbon.db
- SQL analysis reports
- forecasting models
- Streamlit dashboard
- Power BI dashboard (optional)
- screenshots
- documentation

---

## 8. Constraints

- Dependent on historical data quality
- Requires Python environment
- Streamlit deployment requires internet
- Forecast accuracy depends on data completeness

---

## 9. Assumptions

- Dataset values are reliable
- Historical trends reflect meaningful patterns
- Environmental indicators are comparable across countries

---

## 10. Future Enhancements

Possible future improvements:

- live API integration
- real-time ESG dashboards
- IoT environmental monitoring
- cloud deployment
- advanced forecasting models
- anomaly detection