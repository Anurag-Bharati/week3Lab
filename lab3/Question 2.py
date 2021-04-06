# WAP which accepts marks of four subject and displays total marks, percentage and grade.

lab3_Math = int(input("Enter your marks in maths: "))
lab3_English = int(input("Enter your marks in english: "))
lab3_Computer = int(input("Enter your marks in computer: "))
lab3_Physics = int(input("Enter your marks in physics: "))

lab3_totalMarks = lab3_Math + lab3_Computer + lab3_Physics + lab3_English

lab3_Marks_Percentage = lab3_totalMarks/4

lab3_Marks_Grade = ""

if 80 <= lab3_Marks_Percentage < 90:
    lab3_Marks_Grade = "A"
elif lab3_Marks_Percentage >= 90:
    lab3_Marks_Grade = "A+"
elif 70 <= lab3_Marks_Percentage < 80:
    lab3_Marks_Grade = "B+"
elif 60 <= lab3_Marks_Percentage < 70:
    lab3_Marks_Grade = "B"
elif 50 <= lab3_Marks_Percentage < 60:
    lab3_Marks_Grade = "C+"
elif 40 <= lab3_Marks_Percentage < 50:
    lab3_Marks_Grade = "C"
elif 30 <= lab3_Marks_Percentage < 40:
    lab3_Marks_Grade = "D+"
elif 20 <= lab3_Marks_Percentage < 30:
    lab3_Marks_Grade = "D"
elif 0 <= lab3_Marks_Percentage < 20:
    lab3_Marks_Grade = "E"

print(f"Your have secured {lab3_Marks_Percentage}, your total obtained marks is {lab3_totalMarks} and your grade is"
      f" {lab3_Marks_Grade} ")

