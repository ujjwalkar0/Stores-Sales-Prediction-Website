from django.conf import settings
import pickle as pk
import sklearn
import pandas as pd

# Encoding
Item_Fat_Content = {'Low_Fat': 0, 'Regular': 1}
Item_Type = {'Dairy':4,'Soft_Drinks':14,'Meat':10,'Fruits_and_Vegetables':6,'Household':9,'Baking_Goods':0,'Snack_Foods':13,'Frozen_Foods':5,'Breakfast':2,'Health_and_Hygiene':8,'Hard_Drinks':7,'Canned':3,'Breads':1,'Starchy_Foods':15,'Others':11,'Seafood':12}
Outlet_Size = {'Medium': 1, 'High': 0, 'Small': 2}
Outlet_Location_Type = {'Tier_1':0,'Tier_3':2,'Tier_2':1}
Outlet_Type = {'Supermarket_Type1':1,'Supermarket_Type2':2,'Grocery_Store':0,'Supermarket_Type3':3}

# Standardization Normalization

with open(f'{settings.BASE_DIR}/standard_Item_Weight.pk', 'rb') as f:
    standard_Item_Weight = pk.load(f)

with open(f'{settings.BASE_DIR}/standard_Item_Visibility.pk', 'rb') as f:
    standard_Item_Visibility = pk.load(f)

with open(f'{settings.BASE_DIR}/normal_Item_MRP.pk', 'rb') as f:
    normal_Item_MRP = pk.load(f)

with open(f'{settings.BASE_DIR}/rfr.pk', 'rb') as f:
    rfr = pk.load(f)

def predict_price(data):

    # Encoding Categorical Data into numbers.
    data['Item_Fat_Content'] = Item_Fat_Content[data['Item_Fat_Content']]
    data['Item_Type'] = Item_Type[data['Item_Type']]
    data['Outlet_Size'] = Outlet_Size[data['Outlet_Size']]
    data['Outlet_Location_Type'] = Outlet_Location_Type[data['Outlet_Location_Type']]
    data['Outlet_Type'] = Outlet_Type[data['Outlet_Type']]

    # Year Established
    data['Years_Established'] = 2022 - int(data['Outlet_Establishment_Year'])

    data = pd.DataFrame(data, index=[data['i'],])
        
    # Standardization and Normalization
    data['Item_Weight'] = standard_Item_Weight.transform(data[['Item_Weight']])
    data['Item_Visibility'] = standard_Item_Visibility.transform(data[['Item_Visibility']])
    data['Item_MRP'] = normal_Item_MRP.transform(data[['Item_MRP']])

    
    data.drop(columns=['i', 'Outlet_Establishment_Year'], inplace=True)
    
    return rfr.predict(data)[0]