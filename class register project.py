student_list = ["Harish", "Manikandan", "Arun", "Harishwar", "Divya", "Sruthi", "Maha", "Aathi","Narendhiran", "Jeni", "Renuga", "Mark Zekarbug", "Elon Musk", "Ratan Tata","Bill Gates"]

present_student = 0
absent_student = 0 
count = 0
print("\n .........Cyber Security 'A'..........")
print("\nTacking Attendance............")

while (count < len (student_list)):
    attendance = input(f"\n{student_list[count]} is P/A : ")

    if attendance.upper() == "P":
        present_student += 1
        count += 1
        
    elif attendance.upper() == "A":
        absent_student += 1
        count += 1
        
    else:
        print("\nYou entered an invalid input!\nPlease enter valid input (P/A).\n")
        continue

print("\n .............Today attendance summery............")
print("\nTotal strength:", len(student_list))
print("Total present:", present_student)
print("Total absent:", absent_student)
