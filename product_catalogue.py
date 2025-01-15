import random
import numpy as np
import pandas as pd
from faker import Faker

# Create a Faker instance
fake = Faker()

# Define product categories
categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Toys', 'Groceries', 'Beauty', 'Sports']

# Function to generate a product catalog
def get_product_catalog(num_products=20):
    catalog = []
    for _ in range(num_products):
        product = {
            "Product ID": fake.uuid4(),  # Unique product ID
            "Product Name": fake.unique.word().title() if random.random() > 0.2 else None,  # Product name
            "Category": random.choice(categories) if random.random() > 0.2 else None,  # Random category
            "Price": round(random.uniform(5.0, 500.0), 2) if random.random() > 0.2 else None,  # Random price between 5€ and 500€
        }
        catalog.append(product)
        df_catalog = pd.DataFrame(catalog)

    return df_catalog

def get_product_ids(df_catalog):
    # Get product IDs from the catalog
    product_ids = df_catalog["Product ID"].tolist()
    return product_ids  

def main():
    # Generate product catalog with 100 products
    #product_catalog = get_product_catalog(num_products=100)
    # Save to a CSV file
    # df_catalog.to_csv("product_catalog_with_rubbish.csv", index=False)
    pass

if __name__ == "__main__":
    main()