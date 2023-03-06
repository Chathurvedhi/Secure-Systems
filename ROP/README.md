# *Instructions to run*

## Lab 2_1

To generate the explot string run:

```
$ python3 input1.py
```
We obtain payload1.exp as the payload.
Now we run payload on the executable file as:

```
$ ./lab_2_rop < payload1.exp
```

## Lab 2_2
To generate the explot string run:
```
$ python3 input2.py
```
We get an interaction as:
```
Enter the text : <plaintext string>
Enter the key : <key>
```
We obtain payload2.exp as the payload.
Now we run payload on the executable file as:

```
$ ./lab_2_rop < payload2.exp
```