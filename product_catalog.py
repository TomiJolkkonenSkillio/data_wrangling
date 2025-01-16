import random
import numpy as np
import pandas as pd

# Define categories and products
categories = {
    "Electronics": [
        "Smartphone", "Laptop", "Wireless Earbuds", "Smartwatch",
        "LED TV", "Bluetooth Speaker", "Gaming Console", "Digital Camera"
    ],
    "Clothing": [
        "T-shirt", "Jeans", "Jacket", "Sneakers",
        "Hat", "Dress", "Socks", "Scarf"
    ],
    "Books": [
        "Fiction Novel", "Self-Help Book", "Biography", "Science Textbook",
        "Cookbook", "Graphic Novel", "Poetry Collection", "Children's Storybook"
    ],
    "Furniture": [
        "Sofa", "Dining Table", "Office Chair", "Bed Frame",
        "Coffee Table", "Bookshelf", "Wardrobe", "Recliner"
    ],
    "Toys": [
        "Building Blocks", "Action Figure", "Puzzle", "Stuffed Animal",
        "Remote Control Car", "Dollhouse", "Board Game", "Educational Toy"
    ],
    "Groceries": [
        "Bread", "Rice", "Milk", "Eggs",
        "Apples", "Pasta", "Coffee", "Cereal"
    ],
    "Beauty": [
        "Lipstick", "Foundation", "Shampoo", "Body Lotion",
        "Nail Polish", "Perfume", "Face Mask", "Hair Dryer"
    ],
    "Sports": [
        "Basketball", "Tennis Racket", "Yoga Mat", "Football",
        "Dumbbells", "Bicycle", "Running Shoes", "Water Bottle"
    ]
}

# Function to generate a products data
def get_product_catalog(num_products=20):
    catalog = []
    for _ in range(num_products):
        # Randomly choose a category and product
        category = random.choice(list(categories.keys()))
        product_name = random.choice(categories[category])
        product = {
            "product_id": np.random.randint(0, 21),
            "Product Name": product_name if random.random() > 0.2 else None,
            "Category": category if random.random() > 0.2 else None,
            "Price": round(random.uniform(5.0, 500.0), 2) if random.random() > 0.2 else None,  # Random price between 5€ and 500€
        }
        catalog.append(product)
        df_catalog = pd.DataFrame(catalog)

    return df_catalog
def main():
    # Generate products data with 20 products
    product_catalog = get_product_catalog(num_products=20)
    # Save to a CSV file
    product_catalog.to_csv("product_catalog_with_rubbish.csv", index=False)


if __name__ == "__main__":
    main()