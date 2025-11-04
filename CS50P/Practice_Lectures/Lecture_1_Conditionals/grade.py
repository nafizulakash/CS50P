                   #======== USE OF AND ========


score = int(input("Score: "))

"""

if score >= 90:
    print ("Grade A")

elif 80 <= score < 90:
    print("Grade B")

elif 70 <= score < 80:
    print("Grade C")

elif 60 <= score < 70:
    print("Grade D")

else:
    print("Grade F")

"""

# We can more optimize it
# We can use only lowerbound since the conditions are checkd in order
# But if the conditions are not mutually exclusive that approach will fail

if score > 90:
    print ("Grade A")

elif score > 80:
    print("Grade B")

elif score > 70:
    print("Grade C")

elif score > 60:
    print("Grade D")

else:
    print("Grade F")