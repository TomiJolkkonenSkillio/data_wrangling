import users
import product_catalogue
import transactions


def main():
    print(users.get_users())
    print(products.get_product_catalog())
    print(transactions.get_transactions())

if __name__ == "__main__":
    main()