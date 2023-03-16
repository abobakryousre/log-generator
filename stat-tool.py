import pandas as pd

file_path = "traffic_logs__2023-03-16__21-56-19.json"
df = pd.read_json(file_path)

def top_10_allow_source_ip(df):
    return df[df.action=="Allow"].groupby("source-ip")['source-ip'].count().sort_values(ascending=False).head(10)

def to_10_deny_username(df):
    return df[df.action=="Deny"].groupby("username")['username'].count().sort_values(ascending=False).head(10)

def top_5_des_ip_for_deny_username(df,users=to_10_deny_username(df)):
    result = {}
    for user in users.index:
        result[user] = df[df.username==user].groupby("des-ip")['des-ip'].count().sort_values(ascending=False).head(5)
    return result