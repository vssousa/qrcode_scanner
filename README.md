# Scanner of QR codes

## Overview

This repository presents a scanner of QR codes using Django framework, considering HTML with JavaScript web pages.

## Software requirements

The following softwares have to be configured / installed for running this application.

1. [Django framework](https://www.djangoproject.com/) for providing web services.
2. [Python 2.7](https://www.python.org/) as the main programming language.
3. [pip](https://pypi.python.org/pypi/pip), the PyPA recommended tool for installing Python packages.
4. [VirtualEnv](https://virtualenv.pypa.io/en/stable/) for creating a Python environment with all (library) dependencies.
5. [Instascan](https://github.com/schmich/instascan) for scanning QR codes.
6. [SQLite](https://www.sqlite.org/) as the relational database management system.
7. [Bootstrap](http://getbootstrap.com/) as the template of web pages.
8. [jQuery](https://jquery.com/), a JavaScript library that we use to redirect HTTP requests.

## How to start this application

To start our application, it is necessary to go to the root directory and to start a Django server, as follows:

```
cd $ROOT_DIRECTORY
python manage.py runserver
```

If you would like to test in a mobile device, it is necessary to enable external accesses (considering the port 8000) in your firewall security configurations. Moreover, the Django initialization commandline should be replaced, as follows:

```
python manage.py runserver 172.16.4.104:8000
```

## Available URLs in this application

The folllowing URLs are available in this application:

* To scan QR codes at real time

```
http://$HOSTNAME:$PORT/scanner
```

* To analyze database records

```
http://$HOSTNAME:$PORT/admin/scanner/qrcode
```

P.S.: $HOSTNAME should be replaced by the hostname or IP address, **e.g.**, localhost; and $PORT should be replaced by the configured port in Django project, **e.g.**, 8000.