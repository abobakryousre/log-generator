import helpers
import os, json, sys
from datetime import datetime

def log_generator(rows_number):
    ## generate random traffic logs file with the below format 
    ## date time source-ip des-ip port protocol username action
    username_list = helpers.get_usernames_list()[::2]
    result = []

    source_ip_list = []
    username_sources_ip_list = {}

    for i in range(1,rows_number+1):
        try:
                
            date_time = helpers.generate_random_datetime().split(" ")

            if i < 500000:
                # add iteration number to make it uniuqe username
                username = helpers.generate_username(username_list) + str(i)

            else:
                username = helpers.generate_username(username_list)

            if i < 650000:
                # create random unique ip
                source_ip = helpers.generate_random_ip()
                source_ip_list.append(source_ip)
            else:
                # get an old source ip.
                source_ip = helpers.get_old_source_ip(source_ip_list)
                
                while helpers.username_has_this_sourece_iP(username, username_sources_ip_list, source_ip):
                    # get an new one
                    source_ip = helpers.get_old_source_ip(source_ip_list)

            des_ip = helpers.generate_random_ip()
            protocol = helpers.generate_random_protocol()
            port = helpers.generate_random_protocol_port(protocol)

            

            # save the usernamne source ip
            helpers.append_to_username_source_ips(username,username_sources_ip_list,source_ip)
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
    file =  os.path.join(os.getcwd(),f"traffic_logs.json")

    with open(file, 'w') as file:
        json.dump(logs_rows,file)

    print("traffic logs file created successfully at the below path.")
    print(str(file))



if __name__ == "__main__":
    
    execution_start_date = datetime.now()

    # geeting rows number if passed as argument
    try:
        rows_number = int(sys.argv[1])

    except:
        rows_number = 1000000

    logs_rows = log_generator(rows_number)
    save_logs_to_file(logs_rows)

    execution_start_end = datetime.now()
    execution_time = execution_start_end - execution_start_date

    print(f"execution time:  {execution_time}")

    
