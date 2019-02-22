import json


def main():
    pyDict = {
        "name": 'rtx2080ti',
        "price": 1000,
        "isAvailable": True,
        "features": ['high performance', '4k gaming']
    }

    # TODO: convert the python dict to json
    jsonStr = json.dumps(pyDict, indent=4)
    print("JSON: {0}".format(jsonStr))


if __name__ == '__main__':
    main()
