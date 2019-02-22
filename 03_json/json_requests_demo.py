import requests
import json


def main():
    # TODO: url for getting valid json
    URL = 'http://httpbin.org/json'
    result = requests.get(URL)

    # TODO: convert the response json to valid python dict
    pyDict = result.json()

    # TODO: first display json string received
    # print("JSON ------------")
    # print(json.dumps(pyDict, indent=4))
    # print("-----------------")

    # TODO: display few dict values
    print("DICT ---------------")
    print("TITLE: {0}".format(pyDict['slideshow']['title']))
    print("Total Slides: {0}".format(len(pyDict['slideshow']['slides'])))
    print("-----------------------")


if __name__ == '__main__':
    main()
