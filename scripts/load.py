import mysql.connector
from scripts.extract import extract_data
from scripts.transform import transform_data
from config import DB_CONFIG

def load_data():

    df = extract_data()
    df = transform_data(df)
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    for index,row in df.iterrows():

        query = """
        INSERT INTO retail_sales
        (order_id,order_date,customer_id,customer_name,category, sub_category,product_name,sales,quantity,discount,profit,city,state,region)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            row.order_id,
row.order_date,
row.customer_id,
row.customer_name,
row.category,
row["sub-category"],
row.product_name,
row.sales,
row.quantity,
row.discount,
row.profit,
row.city,
row.state,
row.region
        )

        cursor.execute(query,values)

    connection.commit()

    print("Data Loaded")

    cursor.close()
    connection.close()