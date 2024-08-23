#Module 2 Lesson 3: Assignments | Python Lists
#1. Python List Transformation
#Problem Statement: You've been given a list of grades from an exam. You need to process and analyze these grades.

##Task 1: Given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sortedGrades = x = sorted(grades)
print(sortedGrades)
#Task 2: Calculate the average grade and print it.
# Python program to get average of a list 
def Average(grades): 
    return sum(grades) / len(grades) 

average = Average(grades) 
print(average)

#Printing average of the list 
print("Average of the list =", round(average, 2)) 
#Sort the grades in descending order and print the sorted list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(sortedGrades)
#2.Advanced List Methods and Identity Operators
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
#3. Advanced Slicing Techniques
if "Alice" in submitted:
    print("Go Allice")
#Find out if Alice submitted their assignment and attended class.
if "Alice" in submitted:
    print("Go to class, Allice")
#HINT: How might the in keyword be of use here? And how can you check to

#see if Alice is in both submitted and attended in one if statement?
#3. Advanced Slicing Techniques
#Problem Statement: You have a list of daily temperatures for one month, and you'd like to extract specific data from it]
a = grades.extract()
print(sortedGrades)
#Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
                 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
#Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). Expected Outcome:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
expract2 = grades.extract([6,13])
