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

For instance, the command line below  will show a list of testmy.net servers
``` shell
$ ./testmynet.py --list
```
```
 1 Central US — Dallas, TX, USA
 2 Central US — Colorado Springs, CO, USA
 3 East Coast US — Miami, FL, USA
 4 East Coast US — New York, NY, USA
 5 West Coast US — Los Angeles, CA, USA
 6 West Coast US — San Francisco, CA, USA
 7 North America — Toronto, CA
 8 Europe — London, GB
 9 Europe — Frankfurt, DE
10 Asia — Tokyo, JP
11 Asia — Singapore, SG
12 Asia — Bangalore, IN
13 Australia — Sydney, AU
```

Then the command line below will run only download test using Los Angele server
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

