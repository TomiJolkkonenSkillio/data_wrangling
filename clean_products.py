import re
import numpy as np
import pandas as pd


def read_products_data():
    file_path='product_catalog_with_rubbish.csv'
    df=pd.read_csv(file_path)
    print(df.dtypes)
    return df


def get_data_description(df):
    description= df.describe()
    #print(description)

def convert_price(price):
    try:
        return float(price)
    except (ValueError, TypeError):
        return np.nan
    
def convert_category(column):
    pattern = r'^[a-zA-Z\s]+$'
    if isinstance(column, str):
        if re.match(pattern, column):
            return column.strip()  # Clean and return if valid
        else:
            return np.nan 
    elif pd.isna(column):  # Explicitly check for NaN
        return np.nan
    else:
        return np.nan 
   
def handle_wrong_datatype_in_id(df):
    df['product_id']=pd.to_numeric(df['product_id'], errors='coerce')

def handle_wrong_datatype_in_price(df):
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

def handle_wrong_datatype_in_name_and_category(df,column:str):
    df[column]=df[column].apply(convert_category)

def handle_dublicate_values_in_id(df):
    df['product_id'] = df['product_id'].drop_duplicates()

def drop_missing_ids(df):
    # Drop rows where 'Product ID' is NaN
    df.dropna(subset=['product_id'], inplace=True)
     # Reset the index in place to ensure continuity
    df.reset_index(drop=True, inplace=True)

def get_number_of_missing_values(df):
    missing_values=df.isna().sum()

def get_cleaned_products(dataframe):
    handle_wrong_datatype_in_id(dataframe)
    handle_wrong_datatype_in_price(dataframe)
    handle_wrong_datatype_in_name_and_category(dataframe, 'Category')
    handle_dublicate_values_in_id(dataframe)
    drop_missing_ids(dataframe)
    return dataframe

def main():
    dataframe=read_products_data()
    handle_wrong_datatype_in_id(dataframe)
    handle_wrong_datatype_in_price(dataframe)
    handle_wrong_datatype_in_name_and_category(dataframe, 'Category')
    handle_dublicate_values_in_id(dataframe)
    drop_missing_ids(dataframe)
    print(dataframe)

if __name__ == '__main__':
    main()