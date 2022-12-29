def string_test(s):
    d={"upper_case":0, "lower_case":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
                d["LOWER_CASE"]+=1
        else:
          pass
        print ("original string :",s)
        print ("no.of upper case characters :", d["upper_case"])
        print ("no.of lower case characters :", d["lower_case"])
        string_test('the quick brow fox')