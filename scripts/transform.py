def transform_data(df):

    # remove duplicates
    df = df.drop_duplicates()

    # convert date
    df["order_date"] = df["order_date"].astype("datetime64[ns]")

    # create revenue column
    df["total_sales"] = df["sales"]

    return df