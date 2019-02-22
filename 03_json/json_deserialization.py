import json


def main():
    jsonStr = '''{
            "name": "rtx2080ti",
            "price": 1000,
            "isAvailable": true,
            "features": [
                "support 4k",
                "for high performance"
            ]
        }'''

    # TODO: deserialize to python dict the json from string
    pyDict = json.loads(jsonStr)

    # Display the python object values
    print('Name ==> {0}'.format(type(pyDict['name'])))
    print('Price ==> {0}'.format(type(pyDict['price'])))
    print('isAvalaible ==> {0}'.format(type(pyDict['isAvailable'])))
    print('features ==> {0}'.format(type(pyDict['features'])))


if __name__ == '__main__':
    main()
