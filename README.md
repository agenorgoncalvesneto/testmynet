# Testmynet

A command line interface to test the internet speed using [testmy.net](https://testmy.net).


## Requisites

The requisites for install and run Testmynet are [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [python3.3](https://www.python.org/downloads/) or later.


## Install

Clone this repository, move for testmynet directory and run the installation script
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
Testing download and upload speeds...
Miami, USA | Download 10.2 Mbps | Upload 1 Mbps
Test successfully concluded.
```

For see help
``` shell
$ ./testmynet.py -h
```
```
usage: Testmynet [-h] [-d | -u] [--details] [--list] [--server]

A command line interface to test the internet speed using testmy.net

optional arguments:
  -h, --help      show this help message and exit
  -d, --download  performs only download test
  -u, --upload    performs only upload test
  --details       show the details after perform the tests
  --list          display a list of testmy.net servers and exit
  --server        specify a server code to test against

See more on www.github.com/agenorgoncalvesneto/testmynet
```

Thus the command line below will run only download test using the server 5
``` shell
$ ./testmynet.py --download --server 5
```
```
Testing download speed...
Toronto, CA | Download 10 Mbps
Test successfully concluded.
```


## Uninstall

For uninstall Testmynet just remove the testmynet directory
``` shell
$ sudo rm -r testmynet/
```
