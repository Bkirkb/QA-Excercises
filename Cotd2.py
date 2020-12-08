def counting(input):

    uppercount = 0
    lowercount = 0
    for letter in input:
        if letter.isupper():
            uppercount += 1
        elif letter.islower():
            lowercount += 1
        else:
            uppercount = uppercount
            lowercount = lowercount
    print("Uppercase letters :" , uppercount, "Lowercase letters :" , lowercount)
    return uppercount, lowercount

counting("ThIsHasALOtofcase issues")
counting("    THIS IS A TEST")