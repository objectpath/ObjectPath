ObjectPath-NG
==========

[![Downloads](https://img.shields.io/badge/objectpath--ng-downloads-brightgreen.svg)](https://pypi.python.org/pypi/objectpath-ng/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/objectpath-ng/)
[![Build Status](https://travis-ci.org/objectpath/ObjectPath.svg?branch=master)](https://travis-ci.org/objectpath/ObjectPath)
[![Code Health](https://landscape.io/github/objectpath/ObjectPath/master/landscape.png)](https://landscape.io/github/objectpath/ObjectPath/master)
[![Coverage Status](https://coveralls.io/repos/objectpath/ObjectPath/badge.png?branch=master)](https://coveralls.io/r/objectpath/ObjectPath?branch=master)

The agile NoSQL query language for semi-structured data
-----------------------------------------------

**#Python #NoSQL #Javascript #JSON #nested-array-object**

ObjectPath is a query language similar to XPath or JSONPath, but much more powerful thanks to embedded arithmetic calculations, comparison mechanisms and built-in functions. This makes the language more like SQL in terms of expressiveness, but it works over JSON documents rather than relations. ObjectPath can be considered a full-featured expression language. Besides selector mechanism there is also boolean logic, type system and string concatenation available. On top of that, the language implementations (Python at the moment; Javascript is in beta!) are secure and relatively fast.

This is a maintained fork of the [original project](htttps://github.com/adriank/ObjectPath) and still compatible with the specification at the
[ObjectPath site](http://objectpath.org/). New ideas and features are welcome, however changes that break compatibility with the spec will be
rejected.

![ObjectPath img](http://objectpath.github.io/ObjectPath/img/op-colors.png)

ObjectPath makes it easy to find data in big nested JSON documents. It borrows the best parts from E4X, JSONPath, XPath and SQL. ObjectPath is to JSON documents what XPath is to XML. Other examples to ilustrate this kind of relationship are:

| Scope  | Language |
|---|---|
| text documents  | regular expression  |
| XML  | XPath  |
| HTML  | CSS selectors  |
| JSON documents | ObjectPath |

Documentation
-------------

[ObjectPath Reference](http://objectpath.org/reference.html)

Command line usage
-----

`````sh
$ pip install objectpath-ng
$ objectpath file.json
`````
or
`````sh
$ git clone https://github.com/objectpath/ObjectPath.git
$ cd ObjectPath
$ python shell.py file.json
`````

Python usage
----------------

`````sh
$ pip install objectpath-ng
$ python
>>> from objectpath import *
>>> tree=Tree({"a":1})
>>> tree.execute("$.a")
1
>>>
`````

`````sh
$ git clone https://github.com/objectpath/ObjectPath.git
$ cd ObjectPath
$ python
>>> from objectpath import *
>>> tree=Tree({"a":1})
>>> tree.execute("$.a")
1
>>>
`````

Contributing & bugs
-------------------

Pull requests welcome!


License
-------

**MIT**
