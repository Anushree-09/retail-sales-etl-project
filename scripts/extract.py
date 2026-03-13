import pandas as pd

def extract_data():

    df = pd.read_csv("data/retail_sales.csv", encoding="latin1")

    # standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    print("Columns after cleaning:")
    print(df.columns)

    return df


if __name__ == "__main__":
    extract_data()