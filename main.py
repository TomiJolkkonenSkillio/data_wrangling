import transactions
import pandas as pd

def main():
    users, products, transaction_data=transactions.get_transactions()
    print(users)
    print(products)
    print(transaction_data)
    
    # total_spending = transaction_data.groupby('user_id')['quantity'].sum() # total spending per user
    # print(f"Total spending per user: {total_spending}")
    # top5_sold = products.groupby(['Product ID']).agg(total_quantity_sold=('Price'), average_price=('Price')) # top 5 best-selling products & their avr price
    # most_popular = products.groupby('Category')['quantity'].sum() # most popular product category
    transaction_data.to_json('transaction_data.json', orient='records', lines=True) # export dataset to json file
    df_from_json = pd.read_json('transaction_data.json', lines=True) # read json file back into pandas dataframe
    print(f"First few lines from the file: {df_from_json.head()}") # print the head of the file out

if __name__ == "__main__":
    main()