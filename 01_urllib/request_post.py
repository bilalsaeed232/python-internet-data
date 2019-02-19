import urllib.request
import urllib.parse


def main():

    url = 'http://httpbin.org/post'

    # DATA - to send (POST)
    data = {
        "name": "BILAL KHAN",
        "is_active": False
    }

    # NOTE: needs to convert the data using urlencode
    url_encoded = urllib.parse.urlencode(data)

    # NOTE: needs to convert the data to bytes for POST
    bytes_data = url_encoded.encode()

    response = urllib.request.urlopen(url, data=bytes_data)
    # check the response body
    print('BODY -----<POST>-------')
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()
