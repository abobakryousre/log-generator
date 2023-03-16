import pandas as pd
import warnings

file_path = "traffic_logs__2023-03-16__21-56-19.json"
df = pd.read_json(file_path)

def read_log_file_as_dataframe():
    file = "traffic_logs__2023-03-16__21-56-19.json"
    try:
        df = pd.read_json(file)
        return df
    except Exception as e:
        return pd.DataFrame()
    

def top_10_allow_source_ip(df):
    return df[df.action=="Allow"].groupby("source-ip")['source-ip'].count().sort_values(ascending=False).head(10)

def to_10_deny_username(df):
    return df[df.action=="Deny"].groupby("username")['username'].count().sort_values(ascending=False).head(10)

def top_5_des_ip_for_deny_username(df,users=to_10_deny_username(df)):
    result = {}
    for user in users.index:
        result[user] = df[df.username==user].groupby("des-ip")['des-ip'].count().sort_values(ascending=False).head(5)
    return result


def tcp_baypass_traffic_count(df):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        bypass_count = len(df[df.protocol=="TCP"][df.action=="Bypass"])
        return  str(round((bypass_count / len(df)) * 100,2)) + '%'
    
def tcp_baypass_top_5_services(df):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return df[df.protocol=="TCP"][df.action=="Bypass"].groupby("source-ip")["source-ip"].count().sort_values(ascending=False).head(5)
    
def top_5_hours_for_unique_users(df):
    return df.sort_values(by='time',ascending=False).groupby('username').count().head(5)


if __name__ == "__main__":
    df = read_log_file_as_dataframe()
    if len(df) == 0:
        print("please make sure to create log file first..")
        exit()

    exit_loop = False

    while not exit_loop:
        print("please choice the number for one of the below options:")
        print("1) top 10 allow source ip")
        print("2) to 10 deny username")
        print("3) top 5 des ip for deny username")
        print("4) tcp baypass traffic count")
        print("5) tcp baypass top 5 services")
        print("6) top 5 hours for unique users")
        print("7) exit")

        choice = int(input("option: "))
        print("your choice is: ",choice)
        match choice:
            case 1:
                print(top_10_allow_source_ip(df))
            case 2:
                print(to_10_deny_username(df))
            case 3:
                print(top_5_des_ip_for_deny_username(df))
            case 4:
                print(tcp_baypass_traffic_count(df))
            case 5:
                print(tcp_baypass_top_5_services(df))
            case 6:
                print(top_5_hours_for_unique_users(df))
            case 7:
                exit_loop = True
                print("See You Later...")
            
        