# #TASK 1
# def palindrome(text):
#     if text == text[::-1]:
#         print("This word is a palindrome")
#     else:
#         print("This word isn't a palondrime")
#
#
# text = input("შეიყვანეთ ტექსტი: ")
# palindrome(text)

# #TASK 2
# def xurda(amount):
#     sia = [1, 5, 10, 20, 50]
#     monetebi = 0
#     while amount > 0:
#         while amount >= sia[-1]:
#             monetebi += 1
#             amount -= sia[-1]
#         sia.pop(-1)
#
#     return monetebi
#
# amount = int(input())
# xurda(amount)

# #TASK 3
# def min(sia):
#     smallest = 1
#     while smallest in sia:
#         smallest += 1
#     return smallest
#
#
# lst = [12, 4, 6, 1, 2, 5]
# min(lst)

# #TASK 4
# def counter(text):
#     open = '('
#     close = ')'
#     stack = []
#
#     if len(text) % 2 == 1:
#         return False
#     for i in range(len(text)):
#         if text[i] == open:
#             stack.append(open)
#         elif text[i] == close:
#             if len(stack) == 0:
#                 return False
#             stack.pop()
#     return len(stack) == 0

# # TASK 5
# def stairCount(number):
#     array = [1, 1]
#     for i in range(2, number):
#         array.insert(i, array[i-1] + array[i-2])
#     return array[number]

# #TASK 6
# class DataStructure(object):
#     def __init__(self):
#         self.present = {}
#         self.elements = []
#     def remove(self, val):
#         if val not in self.present or self.elements[val] == 0:
#             return False
#         self.present[val] = 0
#         index = self.elements.index(val)
#         if index != len(self.elements) - 1:
#             temp = self.elements[-1]
#             self.elements[-1] = val
#             self.elements[index] = temp
#         self.elements.pop()
#         return True
# ob = DataStructure()
# ob.remove()