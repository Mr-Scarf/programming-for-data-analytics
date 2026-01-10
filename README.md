

 # Programming for Data Analytics

**University**: Atlantic Technological University  
**Module**: Programming for Data Analytics  
**Class**: September 2025  
**Author**: David Scally   


 This repository contains a combination of assignments, coursework and a final project that was completed for the **Programming for Data Analytics** module - see structure & contents below.

 ## Repository Structure & Contents

 ### assignments
 Contains assignments completed as part of the module :  
    - **assignment02-bankholidays.py** -Analysis of Northern Ireland UK Bank Holidays using JSON files.    
    - **assignment03-pie.ipynb** - Analysis of email domains with a pie chart.   
    - **assignment05-population.ipynb** - Analysis of cso population dataset.  
    - **assignment_6_Weather.ipynb** - Analysis of weather data.  

 ### my-work
 Contains coursework completed as part of the module.

 ### project
 Contains project completed as part of the module. This will be further expanded on in **Project -  Analysis of Magnificent Seven Stocks** section.
  - **project.ipynb** - Jupyter notebook containing the full analysis of the Magnificent Seven stocks.
  - **Magnificent 7 Stock Price History - Jan 2015- Nov 2025.csv** - csv file containing historical stock data used for analysis in the project.  


 ### .gitignore
 Tells Git which files to ignore in repository.

 ### requirements.txt
 List of packages used in the analysis.

 ### README.md
 This file, used to explain the layout of the repository & the project.   
  
  
  

  
# Project -  Analysis of Magnificent Seven Stocks

![Magnificent 7 Stocks](https://i.ytimg.com/vi/y6LPqd2_PhE/maxresdefault.jpg)


## Purpose

The goal of the assignment is to demonstrate tools learned in the **Programming for Data Analytics** module.
Using Python, this includes:

 - **Data Acquisition** - Use **yfinance** to download historical stock price data.
 - **Data Cleaning & Preparation** - Preparatory check to ensure datasets are complete & ready for further analysis.  
 - **Exploratory Data Analysis (EDA)** - Calculate resampled returns, rolling averages & correlations for the stocks.  
 - **Visualisation** - Plot returns, rolling averages & correlation heatmaps.  
 - **Linear Regression Modelling** - Apply linear regression to look at trends in a single stock. 

We will analyse the well-known **'Magnificent Seven'** stock companies:


| Company        | Ticker |
|---------------|--------|
| Meta Platforms | META   |
| Apple Inc.     | AAPL   |
| Amazon.com     | AMZN   |
| Tesla Inc.     | TSLA   |
| Alphabet Inc.  | GOOG   |
| Nvidia Corporation   | NVDA   | 
| Microsoft Corporation  | MSFT   | 

This project looks at historical pricing metrics, stock growth, volatility and provides insights into potential future trends in stock prices.

  ## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Mr-Scarf/principles_of_data_analytics.git
```

2. **Install dependencies - see file 'requirements.txt'**

```bash
pip install -r requirements.txt
```

3. **Run the jupyter notebook**
```bash
jupyter notebook  project.ipynb
```
