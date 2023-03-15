import requests
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

