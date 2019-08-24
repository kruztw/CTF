  難度 :  :star: :star:
  
  ![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/crypto/AgainAndAgainAndAgain/pic1.png)

解題想法 : <br>
	加密方式為 [rabin cipher](https://en.wikipedia.org/wiki/Rabin_cryptosystem)  而且有給 p, q , 因此照著解密就行了 <br>
    難就難在 mp , mq 不能照著 wiki 上面做 <br>
    正確作法我引用[這篇的 code](https://github.com/pcw109550/write-up/tree/master/2019/HackCon/AgainAndAgainAndAgain) <br>