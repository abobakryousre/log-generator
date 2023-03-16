import helpers
import os, json
from datetime import datetime

def log_generator(rows_number):
    ## generate random traffic logs file with the below format 
    ## date time source-ip des-ip port protocol username action
    username_list = helpers.get_usernames_list()
    result = []

    for i in range(1,rows_number+1):
        try:
                
            date_time = helpers.generate_random_datetime().split(" ")
            source_ip = helpers.generate_random_ip()
            des_ip = helpers.generate_random_ip()
            protocol = helpers.generate_random_protocol()
            port = helpers.generate_random_protocol_port(protocol)

            if i < 500000:
                # add iteration number to make it uniuqe username
                username = helpers.generate_username(username_list) + str(i)
                
            else:
                username = helpers.generate_username(username_list)

            action = helpers.generate_random_action()

            row = {
                "date" : date_time[0],
                "time" : date_time[1],
                "source-ip" : source_ip,
                "des-ip": des_ip,
                "port": port,
                "protocol" : protocol,
                "username" : username,
                "action" : action
            }

            # append row
            result.append(row)

        except Exception as e:
            print(e)
            continue

    ## return result array
    return result

def save_logs_to_file(logs_rows):
    now  = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
    file =  os.path.join(os.getcwd(),f"traffic_logs__{now}.json")

    with open(file, 'w') as file:
        json.dump(logs_rows,file)

    print("traffic logs file created successfully at the below path.")
    print(str(file))



if __name__ == "__main__":
    
    execution_start_date = datetime.now()

    rows_number = 1000000
    logs_rows = log_generator(rows_number)
    save_logs_to_file(logs_rows)

    execution_start_end = datetime.now()
    execution_time = execution_start_end - execution_start_date

    print(f"execution time:  {execution_time}")

    
