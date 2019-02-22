# XML Parsing

*Two main types of parsers users:*
* SAX Parser  -->   `import xml.sax`
* DOM Parser  -->   `import xml.dom`


## SAX Parser

* Stands for Simple API for XML
* It parses xml from top to bottom sequentially
* It provides events to be overriden if required, e.g when document starts, and element starts etc.

### Advantages of SAX

* Very memory Efficient
* Very fast than dom 
* Great for usecases when only reading xml

### Disadvantages of SAX

* Don't give a context where we are in document currently
* Not ideal for manipulating xml document
* Not ideal for usecases where random xml nodes are required




