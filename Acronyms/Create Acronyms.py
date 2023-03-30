phrase=input("Enter a phrase: ")
words= phrase.split()   #WE use split method to seperate each char in list
#print(words)           #['Data','Science']

res =""
for i in words:
    res+=i[0]
print(res)