import re
import numpy as np
import pandas as pd
import datetime as datetime


def read_products_data():
    file_path = 'users_data_with_rubbish.csv'
    df = pd.read_csv(file_path)
    
    return df

def get_data_description(df):
    description = df.describe()
    print(description)

def convert_signupdate(df):
    df['signup_date'] = df['signup_date'].apply(lambda x: pd.to_datetime(x, errors='coerce'))
    return df

def convert_email(df):
    # regex for email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # conversion to email column
    df['email'] = df['email'].apply(lambda email: email.strip() if isinstance(email, str) and re.match(pattern, email) else np.nan)
    return df  # Return the updated DataFrame

def get_number_of_missing_values(df):
    missing_values = df.isna().sum()
    print(missing_values)

def handle_dublicate_values_in_id(df):
    # take off duplicates, keep the first one on user_id column
    df = df.drop_duplicates(subset='user_id', keep='first')
    return df

def main():
    dataframe = read_products_data()
    dataframe = convert_signupdate(dataframe)
    dataframe = convert_email(dataframe)
    
    get_data_description(dataframe)
    get_number_of_missing_values(dataframe)
    dataframe = handle_dublicate_values_in_id(dataframe)
    
    print(f"Dataframe: {dataframe}")

if __name__ == '__main__':
    main()
