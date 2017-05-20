Test.describe("Basic tests")
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), True)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
a1 = []
a2 = []
test.assert_equals(comp(a1, a2), True)
a1 = []
a2 = None
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11, 1008]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
a1 = [10000000, 100000000]
a2 = [10000000 * 10000000, 100000000 * 100000000]
test.assert_equals(comp(a1, a2), True)
a1 = [10000001, 100000000]
a2 = [10000000 * 10000000, 100000000 * 100000000]
test.assert_equals(comp(a1, a2), False)

Test.describe("Random tests")
from random import randint

sol=lambda a1, a2: sorted(a1)==sorted([item**.5 for item in a2]) if a1!=None and a2!=None else False

for i in range(40):
  a1=[randint(0,100) for i in range(randint(1,8))]
  a2=[elem*elem for elem in a1]
  if randint(0,1)==1: a2[randint(0,len(a2)-1)]+=1
  Test.it("Testing for "+str(a1)+" and "+str(a2))
  Test.assert_equals(comp(a1[:],a2[:]),sol(a1,a2),"It should work with random inputs too")