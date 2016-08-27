pybitflyer
==========

`pybitflyer` is a python wrapper for Bitflyer's REST API.

Description
-----------

Install
-------

```
$ pip install git+https://github.com/yagays/pybitflyer.git
```

Usage
-----

```
import pybitflyer

api = pybitflyer.API(api_key="xxx...", api_secret="yyy...")
```

Example
-------

```
api.board(product_code="BTC_JPY")
```

Author
------

@yag_ays (<yanagi.ayase@gmail.com>)
