import os
import socket
import time
import subprocess

# copy flag to /tmp
os.system("ln -s /home/input2/flag flag")

#stage1
argv = ["0"] * 99
argv[ord("A")-1] = ""
argv[ord("B")-1] = "\x20\x0a\x0d"

#stage2
stdin_r, stdin_w   = os.pipe()
stderr_r, stderr_w = os.pipe()
os.write(stdin_w, "\x00\x0a\x00\xff")
os.write(stderr_w, "\x00\x0a\x02\xff")

#stage3
Env = {"\xde\xad\xbe\xef" : "\xca\xfe\xba\xbe"}

#stage4
with open("\x0a", "wb") as f:
    f.write(b"\x00\x00\x00\x00")

#stage5
port = 8888
argv[ord("C")-1] = str(port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
subprocess.Popen(["/home/input2/input"]+argv, stdin=stdin_r, stderr=stderr_r, env=Env)
time.sleep(1)
s.connect(("127.0.0.1", port))
s.send("\xde\xad\xbe\xef")
s.close()
