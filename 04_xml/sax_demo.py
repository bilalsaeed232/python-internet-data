import xml.sax
import requests


class MySaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    def startElement(self, name, attrs):
        if name == 'slideshow':
            print('Title: {0}'.format(attrs['title']))
        elif name == 'slide':
            self.slideCount += 1
        elif name == 'item':
            self.itemCount += 1
        elif name == 'title':
            self.isInTitle = True

    def endElement(self, name):
        if name == 'title':
            self.isInTitle = False

    # To read actual text of tag
    def characters(self, content):
        if self.isInTitle:
            print("Slide Title: {0}".format(content))

    def startDocument(self):
        print("Starting parsing...")

    def endDocument(self):
        print("Document finished parsing...")


def main():
    URL = 'http://httpbin.org/xml'
    result = requests.get(URL)

    # print(result.text)
    # <slideshow
    #     title = "Sample Slide Show"
    #     date = "Date of publication"
    #     author = "Yours Truly"
    #     >

    #     <!-- TITLE SLIDE - ->
    #     <slide type = "all" >
    #     <title > Wake up to WonderWidgets!< /title >
    #     </slide >

    #     <!-- OVERVIEW - ->
    #     <slide type = "all" >
    #     <title > Overview < /title >
    #     <item > Why < em > WonderWidgets < /em > are great < /item >
    #     <item/>
    #     <item > Who < em > buys < /em > WonderWidgets < /item >
    #     </slide >
    # </slideshow >

    saxHandler = MySaxHandler()
    xml.sax.parseString(result.text, saxHandler)

    # CHeck total slides and items
    print("Total Slides: {0}, Total Items: {1}".format(
        saxHandler.slideCount, saxHandler.itemCount))


if __name__ == '__main__':
    main()
