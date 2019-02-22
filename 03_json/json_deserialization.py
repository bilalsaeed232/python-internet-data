import json
from json import JSONDecodeError


def main():
    pyDict = {}
    jsonStr = '''{
            "name": "rtx2080ti",
            "price": 1000,
            "isAvailable": true,
            "features": [
                'support 4k',
                "for high performance"
            ]
        }'''

    try:
        # TODO: deserialize to python dict the json from string
        pyDict = json.loads(jsonStr)
        showData(pyDict)
    except JSONDecodeError as error:
        print('Error Decoding JSON !!!!')
        print('Message: {0}'.format(error.msg))
        print('at line:{0}, column: {1}'.format(error.lineno, error.colno))


def showData(data):
    # Display the python object values
    print('Name ==> {0}'.format(type(data['name'])))
    print('Price ==> {0}'.format(type(data['price'])))
    print('isAvalaible ==> {0}'.format(type(data['isAvailable'])))
    print('features ==> {0}'.format(type(data['features'])))


if __name__ == '__main__':
    main()
