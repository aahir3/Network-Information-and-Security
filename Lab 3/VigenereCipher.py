from KasaskiTest import findLength

alphabets = "abcdefghijklmnopqrstuvwxyz"
english_probability = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
base=ord('a')
icThreshold = 0.01
def getProb(LangYList):
    alphabetsList = [c for c in alphabets]
    n = len(LangYList)
        # print(LangYList, n)
    ProbList = [LangYList.count(c)/n for c in alphabetsList]
    return ProbList

def getKeyFromCipher(LangX_Probability, LangY, maxChar=26):
        print("____________\nExtracting Key from cipher")
        LangY = [c for c in LangY]
        LangY_Probability = getProb(LangY)
        MI_buffer = []
        for _ in range(len(LangX_Probability)):
            MI = sum([LangX_Probability[countJ]*LangY_Probability[countJ]
                      for countJ in range(len(LangX_Probability))])
            MI_buffer.append(MI)
            LangY_Probability.append(LangY_Probability.pop(0))
        max_MI = max(MI_buffer)
        key = MI_buffer.index(max_MI)
        print("MIC : ", max_MI, "\nKey found :", chr(base + key))
        return key
def encrypt(msg,k):
    l=len(msg)
    l1=len(k)
    msg=list(msg)
    k=[ord(ch)-97 for ch in k]
    for _ in range(l):
        msg[_]=chr(((ord(msg[_]) - 97 + k[_ % l1]) % 26 ) + 97)
    return "".join(msg)

def decrypt(msg,k):
    l=len(msg)
    l1=len(k)
    k=[ord(ch)-97 for ch in k]
    msg=list(msg)
    for _ in range(l):
        msg[_]=chr(((ord(msg[_]) - 97 - k[_ % l1]) % 26 ) + 97)
    return "".join(msg)

def getKeysFromCipher(cipherText, length):
        secretKeysRetrived = []
        Y_parts = []
        for i in range(length):
            part = cipherText[i::length]
            Y_parts.append(part)
            tempKey = getKeyFromCipher(english_probability, Y_parts[i], 26)
            secretKeysRetrived.append(chr(base + tempKey))
        secretKeysRetrived = "".join(secretKeysRetrived)
        return secretKeysRetrived
def cryptanalysis(cipherText):
    m = findLength(cipherText, 25)
    print("M := ", m)
    keysRetrived = getKeysFromCipher(cipherText, m)
    print("Keys : ", keysRetrived)
if __name__ == "__main__":
    msg,k=input().split()
    enc_msg=encrypt(msg,k)
    dec_msg=decrypt(enc_msg,k)
    cryptanalysis(enc_msg)