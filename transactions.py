import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Transactions data
def get_transactions():
    
    num_transactions = 20
    transaction_ids = np.arange(1, num_transactions + 1)
    user_ids = np.random.randint(0, 21,size=num_transactions)
    product_ids = np.random.randint(0, 21,size=num_transactions)
    quantities = np.random.randint(1, 5, size=num_transactions)  # Random quantities between 1 and 4
    transaction_dates = [
        fake.date_between(start_date='-25y', end_date='-1y') for _ in range(num_transactions)
    ]

    transactions = pd.DataFrame({
        'transaction_id': transaction_ids,
        'user_id': user_ids,
        'product_id': product_ids,
        'quantity': quantities,
        'transaction_date': transaction_dates
    })


    return transactions

def main():
    # Generate transactions data with 20 transactions
    transactions_data = get_transactions()
    # Save to a CSV file
    transactions_data.to_csv("transactions_data_with_rubbish.csv", index=False)


if __name__ == "__main__":
    main()