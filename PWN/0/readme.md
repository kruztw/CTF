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

