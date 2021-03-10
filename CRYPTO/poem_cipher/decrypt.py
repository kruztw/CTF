# https://en.wikipedia.org/wiki/Poem_code

#!/usr/bin/env python3

key = "DMFAU"
cipher = "PELA DOZC EBET ETTI RUVF OREE IOAX HHAS MOOU LRSS TKNR ORUE NINR EMVQ TSWT ANEA TSDJ IERM OHEX OTEA"

poem = """
’Twas brillig, and the slithy toves

     Did gyre and gimble in the wabe: 

All mimsy were the borogoves,

     And the mome raths outgrabe.
"""

new_poem = ""
for i in range(len(poem)):
    if ord('A') <= ord(poem[i]) <= ord('Z') or ord('A') <= ord(poem[i]) <= ord('z') or poem[i] == ' ' or poem[i] == '.':
        new_poem += poem[i]

new_poem = new_poem.upper().split()
key_num = [ ord(k) - ord('A') for k in key]
key_word = []
for k in key_num:
    t = []
    while k < len(new_poem):
        t.append(new_poem[k])
        k += 26
    key_word.append(t)

pos = [0]*len(key_word)
while pos[0] != len(key_word[0]):
    key_str = []
    for i in range(len(key_word)):
        key_str += key_word[i][pos[i]]
    
    key_str = ''.join(key_str)
    key_seq = [0] * len(key_str)

    cnt = 1
    for i in range(ord('A'), ord('Z')):
        for j in range(len(key_str)):
            if key_str[j] == chr(i):
                key_seq[j] = cnt
                cnt += 1

    cipher = ''.join(cipher.split())
    cipher_len = len(cipher)
    row_num = cipher_len // len(key_seq)
    
    message = [[0] * len(key_seq) for _ in range(row_num)]
    
    for c in range(len(key_seq)):
        for r in range(row_num):
            message[r][c] = cipher[(key_seq[c]-1)*row_num + r]
     
    m = []
    for mess in message:
        m += mess
    
    print(''.join(m))
    
    pos[-1] += 1
    for i in range(len(pos)-1, 0, -1):
        if pos[i] == len(key_word[i]):
            pos[i] = 0
            pos[i-1] += 1
