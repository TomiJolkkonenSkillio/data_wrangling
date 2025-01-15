import pandas as pd
import numpy as np
import users
import products
from faker import Faker
from datetime import datetime

fake = Faker()

# Transactions data
def get_transactions():
    num_transactions = 200
    transaction_ids = np.arange(1, num_transactions + 1)
    user_id_choices = np.random.choice(users.get_users(user_ids), num_transactions)
    product_id_choices = np.random.choice(products.get_products['product_id'], num_transactions)
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


    return(transactions)