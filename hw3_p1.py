n = int(input("Enter the total number of students: "))

# create a list of student IDs from 1 to n
students = list(range(1, n + 1))

# start the counting from student ID 1
count = 1

# loop until there is only one student left
while len(students) > 1:
    # get the index of the student who reports the next number
    index = (count - 1) % len(students)
    
    # report the number
    print(students[index])
    
    # if the number reported is 3, remove the student from the list
    if students[index] == 3:
        students.pop(index)
        # adjust the index to account for the removed student
        index -= 1
    
    # move to the next student in the list
    count += 1

# the last student remaining on the table is the winner
if len(students) == 1:
    print("The last student seating on the round table is student ID", students[0])
else:
    print("There are no students on the round table.")
