import pandas as pd

def get_bar_chart_data():
    data = {'Date': ['2023-06', '2023-07', '2023-08', '2023-09', '2023-10'],
            'Value': [210, 240, 230, 280, 270]}
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    return df