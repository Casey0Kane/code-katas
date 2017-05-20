Test.describe("Basic tests")
Test.assert_equals(compare("AD", "BC"), True, "\'AD\' vs \'BC\'")
Test.assert_equals(compare("AD", "DD"), False, "\'AD\' vs \'DD\'")
Test.assert_equals(compare("gf", "FG"), True, "\'gf\' vs \'FG\'")
Test.assert_equals(compare("Ad", "DD"), False, "\'Ad\' vs \'DD\'")
Test.assert_equals(compare("zz1", ""), True, "\'zz1\' vs \'\'")
Test.assert_equals(compare("ZzZz", "ffPFF"), True, "\'ZzZz\' vs \'ffPFF\'")
Test.assert_equals(compare("kl", "lz"), False, "\'kl\' vs \'lz\'")
Test.assert_equals(compare(None, ""), True, "\'<null>\' vs \'\'")
Test.assert_equals(compare("!!", "7476"), True, "\'!!\' vs \'7476\'")
Test.assert_equals(compare("##", "1176"), True, "\'##\' vs \'1176\'")

Test.describe("Random tests")
from random import randint,random
sol=lambda s1,s2: (sum(map(ord,s1.upper())) if type(s1)==str and all([l.isalpha() for l in s1]) else 0)==(sum(map(ord,s2.upper())) if type(s2)==str and all([l.isalpha() for l in s2]) else 0)
base="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for _ in range(40):
  s1=[ord(base[randint(0,len(base)-1)]) for q in range(0,randint(1,15))]
  s2="".join(map(chr,sorted(s1,key=lambda a: random())))
  for k in range(randint(2,5)):
      n=randint(1,5)
      s1[randint(0,len(s1)-1)]-=n
      s1[randint(0,len(s1)-1)]+=n
  if randint(0,4)==4: s1[randint(0,len(s1)-1)]=ord(base[randint(0,len(base)-1)])
  s1="".join(map(chr,sorted(s1,key=lambda a: random())))
  s1,s2=sorted([s1,s2], key=lambda a: random())
  Test.it("Testing for %s and %s" %(repr(s1),repr(s2)))
  Test.assert_equals(compare(s1,s2), sol(s1,s2), "It should work for random inputs too")