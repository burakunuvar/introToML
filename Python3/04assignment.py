names = (input('Enter names separated by comas: ')).split(',')
#print(names)
assignments = (input('Enter assignment counts separated by comas: ')).split(',')
#print(assignments)
grades = (input('Enter grades separated by comas: ')).split(',')
#print(grades)

for i in range(0,4):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(names[i],assignments[i],grades[i],int(grades[i])+int(assignments[i])*2 )
    print(message)
