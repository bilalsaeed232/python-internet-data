import requests
from requests.auth import HTTPBasicAuth
from requests import HTTPError


def main():
    try:
        # TODO create url for testing basic auth
        # NOTE: for test with httpbin only
        URL = 'http://httpbin.org/basic-auth/bilal/secret'

        # TODO: Create httpbasicauth object
        # auth = HTTPBasicAuth('bilal', 'secret')
        # result = requests.get(URL, auth=auth)

        # OR

        result = requests.get(URL, auth=('bilal', 'secret'))

        result.raise_for_status()

        printResults(result)
    except HTTPError as error:
        print(error)


def printResults(response):
    print('STATUS -----------------')
    print(response.status_code)
    print(' -----------------')

    print('HEADERS -----------------')
    print(response.headers)
    print(' -----------------')

    print('STATUS -----------------')
    # print(response.content)

    # this will convert our response to string
    print(response.text)
    print(' -----------------')


if __name__ == '__main__':
    main()
