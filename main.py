import transactions

def main():
    users, products, transaction_data=transactions.get_transactions()
    print(users)
    print(products)
    print(transaction_data)

if __name__ == "__main__":
    main()