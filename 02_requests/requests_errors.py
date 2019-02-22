import requests
from requests import HTTPError, Timeout


def main():
    try:
        # URL = 'http://httpbin.org/404'

        # to test timeout error
        URL = 'http://httpbin.org/delay/4'

        result = requests.get(URL, timeout=2)
        result.raise_for_status()
        printResults(result)
    except HTTPError as error:
        print('ERROR: {0}'.format(error))
    except Timeout as error:
        print('Timeout Error: {0}'.format(error))


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
