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
            username = helpers.generate_username(username_list) + str(i)
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



if __name__ == "__main__":
    

    rows_number = 10
    logs_rows = log_generator(rows_number)

