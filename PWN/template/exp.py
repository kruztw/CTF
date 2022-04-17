from util import *

##################################################

debug = True
tmux = False
binary = './a.out'

##################################################

context.arch = 'amd64'
context.log_level = 'debug'

if tmux:
    context.terminal = ['tmux', 'neww']

##################################################


r = process(binary)

if debug:
    gdb.attach(r)

r.interactive()
