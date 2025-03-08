class Member():
    def __init__(self, name, family, age,proficiency):
        self._Name = name
        self.Family = family
        self.Age = age
        self._Subject=None
        self._Nationality = None
        self.Proficiency=proficiency

    def reading_writing(self):
        return True

    def solvine_problem(self):
        return True
    
    def proficiency_in_english(self):
        if 0<self.Proficiency<30:
            print("You need an English proficiency of over 30%")
        elif 30<=self.Proficiency<=100:
            print("you can use this course easily")
        else:
            raise NotImplementedError("Subclass must implement method")
        
    def english_status(self):
        print(self.proficiency_in_english())

    @property
    def subject(self):
        return self._Subject
    @subject.setter
    def subject(self,item):
        courses=["computer sience","python","JS"]
        if item in courses:
            self._Subject=item
        else:
            raise ValueError("This course is unavailable for you")
        
    @property
    def nationality(self):
        return self._Nationality

    @nationality.setter
    def nationality(self, value):
        if value == "iranian":
            self._Nationality = value
        else:
            raise ValueError("This course is unavailable for you")
    
    @classmethod
    def languages(self):
        pass



