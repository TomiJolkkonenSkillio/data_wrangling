import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime

fake = Faker()

# User data
def get_users():
    total_users = 20
    user_ids = np.arange(1, total_users + 1)
    names = [fake.name() for _ in range(total_users)]
    emails = [fake.email() for _ in range(total_users)]
    signup_dates = [fake.date_between(start_date='-25y', end_date='-1y') for _ in range(total_users)]

    users = pd.DataFrame({
        'user_id': user_ids,
        'name': names,
        'email': emails,
        'signup_date': signup_dates
    })

    return users

def main():
    # Generate user data with 20 users
    users_data = get_users()
    # Save to a CSV file
    users_data.to_csv("users_data_with_rubbish.csv", index=False)


if __name__ == "__main__":
    main()