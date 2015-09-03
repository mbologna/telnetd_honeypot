# telnetd honeypot
A very simple telnetd honeypot written in Python, using Twisted framework.

## Why?

As I always wanted to have a look with twisted, seems a good idea. The main 
idea here is to write a simple telnetd server that:

*   shows the root prompt and waits for commands
*   answers with fake answers to some UNIX commands (like `uname` and `id`)
*   answers to all other commands with `Command not found` or with nothing 
(like that the command was accepted). The choice between answering in the 
former way rather than the latter is random
*   record everything that is written by the attacker

Read more at http://michelebologna.net/2015/09/fun-with-python-powered-telnetd-honeypot

## Demo

```
% python telnetd.py &
[1] 15171
% telnet localhost 8023
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
/ # uname -a 
Linux f001 3.13.3-7-high-octane-fueled #3000-LPG SMPx4 Fri Jun 31 25:24:23 UTC 2200 x86_64 x64_86 x13_37 GNU/Linux
/ # id
uid=0(root) gid=0(root) groups=0(root)
/ # ls 
/ # ps auxw 
bash: ps: command not found
```

## Installation

1. Install twisted using `pip`:
    
    `pip install twisted`

2. Clone this repo

    `git clone https://github.com/mbologna/telnetd_honeypot`

## Usage

1. Launch telnetd.py with as little permissions as possible (ideally in a 
Docker container!). Telnetd will listen on 8023/tcp.

    `python telnetd.py`

2. (optional). You can spin up a bouncer (like rinetd) to serve it on 23/tcp

