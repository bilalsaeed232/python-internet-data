import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError


def main():
    # url = 'http://blablabla.dfd'  # URLError
    url = 'http://httpbin.org/status/404'  # HTTPError
    # url = 'http://httpbin.org/status/500'  # HTTPError
    # url = 'http://httpbin.org/html'  # No Errors
    # url = 'http://httpbin.org/json'  # No Errors
    try:
        response = urllib.request.urlopen(url)

        print('RESPONSE ---------------')
        print(response.read().decode('utf-8'))
        if (response.status == HTTPStatus.OK):
            print('--------------<NO ERRORS>-------------------')
    except HTTPError as err:
        print('<HTTP ERROR>')
        print('ERROR CODE: {0}'.format(err.code))
        print('ERROR MESSAGE: {0}'.format(err.reason))
    except URLError as err:
        print('<URL ERROR>')
        print('ERROR MESSAGE: {0}'.format(err.reason))
    except Exception as err:
        print('<Unknown ERROR>')


if __name__ == '__main__':
    main()
