
def sortwords(input):
    newstring = []
    splitinput = input.split(" ")
    for word in splitinput:
        if word.lower() not in newstring: # Eliminate case discrepency
            newstring = [word.lower() for word in newstring] #also eliminate case discrepency
            newstring.append(word)
            newstring.sort() 
        else:
            newstring.sort() # Last word was not sorting with this off
    print(" ".join(newstring))
    return(" ".join(newstring))

sortwords("This is is is a string of words")
sortwords("I Am E very Happy strung strung demonic human")
sortwords("I can BE who I want to beee and am a bee and and can do what i wish to")