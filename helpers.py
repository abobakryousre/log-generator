import requests, radar
from random import randint, randrange


def get_usernames_list():
    headers = {'user-agent': 'Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(url=url,allow_redirects=True, headers=headers)
    usernames_list = response.text.split()
    return usernames_list



def generate_uniqe_username(username_list):
    random_number = randint(0,len(username_list))
    random_range = randrange(0,1000000)
    unique_username = username_list[random_number] + str(random_range)
    return unique_username

def generate_username(username_list):
    random_number = randint(0,len(username_list))
    unique_username = username_list[random_number] + str(random_number)
    return unique_username


def generate_random_datetime(start_date="2019-10-20T01:00:00",end_date="2019-10-30T18:00:00"):
    start = radar.utils.parse(start_date)
    stop = radar.utils.parse(end_date)
    return radar.random_datetime(start=start, stop=stop).strftime("%Y-%m-%d %H:%M:%S")