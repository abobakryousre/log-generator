import requests, radar, ipaddr
from random import randint, randrange, choices


def get_usernames_list():
    headers = {'user-agent': 'Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(url=url,allow_redirects=True, headers=headers)
    usernames_list = response.text.split()
    return usernames_list



def generate_uniqe_username(username_list):
    random_number = randint(0,len(username_list) -1)
    random_range = randrange(0,1000000)
    unique_username = username_list[random_number] + str(random_range)
    return unique_username

def generate_username(username_list):
    random_number = randint(0,len(username_list)-1)
    unique_username = username_list[random_number] + str(random_number)
    return unique_username


def generate_random_datetime(start_date="2019-10-20T01:00:00",end_date="2019-10-30T18:00:00"):
    start = radar.utils.parse(start_date)
    stop = radar.utils.parse(end_date)
    return radar.random_datetime(start=start, stop=stop).strftime("%Y-%m-%d %H:%M:%S")


def generate_random_ip():
    network = ipaddr.IPv4Network('10.0.0.0/8')
    ip = ipaddr.IPv4Address(randrange(int(network.network) + 1, int(network.broadcast) - 1))
    return str(ip)

def generate_random_protocol():
    protocols = ['TCP','UDP']
    random_number = randint(0,len(protocols) -1)
    return protocols[random_number]

def generate_random_protocol_port(protocol_name):
    protocols =  {
        "TCP" : [443,20,22],
        "UDP" : [53,68,88]
    }
    random_number = randint(0,len(protocols.get(protocol_name)) -1)
    return str(protocols[protocol_name][random_number])

def generate_random_action():
    actions = ['Allow','Deny','Bypass','Log-Only']
    random_action = choices(population=actions, weights=[45,5,15,35], k=1)
    return random_action[0]

def get_old_source_ip(source_ip_list):
    random_number = randint(0,len(source_ip_list) -1)
    old_source_ip = source_ip_list[random_number]
    return old_source_ip

def append_to_username_source_ips(username,username_sources_ip_list,new_source_ip):

   source_ip_list = username_sources_ip_list.get(username)
   if source_ip_list != None:
       username_sources_ip_list.get(username).add(new_source_ip)
   else:
       username_sources_ip_list[username] = {new_source_ip}


def username_has_this_sourece_iP(username, username_sources_ip_list, source_ip):
    source_ip_list = username_sources_ip_list.get(username)

    if source_ip_list == None:
        return False
    
    if source_ip in source_ip_list:
        return True
    else:
        return False
