import requests


def main():
    # TODO: basic get request
    URL = 'http://httpbin.org/get'
    result = requests.get(URL)
    # printResults(result)

    # TODO: get request with parameters
    params = {
        'key1': 'value1',
        'key2': 'value2'
    }
    result = requests.get(URL, params=params)
    # printResults(result)

    # TODO: get request with passing header
    headers = {
        'User-Agent': 'blablabla',
        'Dont-Exist': 'notdefined'
    }
    result = requests.get(URL, headers=headers)
    # printResults(result)

    # TODO: basic post with data
    URL = 'http://httpbin.org/post'
    data = {
        'first_name': 'Bilal',
        'last_name': 'Saeed'
    }
    result = requests.post(URL, data=data)
    printResults(result)


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
