def link(n):
        if n <= 5: 
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\5.txt"
        if n == 6:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\6.txt"
        if n == 7:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\7.txt"
        if n == 8:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\8.txt"
        if n == 9:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\9.txt"
        if n == 10:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\10.txt"
        if n == 11:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\11.txt"
        if n == 12:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\12.txt"
        if n == 13:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\13.txt"
        if n == 14:
            return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\14.txt"
        return r"C:\Users\danie\OneDrive\Escritorio\Python\Projectos\Lingo\Texti\15.txt"
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