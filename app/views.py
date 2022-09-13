from django.shortcuts import render
from django.http import JsonResponse
import json
from app.utils import predict_price

features = {
    "Item_Weight" : {
        "type": "numeric"
        },
    "Item_Fat_Content" : {
        "type": "select", 
        "options": ["Low_Fat", "Regular"]
        },
    "Item_Visibility" : {
        "type": "numeric"
        },
    "Item_Type": {
        "type": "select", 
        "options": ["Dairy", "Soft_Drinks", "Meat", "Fruits_and_Vegetables", "Household", "Baking_Goods", "Snack_Foods", "Frozen_Foods", "Breakfast", "Health_and_Hygiene", "Hard_Drinks", "Canned", "Breads", "Starchy Foods", "Others", "Seafood"]
        },
    "Item_MRP" : {
        "type": "numeric"
        },
    "Outlet_Size": {
        "type": "select", 
        "options": ["Medium", "High", "Small"]
        },
    "Outlet_Location_Type": {
        "type": "select", 
        "options": ["Tier_1", "Tier_2", "Tier_3"]
        },
    "Outlet_Type": {
        "type": "select", 
        "options": ["Supermarket_Type1", "Supermarket_Type2", "Supermarket_Type3", "Grocery_Store"]
        },
    "Outlet_Establishment_Year" : {
        "type": "numeric"
        },
    "Item_Outlet_Sales" : {
        "type": "output"
        },            
}

def homepage(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            "response": "Hello World!!!", 
            "features": features,
            "hostname": f"http://{request.get_host()}/"
        }
        return render(request, 'index.html', context)
    if request.method == 'POST':
        body = json.loads(request.body)
        
        return JsonResponse({
            "predictions": {
                "id":body['i'],
                "value":predict_price(body)
                }, 
            "features": features
            })