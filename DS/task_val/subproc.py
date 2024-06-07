# import subprocess


# p = subprocess.run('dir', capture_output=True, shell=True, text=True)
# print(p.stdout)


# x = divmod(5,2)
# print(x)


# import random

# val = ""
# for i in range(6):
#     val += str(random.randint(0,9))
# print(val)

# from datetime import datetime, timedelta

# now_time = datetime.now()
# after_15_days = now_time+timedelta(days=15)
# print(after_15_days)



# list = [1,2,3,4,5]
# a,b,c,*d= list
# print(a,b,c,d)

# def decor(fun):
#     def wrapper(name):
#         val = fun(name)
#         return "Hi, "+val
#     return wrapper

# @decor
# def hlo(name):
#     return f"My name is {name}"

# result = hlo("Akhil")
# print(result)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class Stack:
#     def __init__(self):
#         self.head = None

#     def push(self,data):
#         node = Node((data,0))
#         node.ref = self.head
#         self.head = node

#     def pop(self):
#         if self.head is None:
#             print("Empty stack")
#         else:
#             self.head = self.head.ref

#     def pri(self, data, pr):
#         node = Node((data,pr))
#         if self.head is None or pr > self.head.data[1]:
#             node.ref = self.head
#             self.head = node
#         else:
#             n = self.head
#             while n.ref is not None and pr < n.ref.data[1]:
#                 n = n.ref
#             node.ref = n.ref
#             n.ref = node


#     def display(self):
#         if self.head is None:
#             print("The value is empty")
#             return
#         n = self.head
#         while n is not None:
#             print(n.data)
#             n = n.ref

# s = Stack()
# s.push(10)
# s.push(20)
# s.display()
# print("#################################")
# s.pri(30,9)
# s.pri(40,2)
# s.pri(59,1)
# s.display()
# # s.pop()
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# s.display()



# a=b=10
# print(a)
# print(id(a),id(b))
# print(b)
# b=11
# print(id(a),id(b))
# print(b)
# print(a)

# def rec(val):
#     if val ==1:
#         return 1
#     else:
#         return val+rec(val)
    

# rec(2)

# list = [1,2,3,4,5,6,7,8,9]
# def search(list, val):
#     left = 0
#     right = len(list)-1
#     while left<right:
#         mid = (left+right)//2
#         if list[mid] == val:
#             print("The value is founded in the list")
#             return
#         elif list[mid]>val:
#             right = mid-1
#         else:
#             left = mid+1
#     print("The value is not founded in the list")


# search(list, 10)




# for i in range(len(list)-1):
#     for j in range(i,len(list)):
#         if list[i]>list[j]:
#             list[i], list[j] = list[j], list[i]
# print(list)


# for i in range(len(list)-1):
#     for j in range(len(list)-1):
#         if list[j]>list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]

# print(list)



# def sort(list, first, last):
#     pvot = list[first]
#     left = first+1
#     right = last

#     while True:
#         while left<=right and pvot >= list[left]:
#             left+=1
#         while left<=right and pvot <= list[right]:
#             right-=1
#         if left > right:
#             break
#         list[left], list[right] = list[right], list[left]
#     list[first], list[right] = list[right], list[first]
#     return right


# def quick(list, first, last):
#     if first<last:
#         p = sort(list, first, last)
#         quick(list, first, p-1)
#         quick(list, p+1, last)
            


# list = [3242,53,1,32,475,143,96,12412,7535,421,43245]
# first = 0
# last = len(list)-1
# quick(list, first, last)
# print(list)




# def mer(list):
#     if len(list)>1:
#         mid = len(list)//2
#         left_list = list[:mid]
#         right_list = list[mid:]
#         mer(left_list)
#         mer(right_list)

#         i = 0
#         j = 0
#         k = 0


#         while i<len(left_list) and j<len(right_list):
#             if left_list[i]<right_list[j]:
#                 list[k] = left_list[i]
#                 i += 1
#                 k += 1
#             else:
#                 list[k] = right_list[j]
#                 k += 1
#                 j += 1


       

#         while i < len(left_list):
#             list[k] = left_list[i]
#             i += 1
#             k += 1

#         while j < len(right_list):
#             list[k] = right_list[j]
#             k += 1
#             j += 1


# list = [234,5,32,457,34,35,57342,454,635,2547,35346,5743,64,32214]
# mer(list)
# print(list)




# def ins(list):
#     for i in range(1, len(list)):
#         current = list[i]
#         pos = i

#         while list[pos-1]>current and pos > 0:
#             list[pos] = list[pos-1]
#             pos -= 1

#         list[pos] = current

# list = [2423,52,53246,346,4536,532,5,5734,523,3532,5325,2367632476,12]
# ins(list)
# print(list)



# def ins(list):
#     for i in range(1, len(list)):
#         current = list[i]
#         pos = i

#         while list[pos-1] > current and pos>0:
#             list[pos] = list[pos-1]
#             pos -= 1

#         list[pos] = current


# list = [35346,2,5645475,4573,64,547,546743,23,54537,465,457,584]
# ins(list)
# print(list)


# list = [2,7,4,0,9,5,1,3]
# target = 12
# new_list = []

# i = 0
# j = 1
# k = 0
# m = 0
# while True:
#     if i > len(list)-1 or j > len(list)-1 or k > len(list)-1:
#         break
#     if m != i:
#         j = i+1
#     m = i
#     if list[j]+list[i] < 12:
#         v = list[j]+list[i]
#         if j != len(list)-1:
#             print(j)  
#             for k in range(j, len(list)):
#                 if v+list[k] == 12:
#                     if [list[i],list[j],list[k]] not in new_list:
#                         if i != j and i!= k and j!=k:
#                             new_list.append([list[i],list[j],list[k]])
#                             break
#                 if k == len(list)-1:
#                     j = j+1
#                     break                   
#     else:
#         j = j+1
#     if len(list)-1> i and j == len(list)-1:
#         i += 1
#     else:
#         j = j+1
#     if i == len(list)-1:
#         break
# print(new_list)




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref  = None

# class Stack:
#     def __init__(self):
#         self.head = None

#     def push(self, data):
#         node = Node((data,0))
#         node.ref = self.head
#         self.head = node

#     def pop(self):
#         if self.head is None:
#             print("The linked list empty")
#         else:
#             self.head  = self.head.ref


#     def pri(self, data, val):
#         if self.head.data[1] < val:
#             node = Node((data, val))
#             node.ref = self.head
#             self.head = node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 if n.ref.data[1]>val:
#                     n = n.ref
#                 else:
#                     break
#             node = Node((data, val))
#             node.ref = n.ref
#             n.ref = node

#     def display(self):
#         if self.head is None :
#             print("Empty linked list")
#         else:
#             n = self.head 
#             while n is not None:
#                 print(n.data)
#                 n = n.ref



# s = Stack()
# s.push(10)
# s.push(30)
# s.display()
# print("#########################################")
# s.pri(49,3)
# s.pri(67,1)
# s.display()
# print("#########################################")
# s.pop()
# print("##########################################")
# s.display()




