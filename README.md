# NYC Food Desert Predictor
# (Currently in process 12/9 - 1/6)
Flatiron Capstone Project: Develop regression models that predict food deserts at a census tract level for NYC 5 boroughs

## Overview

Food deserts are geographic areas where constituents have limited access to fresh, healthy and affordable foods. Typically, low-income populations face greater barriers in accessing healthy and affordable retailers, which can lead to food insecurity and higher disease rates. Crisis such as the COVID-19 pandemic can exacerbate these issues. A key finding in September 2020 report entitled [New York Food 20/20](https://static1.squarespace.com/static/572d0fcc2b8dde9e10ab59d4/t/5f7b27b9e0c3e05f19c5442f/1601906624464/ny2020-finalv2.pdf) was, desipite the public's increased food standards and awakening to the threats of diet-related diseases, the pandemic bought forth longstanding tensions between the City's actions to ensure NYC residents have both _enough_, and the _right_ foods to eat. Therefore, empasizing the salient nature of food desert's and the implications for those living within its boundaries. The data utilized was from a [United States Department of Agriculture (USDA) & Economic Research Service (ERS)](https://www.ers.usda.gov/data-products/food-access-research-atlas/) 2017 study, identifying food deserts nationally at the Census Tract (CT) level. Methods applied included subsetting NYC, exploratory data analysis (EDA) and developing a model to predict food deserts for low-income low-access CT's within 1/2 a mile of supermarkets. Results found that more vunerable populations include **low-income people of color with a higher proportion of kids (0-17) and no vehicle access**. Recomendations include _____.

## Business Case

Identification of food deserts at the CT level in NYC is imperative to improving food policy. Improved food policy could end food insecurity and encourage aflicted populations to chose diets rich in fresh and healthy foods. This could limit diseases of modernity thus reducing the strain on the healthcare industry which would in turn make our city more resilent to crisis such as the COVID-19 pandemic. 

## Data

The data used for this project came mostly from the USDA ERS _Food Research Atlas_ study. Additional 2010 CT geospatial data was obtained from [NYC OpenData](https://data.cityofnewyork.us/City-Government/2010-Census-Tracts/fxpq-c8ku) and merged with the USDA dataset to perform various geospatial visuals. 

USDA dataset included multiple _flag for food desert_ binary columns. This study was solely focused on low-access 1/2 mile from supermarkets, subsequently, many columns were dropped. The target variable was a combination of two vriables

**Low-income tract** - A tract with either poverty rate of 20 percent or more, or a median family income less than 80 percent of surrounding metropolitan area median family income

**Low-access tract** - A tract with at least 500 people, or 33 percent of the population, living more than 1/2 mile from the nearest supermarket, supercenter, or large grocery store.

The aforementioned inform the _target_ variable of:

**Low-income and low-access tract measured at .5 mile Urban** (LILATracts_halfAnd10) - A low-income tract with at least 500 people, or 33 percent of the population, living more than 1/2 mile from the nearest supermarket, supercenter, or large grocery store.

Specific columns and their respective definitions are specified below:

|    | Field                | LongName                                                                                                     | Description                                                                                                                                                                                                                       |
|----|----------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0  | CensusTract          | Census tract                                                                                                 | Census tract number                                                                                                                                                                                                               |
| 1  | State                | State                                                                                                        | State name                                                                                                                                                                                                                        |
| 2  | County               | County                                                                                                       | County name                                                                                                                                                                                                                       |
| 3  | Urban                | Urban tract                                                                                                  | Flag for urban tract                                                                                                                                                                                                              |
| 4  | POP2010              | Population, tract total                                                                                      | Population count from 2010 census                                                                                                                                                                                                 |
| 5  | OHU2010              | Housing units, total                                                                                         | Occupied housing unit count from 2010 census                                                                                                                                                                                      |
| 6  | GroupQuartersFlag    | Group quarters, tract with high share                                                                        | Flag for tract where >=67%                                                                                                                                                                                                        |
| 7  | NUMGQTRS             | Group quarters, tract population residing in, number                                                         | Count of tract population residing in group quarters                                                                                                                                                                              |
| 8  | PCTGQTRS             | Group quarters, tract population residing in, share                                                          | Percent of tract population residing in group quarters                                                                                                                                                                            |
| 9  | LILATracts_halfAnd10 | Low income and low access tract measured at 1/2 mile for urban areas and 10 miles for rural areas            | Flag for food desert when considering low accessibilty at 1/2 and 10 miles                                                                                                                                                        |
| 10 | LILATracts_Vehicle   | Low income and low access tract using vehicle access or low income and low access tract measured at 20 miles | Flag for food desert when considering vehicle access or at 20 miles                                                                                                                                                               |
| 11 | HUNVFlag             | Vehicle access, tract with low vehicle access                                                                | Flag for tract where >= 100 of households do not have a vehicle, and beyond 1/2 mile from supermarket                                                                                                                             |
| 12 | LowIncomeTracts      | Low income tract                                                                                             | Flag for low income tract                                                                                                                                                                                                         |
| 13 | PovertyRate          | Tract poverty rate                                                                                           | Share of the tract population living with income at or below the Federal poverty thresholds for family size                                                                                                                       |
| 14 | MedianFamilyIncome   | Tract median family income                                                                                   | Tract median family income                                                                                                                                                                                                        |
| 15 | LAhalfand10          | Low access tract at 1/2 mile for urban areas and 10 miles for rural areas                                    | Flag for low access tract at 1/2 mile for urban areas or 10 miles for rural areas                                                                                                                                                 |
| 16 | LATracts_half        | Low access tract at 1/2 mile                                                                                 | Flag for low access tract when considering 1/2 mile distance                                                                                                                                                                      |
| 17 | LATractsVehicle_20   | Low access tract using vehicle access and at 20 miles  in rural areas                                        | Flag for tract where >= 100 of households do not have a vehicle, and beyond 1/2 mile from supermarket; or >= 500 individuals are beyond 20 miles from supermarket ; or >= 33% of individuals are beyond 20 miles from supermarket |
| 18 | LAPOP05_10           | Low access, population at 1/2 mile for urban areas and 10 miles for rural areas, number                      | Population count beyond 1/2 mile for urban areas or 10 miles for rural areas from supermarket                                                                                                                                     |
| 19 | LALOWI05_10          | Low access, low-income population at 1/2 mile for urban areas and 10 miles for rural areas, number           | Low income population count beyond 1/2 mile for urban areas or 10 miles for rural areas from supermarket                                                                                                                          |
| 20 | lapophalf            | Low access, population at 1/2 mile, number                                                                   | Population count beyond 1/2 mile from supermarket                                                                                                                                                                                 |
| 21 | lapophalfshare       | Low access, population at 1/2 mile, share                                                                    | Share of tract population that are beyond 1/2 mile from supermarket                                                                                                                                                               |
| 22 | lalowihalf           | Low access, low-income population at 1/2 mile, number                                                        | Low income population count beyond 1/2 mile from supermarket                                                                                                                                                                      |
| 23 | lalowihalfshare      | Low access, low-income population at 1/2 mile, share                                                         | Share of tract population that are low income individuals beyond 1/2 mile from supermarket                                                                                                                                        |
| 24 | lakidshalf           | Low access, children age 0-17 at 1/2 mile, number                                                            | Kids population count beyond 1/2 mile from supermarket                                                                                                                                                                            |
| 25 | lakidshalfshare      | Low access, children age 0-17 at 1/2 mile, share                                                             | Share of tract population that are kids beyond 1/2 mile from supermarket                                                                                                                                                          |
| 26 | laseniorshalf        | Low access, seniors age 65+ at 1/2 mile, number                                                              | Seniors population count beyond 1/2 mile from supermarket                                                                                                                                                                         |
| 27 | laseniorshalfshare   | Low access, seniors age 65+ at 1/2 mile, share                                                               | Share of tract population that are seniors beyond 1/2 mile from supermarket                                                                                                                                                       |
| 28 | lawhitehalf          | Low access, White population at 1/2 mile, number                                                             | White population count beyond 1/2 mile from supermarket                                                                                                                                                                           |
| 29 | lawhitehalfshare     | Low access, White population at 1/2 mile, share                                                              | Share of tract population that are white beyond 1/2 mile from supermarket                                                                                                                                                         |
| 30 | lablackhalf          | Low access, Black or African American population at 1/2 mile, number                                         | Black or African American population count beyond 1/2 mile from supermarket                                                                                                                                                       |
| 31 | lablackhalfshare     | Low access, Black or African American population at 1/2 mile, share                                          | Share of tract population that are Black or African American beyond 1/2 mile from supermarket                                                                                                                                     |
| 32 | laasianhalf          | Low access, Asian population at 1/2 mile, number                                                             | Asian population count beyond 1/2 mile from supermarket                                                                                                                                                                           |
| 33 | laasianhalfshare     | Low access, Asian population at 1/2 mile, share                                                              | Share of tract population that are Asian beyond 1/2 mile from supermarket                                                                                                                                                         |
| 34 | lanhopihalf          | Low access, Native Hawaiian or Other Pacific Islander population at 1/2 mile, number                         | Native Hawaiian or Other Pacific Islander population count beyond 1/2 mile from supermarket                                                                                                                                       |
| 35 | lanhopihalfshare     | Low access, Native Hawaiian or Other Pacific Islander population at 1/2 mile, share                          | Share of tract population that are Native Hawaiian or Other Pacific Islander beyond 1/2 mile from supermarket                                                                                                                     |
| 36 | laaianhalf           | Low access, American Indian or Alaska Native population at 1/2 mile, number                                  | American Indian or Alaska Native population count beyond 1/2 mile from supermarket                                                                                                                                                |
| 37 | laaianhalfshare      | Low access, American Indian or Alaska Native population at 1/2 mile, share                                   | Share of tract population that are American Indian or Alaska Native beyond 1/2 mile from supermarket                                                                                                                              |
| 38 | laomultirhalf        | Low access, Other/Multiple race population at 1/2 mile, number                                               | Other/Multiple race population count beyond 1/2 mile from supermarket                                                                                                                                                             |
| 39 | laomultirhalfshare   | Low access, Other/Multiple race population at 1/2 mile, share                                                | Share of tract population that are Other/Multiple race beyond 1/2 mile from supermarket                                                                                                                                           |
| 40 | lahisphalf           | Low access, Hispanic or Latino population at 1/2 mile, number                                                | Hispanic or Latino ethnicity population count beyond 1/2 mile from supermarket                                                                                                                                                    |
| 41 | lahisphalfshare      | Low access, Hispanic or Latino population at 1/2 mile, share                                                 | Share of tract population that are of Hispanic or Latino ethnicity beyond 1/2 mile from supermarket                                                                                                                               |
| 42 | lahunvhalf           | Vehicle access, housing units without and low access at 1/2 mile, number                                     | Housing units without vehicle count beyond 1/2 mile from supermarket                                                                                                                                                              |
| 43 | lahunvhalfshare      | Vehicle access, housing units without and low access at 1/2 mile, share                                      | Share of tract housing units that are without vehicle and beyond 1/2 mile from supermarket                                                                                                                                        |
| 44 | lasnaphalf           | Low access, housing units receiving SNAP benefits at 1/2 mile, number                                        | Housing units receiving SNAP benefits count beyond 1/2 mile from supermarket                                                                                                                                                      |
| 45 | lasnaphalfshare      | Low access, housing units receiving SNAP benefits at 1/2 mile, share                                         | Share of tract housing units receiving SNAP benefits count beyond 1/2 mile from supermarket                                                                                                                                       |
| 46 | TractLOWI            | Tract low-income population, number                                                                          | Total count of low-income population in tract                                                                                                                                                                                     |
| 47 | TractKids            | Tract children age 0-17, number                                                                              | Total count of children age 0-17 in tract                                                                                                                                                                                         |
| 48 | TractSeniors         | Tract seniors age 65+, number                                                                                | Total count of seniors age 65+ in tract                                                                                                                                                                                           |
| 49 | TractWhite           | Tract White population, number                                                                               | Total count of White population in tract                                                                                                                                                                                          |
| 50 | TractBlack           | Tract Black or African American population, number                                                           | Total count of Black or African American population in tract                                                                                                                                                                      |
| 51 | TractAsian           | Tract Asian population, number                                                                               | Total count of Asian population in tract                                                                                                                                                                                          |
| 52 | TractNHOPI           | Tract Native Hawaiian and Other Pacific Islander population, number                                          | Total count of Native Hawaiian and Other Pacific Islander population in tract                                                                                                                                                     |
| 53 | TractAIAN            | Tract American Indian and Alaska Native population, number                                                   | Total count of American Indian and Alaska Native population in tract                                                                                                                                                              |
| 54 | TractOMultir         | Tract Other/Multiple race population, number                                                                 | Total count of Other/Multiple race population in tract                                                                                                                                                                            |
| 55 | TractHispanic        | Tract Hispanic or Latino population, number                                                                  | Total count of Hispanic or Latino population in tract                                                                                                                                                                             |
| 56 | TractHUNV            | Tract housing units without a vehicle, number                                                                | Total count of housing units without a vehicle in tract                                                                                                                                                                           |
| 57 | TractSNAP            | Tract housing units receiving SNAP benefits, number                                                          | Total count of housing units receiving SNAP benefits in tract                                                                                                                                                                     |

## Methodology

After subtantial data cleaning and merging of dataset with geospatial shapefiles, basic EDA was employed. Boxplots informed many numeric features were riddled with outliers, however the decision was consiously made to leave them be, as outliers were important to this study. For instance, if white population was extremely lwo in a CT that was flagged as a food desert, we would want to know that. Geospatial analysis was extensively used to overlay positive target CT's to be on many important features choropleth maps. Features were engineered that allowed better visual analysis of dataset, however aspects such as polynomials were avoided due to a desire to provide an easily interpreted model. 

After EDA the cleaned dataset was bought into the modeling notebook, and all boolean classification columns that could lead to data leakage were dropped. Various models were employed, firstly Logistic Regression which was then improved upon with Recursive Feature Elimination. Next Decision Tree Classifier was employed and concluded in similiar results. The best model by far, ended up being and XGBoost model that was tuned to account for the great deal of class imblanace. 

## Results

Key results included____.

**F1**

**Recall**

***
Questions to consider:
* How do you interpret the results?
* How confident are you that your results would generalize beyond the data you have?
***

### Binary Target 
![Binary Target](./images/binary_target.png)

<u>Observations</u>
- 2165 CT
- 2134 not food deserts (0)
    - 25 N/A (parks etc)
- 31 food deserts (1)



### Whitie per CT with Food Deserts
![graph1](./images/food_deserts,_white_per_census_tract.png)

<u>Observations</u>
- Most food deserts in areas with low rate of white population

### Geospatial (kids)
![graph1](./images/viz1.png)

<u>Observations</u>
- TBA

### Vehicle Access (maybe something other then geospatial?)
![graph1](./images/viz1.png)

<u>Observations</u>
- TBA

### Final Model
![graph1](./images/xg_boost_features.png)

<u>Observations</u>
- TBA

## Conculsions/Next Steps

Provide your conclusions about the work you've done, including any limitations or next steps.

***
Questions to consider:
* What would you recommend the business do as a result of this work?
* What are some reasons why your analysis might not fully solve the business problem?
* What else could you do in the future to improve this project?
***

## For More Information
Please review full analysis in [EDA notebook](./eda.ipynb), [Modeling notebook](./modeling.ipynb) and [presentation](./slide_deck.pdf).

For any additional questions, please contact **Justin Williams - justinmorganwilliams@newschool.edu**

## Repository Structure

```
├── README.md                                    <- Top-level README for reviewers of this project
├── data_cleaning.ipynb                          <- Data cleaning in Jupyter notebook
├── eda.ipynb                                    <- Exploratory data analysis in Jupyter notebook
├── modeling.ipynb                               <- Modeling analysis in Jupyter notebook
├── slide_deck.pdf                               <- PDF version of project presentation
├── data                                         <- Both sourced externally and generated from code
└── images                                       <- Both sourced externally and generated from code
```

