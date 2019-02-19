import urllib.request
import urllib.parse


def main():
    # a GET url (which send back the data we pass - good for testing)
    url = 'http://httpbin.org/get'

    # DATA - to send
    data = {
        "name": "bilal saeed",
        "is_admin": True
    }

    # NOTE: the data needs to be urlencoded before sending
    encoded_data = urllib.parse.urlencode(data)

    # create request using this method
    response = urllib.request.urlopen(url + '?' + encoded_data)

    # check the response body
    print('BODY -----<GET>-------')
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()
