import sys
import requests



if len(sys.argv) not in [2]:
    print('Improrer number of arguments: at least one is requred' +
              "And not more than two are allowed:")
    print('- htto server;s address (requred)')
    print('- port number by default (not specified!)')
    exit(1) 

addr = sys.argv[1]
URL = 'https://' + sys.argv[1] + '/'

try:
    response = requests.head(URL)
except requests.exceptions.InvalidURL:
    print('The given URL ' + sys.argv[1] + 'is invalid.')
    exit(3)
except requests.exceptions.ConnectionError:
    print('Cannot connect to' + addr)
    exit(4)
except requests.exceptions.RequestException:
    print('Some problems appered - sorry.')
    exit(5)

print(response.status_code, response.reason)


if __name__ == "__main__":
    print('main.py запущена сама по себе')
else:
    print('main.py импортирована')
