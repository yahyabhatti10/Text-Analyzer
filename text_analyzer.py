#------------------------------------------------ L I B R A R Y   S E C T I O N ------------------------------------------------

from prettytable import PrettyTable 
import re
import operator

#--------------------------------------- U S E R  -  D E F I N E D   F U N C T I O N S -----------------------------------------

def removeSpecialCharacters(word):
    pattern = r'[^a-zA-Z]' # Regex for Special Characters
    result = re.sub(pattern, '', word) # Substitute all Special Characters with the empty string
    return result

def getSentence(text):
    pattern = r'[^.?!]+[.?!]'
    sentences = re.findall(pattern, text)
    return len(sentences)

#-------------------------------------------------- I N P U T   S E C T I O N -------------------------------------------------

# Input for file
fileName = input("\nEnter the File Name : ") 

# Exception Handling if file is not found
try:
    file = open(fileName,'r')
except FileNotFoundError:
    print(fileName + " not found.")
    exit()

n = int(input("Enter the N-Value for Most Frequent Words : ")) 

#------------------------------------------------ P R O C E S S   S E C T I O N ------------------------------------------------

# Variavles and Dictionary for storing words along with their Frequency, word counts, sentences. 
wordFreqCounter = dict()
totalWords = 0
totalSentences = 0


# Fetching words from lines in file and storing them in Dixtionary
for line in file:
    totalSentences += getSentence(line)
    line = line.split() 
    for word in line:
        word = word.lower()
        word = removeSpecialCharacters(word) # Removing Special Characters
        totalWords += 1
        if word in wordFreqCounter:
            wordFreqCounter[word] += 1
        else:
            wordFreqCounter[word] = 1


wordFreqCounter = dict(sorted(wordFreqCounter.items(),key=operator.itemgetter(1), reverse=True))

#  Creating table for displaying the Words and their Frequency in Table Format 
table = PrettyTable()
table.field_names = ["Words","Frequency"]

for words,freq in wordFreqCounter.items():
    n=n-1
    if(n<0):
        break
    table.add_row([words,freq])

#------------------------------------------------ O U T P U T   S E C T I O N ------------------------------------------------

print("Total Words : " + str(totalWords))
print("Total Sentences : " + str(totalSentences))
print(table)