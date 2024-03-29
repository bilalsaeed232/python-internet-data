# Working With JSON in Python

## Loading JSON

- `load(file)`
- `loads(string)`

## Serializing

- `dump(file)`
- `dumps(string)`

## Converting to JSON types

| Python   	        |      JSON         	|
|-------------------|:---------------------:|
|dict   	        |  object              	|
|list,tuple	        |  array   	            |
|str    	        |  string  	            |
|int,float etc   	|  number           	|
|True               |  true             	|
|False          	|  false             	|
|None          	    |  null             	|


## Converting from JSON types

| JSON   	        |      Python         	|
|-------------------|:---------------------:|
|object   	        |  dict              	|
|array	            |  list   	            |
|string	            |  str   	            |
|integer number    	|  int               	|
|floating number    |  float               	|
|true               |  True             	|
|false          	|  False             	|
|null          	    |  None             	|

*Note: It's not possible to tell the different between list and tuple from json by the parse*