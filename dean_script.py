import random

words = open('words.txt', 'r')
wordlist = [line.split(',') for line in words.readlines()]
#turning the words.txt file into a list
len = int(len(wordlist))
#finding the length of the list
num1 = random.randint(1,len)
num2 = random.randint(1,len)
num3 = random.randint(1,len)
num4 = random.randint(1,len)
num5 = random.randint(1,len)
num6 = random.randint(1,len)
num7 = random.randint(1,len)
num8 = random.randint(1,len)
num9 = random.randint(1,len)
num10 = random.randint(1,len)
word1 = wordlist[num1]
word2 = wordlist[num2]
word3 = wordlist[num3]
word4 = wordlist[num4]
word5 = wordlist[num5]
word6 = wordlist[num6]
word7 = wordlist[num7]
word8 = wordlist[num8]
word9 = wordlist[num9]
word10 = wordlist[num10]
# assigning variables. It's not good practice to dynamically assign varibles, but I may try dictionary key:value pairs in the future 
words = str(word1 + word2 + word3 + word4 + word5 + word6 + word7 + word8 + word9 + word10)

#parsing string
words = words.replace(',',' ')
words = words.replace('_',' ')
words = words.replace("'",'')
words = words.replace('[','')
words = words.replace(']','')
words = words.replace('\\n','')

print(words) 

