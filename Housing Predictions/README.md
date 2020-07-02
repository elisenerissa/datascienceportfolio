# Project 2 - Ames Housing Data and Kaggle Challenge



## Context and Scope

This data-science research and finding is conducted for **a group of stakeholders in a real estate company** who would like to find out the factors that affect the house prices in Ames so that they are able to:
1. **Estimate a good selling price** for sellers based on the features of the house
2. **Advise sellers on how to improve/modify** their houses to fetch better prices in the market
3. **Advise buyers on the things to look out** for while buying a house (neighborhod, home features/qualities)



## Problem Statement

We want to find the factors that affect house pricing in Ames, Iowa. Inituitively, based on property trend, we know that neighbourhood and the size of the house affect property prices. So at the end of this report, we should be able to answer the following questions.
1. Do neighbourhood and the size of the house affect property prices in Ames?
2. What are the other important factors that will help to boost the property prices in Ames?
3. What are the factors that will hurt the price of a house in Ames? 


---

## Content of Notebook

- [Train data](./datasets/train.csv)
    - [Data Import & Cleaning](#Data-Import-and-Cleaning)
    - [Exploratory Data Analysis & Data Visualization](#Exploratory-Data-Analysis-and-Visualizations)
    - [Pre-processing](#Pre-processing)
    - [Modeling](#Train-Modelling)
- [Test data](./datasets/train.csv)
    - [Data Import and Cleaning](#Test-Data-Import-and-Cleaning)
    - [Pre-processing](#Pre-processing)
    - [Kaggle Submission](#Predictions-and-Kaggle-Submission)
- [Inferential Visualizations](#Inferential-Visualizations)
- [Conclusion](#Conclusion)
- [Business Recommendations](#Business-Recommendations)
- [Future Steps](#Future-Steps)



## Datasets

#### Provided Data

For this project, we are analysing the following datasets:

- [Train Data](./datasets/train.csv)
- [Test Data](./datasets/test.csv)


#### Kaggle Submission

- [Kaggle Submission](./datasets/kaggle_submission.csv)


## Data Dictionary 


### Discrete Variables
|Feature|Column Name|Type|Description|
|---|---|---|---|
|**Order**|id|*discrete*|Observation Number| 
|**Year Built**|year_built|*discrete*|Original construction date|
|**Year Remod/Add**|year_remod/add|*discrete*|Remodel date (same as construction date if no remodeling or additions)|
|**Basement Full Bathrooms**|bsmt_full_bath|*discrete*|Number of full bathrooms at the basement|
|**Basement Half Bathrooms**|bsmt_half_bath|*discrete*|Number of half bathrooms at the basement|
|**Full Bathrooms**|full_bath|*discrete*|Number of full bathrooms above grade|
|**Half Bathrooms**|half_bath|*discrete*|Number of half bathrooms above grade|
|**Bedroom**|bedroom_abvgr|*discrete*|Number of bedrooms above grade (does not include basement bedrooms|
|**Kitchen**|kitchen_abvgr|*discrete*|Number of ktchens above grade |
|**Total Rooms above grade**|totrms_abvgrd|*discrete*|Number of total rooms above grade (does not include bathrooms |
|**Fireplaces**|fireplaces|*discrete*|Number of fireplaces|
|**Garage Year Built**|garage_yr_blt|*discrete*|Year garage was built (YYYY)|
|**Garage Cars**|garage_cars|*discrete*|Size of garage in car capacity|
|**Month Sold**|mo_sold|*discrete*|Month Sold (MM)|
|**Year Sold**|yr_sold|*discrete*|Year Sold(YYYY)|

### Continous Variables
|Feature|Column Name|Type|Description|
|---|---|---|---|
|**Lot Frontage**|lot_frontage|*continuous*|Linear feet of street connected to property| 
|**Lot Area**|lot_area|*continuous*|Lot size in square feet| 
|**Masonry Veneer Area**|mas_vnr_area|*continuous*|Masonry veneer area in square feet| 
|**Basement Finish SF 1**|bsmtfin_sf_1|*continuous*|Type 1 finished square feet| 
|**Basement Finish SF 2**|bsmtfin_sf_2|*continuous*|Type 2 finished square feet| 
|**Basement Unfinished SF**|bsmtfin_unf_sf|*continuous*|Unfinished square feet of basement area| 
|**Total Basement SF**|total_bsmt_sf|*continuous*|Total square feet of basement area|
|**1st Floor SF**|1st_flr_sf|*continuous*|First Floor square feet|
|**2nd Floor SF**|2nd_flr_sf|*continuous*|Second Floor square feet|
|**Low Quality Finish SF**|low_qual_fin_sf|*continuous*|Low quality finished suqare feet (all floors|
|**Gr Liv Area**|gr_liv_area|*continuous*|Above grade (ground) living area square feet|
|**Garage Area**|garage_area|*continuous*|Size of garage in square feet|
|**Wood Deck SF**|wood_deck_sf|*continuous*|Wood deck area in square feet|
|**Open Porch SF**|open_porch_sf|*continuous*|Open porch area in square feet|
|**Enclosed Porch**|enclosed_porch|*continuous*|Enclosed Porch area in square feet|
|**3-Ssn Porch**|3ssn_porch|*continuous*|Three season porch area in square feet|
|**Screen Porch**|screen_porch|*continuous*|Screen porch area in square feet|
|**Pool Area**|pool_area|*continuous*|Pool area in square feet|
|**Misc Val**|misc_val|*continuous*|Value of miscellaneous feature|
|**SalePrice**|saleprice|*continuous*|Sale Price $$|

### Ordinal Variables

|Feature|Column Name| Variable Type|Description|Values Description|
|---|---|---|---|---|
|**Lot Shape**|lot_shape|*ordinal*|General shape of property|**Reg** - Regular, **IR1**- Slightly irregular, **IR2**-  Moderately Irregular, **IR3** - Irregular|
|**Utilities**|utilities|*ordinal*|Type of utilities available|**AllPub** - All public Utilities (E,G,W,& S), **NoSewr**- Electricity, Gas, and Water (Septic Tank), **NoSeWa**- Electricity and Gas Only, **ELO** - Electricity only|
|**Land Slope**|land_slope|*ordinal*|Slope of property|**Gtl** - Gentle Slope, **Mod**- Moderate Slope, **Sev**- Severe Slope|
|**Overall quality**|overall_qual|*ordinal*|Rates the overall material and finish of the house|**Very Excellent, Excellent, Very Good, Good, Above Average, Average, Below Average, Fair, Poor, Very Poor** (Scale 10 to 1)|
|**Overall Condition**|overall_cond|*ordinal*|Rates the overall condition of the house|**Very Excellent, Excellent, Very Good, Good, Above Average, Average, Below Average, Fair, Poor, Very Poor** (Scale 10 to 1)|
|**External Quality**|exter_qual|*ordinal*|Evaluates the quality of the material on the exterior|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor|
|**External Condition**|exter_cond|*ordinal*|Evaluates the present condition of the material on the exterior|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor|
|**Basement Quality**|bsmt_qual|*ordinal*|Evaluates the height of the basement|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor,**NA**- No Basement|
|**Basement Condition**|bsmt_cond|*ordinal*|Evaluates the general condition of the basement|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor,**NA**- No Basement|
|**Basement Exposure**|bsmt_exposure|*ordinal*|Refers to the walkout or garden level walls|**Gd**- Good Exposure, **Av**- Average Exposure, **Mn**- Minimum Exposure, **No**- No Exposure,**NA**- No Basement|
|**Basement Finish Type 1**|bsmtfin_type_1|*ordinal*|Rating of basement finished area|**GLQ**- Good Living Quarters, **ALQ**- Average Living Quarters, **BLQ**- Below Average Living Quarters, **Rec**- Average Rec Room,**LwQ**- Low Quality, **Unf**- Unfinished, **NA**- No Basement|
|**Basement Finish Type 2**|bsmtfin_type_2|*ordinal*|Rating of basement finished area(if multople types)|**GLQ**- Good Living Quarters, **ALQ**- Average Living Quarters, **BLQ**- Below Average Living Quarters, **Rec**- Average Rec Room,**LwQ**- Low Quality, **Unf**- Unfinished, **NA**- No Basement|
|**Heating QC**|heating_qc|*ordinal*|Heating quality and condition|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor|
|**Electrical**|electrical|*ordinal*|Electrical system|**SBrkr** - Standard Circuit Breakers & Romex, **FuseA**- Fuse Box over 60 AMP and all Romex wiring (Average), **FuseF**- 60 AMP Fuse Box and mostly Romex wiring (Fair), **FuseP**- 60 AMP Fuse Box and mostly knob & tube wiring (poor), **Mix**- Mixed|
|**Kitchen Quality**|kitchen_qual|*ordinal*|Quality of kitchen|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor|
|**Functional**|functional|*ordinal*|Home functionality (Assume typical unless deductions are warranted)|**Typ** - Typical Functionality, **Min1**- Minor Deductions 1, **Min2**- Minor Deductions 2, **Mod**- Moderate Deductions, **Maj1**- Major Deductions 1,**Maj2**- Major Deductions 2,**Sev**- Severely Damaged, **Sal**- Salvage only|
|**Fireplace Quality**|fireplace_qual|*ordinal*|Quality of fireplace|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor, **NA**- No fireplace|
|**Garage Finish**|garage_finish|*ordinal*|Interior finish of the garage|**Fin** - Finished, **RFn**- Rough Finished, **Unf**- Unfinished, **NA**- No garage|
|**Garage Quality**|garage_qual|*ordinal*|Quality of garage|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor, **NA**- No garage|
|**Garage Condition**|garage_cond|*ordinal*|Quality of garage|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor, **NA**- No garage|
|**Paved Drive**|paved_drive|*ordinal*|Paved driveway|**Y** - Paved, **P**- Partial Pavement, **N**- Dirt/Gravel|
|**Pool QC**|pool_qc|*ordinal*|Pool Quality|**Ex** - Excellent, **Gd**- Good, **TA**- Average/Typical, **Fa**- Fair, **Po**- Poor, **NA**- No pool|
|**Fence**|fence|*ordinal*|Fence quality|**GdPrv** - Good Privacy, **MnPrv**- Minimum Privacy, **GdWo**- Good Wood, **MnWw**- Minimum Wood/Wire, **NA**- No fence|

### Nominal Variables

|Feature|Column Name|Type|Description|
|---|---|---|---|
|**PID**|pid|*nominal*|Parcel identification number| 
|**Ms Subclass**|ms_subclass|*nominal*|Identifies the type of dwelling involved in the sale|
|**Ms Zoning**|ms_zoning|*nominal*|Identifies the general zoning classification of the sale|
|**Street**|street|*nominal*|Type of road access to property|
|**Alley**|alley|*nominal*|Type of alley access to property|
|**Land Contour**|land_contour|*nominal*|Flatness of the property|
|**Lot Configuration**|lot_config|*nominal*|Lot Configuration|
|**Neighborhood**|neighborhood|*nominal*|Physical locations within Ames city limits(map available)|
|**Condition 1**|condition_1|*nominal*|Proximisty to various conditions|
|**Condition 2**|condition_2|*nominal*|Proximisty to various conditions(if more than one is present)|
|**Building Type**|bldg_type|*nominal*|Type of dwelling|
|**House Style**|house_style|*nominal*|Style of dwelling|
|**Roof Style**|roof_style|*nominal*|Type of roof|
|**Roof Material**|roof_matl|*nominal*|Roof Material|
|**Exterior 1**|exterior_1st|*nominal*|Exterior covering on house|
|**Exterior 2**|exterior_2nd|*nominal*|Exterior covering on house(if more than one materials|
|**Masonry Vaneer Type**|mas_vnr_type|*nominal*|Masonry Veneer Type|
|**Foundation**|foundation|*nominal*|Type of foundation|
|**Heating**|heating|*nominal*|Type of Heating|
|**Central Air**|central_air|*nominal*|Central Air Conditioning|
|**Garage Type**|garage_type|*nominal*|Garage Location|
|**Miscellaneous Feature**|misc_feature|*nominal*|Miscellaneous feature not covered in other categories|
|**Sale Type**|sale_type|*nominal*|Type of sale|

---

## Business Recommendations

We wanted to know the factors that actually affect the housing price in Ames. Intuitively, in most places, we all know that **the size of the house and the price of the land that is determined by the neighbourhood will affect house prices.** This "known fact" has proven to be true in Ames as well. In fact, the living area **the strongest factor that will affect the price of the house.** The neighbourhood also does affect the house prices in Ames. 

We also know from the model which neighbourhood has the highest property value. It seems like **houses located at Northridge Heights and Stone Brook seem to be valued a lot higher.** In contrary, being located **at Northwest Ames seems to lower the value of the house.**

**Other important factors that boost home prices besides obvious factors such as size of living area, overall home quality and age of the house are:**
1. Masonry veneer made of brick face or stone 
2. Having a big basement
3. Big garage with a good interior finish of the garage (Detached garage is also an added bonus)
4. Good neighborhood: Northridge Heights and Stone Brook 
   - It seems that Northridge Heights and Stone Brook estate are near to Gilbert School District which is top school in Iowa (Source: [Ames Tribune](https://www.amestrib.com/news/20200121/gilbert-and-ames-ranked-as-top-school-districts-in-iowa))
   
5. Fireplace quality 
> It also seems like people in the United States still feel that fireplaces bring luxurious feel to a house. The National Association of Realtors conducted a 2013 survey of homeowners’ desire for a fireplace. Participants listed fireplaces as one of their most sought-after features, with **40 percent stating that they would pay extra** if the home had one(Source: [Angie's List](https://www.angieslist.com/articles/do-fireplaces-make-your-home-value-hot.htm))


**Neighborhood that will devalue the houseprices are:** 
Northwest Ames, Somerset, Old Town and North Ames

## Future Steps

This model will do reasonably well in estimating home prices in Ames (in the context of advising home sellers on deciding on homeprices). It also gave us valuable insights in terms of the factors that will affect home prices in Ames. Hence, I would think that this model has largely addressed our business problems. 

However, as mentioned earlier, it definitely can be improved **given more time and data.** Some features in the model do seem redundant. Some features seem to be affecting the accuracy of the model. If I am given more time to improve this model, I would **consider removing building type, land contour, masonry veneer type from my model** until we are able to collect more conclusive samples that gives more information on how these features will affect home prices. I would also consider **making some changes to how total rooms above grade is being "fed" into the model.** From the **feature coefficient of the model, it shows that the number of rooms affect the house price negatively.** This does not really make sense. Hence, as mentioned in the inferential statistics section above, I would consider imputing the observations above 8 rooms differently.

All in all, there is definitely a lot of improvements that can be done to this model. However, this model is able to provide the stakeholders (in this context) a good answer to the business problems.

I do not think that **this model can be used to predict other cities accurately as house prices vary vastly across different cities in United States and globally** depending on the land prices and the standard of living of each city. However, there are insights that will be applicable to other cities in the United States. For example, as seen in the model and various sources, we know that **having a finished basement and having a fireplace with good quality** will generally increase the value of the property in the US. (Source: [The balance SMB](https://www.thebalancesmb.com/pros-of-finishing-a-basement-for-property-investors-2124861) and [Angie's List](https://www.angieslist.com/articles/do-fireplaces-make-your-home-value-hot.htm))

