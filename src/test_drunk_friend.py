Test.describe("Basic tests")
Test.assert_equals(decode("yvvi"), "beer")
Test.assert_equals(decode("Blf zoivzwb szw 10 yvvih"), "You already had 10 beers")
Test.assert_equals(decode("Ovg'h hdrn rm gsv ulfmgzrm!"), "Let's swim in the fountain!")
Test.assert_equals(decode({"brand": "Starobrno" }), "Input is not a string")
Test.assert_equals(decode("Tl slnv, blf'iv wifmp"), "Go home, you're drunk") 
Test.assert_equals(decode("Hfiv r xzm wzmxv lm xlk'h xzi, slow nb yvvi"), "Sure i can dance on cop's car, hold my beer")
Test.assert_equals(decode(True), "Input is not a string")
Test.assert_equals(decode("Hvv? R'n mlg gszg wifmp, r xzm hgroo gzpv nb xolgsvh luu"), "See? I'm not that drunk, i can still take my clothes off")
Test.assert_equals(decode(123), "Input is not a string")
Test.assert_equals(decode(["Beer"]), "Input is not a string")

Test.describe("Random tests")
from random import randint
base="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 .,:;?!"
sol=lambda s: "".join(["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"["zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA".index(char)] if char.isalpha() else char for char in s])

for _ in range(40):
    s="".join([base[randint(0,len(base)-1)] for x in xrange(randint(1,50))])
    Test.it("Testing for "+s)
    Test.assert_equals(decode(s),sol(s),"It should work for random inputs too")