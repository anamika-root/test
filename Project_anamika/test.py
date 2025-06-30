# print("hello world.....")

class SchoolData:
    def __init__(self,school_name,school_address,school_id,principle_name,techer_name,total_techer,student_name,total_student,total_class,total_room,total_everyworkplace):
        self.school_name = school_name
        self.school_address = school_address
        self.school_id = school_id
        self.principle_name = principle_name
        self.techer_name = techer_name
        self.total_techer = total_techer
        self.student_name = student_name
        self.total_student = total_student
        self.total_class = total_class
        self.total_room = total_room
        self.total_everyworkplace = total_everyworkplace

    def fun(self):
        print(f"School Name is = {self.school_name},\nSchool Address is = {self.school_address},\nSchool Id is = {self.school_id},\nSchool Principle Name is = {self.principle_name},\nSchool Techer Name is = {self.techer_name},\nSchool Tptal Techer = {self.total_techer},\nShool Student Name = {self.student_name},\nTotal Student is = {self.total_student},\nTotal Class room = {self.total_class},\nSchool Total Room = {self.total_room},\nSchool Total Every_Work_Space = {self.total_everyworkplace},\n")

obj = SchoolData("Santhome.Her.Sec.School Maihar","Valabh_Nagar",3,"Tom","Tarana",37,"Ana",2600,15,35,5)
print(obj.fun())

class StudentData:
    def __init__(self,student_name,student_age,student_id,student_class,student_subject,student_address):
        self.student_name = student_name
        self.student_age = student_age
        self.student_id = student_id
        self.student_class = student_class
        self.student_subject = student_subject
        self.student_address = student_address

    def __str__(self):
        print(f"Student Name is = {self.student_name } , \nStudent age is = {self.student_age} , \nStudent Id is = {self.student_id} , \nStudent Class is =  {self.student_class} , \nStudent Subject is = {self.student_subject} , \nStudent Address is = {self.student_address} , \n")    

obj1 = ("Shiv",100,1,12,"math","Indore")
print(obj1)




