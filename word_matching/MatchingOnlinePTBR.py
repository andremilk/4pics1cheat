import requests

# This one looks on http://www.dicionario-aberto.net/estaticos/api.html
def word_exists(word):
    response = requests.get('http://dicionario-aberto.net/search-json/{0}'.format(word))
    return True if response.status_code == 200 else False
