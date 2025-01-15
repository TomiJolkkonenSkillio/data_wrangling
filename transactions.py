import pandas as pd
import numpy as np
import product_catalogue
import users
from faker import Faker

fake = Faker()

# Transactions data
def get_transactions():
    products=product_catalogue.get_product_catalog()
    product_ids=product_catalogue.get_product_ids(products)
    users_data=users.get_users()
    users_ids=users.get_users_ids(users_data)

    num_transactions = 20
    transaction_ids = np.arange(1, num_transactions + 1)
    user_id_choices = users_ids
    product_id_choices = product_ids
    quantities = np.random.randint(1, 5, size=num_transactions)  # Random quantities between 1 and 4
    transaction_dates = [
        fake.date_between(start_date='-25y', end_date='-1y') for _ in range(num_transactions)
    ]

    transactions = pd.DataFrame({
        'transaction_id': transaction_ids,
        'user_id': user_id_choices,
        'product_id': product_id_choices,
        'quantity': quantities,
        'transaction_date': transaction_dates
    })


    return users_data, products, transactions