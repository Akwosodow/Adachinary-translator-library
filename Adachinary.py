def Adachit(sentence: str) -> str:
    newstring = ""
    for i in sentence:
        if i == "0":
            newstring += ":AdachiFalse: "
        elif i == "1":
            newstring += ":AdachiTrue: "
        else:
            newstring += "/ "
    return(newstring)

#turns ASCII (ascdachii) characters into binary
#so like you kinda have to tell people that when they go to translate
#because it will not translate correctly on the online binary translator's default setting
def Binary(sentence: str) -> str:
    newstring = ""
    for i in sentence:
        if i != " ":
            newstring += format(ord(i), '08b')
        else:
            newstring += " "
    return(newstring)

def Morse(sentence: str) -> str:
    #evil ass eval function :adachitroll:
    #this dict long as hell I don't wanna hardcode it
    #also it allows people to swap out the dictionary or smth idk
    try:
        with open("./MorseDict.txt", "r") as file:
            morseqiv = eval(file.read())
    except:
        return("Dawg you have no morse dictionary")

    newstring = ""
    for i in sentence:
        try:
            newstring += morseqiv[i.upper()]
            newstring += " "
        except:
            if i == " ":
                newstring += "/ "
            #we just ignore the shit that doesnt map to anything fr
    return(newstring)

#fuck if I know what ts does bruh
def InvBinary(sentence: list) -> str:
    newstring = ""
    for i in sentence:
        letters = [i[j:j+8] for j in range(0, len(i), 8)]
        newstring += "".join([chr(int(k, 2)) for k in letters])
        newstring += " "
    return(newstring)

def InvMorse(sentence: list) -> str:
    try:
        with open("./MorseDict.txt", "r") as file:
            morseqiv = eval(file.read())
    except:
        return("Dawg you have no morse dictionary")
    invmorseqiv = dict(map(reversed, morseqiv.items()))
    newstring = ""

    for i in sentence:
        newstring += invmorseqiv[i]
    return(newstring)

def TheOtherWay(adactence: list) -> str:
    adachilate = {":AdachiTrue:" : "1", ":AdachiFalse:" : "0"}
    
    newstring = ""
    for i in adactence.split("/"):
        for j in i.split():
            try:
                newstring += adachilate[j]
            except:
                #again we just ignore shit that doesnt map, I am not writing error messages
                ...
        newstring+= " "

    newarray = newstring.split()
    if len(newarray[0])%8==0:
        final = InvBinary(newarray)
    else:
        final = InvMorse(newarray)
    return(final)

#CLI stuff:
if __name__ == "__main__":
    string = input("Enter plaintext (all special characters will be ignored by the morse function): ")
    print(Adachit(Binary(string)))
    print(Adachit(Morse(string)))
    string = input("Enter adachi text: ")
    print(TheOtherWay(string))
