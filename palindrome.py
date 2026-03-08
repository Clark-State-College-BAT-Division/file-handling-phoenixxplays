#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

count = 0

with open("words.txt") as wordFile:
    for curLine in wordFile:
        words = curLine.lower().split()
        for w in words:
            if w == w[::-1]:
                count += 1
                print(curLine)
                
print(f"There are " + str(count) + " palidromes in the list")
