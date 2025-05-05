dict = {'Alice':45, 'John':60, 'Bob':85, 'Riya':76}

k = input("Enter the student's name: ")

if k in dict.keys():
    print(f"{k}'s marks: {dict[k]}")
else:
    print("Student not found.")
    