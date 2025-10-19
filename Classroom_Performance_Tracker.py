class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        avg = sum(self.marks) / len(self.marks)
        return (self.name, avg)

    @staticmethod
    def topper(students):
        averages = {name: sum(marks)/len(marks) for name, marks in students.items()}
        top_student = max(averages, key=averages.get)
        print(f'Top Performer: "{top_student}" ')

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
newstu={}
for name, marks in students.items():
    obj = Student(name, marks)
    name, avg = obj.average_marks()
    if avg.is_integer():
        newstu[name] = int(avg)
    else:
        newstu[name] = round(avg, 2)

print("Average Marks:", newstu)
Student.topper(students)
