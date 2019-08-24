c1 = "\x05\x46\x17\x12\x14\x18\x01\x0c\x0b\x34"
c2 = "\x3e\x1f\x00\x14\x0a\x08\x07\x51\x0a\x0e"

c = c1 + c2

m = "emem"
m = (len(c)//len(m))*m + m[:len(c)%len(m)]


key = ''
for i, j in zip(m, c):
	key += chr(ord(i)^ord(j))

print key


# m = "d4rk{meme__meme}c0de"
