                               #============LIST=================#

"""
students = ["Herminie", "Harry", "Ron"]
"""

"""
print(students)
"""

#How to print any specific item/ index of a list
"""
print(students[0])
print(students[1])
print(students[2])

"""


# Same using list 
"""


for students in students:
    print(students)

"""
# Using "Len"
# "len " will take the length of the list and iterate in index

"""

for i in range (len(students)):
    print(i + 1, students[i])


"""

                        #===== Dictonary ===========

"""

students = {
    "Nafiz" : "Manikganj",
    "Saif" : "Chuadanga",
    "Saad" : "Dinajpur",
    "Rafat" : "Naogaon"
}
"""


"""
print(students["Nafiz"])
print(students["Saif"])
print(students["Saad"])
print(students["Rafat"])

"""

# Using for loop
# For loop on a Dictionary
#By default python will iterate over keys not values

"""
for student in students:
    print(student)

"""

# to print values inside dictionary
"""
for student in students:
    print(student, students[student], sep = ", ")

"""

# Combining list and dictionary for more information

students = [
    {"name" : "Nafiz", "from" : "Manikganj", "age" : "25"},
    {"name" : "Saif", "from" : "Chuadanga", "age" : "26"},
    {"name" : "Saad", "from" : "Dinajpor", "age" : "27"},
    {"name" : "Rafat", "from" : "Naogaown", "age" : "25"},
]

for student in students:
    print(student["name"], student["from"], student["age"], sep = ", ")