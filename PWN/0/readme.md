# int_2_float

```python
def int_2_float(data):
    return str(struct.unpack('f', bytes(data))[0])

# optional
def write_8_bytes(data):
    r.sendline(int_to_float(data[:4]))
    r.sendline(int_to_float(data[4:]))
```

# int_2_double

```python
def to_double(data):
	return "%.800f " % unpack("<d", p64(data))
```

# double to hex
```python
def double_to_hex(f):
    return hex(struct.unpack('<Q', struct.pack('<d', float(f)))[0])
```

# format string buffer 
```python=
def fmt(prev, value, idx, byte=1):
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
```
