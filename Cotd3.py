def blah(i1,i2):

    i1l = len(i1)
    i2l = len(i2)
    output = ""
    i = 0

    while i < i1l:
        output += i1[i]
        output += i2[i]
        i += 1
    print(output)
    return output


blah("STRRRI", "string")
blah("String","Fridge")