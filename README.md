# testmynet

A command line interface to test the internet speed using testmy.net


## requisites

The prerequisites for run *testmynet* are ```firefox```, ```python3``` and ```virtualenv```.


## install

Clone this repository
```shell
$ git clone https://github.com/agenorgoncalvesneto/testmynet.git
```

Create a virtual environment and install selenium
```shell
$ virtualenv -p python3 testmynet/venv
$ source testmynet/venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install selenium && deactivate
```

Download geckodriver and move it for testmynet/venv/bin/

For 32-bit linux use
```shell
$ wget github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz
$ tar -xf geckodriver-v0.24.0-linux32.tar.gz
$ mv geckodriver testmynet/venv/bin/
```

For 64-bit linux use
```shell
$ wget github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
$ tar -xf geckodriver-v0.24.0-linux64.tar.gz
$ mv geckodriver testmynet/venv/bin/
```


## usage

Move for testmynet directory and active the virtual environment
```shell
$ source venv/bin/activate
```

For typical test use the command-line below
```shell
(venv) $ python testmynet.py
```

For see help
```shell
(venv) $ python testmynet.py -h
usage: testmynet [-h] [-d | -u]

A command line interface to test the internet speed using testmy.net

optional arguments:
  -h, --help         show this help message and exit
  -d, --no-download  do not perform donwload test
  -u, --no-upload    do not perform upload test

See more on www.github.com/agenorgoncalvesneto/testmynet
```

For example, the command-line below  will run only download test
```shell
(venv) $ python testmynet.py --no-upload
```

After perform tests, just deactivate the virtual environment
```shell
(venv) $ deactivate
```


## uninstall

For uninstall *testmynet* just remove the testmynet directory

```shell
$ rm -r testmynet/
```

