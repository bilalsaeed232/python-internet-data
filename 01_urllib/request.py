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
    print(request.read())
    print('-----------------')


if __name__ == "__main__":
    main()
