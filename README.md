# Testmynet

A command line interface to test the internet speed using [testmy.net](https://testmy.net)


## Requisites

The requisites for install and run *testmynet* are [Firefox](https://www.mozilla.org/en-US/firefox/new/), [python3](https://www.python.org/downloads/) and [virtualenv](https://virtualenv.pypa.io/en/latest/).


## Install

Clone this repository, move for testmynet directory and run te installation script
``` shell
$ git clone https://github.com/agenorgoncalvesneto/testmynet.git
$ cd testmynet/ && ./install.sh
```

## Usage

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


## Uninstall

For uninstall *testmynet* just remove the testmynet directory
``` shell
$ sudo rm -r testmynet/
```
