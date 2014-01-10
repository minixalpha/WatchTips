#WatchTips

This project is a tips mangager, used to manage tips: watch, add, edit, view.
It is similar to a blog system, just replace the posts with tips.

The target of this project is to demo usage of framwork of both server 
and client, especially:

  * [web.py](http://webpy.org/)
  * [Bootstrap](http://getbootstrap.com/)

In a view of programming language, this project is also a demo of

  python
  javascript


# Requirements:

## server
  * [web.py](http://webpy.org/): a web framework for Python 
  that is as simple as it is powerful
  * [pycrypto](https://pypi.python.org/pypi/pycrypto): a collection of both 
  secure hash functions
  * [validate\_email](https://pypi.python.org/pypi/validate_email): a package for
   Python that check if an email is valid, properly formatted and really exists

## client
  * [Bootstrap](http://getbootstrap.com/): Sleek, intuitive, and powerful mobile
   first front-end framework for faster and easier web development.
  * [jQuery](http://jquery.com/): a fast, small, and feature-rich JavaScript 
  library.
  * [holder.js](http://imsky.github.io/holder/): Holder renders image 
  placeholders entirely on the client side.
  * [Buttons](http://alexwolfe.github.io/Buttons/): A CSS button library built 
  using Sass and Compass


# Configure:

  * Rename config\_sample.py to config.py
  * mysql: fill info in config.py, run scripts in sql/
  * crtkey: generate crtkey to support https, read README.md in crtkey


# Run:

    python index.py


# Tech

The techniques using in this project are listed in the following.

## Programs Style

Your Programs should comply with a Progrmas Style Guide, in this Project,
we use:

  * python: all the python programs should comply with 
  [PEP8](http://www.python.org/dev/peps/pep-0008/), using
  a tool called [pep8](https://pypi.python.org/pypi/pep8)

  * html/css: all the html/css file should pass 
  [W3C HTML Validator](http://validator.w3.org/) and 
  [W3C CSS Validator](http://jigsaw.w3.org/css-validator/)


## Unit Test

Progrmas should pass Unit Test, using `unittest` module in python


## Server

### web.py
  * URL handling
  * Deal with request: GET, POST
  * Redirect request
  * Subapplications
  * Custome not found message
  * Usage of Contextual and Environment variables: web.ctx
  * Application processors, loadhooks and unloadhooks
  * SSL support
  * Session and Cookie
  * Template
  * Operating database: mysql

### pycrypto
  * How to encrypt and validate information

### validate_email
  * How to check a email address is legal

### Mysql
  * Create database
  * Add User
  * Create Table

## Client

### Bootstrap
  * Grid System
  * Form
  * Buttons
  * Images
  * Glyphicons
  * Dropdowns
  * Navbar
  * Alerts
  * Progress Bar
  * Modals
  * Carousel

# Future features
  * process `__getattr__`
  * process `parameter type`
  * implementing logging middleware
  * add i18n support
