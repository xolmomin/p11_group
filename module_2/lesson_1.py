'''
OOP concepts
1) inheritance
    - Single inheritance (oddiy)
    - Multiple inheritances
    - Multilevel inheritance
    - Hierarchical inheritance
    - Hybrid inheritance
2) polymorphism
    - overloading
    - overriding

3) encapsulation

4) abstraction
5) object
6) class


'''


# polymorphism
# - overloading ❌
# def add(a, b):
#     return a + b
#
# def pprint(a, b, c, g):
#     return a + b
#
# from pprint import pprint
#
#
# pprint(locals())
#
# def add(a, b, c=5):
#     return a - b
#
#
# print(add(6, 4))
#
# a = 5
# a = 'hello'
# print(a)

# - overriding ✅
#
# class A:
#     def show_print(self):
#         print('A class')
#
#
# class B(A):
#     def show(self):
#         print('B class')
#         # super().show()
#
#     def add(self, a, b):
#         return a + b
#
#     def sub(self, a, b):
#         return a - b
#
#
# class C(B):
#
#     def show(self):
#         super().show()
#
#     def add(self, a, b):
#         return super().add(a, b)
#
#     def sub(self, a, b):
#         return super().sub(a, b)
# def show(self):
#     super().show()

# def show(self):
#     print('C class')
# super().show()
# c = C()
# c.show()


# - Single inheritance(oddiy)
#
# class People:
#     def speak(self):
#         print('Hello')
#
#
# class Student(People):
#     pass
#
#
# student = Student()
# student.speak()


# - Multiple inheritances
# class Staff:
#     def work(self):
#         print('Ishlash')
#
#
# class Teacher:
#     def teach(self):
#         print('Dars berish')
#
#
# class Mentor(Staff, Teacher):
#     pass
#
#
# mentor = Mentor()


# # - Multilevel inheritance
#
# class A:
#     def show_a(self):
#         print('A class')
#
# class B(A):
#     def show_b(self):
#         print('B class')
#
# class C(B):
#     def show_c(self):
#         print('C class')
#
# c = C()
# c.show_a()
# c.show_b()


# inheritance

# - Hierarchical inheritance
# class A:
#     def print_a(self):
#         pass
#
# class B:
#     def print_b(self):
#         pass
#
# class C:
#     def print_c(self):
#         pass
#
# class D(A, B, C):
#     pass
#
# d = D()
# d.print_c()
#
# list()
#
# int()


# - Hybrid inheritance

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C:
#     pass
#
# class D(B, C):
#     pass
#


# # dunder method bosh va oxirida __
#
# class Student:
#     def __init__(self, name, age, address, university, course):  # constructor
#         self.name = name
#         self.age = int(age)
#         self.address = address
#         self.university = university
#         self.course = int(course)
#
#     def __str__(self) -> str:
#         return f'{self.name} {self.age} {self.address} {self.university} {self.course}'
#
#
# #
# # student1 = Student('Botirjon', 2000)
# # student2 = Student('Uktamjon', 1994)
# # student3 = Student('Alijon', 2008)
# #
# # snakecase
# # ozgaruvchining_ismi =  2
#
#
# # CamelCase
# # StudentCourse
#
#
# students = []
# for i in range(2):
#     data = input().split(', ')
#     student = Student(*data)
#     students.append(student)
#
# for student in students:
#     print(student)
#
# '''
# name, age, address, university, course
# botirjon, 22, Toshkent, Toshmi, 4
# nematjon, 14, Samarqand, Toshmi, 2
#
# '''
#
# #
# # class Hayvon:
# #     pass
# #
# # class Ayiq(Hayvon):
# #     pass
# #
# # class Sher(Hayvon):
# #     pass


# drive
# Car, Tesla, Audi
#
#
#
# class Car:
#     def drive(self):
#         print('driving')
#
#
# class Tesla(Car):
#
#     def drive(self):
#         print('tezroq')
#         super().drive()
#
#
# class Audi(Car):
#     pass
#
#
# tesla = Tesla()
# tesla.drive()
#
# 'hello world' 1, 5, 2
# s.to_any(tuple) [tuple, list, set, str]
# String - reverse, slicing(start, stop), to_list, count_vowels
# MasterString - slicing(start, stop, step), to_any(type)


# class String:
#
#     def __init__(self, value: str) -> None:
#         self.value = value
#
#     def reverse(self) ->  str:
#         return self.value[::-1]
#
#     def slicing(self, start: int, stop: int) -> str:
#         return self.value[start:stop + 1]
#
#     def to_list(self) -> list:
#         return list(self.value)
#
#     def count_vowels(self) -> int:
#         return sum(i in 'aioue' for i in self.value)
#
#         # return sum(1 for i in self.value if i in 'aioue')
#
#         # vowels = 'aioue'
#         # count = 0
#         # for i in self.value:
#         #     if i in vowels:
#         #         count += 1
#         # return count
#
# class MasterString(String):
#
#     def to_any(self, _type):
#         return tuple(self.value)
#
#
#
# m_str = MasterString('hello world')
# m_str.to_any(tuple)

#
# def add(a, b):
#     return a + b


# salom = add
#
#
# salom(2, 3)
# Integer

# s = 'hello world'
# slicing(2, 5)


# class Integer:
#     def __init__(self, value):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def decrement(self):
#         self.value -= 1
#
#     def doubled(self):
#         self.value *= 2
#
#     def divided(self, n):
#         self.value /= n
#
#     def multiplication(self, n):
#         self.value *= n
#
#     def __str__(self) -> str:
#         return str(self.value)
#
#
# a = Integer(15)
# print(a)
# a.increment()
# a.increment()
# print(a)
# a.doubled()
# print(a)
# a.multiplication(2)
# print(a)
