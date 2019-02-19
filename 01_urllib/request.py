import urllib.request


def main():
    url = 'http://httpbin.org/xml'

    request = urllib.request.urlopen(url=url)

    # Print status code from server
    print('STATUS ----------')
    print(request.status)
    print('-----------------')

    # Print headers from server
    print('HEADERS ----------')
    print(request.getheaders())
    print('-----------------')

    # Print body from server
    print('BODY ----------')
    # need to decode to utf8 string as body (by default) is in raw bytes
    print(request.read().decode('utf-8'))
    print('-----------------')


if __name__ == "__main__":
    main()
