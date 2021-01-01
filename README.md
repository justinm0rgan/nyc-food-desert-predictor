# NYC Food Desert Predictor
## Flatiron Capstone Project by Justin Morgan Williams
### January 2021

## In Progress 12/7/2020 - 1/6/2021

## Overview

Using low-income/low-access Census Tract's (CT's) greater then 1/2 a mile from supermarkets as a proxy, this study will predict food deserts in NYC's 5 boroughs. Food deserts are geographic areas where constituents have limited access to fresh, healthy and affordable foods. Typically, low-income populations face greater barriers in accessing healthy and affordable retailers, which can lead to food insecurity and higher disease rates. Crisis such as the COVID-19 pandemic can exacerbate these issues. A key finding in September 2020 report entitled [New York Food 20/20](https://static1.squarespace.com/static/572d0fcc2b8dde9e10ab59d4/t/5f7b27b9e0c3e05f19c5442f/1601906624464/ny2020-finalv2.pdf) was, despite the public's increased food standards and awakening to the threats of diet-related diseases, the pandemic bought forth longstanding tensions between the City's actions to ensure NYC residents have both _enough_, and the _right_ foods to eat. Therefore, emphasizing the implications for those living within food desert's and the importance of addressing access limitations to fresh, healthy and affordable foods. The data utilized comes from a [United States Department of Agriculture (USDA) & Economic Research Service (ERS)](https://www.ers.usda.gov/data-products/food-access-research-atlas/) 2017 study, identifying food deserts nationally at the CT level. Methods applied include sub-setting NYC 5 boroughs, exploratory data analysis (EDA) with extensive geospatial renderings, and developing a model to predict food deserts for low-income/low-access CT's within 1/2 a mile of supermarkets. Results found that more vulnerable CT include **low-income, low-access tracts with increased poverty, lower median income, higher proportion of kids (0-17) and those with higher proportions of people of color (POC)**. Recommendations and next steps include looking into incentives for supermarket expansion within the affected tracts, perhaps through an already established program such as [Food Retail Expansion to Support Health (FRESH)](https://edc.nyc/program/food-retail-expansion-support-health-fresh). As well as exploring opportunities for local community urban agriculture initiatives with youth involvement such as [Red Hook Farms](http://www.added-value.org/).

## Business Case

Identification of food deserts at the CT level in NYC is imperative to the improvement of food policy. Improved food policy could end food insecurity and encourage afflicted populations to choose diets rich in fresh and healthy foods. This could limit diseases of modernity thus reducing the strain on the healthcare industry which would in turn make our city more resilient to crisis such as the COVID-19 pandemic. However, simply finding food deserts identified previously in a recent dataset is inadquate. In order to mitigate future food insecurity and disease rates, changes to food policy need to be implemented in advance. For example, as it takes a number of years to build new supermarkets, the FRESH initiative should be revamped to identify locations that will become food deserts. Therefore, the model implemented within this study, will be trained on the aforementioned USDA dataset, and then can be applied to predicting food deserts at the CT level for newer American Community Survey data. 

## Data

The data used for this project came mostly from the USDA ERS _Food Research Atlas_ study. Additional 2010 CT geospatial data was obtained from [NYC OpenData](https://data.cityofnewyork.us/City-Government/2010-Census-Tracts/fxpq-c8ku) and merged with the USDA dataset to perform various geospatial visuals. 

USDA dataset included multiple _flag for food desert_ binary columns. This study was solely focused on low-access 1/2 mile from supermarkets, subsequently, many columns were dropped. The target variable was a combination of two variables

**Low-income tract** - A tract with either poverty rate of 20 percent or more, or a median family income less than 80 percent of surrounding metropolitan area median family income

**Low-access tract** - A tract with at least 500 people, or 33 percent of the population, living more than 1/2 mile from the nearest supermarket, super-center, or large grocery store.

The aforementioned inform the _target_ variable of:

**Low-income and low-access tract measured at .5 mile** (LILATracts_halfAnd10) - A low-income tract with at least 500 people, or 33 percent of the population, living more than 1/2 mile from the nearest supermarket, super-center, or large grocery store.

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
| 9  | LILATracts_halfAnd10 | Low income and low access tract measured at 1/2 mile for urban areas and 10 miles for rural areas            | Flag for food desert when considering low accessibility at 1/2 and 10 miles                                                                                                                                                        |
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

After substantial data cleaning and merging with 2010 CT geospatial shapefiles, basic EDA was employed. Boxplots showed many numeric features were riddled with outliers, however the decision was made to leave them be, as outliers are integral to this study. For instance, many columns dealing with low-access demographic subsets of the population are by definition outliers, to impute them as otherwise would simply erase their significance.  Geospatial analysis was used extensively to geographically visualize important features and their inherent relationships. Features were engineered that allowed better visual analysis of dataset, however complex interactions were avoided in lieu of model interpretability. 

After EDA, the cleaned dataset was bought into the modeling notebook, and all boolean classification columns that could lead to data leakage were dropped. Next various models were iterated on, these included: Logistic Regression with all features, a GridSearch model and subsequently a trimmed down version with Recursive Feature Elimination. Next was Decision Tree Classifier with GridSearch, which resulted in fantastic results. However, in hopes of getting a perfect prediction, Random Forest and XGBoost were also iterated over. The best model which had a near perfect F1 and Recall score (one False Negative, no False Positives), ended up being Decision Tree Classifier model with GridSearch being used for hyperparameter tuning. After this, predictions were geospatially visualized, and FRESH geometry was overlayed to see which CT classified as food deserts were not within its boundaries. 

## EDA Visualizations

### Binary Target 
<p align="center">
<img src="./images/binary_target.png" width="500">
</p>
High class imbalance with:

- 2165 CT
- 2134 not food deserts (0)
    - 25 N/A (parks etc)
- 31 food deserts (1)

## Geographic distribution
<p align="center">
<img src="./images/map_target_trans_no.png" width="800">
</p>
<p align="center">
<img src="./images/food_desert_rate_county.png" width="600">
</p>

<u>Observations</u>
- No CT flagged for food desert in Manhattan
- Although most frequent in Kings and Queens counties, highest proportion in Richmond

### White per CT with Food Deserts
<p align="center">
<img src="./images/white_per_census_tract_&_food_deserts.png">
</p>

### Black per CT with Food Deserts
<p align="center">
<img src="./images/black_per_census_tract_&_food_deserts.png">
</p>

### Latinx per CT with Food Deserts
<p align="center">
<img src="./images/latinx_per_census_tract_&_food_deserts.png">
</p>

### Asian per CT with Food Deserts
<p align="center">
<img src="./images/asian_per_census_tract_&_food_deserts.png">
</p>

<u>Observations</u>
- Most food deserts in areas with low rate of white and asian populations
- Most food deserts in areas with high rate of black population
- Some food deserts in areas with high rate of latinx population

### Median Income vs. Poverty Rate
<p align="center">
<img src="./images/income_pov_rate.png" width="600">
</p>

<u>Observations</u>
- Highly negatively correlated features suggesting more significant weights in modeling

## Results
Our final model is Decision Tree Classifier (DTC) with GridSearch. 

#### Decision Tree Classifer Plot
<p align="center">
<img src="./images/decision_tree_plot.png">
</p>

Final model results indicate most efficient feature splitting on:

1) `lalowihalfshare` - Share of tract population that are low income individuals beyond 1/2 mile from supermarket

2) `lawhitehalfshare` - Share of tract population that are white beyond 1/2 mile from supermarke

3) `MedianFamilyIncome` - Tract median family income

4) `TractKids` - Total count of children age 0-17 in tract

5) `laseniorshalfshare` - Share of tract population that are seniors beyond 1/2 mile from supermarke

6) `PovertyRate` - Share of the tract population living with income at or below the Federal poverty thresholds for family size

7) `laaianhalf` - American Indian or Alaska Native population count beyond 1/2 mile from supermarket

8) `lahisphalf` - Hispanic or Latino ethnicity population count beyond 1/2 mile from supermarket

This highlights most important indicator of food deserts are share of tract that are low-access/low-income. Secondarily are share of tract that are white (or not white), followed by median income, count of kids, senior share, poverty rate, and finally by share of tract low-access American Indian/Alaskan Native or latinx.

This tells us that although that low-access and low-income are the primary indicators, share of white population within a given tract has a direct relation to weather or not it was classified as a food desert. That coupled with median income and poverty rate, count of kids/share of seniors and a few other demographic indicators, gives us almost a perfect result. 

<u>**Decision Tree Classifier Metrics**</u>

**F1** = .92

**Recall** = .85

**Decision Tree Classifer Confusion Matrix**
<p align="center">
<img src="./images/dtc_con_matrix_with_grid.png" width="600">
</p>

In this instance `F1` was chosen as the primary metric with `Recall` secondary. This is because with the goal of expanded FRESH coverage to areas identified as food deserts, or introducing urban agriculture initiatives, limitation of False Positives was of the utmost importance. We would not want to identify an area as a food desert, and start shifting resources to implement zoning or tax incentives only to find it is not in need of supermarket expansion. Therefore, utilizing `F1` as a primary metric to achieve a more harmonic mean was desirable. However, limiting False Negatives (not identfying a food desert when it is) was important as well. Therefore, `Recall` was chosen as a secondary metric to limit False Negatives.

### Geospatial depictions of Final Model Predictions
<p align="center">
<img src="./images/dtc_final_model_predictions.png">
</p>

Model predicted 30 (out of 31) values as True and 2134 as False.
- True Positive - 30 Olive CT are those that were predicted corectly 
- False Postive - 0 yellow CT that were incorrectly predicted as positve
- Food Desert - 31 black CT that are positive labels from the original dataset
- Not Food Desert - purple CT that are negative labels from the original dataset
- Missing Values - lightgrey CT that do not have values i.e. parks, cemetaries etc...

###  Geospatial depictions of Final Model Predictions with FRESH geometry overlay
<p align="center">
<img src="./images/compressed/dtc_final_model_predictions_with_fresh.png">
</p>

The above map shows us that most food deserts lay within FRESH boundaries, however there are some that do not, most prominently in Queens and Staten Island. That said, these food deserts classifications are based on a study conducted in 2017, and the FRESH data is recent, therefore this model would need to be run on newer data, then compared and contrasted with FRESH boundaries prior to invoking any policy changes. 

## Conclusions/Next Steps
Low-access and low-income are the primary drivers of food deserts, therefore prepetuating the inequities present in our economic system, racial demographics have a great influence as well. Meaning areas with higher proportions of white residents are less likely to be a food desert. Wicked issues such as _income_ and _poverty_  are outside the scope of this study, yet are also major drivers. Additionally, higher proportions of non-earners, i.e. kids (0-17)and seniors (65+), indicate more susceptability to becoming a food desert. Expansion of supermarkets encouraged through adjusted FRESH boundaries, will help increase accesss to fresh, healthy and affordable foods. This will address the top driver of food deserts, however the other drivers can only be mitigated through addressing the systemic inequities embedded within our system. 

Next steps include running modeling predictions on newer data, and contrasting with [Food Retail Expansion to Support Health (FRESH)](https://edc.nyc/program/food-retail-expansion-support-health-fresh) boundaries to identify CT in need. As well as, exploring opportunities for local community urban agriculture by looking at city owned sites that are suitable for urban agriculture within CT identified as food deserts. Using [Red Hook Farms](http://www.added-value.org/) as a model, these sites could be transformed into thriving community centers that help increase access to fresh, healthy and affordable foods. 

## For More Information
Please review full analysis in [EDA notebook](./notebooks/eda.ipynb), [Modeling notebook](./notebooks/modeling.ipynb) and [presentation](./slide_deck.pdf).

For any additional questions, please contact **Justin Williams - justinmorganwilliams@newschool.edu**

## Repository Structure

```
├── README.md                                    <- Top-level README for reviewers of this project
├── notebooks
│   ├── data_cleaning.ipynb                          <- Data cleaning in Jupyter notebook
│   ├── eda.ipynb                                    <- Exploratory data analysis in Jupyter notebook
│   ├── modeling.ipynb                               <- Modeling analysis in Jupyter notebook
├── slide_deck.pdf                               <- PDF version of project presentation
├── src                                          <- Functions imported into Jupyter Notebooks
└── images                                       <- Generated from code
```

