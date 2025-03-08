from Members import Member
class Teacher(Member):
    def __init__(self, name, family, age, proficiency,work_experience):
        super().__init__(name, family, age, proficiency)
        self.Work_experience=work_experience
         
        if self.Work_experience<4:
            raise ValueError("we need more experience")
    def languages(self):
        return "persion and english"

h=Teacher("fd","df",12,86,23)

print(h.languages())
