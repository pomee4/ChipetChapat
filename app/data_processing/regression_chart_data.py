import pandas as pd

def get_regression_chart_data():
    data = {'Date': ['2023-11', '2023-12', '2024-01', '2024-02', '2024-03'],
            'Value': [215, 245, 235, 285, 275]}
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date_ordinal'] = df['Date'].map(pd.Timestamp.toordinal)
    return df