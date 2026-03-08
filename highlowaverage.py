#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

numFile = open("numbers.txt" , 'r')

numList = []

for curLine in numFile:
    print(int(curLine))
    numList.append(int(curLine))
totalNum = len(numList)
sumNumbers = sum(numList)
average = sumNumbers / totalNum
highestNum = max(numList)
lowestNum = min(numList)
    
numFile.close

print(f"The total amount of numbers is {totalNum}")
print(f"The sum of all the numbers is {sumNumbers}")
print(f"The average of all the numbers is {average}")
print(f"The highest number is {highestNum}")
print (f"The lowest number is {lowestNum}")



