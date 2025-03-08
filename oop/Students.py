from Members import Member
class Student(Member):
    def __init__(self, name, family, age, proficiency,seat_number):
        super().__init__(name, family, age, proficiency)
        self.number_of_attendees=0
        
        if seat_number>20:
            raise ValueError("your seat number is wrong")
        self.seat_number=seat_number

    def isfail(self):
        if self.number_of_attendees<15:
            print("fail!!")
        else:
            return f"number of attends :{self.number_of_attendees}"
        
    def languages(self):
        return "persion"

h=Student("fd","df",12,86,23)
print(h.Age)
print(h._Name)
print(h.languages())

h.number_of_attendees=16


print(h.seat_number)

    

    

