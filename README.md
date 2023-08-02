# EV-registration
EV-registration is a small project to model and predict the number of electric vehicle (EV) registrations using socio-economic factors (tied to a ZIP code). This project originally began as a favor to a friend at [CALSTART](https://calstart.org/) who, overall, are interested in extrapolating where the greatest number of EV registrations might occur in the future.

## Table of contents
- [Dependencies](#1)
- [Dataset](#2)
- [Using EV-registration](#3)
- [Note on the limitations of spatial analysis using ZIP codes](#4)
- [Licensing](#5)

<a name='1'></a>
## Dependencies
This project was designed to work with Python 3.11.4, but other Python 3.X versions may be supported if dependency and compatibility requirement are met.
- numpy
- pandas
- matplotlib
- tensorflow
- seaborn

<a name='2'></a>
## Dataset
This data set is compiled from the Census Bureau's American Community Survey (2021) and the Department of Motor Vehicles from available states, as sourced by [Atlas EV Hub](https://www.atlasevhub.com/materials/state-ev-registration-data/).
- 33774 Total ZIP codes
- 27299 ZIP codes without EV registration
-  6475 ZIP codes with EV registration

Dataset is a 33774x32 matrix, with columns (0 to 31)

|Column| Variable List | Description |
| :- | :- | --- |
| 0 | zip | ZIP code |
| 1 | evs_reg | number of EVs registered in 2022 |
| 2 | tot_pop | total population |
| 3 | tot_pop_16up | total population of 16 y/o and up |
| 4 | tot_pop_18up | total population of 18 y/o and up |
| 5 | num_house | number of households |
| 6 | med_income | median income by household |
| 7 | per_10k_income | \% of households earning less than \\$10,000 |
| 8 | per_15k_income | \% of Households Earning \\$10,000 to \\$14,999 |
| 9 | per_25k_income | \% of Households Earning \\$15,000 to \\$24,999 |
| 10 | per_35k_income | \% of Households Earning \\$25,000 to \\$34,999 |
| 11 | per_50k_income | \% of Households Earning \\$35,000 to \\$49,999 |
| 12 | per_75k_income | \% of Households Earning \\$50,000 to \\$74,999 |
| 13 | per_100k_income | \% of Households Earning \\$75,000 to \\$99,999 |
| 14 | per_150k_income | \% of Households Earning \\$100,000 to \\$149,999 |
| 15 | per_200k_income | \% of Households Earning \\$150,000 to \\$199,999 |
| 16 | per_200kup_income | \% of Households Earning \\$200,000 or more |
| 17 | pop_18_24 | Population 18 to 24 years |
| 18 | pop_18_24_nohs | 18 to 24 years - Less than high school graduate |
| 19 | pop_18_24_hsgrad | 18 to 24 years - High school graduate (includes equivalency) |
| 20 | pop_18_24_adgrad | 18 to 24 years - Some college or associate's degree |
| 21 | pop_18_24_bsup| 18 to 24 years - Bachelor's degree or higher |
| 22 | pop_25up | Population 25 years and over |
| 23 | pop_25up_no | 25 years and over - Less than 9th grade |
| 24 | pop_25up_nohs | 25 years and over - 9th to 12th grade, no diploma |
| 25 | pop_25up_hsgrad | 25 years and over - High school graduate (includes equivalency) |
| 26 | pop_25up_some | 25 years and over - Some college, no degree |
| 27 | pop_25up_adgrad | 25 years and over - Associate's degree |
| 28 | pop_25up_bsgrad | 25 years and over - Bachelor's degree |
| 29 | pop_25up_grad | 25 years and over - Graduate or professional degree |
| 30 | pop_25up_hsup | 25 years and over - High school graduate or higher |
| 31 | pop_25up_bsup | 25 years and over - Bachelor's degree or higher |

<a name='3'></a>
## Using EV-registration
*under construction*

<a name='4'></a>
## Note on the limitations of spatial analysis using ZIP codes
Contrary to common belief, ZIP codes **do not** represent geographical areas, but correspond to mail delivery routes. Some problems using ZIP codes as geospatial units include:<br>
- overlapping geographical areas,<br>
- spatial subsets of geographical areas,<br>
- constructs with no physical address (such as 00095, which represents mail for the Navy),<br>
- rural areas without postal routes or underdeveloped areas with no mail delivery, and <br>
- frequent realigns, merges, or splits by the United States Postal Service to meet changing needs.

As a consequence, ZIP codes are not the ideal form of spatial representation for human behavior. So why do we continue to use them? Simply put, ZIP codes are familiar to the general population, easily collected for data analysis, and most importantly: *may be the only geospatial unit that a business has to work with*. 

More ideal measures, such as [ZIP code tabulation areas (ZCTAs)](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) (generalized area representations of ZIP code service areas) or [Census Block Groups](https://www.census.gov/geographies/reference-maps/2020/geo/2020-census-block-maps.html) (the smallest geospatial area the Burea of the Census collects), are less familiar to the general population. For further information, I recommend reading [Stop using Zip Codes for GeoSpatial analysis](https://carto.com/blog/zip-codes-spatial-analysis) for examples of real-world complications of using ZIP codes, but more importantly, for useful tips for utlizing more accurate geospatial metrics.

In the case of our dataset, vehicle registration is currently aggregated on the ZIP level, but may provide a useful "jumping off" point until vehicle registrations are further refined in the future.

<a name='5'></a>
## Licensing
This project is created under the MIT License. Copyright 2023 [Stephen Allen](https://github.com/stal2478)
