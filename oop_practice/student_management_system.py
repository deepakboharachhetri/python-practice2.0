# Student Management System
class Student:
    SCHOOL_NAME="Raymers Presidental High Secondary School"
    def __init__(self,name, roll_no, marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks # dictionary
        self._full_marks=100
        self._pass_marks=32

    def calculate_fee(self):
        pass


    def check_fail_sub(self):
        fail_subject={}
        for key,score in self.marks.items():
            if self.score < self._pass_marks:
                fail_subject["key"]=score
        return fail_subject

    def calculate_percent(self):
        fail_count= len(self.check_fail_sub())
        if fail_count >0:
            return -1
        total=0
        for key,score in self.marks.items():
            total+=score

        return round(total/(self._full_marks* len(self.marks))*100,2)

    def __str__(self):
        print(f"Student:{self.name}, Grade:{self.grade_level}, Roll No:{self.roll_no}")

    def __repr__(self):
        print(f"Student object {self}")

class RegularStudent(Student):
    def __init__(self,name,roll_no,marks):
        super().__init__(name,roll_no,marks)
        self._base_amount=0

    def calculate_fee(self):
        return self._base_amount

class ScholarshipStudent(Student):
    def __init__(self, name, roll_no,marks, scholarship_percent):
        super().__init__(name, roll_no, marks)
        self._base_amount = 1000
        self._scholarship_percent=scholarship_percent

    def calculate_fee(self):
        return int(self._base_amount-(self._scholarship_percent * self._base_amount/100))

    def __repr__(self):
        print(f"Scholarship Student:{self}")


class InternationalStudent(Student):
    def __init__(self, name,  roll_no, marks):
        super().__init__(name,  roll_no, marks)
        self._base_tution = 1000
        self._international_extra=1000

    def calculate_fee(self):
        return self._base_tution+self._international_extra
    def __repr__(self):
        print(f"International Student:{self}")



class Grade:
    def __init__(self,grade):
        self.grade=grade
        self.student ={}   #  dict key registration_number : student object

    def add_student(self,registration_number,student):
        self.student[registration_number]=student

    def delete_student(self, registration_number):
        self.student.pop(registration_number)

    def total_class_student(self):
        return len(self.student)

    def total_class_revenue(self):
        total=0
        for registration_number,student in self.student.items():
            total+=student.calculate_fee()

        return total

    def __add__(self,other):
        return (self.total_class_student()+other.total_class_student(),self.total_class_revenue()+other.total_class_revenue())


if __name__=="__main__":
    rstudentpass1=RegularStudent(name="deepak1",roll_no="021-341",marks={"english":50,"math":70,"Nepali":60})
    rstudentfail=RegularStudent(name="deepak2",roll_no="021-342",marks={"english":20,"math":70,"Nepali":60})
    rstudentpass2=RegularStudent(name="deepak3",roll_no="021-343",marks={"english":100,"math":100,"Nepali":100})
    sstudentpass2=ScholarshipStudent(name="deepak4",roll_no="021-344",marks={"english":100,"math":100,"Nepali":100},scholarship_percent=10)
    istudentpass2=InternationalStudent(name="deepak5",roll_no="021-345",marks={"english":100,"math":100,"Nepali":100})
    grade_10=Grade(10)
    grade_10.add_student(1,rstudentpass1)
    grade_10.add_student(2,rstudentfail)
    grade_10.add_student(3,rstudentpass2)
    grade_10.add_student(4,sstudentpass2)
    grade_10.add_student(5,istudentpass2)

    grade_11=Grade(11)
    grade_11.add_student(1,rstudentpass1)
    grade_11.add_student(2,rstudentpass2)




    print("Total Student in Grade 10",grade_10.total_class_student())
    print("Total Revenue in Grade 10",grade_10.total_class_revenue())
    print("Total Student in Grade 10",grade_11.total_class_student())
    print("Total Revenue in Grade 10",grade_11.total_class_revenue())

    print("Total Revenue in Grade 10","Total Student in Grade 10 and Grade11",grade_11+grade_10)
