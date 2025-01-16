
import re
import numpy as np
import pandas as pd


def read_products_data():
    file_path='product_catalog_with_rubbish.csv'
    df=pd.read_csv(file_path)
    return df


def get_data_description(df):
    description= df.describe()
    print(description)

def convert_price(price):
    try:
        return float(price)
    except (ValueError, TypeError):
        return np.nan
    
def convert_category(category):
    pattern=r'^[\w\s]+$'
    if isinstance(category, str):
        if re.match(pattern, category):
            return category.strip()  # Clean and return if valid
        else:
            return np.nan 
    elif pd.isna(category):  # Explicitly check for NaN
        return np.nan
    else:
        return np.nan 
   

def handle_wrong_datatype_in_price(df):
    df['Price']=df['Price'].apply(convert_price)

    """
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    return df
    """

def handle_wrong_datatype_in_category(df):
    df['Category']=df['Category'].apply(convert_category)

def handle_dublicate_values_in_id(df):
    pass


def get_number_of_missing_values(df):
    missing_values=df.isna().sum()
    print(missing_values)


def main():
    dataframe=read_products_data()
    get_data_description(dataframe)
    handle_wrong_datatype_in_price(dataframe)
    get_number_of_missing_values(dataframe)
    handle_wrong_datatype_in_category(dataframe)
    handle_dublicate_values_in_id(dataframe)
    print(dataframe)


if __name__ == '__main__':
    main()