# Bandit Writeup on [overthewire.org](https://overthewire.org/wargames/bandit/)

This writeup is similar to other writeups from around the web and the few resources that I did use are around the web. We will use `sshpass` to make things easier to login without having to enter the password everytime. 

## Bandit Level 0

Not too hard. First `ssh` into the system as `bandit0` user. We use `sshpass` with the file `bandit0` and its password to login. We will create files for each level so `bandit0`, `bandit1`, `bandit2`, etc.
```
sshpass -f bandit0 ssh bandit0@bandit.labs.overthewire.org -p 2220
```
in some cases, you may need to use `cat bandit0`, instead of just `bandit0` to login.

## Bandit Level 0 --> Level 1

Password is stored in a file called `readme` so just `cat readme`.
```
sshpass -f bandit1 ssh bandit1@bandit.labs.overthewire.org -p 2220
```
## Bandit Level 1 --> Level 2

To output the file `-`, you need to escape the '-' character so `cat ~/-` will work just fine.
```
sshpass -f bandit2 ssh bandit2@bandit.labs.overthewire.org -p 2220
```
## Bandit Level 2 --> Level 3

We are trying to look for a file with the name `spaces in this filename`, but since there are spaces in the file, we have to escape the spaces so that the shell can interpret our command.

So we can do `cat spaces\ in\ this\ filename ` which will output the contents of the file. Fortunately with tab completion, we can press <button>Tab</button> to fill in the remainder of the filename.
```
sshpass -f bandit3 ssh bandit3@bandit.labs.overthewire.org -p 2220
```
## Bandit Level 3 --> Level 4

The flag is in the `inhere` folder so:
```
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -alt
total 12
drwxr-xr-x 2 root    root    4096 Oct 16  2018 .
drwxr-xr-x 3 root    root    4096 Oct 16  2018 ..
-rw-r----- 1 bandit4 bandit3   33 Oct 16  2018 .hidden
bandit3@bandit:~/inhere$ cat .hidden 
```
to get flag. Notice that when we leave out `-a` in `ls`, we don't see `.hidden`

```
sshpass -f bandit4 ssh bandit4@bandit.labs.overthewire.org -p 2220
```
## Bandit Level 4 --> Level 5

There are a host of similarly named files in the `inhere` folder and instead of checking them one by one for the password, we can try to `cat` all of them out using `cat ~/*` or using the `file ./*` command to `cat` out all files, in this case we want the `ASCII text` file.
```
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
```

```
sshpass -f bandit5 ssh bandit5@bandit.labs.overthewire.org -p 2220
```
## Bandit Level 5 --> Level 6

Find a file that is not executable, has a size of 1033 bytes and is human readable.
```
bandit5@bandit:~$ ls -l
total 4
drwxr-x--- 22 root bandit5 4096 Oct 16  2018 inhere
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere02  maybehere04  maybehere06  maybehere08  maybehere10  maybehere12  maybehere14  maybehere16  maybehere18
maybehere01  maybehere03  maybehere05  maybehere07  maybehere09  maybehere11  maybehere13  maybehere15  maybehere17  maybehere19
bandit5@bandit:~/inhere$ find \! -executable -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2 
```
`.file2` will have extra whitespace because of its 1033 bytes size.

```
sshpass -f bandit6 ssh bandit6@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 6 --> Level 7

Find a file somewhere on the server, so first `cd` into the root directory first and then:
```
bandit6@bandit:/$ find -user bandit7 -group bandit6 -size 33c 2> /dev/null
./var/lib/dpkg/info/bandit7.password
bandit6@bandit:/$ cat ./var/lib/dpkg/info/bandit7.password 
```
Use `2> /dev/null` to remove stderr messages.

```
sshpass -f bandit7 ssh bandit7@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 7 --> Level 8

Using a pipe with `cat` to `grep` for the word "millionth" is not necessary. For example, `cat data.txt | grep millionth` will work just fine but `grep millionth data.txt` is much easier.
```
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ grep millionth data.txt
```

```
sshpass -f bandit8 ssh bandit8@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 8 --> Level 9

First `sort` the `data.txt` file and then piping to `uniq` to find "the only line of text that appears only once"
```
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ sort data.txt | uniq -u
```

```
sshpass -f bandit9 ssh bandit9@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 9 --> Level 10

Print out strings that are human-readable so using `strings` and piping to `grep`: 
```
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ cat data.txt | strings | grep =
```

```
sshpass -f bandit10 ssh bandit10@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 10 --> Level 11

The password is `base64` encoded and we can decode it using `base64 -d`
```
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
bandit10@bandit:~$ base64 -d data.txt 
```

```
sshpass -f bandit11 ssh bandit11@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 11 --> Level 12

The contents in `data.txt` have been rotated by 13 positions so either search for cyberchef or `rot13.com` to get the password.

You can also create your own like the one below using `tr`. Or install `bsdgames`.
```
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

```
sshpass -f bandit12 ssh bandit12@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 12 --> Level 13

Use `mktemp -d` to save data temporarily.
```
bandit12@bandit:~$ ls
data.txt
bandit12@bandit:~$ mktemp -d
/tmp/tmp.dnpyFRVVPF
bandit12@bandit:~$ cp data.txt /tmp/tmp.dnpyFRVVPF
bandit12@bandit:~$ cd /tmp/tmp.dnpyFRVVPF
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data.txt
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ xxd -r data.txt > reversed
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data.txt  reversed
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file reversed 
reversed: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ mv reversed reversed.gz
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ gunzip reversed.gz 
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data.txt  reversed
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file reversed 
reversed: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ bunzip2 reversed
bunzip2: Can't guess original name for reversed -- using reversed.out
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data.txt  reversed.out
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file reversed.out 
reversed.out: gzip compressed data, was "data4.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ mv reversed.out reversed.gz
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data.txt  reversed.gz
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file reversed.gz 
reversed.gz: gzip compressed data, was "data4.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ gunzip reversed.gz 
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data.txt  reversed
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file reversed 
reversed: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ tar xf reversed
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data5.bin  data.txt  reversed
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file data.txt 
data.txt: ASCII text
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file *
data5.bin: POSIX tar archive (GNU)
data.txt:  ASCII text
reversed:  POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ tar xvf data5.bin
data6.bin
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file data6.bin 
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ bunzip2 data6.bin
bunzip2: Can't guess original name for data6.bin -- using data6.bin.out
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data5.bin  data6.bin.out  data.txt  reversed
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file *
data5.bin:     POSIX tar archive (GNU)
data6.bin.out: POSIX tar archive (GNU)
data.txt:      ASCII text
reversed:      POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ tar xvf data6.bin.out
data8.bin
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ mv data8.bin data8.bin.gz
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ gunzip data8.bin.gz 
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ ls
data5.bin  data6.bin.out  data8.bin  data.txt  reversed
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ file *
data5.bin:     POSIX tar archive (GNU)
data6.bin.out: POSIX tar archive (GNU)
data8.bin:     ASCII text
data.txt:      ASCII text
reversed:      POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.dnpyFRVVPF$ cat data8.bin
```

```
sshpass -f bandit13 ssh bandit13@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 13 --> Level 14

Use `ssh -i` to get to level 14. 
```
bandit13@bandit:~$ ls -l
total 4
-rw-r----- 1 bandit14 bandit13 1679 Oct 16  2018 sshkey.private
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
Could not create directory '/home/bandit13/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA2lo56:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
```

## Bandit Level 14 --> Level 15

Use `cat` in combination with `netcat` to get the password for the next level. 
```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14 | nc localhost 30000
```

```
sshpass -f bandit15 ssh bandit15@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 15 --> Level 16

Just like in `bandit13`, except using `openssl` instead of `nc`. Also include `-ign_eof` (ignore end of file).
```
bandit15@bandit:~$ cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -ign_eof
```
The password is shown below the output where it says `Correct!` 

```
sshpass -f bandit16 ssh bandit16@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 16 --> Level 17

Use `nmap` to find open port on `localhost`. Then use `openssl` to get RSA private key for `bandit17`.
```
bandit16@bandit:~$ nmap localhost -p31000-32000

Starting Nmap 7.40 ( https://nmap.org ) at 2020-03-26 00:03 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00022s latency).
Not shown: 999 closed ports
PORT      STATE    SERVICE
31518/tcp filtered unknown
31790/tcp open     unknown

Nmap done: 1 IP address (1 host up) scanned in 1.25 seconds
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31518 -ign_eof
^C
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31790 -ign_eof
CONNECTED(00000003)
```

Before continuing to the next level, make a temporary directory and set the permissions as follows for the RSA private key:
`chmod 600 bandit17.key`. The name of the file can be anything such as `bandit17` without the `.key` extension.

```
bandit16@bandit:~$ mktemp -d
/tmp/tmp.80Uhd4zp7i
bandit16@bandit:~$ cd /tmp/tmp.80Uhd4zp7i
bandit16@bandit:/tmp/tmp.80Uhd4zp7i$ vim bandit17
bandit16@bandit:/tmp/tmp.80Uhd4zp7i$ ls -l
total 4
-rw-r--r-- 1 bandit16 root 1675 Mar 28 23:25 bandit17
bandit16@bandit:/tmp/tmp.80Uhd4zp7i$ chmod 600 bandit17 
bandit16@bandit:/tmp/tmp.80Uhd4zp7i$ ls -l
total 4
-rw------- 1 bandit16 root 1675 Mar 28 23:25 bandit17
bandit16@bandit:/tmp/tmp.80Uhd4zp7i$ ssh -i bandit17 bandit17@localhost
Could not create directory '/home/bandit16/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit16/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

```

## Bandit Level 17 --> Level 18

Compare `passwords.old` with `passwords.new` using `diff`

```
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< hlbSBPAWJmL6WFDb06gpTx1pPButblOA
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

```
sshpass -f bandit18 ssh bandit18@bandit.labs.overthewire.org -p 2220
```

When it outputs `ByeBye !`, the connection will close, which is directly related to solving `bandit19`.

## Bandit Level 18 --> Level 19

`sshpass` allows us to pass commands before the connection closes so add `"cat readme"` at the end of the previous command to get the password for the next level.

```
sshpass -f bandit18 ssh bandit18@bandit.labs.overthewire.org -p 2220 "id"
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

uid=11018(bandit18) gid=11018(bandit18) groups=11018(bandit18)

sshpass -f bandit18 ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames
```

```
sshpass -f bandit19 ssh bandit19@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 19 --> Level 20

Run the `setuid` binary like so: `./bandit20-do`. The password files are in `/etc/bandit_pass/`.

```
bandit19@bandit:~$ ls -l
total 8
-rwsr-x--- 1 bandit20 bandit19 7296 Oct 16  2018 bandit20-do
bandit19@bandit:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20 
```

```
sshpass -f bandit20 ssh bandit20@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 20 --> Level 21

This level is similar to the previous one except a second `ssh` connection will be needed to complete it.

In one shell:
```
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ nc -lvp 8888
listening on [any] 8888 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 58308
```
In another:
```
bandit20@bandit:~$ ./suconnect 8888
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
```

```
sshpass -f bandit21 ssh bandit21@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 21 --> Level 22

```
bandit21@bandit:~$ ls /etc/cron.d/
atop  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
bandit21@bandit:~$ cd /etc/cron.d/
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh 
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ ls -l /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
-rw-r--r-- 1 bandit22 root 33 Apr  3 20:26 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

```
sshpass -f bandit22 ssh bandit22@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 22 --> Level 23

```
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ ls -l /usr/bin/cronjob_bandit23.sh 
-rwxr-x--- 1 bandit23 bandit22 211 Oct 16  2018 /usr/bin/cronjob_bandit23.sh
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh 
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$ mytarget=$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
bandit22@bandit:~$ echo $mytarget
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

```
sshpass -f bandit23 ssh bandit23@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 23 --> Level 24

```
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh 
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
    echo "Handling $i"
    timeout -s 9 60 ./$i
    rm -f ./$i
    fi
done


bandit23@bandit:~$ cd /var/spool/bandit24/
bandit23@bandit:/var/spool/bandit24$ mkdir /tmp/temp1
bandit23@bandit:/var/spool/bandit24$ chmod 777 /tmp/temp1
bandit23@bandit:/var/spool/bandit24$ date
Fri Apr  3 23:02:49 CEST 2020
bandit23@bandit:/var/spool/bandit24$ date
Fri Apr  3 23:03:01 CEST 2020
bandit23@bandit:/var/spool/bandit24$ nano get.sh
Unable to create directory /home/bandit23/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue

bandit23@bandit:/var/spool/bandit24$ date
Fri Apr  3 23:04:05 CEST 2020
bandit23@bandit:/var/spool/bandit24$ chmod +x get.sh
bandit23@bandit:/var/spool/bandit24$ date
Fri Apr  3 23:04:39 CEST 2020
bandit23@bandit:/var/spool/bandit24$ ls get.sh
get.sh
bandit23@bandit:/var/spool/bandit24$ ls -l get.sh
-rwxr-xr-x 1 bandit23 bandit23 73 Apr  3 23:04 get.sh
bandit23@bandit:/var/spool/bandit24$ date
Fri Apr  3 23:04:59 CEST 2020
bandit23@bandit:/var/spool/bandit24$ date
Fri Apr  3 23:05:03 CEST 2020
bandit23@bandit:/var/spool/bandit24$ ls /tmp/temp1
the_password.txt
bandit23@bandit:/var/spool/bandit24$ cat /tmp/temp1/the_password.txt
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
bandit23@bandit:/var/spool/bandit24$ date
Fri Apr  3 23:06:00 CEST 2020
bandit23@bandit:/var/spool/bandit24$ cat /tmp/temp1/the_password.txt
```

```
sshpass -f bandit24 ssh bandit24@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 24 --> Level 25

Brute force with for loop either using bash or python with sockets to get the password.

```
bandit24@bandit:~$ cd /tmp/temp1
bandit24@bandit:/tmp/temp1$ ls
the_password.txt
bandit24@bandit:/tmp/temp1$ nano hammer.sh
Unable to create directory /home/bandit24/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue

bandit24@bandit:/tmp/temp1$ chmod +x hammer.sh 

bandit24@bandit:/tmp/temp1$ ./hammer.sh > bruteforce.txt
bandit24@bandit:/tmp/temp1$ cat bruteforce.txt | nc localhost 30002
...
...
... 
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Correct!
```

```
sshpass -f bandit25 ssh bandit25@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 25 --> Level 26

You will need to change the size of the window in such a way that it is "thin" enough to enter a sub shell, or in this case a editor in `vi`.
When you see `--MORE--(NN%)`, you have a buffer.

After entering vim mode, enter: `:r /etc/bandit_pass/bandit26` <button>Enter</button>
After escape from `vi`, you should see the password.
```
bandit25@bandit:~$ ls
bandit26.sshkey
bandit25@bandit:~$ cat bandit26.sshkey 
...
...
...
bandit25@bandit:~$ file /usr/bin/showtext 
/usr/bin/showtext: POSIX shell script, ASCII text executable
bandit25@bandit:~$ cat /usr/bin/showtext 
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost
Could not create directory '/home/bandit25/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit25/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames
```

```
sshpass -f bandit26 ssh bandit26@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 26 --> Level 27

Just like in the previous level, we shrink our window to get a buffer and, after entering `vi`, enter a shell with `:set shell=/bin/bash`
and running the shell in `vi`.
```
:shell
bandit26@bandit:~$ ls
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Zbandit27-do  text.txt
bandit26@bandit:~$ cat text.txt
  _                     _ _ _   ___   __  
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \ 
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/ 
bandit26@bandit:~$ ls -l
total 12
-rwsr-x--- 1 bandit27 bandit26 7296 Oct 16  2018 bandit27-do
-rw-r----- 1 bandit26 bandit26  258 Oct 16  2018 text.txt
bandit26@bandit:~$ ./bandit27-do 
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
```

```
sshpass -f bandit27 ssh bandit27@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 27 --> Level 28

You will need to create a temporary directory to `git clone` the repo and read the `README` for the password. 
```
bandit27@bandit:~$ ls
bandit27@bandit:~$ mktemp -d
/tmp/tmp.yoPkZ2zKIl
bandit27@bandit:~$ cd /tmp/tmp.yoPkZ2zKIl
bandit27@bandit:/tmp/tmp.yoPkZ2zKIl$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit27/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/tmp.yoPkZ2zKIl$ ls
repo
bandit27@bandit:/tmp/tmp.yoPkZ2zKIl$ cd repo/
bandit27@bandit:/tmp/tmp.yoPkZ2zKIl/repo$ ls
README
bandit27@bandit:/tmp/tmp.yoPkZ2zKIl/repo$ cat README
```

```
sshpass -f bandit28 ssh bandit28@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 28 --> Level 29

```

bandit28@bandit:~$ mktemp -d
/tmp/tmp.1YYcQI9fvX
bandit28@bandit:~$ cd /tmp/tmp.1YYcQI9fvX
bandit28@bandit:/tmp/tmp.1YYcQI9fvX$ ls
bandit28@bandit:/tmp/tmp.1YYcQI9fvX$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit28/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password: 
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0)
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.1YYcQI9fvX$ ls
repo
bandit28@bandit:/tmp/tmp.1YYcQI9fvX$ cd repo/
bandit28@bandit:/tmp/tmp.1YYcQI9fvX/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.1YYcQI9fvX/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.1YYcQI9fvX/repo$ git log
commit 073c27c130e6ee407e12faad1dd3848a110c4f95
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    fix info leak

commit 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    add missing data

commit b67405defc6ef44210c53345fc953e6a21338cc7
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    initial commit of README.md
bandit28@bandit:/tmp/tmp.1YYcQI9fvX/repo$ git show 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
commit 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    add missing data

diff --git a/README.md b/README.md
index 7ba2d2f..3f7cee8 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: <TBD>
```

```
sshpass -f bandit29 ssh bandit29@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 29 --> Level 30

```
bandit29@bandit:~$ mktemp -d
/tmp/tmp.gWfvkfXRxv
bandit29@bandit:~$ cd /tmp/tmp.gWfvkfXRxv
bandit29@bandit:/tmp/tmp.gWfvkfXRxv$ git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit29/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit29-git@localhost's password: 
remote: Counting objects: 16, done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0)
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/tmp.gWfvkfXRxv$ ls
repo
bandit29@bandit:/tmp/tmp.gWfvkfXRxv$ cd repo/
bandit29@bandit:/tmp/tmp.gWfvkfXRxv/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.gWfvkfXRxv/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.gWfvkfXRxv/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.gWfvkfXRxv/repo$ git checkout remotes/origin/dev
Note: checking out 'remotes/origin/dev'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at 33ce2e9... add data needed for development
bandit29@bandit:/tmp/tmp.gWfvkfXRxv/repo$ git log
commit 33ce2e95d9c5d6fb0a40e5ee9a2926903646b4e3
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:41 2018 +0200

    add data needed for development

commit a8af722fccd4206fc3780bd3ede35b2c03886d9b
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:41 2018 +0200

    add gif2asc

t 84abedc104bbc0c65cb9eb74eb1d3057753e70f8
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:41 2018 +0200

    fix username

commit 9b19e7d8c1aadf4edcc5b15ba8107329ad6c5650
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:41 2018 +0200

    initial commit of README.md
bandit29@bandit:/tmp/tmp.gWfvkfXRxv/repo$ git show 33ce2e95d9c5d6fb0a40e5ee9a2926903646b4e3
commit 33ce2e95d9c5d6fb0a40e5ee9a2926903646b4e3
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:41 2018 +0200

    add data needed for development

diff --git a/README.md b/README.md
index 1af21d3..39b87a8 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for bandit30 of bandit.
 ## credentials
 
 - username: bandit30
-- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.gWfvkfXRxv/repo$ git grep password
README.md:- password:
```

```
sshpass -f bandit30 ssh bandit30@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 30 --> Level 31

```
bandit30@bandit:~$ mkdir /tmp/sud0
bandit30@bandit:~$ cd /tmp/sud0
bandit30@bandit:/tmp/sud0$ ls
bandit30@bandit:/tmp/sud0$ git clone ssh://bandit30-git@localhost/home/bandit30-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit30/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password: 
remote: Counting objects: 4, done.
remote: Total 4 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/sud0$ ls
repo
bandit30@bandit:/tmp/sud0$ cd repo/
bandit30@bandit:/tmp/sud0/repo$ ls
README.md
bandit30@bandit:/tmp/sud0/repo$ cat README.md 
just an epmty file... muahaha
bandit30@bandit:/tmp/sud0/repo$ git log
commit 3aa4c239f729b07deb99a52f125893e162daac9e
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:44 2018 +0200

    initial commit of README.md
bandit30@bandit:/tmp/sud0/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
bandit30@bandit:/tmp/sud0/repo$ ls -a
.  ..  .git  README.md
bandit30@bandit:/tmp/sud0/repo$ cd .git/
bandit30@bandit:/tmp/sud0/repo/.git$ ls
branches  config  description  HEAD  hooks  index  info  logs  objects  packed-refs  refs
bandit30@bandit:/tmp/sud0/repo/.git$ cat packed-refs 
# pack-refs with: peeled fully-peeled 
3aa4c239f729b07deb99a52f125893e162daac9e refs/remotes/origin/master
f17132340e8ee6c159e0a4a6bc6f80e1da3b1aea refs/tags/secret
bandit30@bandit:/tmp/sud0/repo/.git$ git show f17132340e8ee6c159e0a4a6bc6f80e1da3b1aea
```

```
sshpass -f bandit31 ssh bandit31@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 31 --> Level 32

```
bandit31@bandit:~$ mkdir /tmp/sud01
bandit31@bandit:~$ cd /tmp/sud01
bandit31@bandit:/tmp/sud01$ git clone ssh://bandit31-git@localhost/home/bandit31-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit31/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (4/4), done.
bandit31@bandit:/tmp/sud01$ ls
repo
bandit31@bandit:/tmp/sud01$ cd repo/
bandit31@bandit:/tmp/sud01/repo$ ls
README.md
bandit31@bandit:/tmp/sud01/repo$ cat README.md 
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/sud01/repo$ git branch
* master
bandit31@bandit:/tmp/sud01/repo$ nano key.txt
Unable to create directory /home/bandit31/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue

bandit31@bandit:/tmp/sud01/repo$ git add key.txt 
The following paths are ignored by one of your .gitignore files:
key.txt
Use -f if you really want to add them.
bandit31@bandit:/tmp/sud01/repo$ ls -al
total 24
drwxr-sr-x 3 bandit31 root 4096 Apr  5 01:35 .
drwxr-sr-x 3 bandit31 root 4096 Apr  5 01:32 ..
drwxr-sr-x 8 bandit31 root 4096 Apr  5 01:36 .git
-rw-r--r-- 1 bandit31 root    6 Apr  5 01:33 .gitignore
-rw-r--r-- 1 bandit31 root   15 Apr  5 01:35 key.txt
-rw-r--r-- 1 bandit31 root  147 Apr  5 01:33 README.md
bandit31@bandit:/tmp/sud01/repo$ cat .gitignore 
*.txt
bandit31@bandit:/tmp/sud01/repo$ git add key.txt -f
bandit31@bandit:/tmp/sud01/repo$ git commit 
Unable to create directory /home/bandit31/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue

[master 4f1d50e] Added key.txt
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
bandit31@bandit:/tmp/sud01/repo$ git push
Could not create directory '/home/bandit31/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
Permission denied, please try again.
bandit31-git@localhost's password: 
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 323 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
```

```
sshpass -f bandit32 ssh bandit32@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 32 --> Level 33

When we start the `ssh` connection, we are brought to an shell that turns all input into uppercase.
```
WELCOME TO THE UPPERCASE SHELL
$ mkdir /tmp/upper
$ cd /tmp/upper 
$ ls
$ vim SCRIPT.SH 
$ chmod +x SCRIPT.SH
$ ./SCRIPT.SH
bandit33@bandit:/tmp/upper$ ls
SCRIPT.SH
bandit33@bandit:/tmp/upper$ cat /etc/bandit_pass/bandit33
```

Another way to do it would be to run `$0` to get the password for the next level.
```
>> $0
$ cat /etc/bandit_pass/bandit33
```

```
sshpass -f bandit33 ssh bandit33@bandit.labs.overthewire.org -p 2220
```

## Bandit Level 33 --> Level 34

Not available at this time.
