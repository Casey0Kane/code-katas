def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("contain_all_rots")
Test.it("Basic tests")
testing(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True)
testing(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]), False)
testing(contain_all_rots("QJAhQmS", ["hQmSQJA", "QJAhQmS", "QmSQJAh", "yUgUXoQE", "AhQmSQJ", "mSQJAhQ", "SQJAhQm", "JAhQmSQ"]), True)
testing(contain_all_rots("Etsshp", ["nVOETcaxdvuk", "shpEts", "hpEtss", "Etsshp", "OuIiQ", "sXrDdPXIaW", "tsshpE", "pEtssh"]), False)
testing(contain_all_rots("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl"]), False)
testing(contain_all_rots("MqhWvHF", ["numMfygcH", "HFMqhWv", "qhWvHFM", "ZJKKxM", "hWvHFMq", "MqhWvHF", "hfZWYSqk", "BTcSoEdchPlL", "WvHFMqh", "vHFMqhW", "FMqhWvH"]), True)
testing(contain_all_rots("UDvG", ["vGUD", "UDvG", "GUDv", "DvGU"]), True)
testing(contain_all_rots("sObPfw", ["ObPfws", "Cofuhqrmmzq", "wFvfcqU", "sObPfw", "bPfwsO", "PfwsOb", "wsObPf", "fwsObP"]), True)
testing(contain_all_rots("KUckM", ["MKUck", "EDjfbQB", "GUPwzk", "SKZvilwnL", "UckMK", "KUckM", "kMKUc"]), False)
testing(contain_all_rots("FDIe", ["DIeF", "IeFD", "FDIe", "eFDI"]), True)
testing(contain_all_rots("12341234", ["DIeF", "IeFD", "12341234", "41234123", "34123412", "23412341"]), True)

from random import randint
from random import shuffle

def do_str(k):
    i = 0; s = ""
    while (i < k):
        if (randint(0, 100) % 2 == 0):
            s += chr(randint(97, 122)) 
        else:
            s += chr(randint(65, 90))
        i += 1
    return s

def rotations_array_sol32(strng):
    result = []
    for mid in range(len(strng)):
        rot = strng[mid:] + strng[:mid]
        if rot in result:
            return result
        else:
            result.append(rot)
    return result
def contain_all_rots_sol32(strng, arr):
    rots = rotations_array_sol32(strng)
    i = 0
    while (i < len(rots)):
        if (not (rots[i] in arr)):
            return False
        i += 1
    return True

def do_ex(strng):
    rot = rotations_array_sol32(strng)
    k = randint(0, 100)
    if (k % 2 == 0):
        i = randint(0, len(rot)-1)
        del(rot[i])
    n = randint(0, 5)
    i = 0
    while (i < n):
        rot.append(do_str(randint(8, 15)))
        i += 1
    shuffle(rot)
    return rot

def tests():
    print("Random Tests contain_all_rots")
    i = 0
    while (i < 200):
        a = do_str(randint(10, 15))
        r = do_ex(a)
        testing(contain_all_rots(a, r), contain_all_rots_sol32(a, r))
        i += 1

tests()