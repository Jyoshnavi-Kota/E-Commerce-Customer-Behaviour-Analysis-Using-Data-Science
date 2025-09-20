import pandas as pd

def make_rfm(df, today=None):
    if today is None:
        today = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    agg = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (today - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    }).reset_index()
    agg.columns = ['CustomerID','Recency','Frequency','Monetary']
    return agg
