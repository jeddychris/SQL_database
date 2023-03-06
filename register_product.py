from main import Product

try:
    product_price = input("Enter price \n")
    product_quantity = input("Enter quantity \n")
    product_description = input("Enter description \n")

    Product.create(prod_price=product_price, prod_quantity=product_quantity,  prod_description=product_description)
    print("Product Created Successfully")
except:
    print("Failed to Create Product")
