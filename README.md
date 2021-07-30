# Project_2_Impacts_on_US_Housing



Hello! 

This project analyzes coorelations in the Unite States housing market. The factors we look at include: 

- Avergae home price
- Interest rates
- Permit ammounts
- Steel price index
- Lumber price index


We begin by gathering data from csv's from the given sources below. We then transform the data in the ipynb that returns cleaned csv's. The etl file then push the data to a SQL database. Using the app.py the data is then pushed to flask api's, one for each csv file. Each api returns a JSON formated dataset. Using the api's we created a app.js file that pushes plots, using functions, to our html file. This is all done being hosted by Heroku. 

Enjoy!

# Data Sources & Datasets

## Federal Reserve Economic Data (FRED) Housing Category

https://fred.stlouisfed.org/categories/97

## Homeownership Rate in the United States (RHORUSQ156N)

homeownership_rate_RHORUSQ156N.csv

Source: U.S. Census Bureau  

Release: Housing Vacancies and Homeownership  

Units:  Percent, Not Seasonally Adjusted

Frequency:  Quarterly

The homeownership rate is the proportion of households that is owner-occupied.

Citation:
U.S. Census Bureau, Homeownership Rate in the United States [RHORUSQ156N], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/RHORUSQ156N, July 16, 2021.

## Monthly Supply of Houses in the United States (MSACSR)

monthly_supply_houses_us_MSACSR.csv

Source: U.S. Census Bureau, U.S. Department of Housing and Urban Development

Release: New Residential Sales  

Units:  Months' Supply, Seasonally Adjusted

Frequency:  Monthly

The months' supply is the ratio of houses for sale to houses sold. This statistic provides an indication of the size of the for-sale inventory in relation to the number of houses currently being sold. The months' supply indicates how long the current for-sale inventory would last given the current sales rate if no additional new houses were built.

Citation:
U.S. Census Bureau and U.S. Department of Housing and Urban Development, Monthly Supply of Houses in the United States [MSACSR], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/MSACSR, July 17, 2021.

## New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units (PERMITNSA)

new_housing_permits_PERMITNSA.csv

Source: U.S. Census Bureau, U.S. Department of Housing and Urban Development

Release: New Residential Construction  

Units:  Thousands of Units, Not Seasonally Adjusted

Frequency:  Monthly

Citation:
U.S. Census Bureau and U.S. Department of Housing and Urban Development, New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units [PERMITNSA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/PERMITNSA, July 17, 2021.

## New Privately-Owned Housing Units Completed: Total Units (COMPUTNSA)

units_completed_COMPUTNSA.csv

Source: U.S. Census Bureau, U.S. Department of Housing and Urban Development  

Release: New Residential Construction  

Units:  Thousands of Units, Not Seasonally Adjusted

Frequency:  Monthly

Citation:
U.S. Census Bureau and U.S. Department of Housing and Urban Development, New Privately-Owned Housing Units Completed: Total Units [COMPUTNSA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/COMPUTNSA, July 17, 2021.

