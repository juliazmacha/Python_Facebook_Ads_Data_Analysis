# Python_Facebook_Ads_Data_Analysis
This Python script analyzes Facebook advertising data from a CSV file. The analysis includes plotting various metrics and aggregations related to advertising spend and return on marketing investment (ROMI) for the year 2021. It also provides insights into campaign performance, distribution of ROMI values, and correlations among different variables.

# Facebook Ads Data Analysis

This repository contains a Python script for analyzing Facebook ads data. The script processes a CSV file containing advertising metrics, performs data aggregation, and generates various visualizations to help understand spending and return on marketing investment (ROMI).

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Data Description](#data-description)
- [Visualizations](#visualizations)
- [License](#license)

## Requirements

To run this script, you'll need the following Python libraries:

- `pandas`
- `matplotlib`
- `seaborn`

## Data Description
The script expects a CSV file with the following columns:

- ad_date: Date of the advertisement.
- total_spend: Total amount spent on advertisements.
- romi: Return on Marketing Investment.
- total_value: Total value generated from advertisements.
- campaign_name: Name of the advertising campaign.
### Visualizations
The script generates the following visualizations:

- Daily Advertising Spend in 2021
- Daily ROMI in 2021
- 7-day Rolling Average of Advertising Spend in 2021
- 7-day Rolling Average of ROMI in 2021
- Total Advertising Spend by Campaign
- Total ROMI by Campaign
- Daily ROMI Distribution by Campaign
- Distribution of ROMI Values
- Correlation Heatmap
- Linear Regression: Total Spend vs Total Value
