def RomToInt(s):
    translation = {
        'I': 1,'V' : 5,'X' : 10,'L' : 50,'C' : 100,'D' : 500,'M' : 1000
    }
    
    Integer = 0
    n = len(s)
    i = 0
    while i < n:
        if i < n - 1 and translation[s[i]] < translation[s[i+1]]:
            Integer += translation[s[i+1]] - translation[s[i]]
            i += 2
        else:
            Integer += translation[s[i]]
            i +=1
    return Integer


s = input("Enter Roman : ")

print(RomToInt(s))


