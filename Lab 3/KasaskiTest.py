englishIC = 0.065
alphabets = "abcdefghijklmnopqrstuvwxyz"
icThreshold = 0.01

def findLength(cipherText, max_length):
    for i in range(1, max_length):
        res = TestLength(cipherText, i)
        if res:
            return i

def TestLength(cipherText, length):
    Y_parts = []
    Y_ICs = []
    AllEqual = True
    comparisonString = ""
    for i in range(length):
        part = cipherText[i::length]
        Y_parts.append(part)
        tempIC = calculateIC(part)
        if abs(tempIC - englishIC) < icThreshold:
            comparisonString += "1"
        else:
            comparisonString += "0"
            AllEqual = False
        Y_ICs.append(tempIC)
    avgIc = sum(Y_ICs)/len(Y_ICs)
    majorityRation = 0.6  # ration to consider whether match is valid or not
    if(comparisonString.count("1")/len(comparisonString) > majorityRation):
        AllEqual = True
    if abs(englishIC - avgIc) < icThreshold and AllEqual:
        return True
    else:
        return False 

def calculateIC(Lang):
    n = len(Lang)
    langFreq = getFreq(Lang)
    Ic = sum([f*(f-1)/(n*n) for f in langFreq])
    return Ic

def getProb(LangYList):
    alphabetsList = [c for c in alphabets]
    n = len(LangYList)
    ProbList = [LangYList.count(c)/n for c in alphabetsList]
    return ProbList

def getFreq(LangYList):
    alphabetsList = [c for c in alphabets]
    freqList = [LangYList.count(c) for c in alphabetsList]
    return freqList

def test():
    key = "pascal"
    cipher = "ihwjierhzkkpgsywiottgvhpvadcxjxsljeqxrkvoqhipdozzsaptsthavcswicgrdvuafeedtzgglaapaczbevasnxefeeqxclkoyiranornbqfofvlsuaopmkvhpconglthafcdletsvizcoxvhpuijutqdujracisghaopmkurlsiguecxekqfewekcmpcaegtstngxewlakhichthwbwxszgdtclgpdzcofqcedbwtiehodfczeiwuiyihwhichtljrptmgptsh"
    length = findLength(cipher, 26)
    print("key was ", key)
    print("cipher was : ", cipher)
    print("predicted length : ", length)