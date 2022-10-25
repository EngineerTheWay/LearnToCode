# Playing around with lists. Adding and removing to lists, combined lists, and how to access certain items from a combined list.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#Lists the subjects in this semester's gradebook
subjects = ["physics", "calculus", "poetry", "history"]

#Lists grades for the subjects above
grades = [98, 97, 85, 88]

#Combined list from semester grades and subjects
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

#Add Computer Science
gradebook.append(["computer science", 100])

#Add Visual Arts
gradebook.append(["visual arts", 93])

#Modify VA grade
gradebook[-1][-1] = 98

#Change Poetry to pass fail
gradebook[2].remove(85)
gradebook[2].append("Pass")

#Progress Check
print(gradebook)

#add semesters together
full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)