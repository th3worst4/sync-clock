# Sync-clock

It has been sometime I've been using dual boot on my PCs(notebook and desktop), and something I notice is the PC clock always is messed up. So I spent my night writing this Python script, it doesn't have much utility for someone besides me(because it sets your clock according to GMT-3), but was something funny to do. So here it is.

## How to use it?

ATTENTION: You will need root access to run the bash script

First, run the `setup.sh` script, it will create the Python Virtual Environment and install the needed packages.

This script uses the following packages:
* requests
* beautifulsoup4

After setting everything up, you just need to run the `sync-clock` bash script, under the `src/` folder as a root user. Now you can set this script on your PATH and use it through the system.

ATTENTION: Bash scripts can be very volatile, to ensure everything will work properly, you should have your working directory as the `src/` directory

## How it works?

It performs a http GET request to the following link: https://free.timeanddate.com/clock/i9aa1cck/n213/tlbr5/tt0/tw0/tm3/td2/th1

What is this link? This domain offers you to display a clock on your website or blog, you can customize the clock and paste the href to it on your website source file. What I did was just to request the info and parse it to some HTML parser and with this raw data I just ran some Python script to format it to be accepted by th `date` command on Linux.
