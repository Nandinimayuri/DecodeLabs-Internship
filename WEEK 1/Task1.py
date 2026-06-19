import pandas as pd
import numpy as np
from scipy.stats import zscore
df=pd.read_excel(r"C:\Users\manas\OneDrive\Desktop\Decodelabs project\Dataset\Product-Sales-Region.xlsx")
print("Original Shape:",df.shape)
print(df.isnull().sum())
#handling missing values
df["Promotion"]=df["Promotion"].fillna("No Promotion")
#outliers
numeric_cols=["Quantity","UnitPrice","Discount","TotalPrice","ShippingCost"]
z_scores=np.abs(zscore(df[numeric_cols]))
df=df[(z_scores < 3).all(axis=1)]
print("Shape After Outlier Removal:", df.shape)
#features

#feature 1: Delivery Days
df["DeliveryDays"]=(df["DeliveryDate"] - df["OrderDate"]).dt.days

#feature 2: Revenue After Shipping
df["NetRevenue"]=(df["TotalPrice"] - df["ShippingCost"])
 
#feature 3: Discount Amount
df["DiscountAmount"]=(df["Quantity"]*df["UnitPrice"]*df["Discount"] )

#feature 4 price of each item
df["PricePerItem"]=(df["TotalPrice"] /df["Quantity"])
    
#summary
print("\nSummary Statistics")
print(df[numeric_cols].describe())
#cleaned dataset
df.to_excel("WEEK 1/Cleaned_Product_Sales_Region.xlsx",index=False)
print("\nDataset cleaned successfully!")
