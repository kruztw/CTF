# encoding: utf-8

from Crypto.Util.number import long_to_bytes as l2b
import binascii
from modular_sqrt import modular_sqrt

p = 5411451825594838998340467286736301586172550389366579819551237
q = 5190863621109915362542582192103708448607732254433829935869841

n = p*q

c = 196353764385075548782571270052469419021844481625366305056739966550926484027148967165867708531585849658610359148759560853

def CRT(p, q):
	p_inverse_mod_q = lambda p, q,s=1,t=0,N=0: (q < 2 and t%N or p_inverse_mod_q(q, p%q, t, s-p//q*t, N or q),-1)[q<1]
	p_inverse = p_inverse_mod_q(p, q)
	q_inverse = -(p*p_inverse-1)//q
	return (p_inverse, q_inverse)

ans = []
def decrypt(c):
	try:
		global ans
		mp = modular_sqrt(c, p)
		mq = modular_sqrt(c, q)

		yp, yq = CRT(p, q)
		assert(yp*p + yq*q == 1)
		r1 = (yp*p*mq + yq*q*mp) % n
		r2 = n - r1
		r3 = (yp*p*mq - yq*q*mp) % n
		r4 = n - r3

		print l2b(r1)
		print l2b(r2)
		print l2b(r3)
		print l2b(r4)


		if all(r in ans for r in [r1, r2, r3, r4]):
			return

		ans += [r  for r in [r1, r2, r3, r4] if r not in ans]
		raw_input()
	except:
		exit(0)

	decrypt(r1)
	decrypt(r2)
	decrypt(r3)
	decrypt(r4)

# flag 會出現在第 20 回
decrypt(c)
