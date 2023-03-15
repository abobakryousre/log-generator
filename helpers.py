import requests


def get_usernames_list():
    headers = {'user-agent': 'Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(url=url,allow_redirects=True, headers=headers)
    usernames_list = response.text.split()
    return usernames_list





