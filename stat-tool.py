import pandas as pd

file_path = "traffic_logs__2023-03-16__21-21-00.json"
df = pd.read_json(file_path)

def top_10_allow_source_ip(df):
    return df[df.action=="Allow"].groupby("source-ip")['source-ip'].count().sort_values(ascending=False).head(10)
