__author__ = 'becca.elenzil'

class Person():
    def __init__(self,name):
        """take name, birth month (#), birthday (#), and age"""
        self.name = name

        #self.birthMonth = birthMonth
        #self.birthDay = birthDay

    def __repr__(self):
        s = "My name is "+str(self.name)+"."
        return s

    def iLike(self):
        return "I like going for walks"

    def pigLatin(self):
        name = self.name
        word_length = len(name)

        first_letter = name[0]
        vowels = ['A','E','I','O','U','a','e','i','o','u']

        if first_letter in vowels:
            newName = name + 'yay'
        else:
            newName = name[1:word_length] + name[0] + 'ay'
        print "Hi, I'm %s " % (newName)
    """
    def seasonOfBirth(self):
        month = self.birthMonth
        return "spring"

    def yearBorn(self):
        year = 1999
        return year
    """

class Student(Person):
    def __init__(self,name):
        # Call the parent/super class constructor first
        Person.__init__(self,name)
        # Now set up our variables
        self.grade = ""
        self.name = name

    def __repr__(self):
        s = "My name is "+str(self.name)+". I am in "+str(self.grade)+" grade."
        return s

    def iLike(self):
        print "I like hanging out with friends"

class Teacher(Person):
    def __init__(self,name):
        Person.__init__(self,name)
        self.subject = ""
    def __repr__(self):
        s = "My name is " +str(self.name)+". I teach "+str(self.subject)+"."
        return s
    def iLike(self):
        print "I like working with students"


john_smith = Person("John")
john_smith.name = "John"
print john_smith
john_smith.pigLatin()

jane_student = Student("Jane")

jane_student.grade = "9th"
print jane_student
jane_student.pigLatin()
jane_student.iLike()

"""
becca_teacher = Teacher("Becca",5,25,31)
becca_teacher.subject = "computer science"
print becca_teacher
becca_teacher.pigLatin()
becca_teacher.iLike()
"""