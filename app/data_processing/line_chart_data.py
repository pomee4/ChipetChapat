import pandas as pd

def get_line_chart_data():
    data = {'Date': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05'],
            'Value': [200, 250, 220, 270, 260]}
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    return df