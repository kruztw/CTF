import gmpy2

cipher = 2205316413931134031046440767620541984801091216351222789180582564557328762455422721368029531360076729972211412236072921577317264715424950823091382203435489460522094689149595951010342662368347987862878338851038892082799389023900415351164773
 
with gmpy2.local_context(gmpy2.context(), precision=100000) as ctx:
  m = gmpy2.cbrt(cipher)

try:
    print(str('%x' % + int(m)).decode('hex'))
except AttributeError:
    print(bytes.fromhex(str('%x' % + int(m))).decode('utf-8'))
