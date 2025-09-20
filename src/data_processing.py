import pandas as pd
import argparse

def load_data(path):
    return pd.read_csv(path)

def clean(df):
    df = df.dropna(subset=['CustomerID'])
    df = df[df.Quantity > 0]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df

def save(df, path):
    df.to_csv(path, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output')
    args = parser.parse_args()
    df = load_data(args.input)
    df = clean(df)
    save(df, args.output)
