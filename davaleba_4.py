# მაგალითი_1

class People:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        return f" {self.firstname}.{self.lastname}.school@edu.ge"


class Lecturer(People):

    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self):
        return f" ლექტორის მეილია: {self.firstname}.{self.lastname}@edu.ge \n ლექტორის ხელფასია: {self.salary} ლარი"


class Student(People):

    def __init__(self, firstname, lastname, courses):
        super().__init__(firstname, lastname)
        self.courses = courses

    def get_email(self):
        return f" მოსწავლის მეილია {self.firstname}.{self.lastname}.1@edu.ge \n მოსწავლის გაკვეთილების სიაა: {', '.join(self.courses)}"


people_1 = People("Data", "karchava")
print(people_1.get_email())
lecturer_1 = Lecturer("Data", "karchava", 2250)
print(lecturer_1.get_email())
student_1 = Student("data", "karchava", ["ქართული", "მათემატიკა", "ინგლისური", "ქიმია", "ფიზიკა"])
print(student_1.get_email())

# მაგალითი_2


class Library_item:

    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        if self.status == "available":
            return "თქვენ შეგიძლიათ დაჯავშნა"
        elif self.status == "occupied":
            return "თქვენ არ შეგიძლიათ დაჯავშნა"


class Book(Library_item):

    def __init__(self, isbn, authors, title, subject, status):
        super().__init__(title, subject, status)
        self.authors = authors
        self.isbn = isbn

    def booking(self):
        if self.status == "available":
            return "თქვენ შეგიძლიათ დაჯავშნა"
        elif self.status == "occupied":
            return "თქვენ არ შეგიძლიათ დაჯავშნა"


class Magazine(Library_item):

    def __init__(self, jour_name, volume, status, title=None, subject=None):
        Library_item.__init__(self, status, title, subject)
        self.jourName = jour_name
        self.volume = volume
        self.status = status

    def booking(self):
        if self.status == "available":
            return "თქვენ შეგიძლიათ დაჯავშნა"
        elif self.status == "occupied":
            return "თქვენ არ შეგიძლიათ დაჯავშნა"


class Cd(Library_item):

    def __init__(self, title, status, subject=None):
        Library_item.__init__(self, title, subject, status)

    def booking(self):
        return "თქვენ არ შეგიძლიათ Cd-ის დაჯავშნა"


book_1 = Library_item("titlr", "sublect", "available")
print(book_1.booking())
book_2 = Book("isbn", "autors", "f", "m", "available")
print(book_2.booking())
book_3 = Magazine("Avon", "volume", "occupied")
print(book_3.booking())
book_4 = Cd("title", "occupied")
print(book_4.booking())


# მაგალითი_3


class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"სახელი:{self.firstname}, გვარი:{self.lastname}, ასაკი:{self.age}"


class Employee:

    def __init__(self, profession, monthly_salary, working_hours):
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

    def hourly_salary(self):
        return f"საათობრივი ხელფასია დაალოებით:{self.monthly_salary / (self.working_hours * 30)} ლარი"


class Doctor(Person, Employee):
    def __init__(self, firstname, lastname, age, profession, monthly_salary, working_hours):
        super().__init__(firstname, lastname, age)
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

    def __str__(self):
        super().__str__()
        return f"სახელი:{self.firstname}, გვარი:{self.lastname}, ასაკი:{self.age}"

    def hourly_salary(self):
        super().hourly_salary()
        return f"საათობრივი ხელფასია დაალოებით:{self.monthly_salary / (self.working_hours * 30)} ლარი"

    def perform_operation(self):
        if self.age == 20:
            return f"{self.firstname}ს შეუძლია პირველი ოპერაცია ჩაატაროს მეთვალყურეობის ქვეშ"
        elif self.age >= 26:
            return f"{self.firstname}ს შეუძლია დამოუკიდებლადს ჩაატაროს ოპერაციები"
        else:
            return f"{self.firstname}ს ჯერ არ შეუძლია ოპერაციების ჩატარება. {self.firstname}ს შეუძლია მხოლოდ დაკვირვება და დახმარება"


doc_1 = Doctor("დავით", "ქარჩავა", 18, "კარდიო ქირურგი", 30000, 10)
print(doc_1)
print(doc_1.hourly_salary())
print(doc_1.perform_operation())
