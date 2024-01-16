def link(n):
        if n <= 5: 
            return r"5.txt"
        if n == 6:
            return r"6.txt"
        if n == 7:
            return r"7.txt"
        if n == 8:
            return r"8.txt"
        if n == 9:
            return r"9.txt"
        if n == 10:
            return r"10.txt"
        if n == 11:
            return r"11.txt"
        if n == 12:
            return r"12.txt"
        if n == 13:
            return r"13.txt"
        if n == 14:
            return r"14.txt"
        return r"15.txt"
def isAnagram(word, c):
    for letter in word:
        if word.count(letter) != c.count(letter):
            return False
    return True
def Permutations(c):
    f = open(link(len(c)), "r")
    array = f.readlines()
    f.close()
    ans = []
    for word in array:
        if isAnagram(word[:len(word)-1], c) == True:
            ans.append(word)
    return ans
