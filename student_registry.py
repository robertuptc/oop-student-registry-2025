class Student():
    student_count = 0

    def __init__(self, _name, _grade='12th', _age=13):
        self._name = _name
        self._age = _age
        self._grade = _grade
        Student.student_count += 1
    
    @classmethod
    def get_student_count(cls):
        return cls.student_count

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3 and new_name.isalpha():
            self._name = new_name
        else:
            print("New name should only contain letters, no spaces, and must be at least 3 characters long")
    
    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 11 and new_age < 18:
            self._age = new_age
        else:
            print("Age must be an integer between 12 and 17")
    
    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        grade = new_grade[:len(new_grade) - 2]
        ending_th = new_grade[len(new_grade) - 2 : len(new_grade)]
        try:
            if int(grade) and int(grade) > 8 and int(grade) < 13:
                if ending_th == 'th':
                    self._grade = new_grade
            return self._grade
        except:
            print("Format should be Number + th. Sample: 9th or 10th")


# robert = Student('Robert', "4th", 34)
# print(robert.get_name)
# robert.set_name = 'Bob'
# print(robert.get_name)
# print(robert.get_age)
# robert.set_age = 15
# print(robert.get_age)
# print(robert.get_grade)
# robert.set_grade = '10th'
# print(robert.get_grade)