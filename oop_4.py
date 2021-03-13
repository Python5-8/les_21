class Human:
    def __init__(self, age, name, height):
        self.age = age
        self.name = name
        self.height = height
        print('I was born here! My name is', name)

    def say_hello_to(self, name_to):
        print('Hello', name_to)
    
    def tell_about_yourself(self):
        print('Hello, my name is', self.name)
        print('I am', self.age, 'y o')

    def happy_birthday(self):
        print('Today is my birthday!')
        self.age += 1
    
# print('ALEX')
Alex = Human(10, 'Alex', 130)
# Mike = Human(15, 'Mike', 160)
Alex.tell_about_yourself()
Alex.happy_birthday()
Alex.tell_about_yourself()

# Mike.tell_about_yourself()

# Alex.say_hello_to("Mike")
# Alex.tell_about_yourself()
# John = Human(10, 'John', 130)
# John.tell_about_yourself()

# Alex.say_hello_to('Sarah')
# print(Alex.age)
# Alex.happy_birthday()
# print(Alex.age)
# Alex.tell_about_yourself()

# print('ANDREW')
# Andrew = Human(15, 'Andrew', 170)
# Andrew.say_hello_to('Sarah')