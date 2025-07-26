import os
import pandas as pd
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]  # Create/use a DB called 'ecommerce'

# Path to CSV folder
csv_folder = "archive"

# Mapping: collection name -> CSV filename
csv_files = {
    "distribution_centers": "distribution_centers.csv",
    "inventory_items": "inventory_items.csv",
    "order_items": "order_items.csv",
    "orders": "orders.csv",
    "products": "products.csv",
    "users": "users.csv"
}

# Load each CSV and insert into corresponding collection
for collection, filename in csv_files.items():
    df = pd.read_csv(os.path.join(csv_folder, filename))
    db[collection].insert_many(df.to_dict("records"))
    print(f"Inserted {len(df)} records into {collection}")
