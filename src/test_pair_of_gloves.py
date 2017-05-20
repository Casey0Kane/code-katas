Test.describe("Basic tests")
Test.assert_equals(number_of_pairs(["red","red"]),1)
Test.assert_equals(number_of_pairs(["red","green","blue"]),0)
Test.assert_equals(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
Test.assert_equals(number_of_pairs([]),0)
Test.assert_equals(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]),4)

Test.describe("Random tests")
from random import randint
sol=lambda g: sum(int(g.count(a)/2) for a in set(g))
colors = ["White","Yellow","Fuchsia","Red","Silver","Gray","Olive","Purple","Maroon","Aqua","Lime","Teal","Green","Blue","Navy","Black"]

for _ in range(40):
  g=[colors[randint(0,len(colors)-1)] for q in range(randint(1,25))]
  Test.it("Testing for "+repr(g))
  Test.assert_equals(number_of_pairs(g[:]),sol(g),"It should work for random inputs too")