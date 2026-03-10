import pandas as pd 


def csv_cleaner(df):
  
    # remove duplicates
    df = df.drop_duplicates()

    # fill in the missing values
    df = df.fillna("unknown")

    return df 
