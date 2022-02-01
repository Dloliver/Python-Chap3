# #OOP
# class Player Character:
#     membership = True
#     def __init__(self, name, age):
#         self.name = name #attributes
#         self.age = age
#
#     def shout(self):
#
#     @classmethod
#     def adding_things(num1, num2):
#         return cls('Teddy', num1 + num2)
#
#     @staticmethod
#     def adding_things2(num1, num2):
#         return num1 + num2
# #player1 = PlayerCharacter('Tom', 20)
#
# #using a class method or static method you can call upon that method without defining an instance afterwards.
# player3 = PlayerCharacter.adding_things(2,3)
#
# print(player3.age)

#Encapsulation - binding of data and functions ht manipulate data into an object that users coder or machines can interact with. Helps from having to keep writing a code over and over.

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('Dennis', 32)
player1.speak()
