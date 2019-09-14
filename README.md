# testmynet

A command line interface to test the internet speed using [testmy.net](https://testmy.net)


## requisites

The requisites for install and run *testmynet* are ```firefox```, ```python3``` and ```virtualenv```.


## install

Clone this repository, move for testmynet directory and make the file testmynet.py executable
``` shell
$ git clone https://github.com/agenorgoncalvesneto/testmynet.git
$ cd testmynet/ && chmod +x testmynet.py
```

Create and activate a virtual environment and install the requirements
``` shell
$ virtualenv -p python3 venv && source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt && deactivate
```

Download geckodriver and move it for venv/bin/

For 32-bit linux use
``` shell
$ wget github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz
$ tar -xf geckodriver-v0.24.0-linux32.tar.gz && rm geckodriver-v0.24.0-linux32.tar.gz
$ mv geckodriver venv/bin/
```

For 64-bit linux use
``` shell
$ wget github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
$ tar -xf geckodriver-v0.24.0-linux64.tar.gz && rm geckodriver-v0.24.0-linux64.tar.gz
$ mv geckodriver venv/bin/
```


## usage

In the testmynet directory, for typical test use the command line below
``` shell
$ ./testmynet.py
```
```
testing download speed...
testing upload speed...
server Dallas, TX | download 9.3 Mbps | upload 4 Mbps
test successfully concluded
```

For see help
``` shell
$ ./testmynet.py -h
```
```
usage: testmynet [-h] [-d | -u] [--list] [--server]

A command line interface to test the internet speed using testmy.net

optional arguments:
  -h, --help         show this help message and exit
  -d, --no-download  do not perform donwload test
  -u, --no-upload    do not perform upload test
  --list             display a list of testmy.net servers and exit
  --server           specify a server id to test against

See more on www.github.com/agenorgoncalvesneto/testmynet
```

Thus the command line below will run only download test using the server 5
``` shell
$ ./testmynet.py --no-upload --server 5
```
```
testing download speed...
server Los Angeles, CA | download 4.6 Mbps
test successfully concluded
```


## uninstall

For uninstall *testmynet* just remove the testmynet directory
``` shell
$ sudo rm -r testmynet/
```
