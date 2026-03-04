from langchain_community.document_loaders import CSVLoader

csv_loader = CSVLoader(
    file_path="./docs/customer-order.csv",
    autodetect_encoding=True
)

csv_data = csv_loader.load()

# print(f"contents: {csv_data[0].page_content}")
# print() # - new line

# print(f"meta-data: {csv_data[0].metadata}")


## - if you want all the data remove the index

for i, doc in enumerate(csv_data):
    print(f"Document {i+1}:")
    print(f"  Contents: {doc.page_content}")
    print(f"  Metadata: {doc.metadata}")
    print()


## -- O/p:

# Document 1:
#   Contents: Order_ID: ORD001
# Customer_Name: John Michael
# Order_Date: 2024-01-15
# Product: Laptop Pro
# Quantity: 1
# Total_Amount: 1299.99
# Status: Delivered
#   Metadata: {'source': './docs/customer-order.csv', 'row': 0}

# Document 2:
#   Contents: Order_ID: ORD002
# Customer_Name: Sarah Connor
# Order_Date: 2024-01-18
# Product: Wireless Mouse
# Quantity: 2
# Total_Amount: 59.98
# Status: Delivered
#   Metadata: {'source': './docs/customer-order.csv', 'row': 1}

# Document 3:
#   Contents: Order_ID: ORD003
# Customer_Name: Mike Johnson
# Order_Date: 2024-01-20
# Product: Monitor 27"
# Quantity: 1
# Total_Amount: 349.99
# Status: Processing
#   Metadata: {'source': './docs/customer-order.csv', 'row': 2}

# Document 4:
#   Contents: Order_ID: ORD004
# Customer_Name: Emily Watson
# Order_Date: 2024-01-22
# Product: Keyboard Mechanical
# Quantity: 1
# Total_Amount: 89.99
# Status: Shipped
#   Metadata: {'source': './docs/customer-order.csv', 'row': 3}

# Document 5:
#   Contents: Order_ID: ORD005
# Customer_Name: James Brown
# Order_Date: 2024-01-25
# Product: USB-C Cable
# Quantity: 5
# Total_Amount: 64.95
# Status: Delivered
#   Metadata: {'source': './docs/customer-order.csv', 'row': 4}

# Document 6:
#   Contents: Order_ID: ORD006
# Customer_Name: Lisa Anderson
# Order_Date: 2024-01-28
# Product: Desk Lamp LED
# Quantity: 3
# Total_Amount: 137.97
# Status: Processing
#   Metadata: {'source': './docs/customer-order.csv', 'row': 5}