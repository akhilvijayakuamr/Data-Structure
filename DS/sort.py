

# # Selection sort



# # list = [7, 4, 3, 5, 6, 2, 1, 7, 8]
# # print(list)
# # for i in range(len(list)):
# #     minval = min(list[i:])
# #     index = list.index(minval)
# #     if list[i] != list[index]:
# #         list[i], list[index] = list[index], list[i]

# # print("<--------------------------------------------->")
# # print(list)



# # list1 = [9,5,3,0,8,7,5,3,1,6,4]
# # print(list1)
# # for i in range(len(list1)-1):
# #     for j in range(i+1, len(list1)):
# #         if list1[j]<list1[i]:
# #             list1[i], list1[j] = list1[j], list1[i]

# # print("<-------------------------------------->")
# # print(list1)



# # list1 = [9,5,3,0,8,7,5,3,1,6,4]
# # print(list1)

# # # for i  in range(len(list1)-1):
# # #     for j in range(len(list1)-1):
# # #         if list1[j]>list1[j+1]:
# # #             list1[j], list1[j+1] = list1[j+1], list1[j]


# # for i in range(len(list1)-1):
# #     for j in range(len(list1)-1):
# #         if list1[j]<list1[j+1]:
# #             list1[j], list1[j+1] = list1[j+1], list1[j]

# # print("<--------------------------------------------->")
# # print(list1)



# # def sort(list, first, last):
# #     pvot = list[last]
# #     left = first
# #     right = last+1
# #     while True:
# #         while left <= right and list[left] <= pvot:
# #             left = left+1
        
# #         while left <= right and list[right] >= pvot:
# #             right = right-1

# #         if right<left:
# #             break
# #         else:
# #             list[left], list[right] = list[right], list[left]
# #     list[last], list[right] = list[right], list[last]
# #     return right

# # def quick(list, first, last):
# #     if first<last:
# #         p = sort(list, first, last)
# #         print(p)
# #         quick(list, first, p-1)
# #         quick(list, p+1, last)



# # list = [2,1,4,3,7,54,62,2,5,6,78,564,332]
# # first = 0
# # last = len(list)-1
# # quick(list, first, last)
# # print(list)



# # def sort(list, first, last):
# #     pvot = list[first]
# #     left = first+1
# #     right = last
# #     while True:
# #         while left <= right and list[left] <= pvot:
# #             left = left+1
# #         while left <= right and list[right] >= pvot:
# #             right = right+1

# #         if left>right:
# #             break
# #         else:
# #             list[left], list[right] = list[right], list[left]
# #     list[first], list[left] = list[left], list[first]



# # def quick(list, first, last):
# #     if first<last:
# #         p = sort(list, first, last)
# #         quick(list, first, p-1)
# #         quick(list, p+1, last)


# # list = [2,1,4,3,7,54,62,2,5]
# # first = 0
# # last = len(list)-1
# # quick(list, first, last)
# # print(list)


# # def get_hash(key):
# #     list = []
# #     for i in key:
# #         list.append(ord(i))
# #     return list


# # print(get_hash('poda myre poyi irunne padi'))

# # hai=[112, 111, 100, 97, 32, 109, 121, 114, 101, 32, 112, 111, 121, 105, 32, 105, 114, 117, 110, 110, 101, 32, 112, 97, 100, 105]
# # for i in hai:
# #     print(chr(i), end='')





# # def sort(list, first, last):
# #     pvot = list[last]
# #     left = first
# #     right = last - 1
# #     while True:
# #         while left<=right and list[left]<=pvot :
# #             left = left+1
# #             print(list)

# #         while left<=right and list[right]>=pvot:
# #             right = right-1
# #             print(list)
# #         if right<left:
# #             break
# #         list[left], list[right] = list[right], list[left]
# #     list[last], list[left] = list[left], list[last]
# #     print(list)
# #     return left


# # def quick(list, first, last):
# #     if first<last:
# #         p = sort(list, first, last)
# #         print(list[p])
# #         quick(list, first, p-1)
# #         quick(list, p+1, last)



# # list = [1,43,5,2]
# # first = 0
# # last = len(list)-1
# # quick(list, first, last)
# # print(list)





# # def sort(list, first, last):
# #     pvot = list[first]
# #     left  = first+1
# #     right = last

# #     while True:
# #         while left<=right and list[left]>=pvot:
# #             left = left+1
# #         while left<=right and list[right]<=pvot:
# #             right = right-1

# #         if right<left:
# #             break
# #         list[left], list[right] = list[right], list[left]
# #     list[first], list[right] = list[right], list[first]
# #     return right


# # def quick(list, first, last):
# #     if first < last:
# #         p = sort(list, first, last)
# #         quick(list, first, p-1)
# #         quick(list, p+1, last)


# # list = [1,53,2,3,56,211,4,6,7]
# # first = 0
# # last = len(list)-1
# # quick(list, first, last)
# # print(list)
# # # 
# # n = 2
# # def rec(n):
# #     if n <= 0 :
# #         return n
# #     n = n/2
# #     return rec(n)
# # va = True if n == 0 else False
# # print(va)




# # def m(list):
# #     if len(list)>1:
# #         mid = len(list)//2
# #         left_list = list[:mid]
# #         right_list = list[mid:]
# #         m(left_list)
# #         m(right_list)
# #         k = 0
# #         i = 0
# #         j = 0
# #         while i<len(left_list) and j<len(right_list):
# #             if left_list[i]<right_list[j]:
# #                 list[k]=left_list[i]
# #                 k = k+1
# #                 i = i+1
# #             else:
# #                 list[k] = right_list[j]
# #                 k = k+1
# #                 j = i+1

# #         while i<len(left_list):
# #             list[k] = left_list[i]
# #             k = k+1
# #             i = i+1

# #         while j<len(right_list):
# #             list[k] = right_list[j]
# #             k = k+1
# #             j = j+1




# # num = int(input("Enter the limit of the list"))
# # list = [int(input()) for i in range(num)]
# # m(list)
# # print(list)


# # def mer(list):
# #     if len(list)>1:
# #         mid = len(list)//2
# #         left_list = list[:mid]
# #         right_list = list[mid:]
# #         mer(left_list)
# #         mer(right_list)
# #         k = 0
# #         i = 0
# #         j = 0

# #         while i<len(left_list) and j<len(right_list):
# #             if left_list[i]<right_list[j]:
# #                 list[k] = right_list[j]
# #                 k = k+1
# #                 j = j+1
# #             else:
# #                 list[k] = left_list[i]
# #                 k = k+1
# #                 i = i+1


# #         while i < len(left_list):
# #             list[k] = left_list[i]
# #             k = k+1
# #             i = i+1


# #         while j < len(right_list):
# #             list[k] = right_list[j]
# #             j = j+1
# #             k = k+1




# # list=[7,3,9,2,8,1,0,1]
# # mer(list)
# # print(list)



# # for i in range(len(list1)-1):
# #     for j in range(i+1, len(list1)):
# #         if list1[i]>list1[j]:
# #             list1[i], list1[j] = list1[j], list1[i]



# # for i in range(len(list1)-1):
# #     for j in range(len(list1)-1):
# #         if list1[j] > list1[j+1]:
# #             list1[j], list1[j+1] = list1[j+1], list1[j]

# # def sort(list, first, last):
# #     pvot = list[first]
# #     left = first+1
# #     right = last

# #     while True:
# #         while left<=right and list[left]<=pvot:
# #             left = left+1
    
# #         while left<=right and list[right]>=pvot:
# #             right = right-1

# #         if left>right:
# #             break
        
# #         list[left], list[right] = list[right], list[left]
# #     list[first], list[right] = list[right], list[first]
# #     return right


# # def quickt(list, first, last):
# #     if first<last:
# #         p = sort(list, first, last)
# #         quickt(list, first, p-1)
# #         quickt(list, p+1, last)


# # list1 = [45,3,2,12,5,6,3,212]
# # first = 0
# # last = len(list1)-1
# # quickt(list1, first, last)
# # print(list1)


# # def mr(list):
# #     if len(list)>1:
# #         mid =  len(list)//2
# #         left_list = list[:mid]
# #         right_list = list[mid:]
# #         mr(left_list)
# #         mr(right_list)
# #         i = 0
# #         j = 0
# #         k = 0

# #         while i<len(left_list) and j<len(right_list):
# #             if left_list[i]<right_list[j]:
# #                 list[k] = left_list[i]
# #                 k = k+1
# #                 i = i+1
# #             else:
# #                 list[k] = right_list[j]
# #                 j = j+1
# #                 k = k+1

# #         while i<len(left_list):
# #             list[k] = left_list[i]
# #             i = i+1
# #             k = k+1

# #         while j<len(right_list):
# #             list[k] = right_list[j]
# #             j = j+1
# #             k = k+1



# # list = [4,3,4,15,67,21,1]
# # mr(list)
# # print(list)



# # def ins(list):
# #     for i in range(1, len(list)-1):
# #         current_value = list[i]
# #         pos = i
# #         while current_value<list[pos-1] and pos>0:
# #             list[pos]=list[pos-1]
# #             pos = pos-1
# #         list[pos] = current_value

# # list = [4,3,2,5,67,3,67,2,7,1,67]
# # ins(list)
# # print(list)



# # def ins(list):
# #     for i in range(1,len(list)-1):
# #         current = list[i]
# #         pos = i
# #         while current<list[pos-1] and pos>0:
# #             list[pos] = list[pos-1]
# #             pos = pos-1
# #         list[pos] = current



# # list = [4,3,2,5,67,3,67,2,7,1,67]
# # ins(list)
# # # print(list)





# # for i in range(len(list)-1):
#     # for j in range(i+1, len(list)):
#     #     if list[i]>list[j]:
#     #         list[i], list[j] = list[j], list[i]


# # for i in range(len(list)-1):
# #     for j in range(len(list)-1):
# #         if list[j]>list[j+1]:
# #             list[j], list[j+1] = list[j+1], list



# # def sort(list, first, last):
# #     pvot = list[first]
# #     left = first+1
# #     right = last

# #     while True:
# #         while left<=right and list[left]<=pvot:
# #             left=left+1
# #         while left<=right and list[right]>=pvot:
# #             right=right-1

# #         if right<left:
# #             break
# #         list[right], list[left] = list[left], list[right]
# #     list[first], list[right] = list[right], list[first]
# #     return right

# # def quick(list, first, last):
# #     if first<last:
# #         p = sort(list, first, last)
# #         quick(list, first, p-1)
# #         quick(list, p+1, last)
# # list = [8778,242,6,32,74,14,4657,124]
# # first = 0
# # last = len(list)-1
# # quick(list, first, last)
# # print(list)


# # def mer(list):
# #     if len(list)>1:
# #         mid = len(list)//2
# #         left_list = list[:mid]
# #         right_list = list[mid:]
# #         mer(left_list)
# #         mer(right_list)
# #         i=0
# #         j=0
# #         k=0

# #         while i<len(left_list) and j<len(right_list):
# #             if left_list[i]<right_list[j]:
# #                 list[k]=left_list[i]
# #                 k=k+1
# #                 i=i+1
# #             else:
# #                 list[k]=right_list[j]
# #                 k = k+1
# #                 j = j+1

# #         while i<len(left_list):
# #             list[k] = left_list[i]
# #             i = i+1
# #             k = k+1


# #         while j<len(right_list):
# #             list[k] = right_list[j]
# #             k = k+1
# #             j = j+1


# # list = [8778,242,6,32,74,14,4657,124]
# # mer(list)
# # print(list)



# # def ins(list):
# #     for i in range(1, len(list)-1):
# #         current = list[i]
# #         pos = i
# #         while current<list[pos-1] and pos>0:
# #             list[pos]=list[pos-1]
# #             pos = pos-1
# #         list[pos]=current



# # ins(list)
# # print(list)

# # def ins(list):
# #     for i in range(1, len(list)):
# #         current_value = list[i]
# #         pos = i
# #         while current_value<list[pos-1] and pos>0:
# #             list[pos]=list[pos-1]
# #             pos = pos-1
# #         list[pos] = current_value

# # list = [1,234,741,2,12,2,457,967,2]
# # ins(list)
# # print(list)


# # def sort(list, first, last):
# #     pvot = list[first]
# #     left = first+1
# #     right = last

# #     while True:

# #         while left<=right and  pvot >= list[left]:
# #             left = left+1
# #         while left<=right and pvot <= list[right]:
# #             right = right-1

# #         if left>right:
# #             break

# #         list[left], list[right] = list[right], list[left]
# #     list[first], list[right] = list[right], list[first]
# #     return right



# # def quick(list, first, last):
# #     if first<last:
# #         p = sort(list, first, last)
# #         quick(list, first, p-1)
# #         quick(list, p+1, last)


# # def mer(list):
# #     if len(list)>1:
# #         mid = len(list)//2
# #         left_list = list[:mid]
# #         right_list = list[mid:]
# #         mer(left_list)
# #         mer(right_list)
# #         k=0
# #         i=0
# #         j=0
# #         while i<len(left_list) and j<len(right_list):
# #             if left_list[i]<right_list[j]:
# #                 list[k]=left_list[i]
# #                 k = k+1
# #                 i = i+1
# #             else:
# #                 list[k] = right_list[j]
# #                 k = k+1
# #                 j = j+1

# #         while i<len(left_list):
# #             list[k] = left_list[i]
# #             k = k+1
# #             i = i+1

# #         while j<len(right_list):
# #             list[k] = right_list[j]
# #             k = k+1
# #             j = j+1

# # def mer(list):
# #     if len(list)>1:
# #         mid = len(list)//2
# #         left_list = list[:mid]
# #         right_list = list[mid:]
# #         mer(left_list)
# #         mer(right_list)
# #         i=0
# #         j=0   
# #         k=0
# #         while i<len(left_list) and j<len(right_list):
# #             if left_list[i]<right_list[j]:
# #                 list[k]=left_list[i]
# #                 k=k+1
# #                 i=i+1
# #             else:
# #                 list[k]=right_list[j]
# #                 k = k+1
# #                 j = j+1

# #         while i<len(left_list):
# #             list[k] = left_list[i]
# #             i = i+1
# #             k = k+1


# #         while j<len(right_list):
# #             list[k] = right_list[j]
# #             k = k+1
# #             j = j+1


# # list = [8778,242,6,32,74,14,4657,124]
# # mer(list)
# # print(list)






# # list = [1,2,3,4,5,62,2,211,4123,52,1,4,2,1]
# # mer(list)
# # print(list)
# # first = 0
# # last = len(list)-1
# # quick(list, first, last)
# # print(list)

# # stack = []
# # def push():
# #     if len(stack)==n:
# #         print("The stack is full")
# #     else:
# #         v = input("Enter Value: ")
# #         stack.append(v)
# #         print(stack)

# # def pop():
# #     if not stack:
# #         print("The stack is empty: ")
# #     else:
# #         v = stack.pop()
# #         print("Remove the element is: ", v)
# #         print(stack)


# # n = int(input("Enter the limit of stack: "))
# # while True:
# #     print("Select oprations : 1 -> push element, 2 -> pop element, 3 -> quit, ")
# #     choice = (input("Enter: "))
# #     if choice == '1':
# #         push()
# #     elif choice == '2':
# #         pop()
# #     elif choice == '3':
# #         print("Successfully quit stack")
# #         break
        
# #     else:
# #         print("Please enter proper oprations !!!")




# # import collections
# # stack = collections.deque()
# # stack.append(10)
# # stack.append(20)
# # print(stack)
# # stack.pop()
# # print(stack)
# # stack.pop()



# # import queue
# # stack = queue.LifoQueue(5)
# # stack.put(10)
# # stack.put(20)
# # print(stack.get())
# # print(stack.get())
# # print(stack.get())


# # queue = []
# # def enqueue():
# #     if len(queue) == n:
# #         print("Queue is full")
# #     else:
# #         val =input("Enter the value: ")
# #         queue.append(val)
# #         print(queue)


# # def dequeue():
# #     if not queue:
# #         print("Queue is empty")
# #     else:
# #         val = queue.pop(0)
# #         print("The remove elements is: ",val)
# #         print(queue)

# # def display():
# #     print(queue)


# # n = int(input("Enter limit of queue: "))
# # while True:
# #     print("Please select opration 1--> add , 2--> remove, 3--> display, 4--> quit")
# #     choice = input("Enter: ")
# #     if choice == '1':
# #         enqueue()
# #     elif choice == '2':
# #         dequeue()
# #     elif choice == '3':
# #         display()
# #     elif choice == '4':
# #         break
# #     else:
# #         print('Please enter proper oprations ')




# # list = [7,326,7,13,4,32,7,9,532,2]
# # # for i in range(len(list)-1):
# # #     for j in range(i+1, len(list)):
# # #         if list[i]>list[j]:
# # #             list[i], list[j] = list[j], list[i]


# # for i in range(len(list)-1):
# #     for j in range(len(list)-1):
# #         if list[j]>list[j+1]:
# #             list[j], list[j+1] = list[j+1], list[j] 
# # print(list)
# # # 



# # def sort(list, first, last):
# #     pvot = list[first]
# #     left = first+1
# #     right = last

# #     while True:
# #         while left<=right and list[left]<=pvot:
# #             left = left+1

# #         while left<=right and list[right]>=pvot:
# #             right = right-1

# #         if right<left:
# #             break
# #         list[left], list[right] = list[right], list[left]
# #     list[first], list[right] = list[right], list[first]
# #     return right




# # def quick(list, first, last):
# #     if first<last:
# #         p = sort(list, first, last)
# #         quick(list, first, p-1)
# #         quick(list, p+1, last)



# # list=[9,1,3,90,54,82,1,92,0,56]
# # first = 0
# # last = len(list)-1
# # quick(list, first, last)
# # print(list)

# # def mer(list):
# #     if len(list)>1:
# #         mid = len(list)//2
# #         left_list = list[:mid]
# #         right_list = list[mid:]
# #         mer(left_list)
# #         mer(right_list)
# #         k = 0
# #         i = 0
# #         j = 0

# #         while i<len(left_list) and j<len(right_list):
# #             if left_list[i]<right_list[j]:
# #                 list[k]=left_list[i]
# #                 k = k+1
# #                 i = i+1
# #             else:
# #                 list[k] = right_list[j]
# #                 k = k+1
# #                 j = j+1

# #         while i<len(left_list):
# #             list[k]=left_list[i]
# #             k = k+1
# #             i = i+1

# #         while j<len(right_list):
# #             list[k]=right_list[j]
# #             k = k+1
# #             j = j+1


# # list = [1,2,12,0,4332,65,3267,42,5]
# # mer(list)
# # print(list)

# # def ins(list):
# #     for i in range(1,len(list)):
# #         current = list[i]
# #         pos = i
# #         while list[pos-1]>current and pos>0:
# #             list[pos] = list[pos-1]
# #             pos = pos-1
# #         list[pos] = current




# # list = [5,2,1,5,654,2,56,8432,75,2,67424,233]
# # ins(list)
# # print(list)




# # Stack

# # stack = []

# # def push():
# #     if n == len(stack):
# #         print("Stack is full ")
# #     else:
# #         val = input("Enter the value: ")
# #         stack.append(val)
# #         print(stack)


# # def pop():
# #     if not stack:
# #         print("The stack is empty ")
# #     else:
# #         val=stack.pop()
# #         print("Remove the elemets is :",val)
# #         print(stack)

        

# # def display():
# #     print(stack)


# # n = int(input("Enter the limit = "))
# # while True:
# #     print("Select oprations")
# #     print("1--> Push element, 2--> pop element, 3--> display, 4--> quit")

# #     choice = input("Enter the value: ")

# #     if choice == '1':
# #         push()
# #     elif choice == '2':
# #         pop()
# #     elif choice == '3':
# #         display()
# #     elif choice == '4':
# #         break
# #     else:
# #         print("Please enter valid oprations")



# # queue = []
# # def enqueue():
# #     if n == len(queue):
# #         print("The queue is full")
# #     else:
# #         val = input("Enter the value: ")
# #         queue.append(val)

# # def dequeue():
# #     if not queue:
# #         print("Empty queue")
# #     else:
# #         val=queue.pop(0)
# #         print("Remove the value is :", val)



# # def display():
# #     print(queue)


# # n = int(input("Enter the size of the queue: "))
# # while True:
# #     print("Select opration")
# #     print("1--> Add, 2--> Remove, 3--> Display, 4--> quit")
# #     choice = input("Enter the oprations")
# #     if choice == '1':
# #         enqueue()
# #     elif choice == '2':
# #         dequeue()
# #     elif choice == '3':
# #         display()
# #     elif choice == '4':
# #         print("Please enter the valid opration !!!!")



# # pqueue=[]       
# # def enqueue():
# #     if n == len(pqueue):
# #         print("The queue is full")
# #     else:
# #         p = int(input("Enter the priority: "))
# #         val = input("Enter the value: ")
# #         pqueue.append((p,val))
# #         pqueue.sort(reverse=True)


# # def dequeue():
# #     if not pqueue:
# #         print("The queue is empty")
# #     else:
# #         val = pqueue.pop()
# #         print(val)

# # def display():
# #     print(pqueue)


# # n = int(input("Enter the size of priority queue: "))
# # while True:
# #     print("Please enter the oprations")
# #     print("1--> add, 2--> remove, 3--> display, 4--> quit")
# #     choice = input("Enter: ")
# #     if choice == '1':
# #         enqueue()
# #     elif choice == '2':
# #         dequeue()
# #     elif choice == '3':
# #         display()
# #     elif choice == '4':
# #         break
# #     else:
# #         print("Please enter the proper oprations")




# # class Node:
# #     def __init__(self, key, value):
# #         self.value = value
# #         self.key = key
# #         self.ref = None



# # class HashTable:
# #     def __init__(self, capacity):
# #         self.capacity = capacity
# #         self.size = 0
# #         self.table = [None]*capacity


# #     def hash_(self, key):
# #         return hash(key)%self.capacity
    

# #     def insert(self, key, value):
# #         index = self.hash_(key)
# #         if self.table[index] is None:
# #             self.table[index] = Node(key, value)
# #             self.size = self.size+1

# #         else:
# #             current = self.table[index]
# #             while current:
# #                 if current.key == key:
# #                     current.value = value
# #                     return
# #                 current = current.ref
# #             newnode = Node(key, value)
# #             newnode.ref = self.table[index]
# #             self.table[index] = newnode
# #             self.size = self.size+1
    




# # class Node:
# #     def __init__(self, key, value):
# #         self.key = key
# #         self.value = value
# #         self.ref = None




# class HashTable:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.size = 0
#         self.table = [None]*capacity


#     def hash_(self, key):
#         return hash(key)%self.capacity
    

#     def insert(self, key, value):
#         index = self.hash_(key)
#         if self.table[index] is None:
#             self.table[index]=Node(key, value)
#             self.size = self.size+1
#         else:
#             current = self.table[index]
#             while current:
#                 if current.key == key:
#                     current.value = value
#                     return
#                 current = current.ref
#             newnode = Node(key, value)
#             newnode.ref = self.table[index]
#             self.table[index] = newnode
#             self.size = self.size+1




#     def search(self, key):
#         index = self.hash_(key)
#         current = self.table[index]
#         while current:
#             if current.key == key:
#                 return current.value
#             current = current.ref

#         raise KeyError(key)
                


# # class Node:
# #     def __init__(self, key, value):
# #         self.key = key
# #         self.value = value
# #         self.ref = None


# # class HashTable:
# #     def __init__(self, capacity):
# #         self.capacity = capacity
# #         self.size = 0
# #         self.table = [None]*capacity


# #     def hash_(self, key):
# #         return hash(key)%self.capacity
    


# #     def insert(self, key, value):
# #         index = self.hash_(key)
# #         if self.table[index] is None:
# #             self.table[index] = Node(key, value)
# #             self.size = self.size+1
# #         else:
# #             current =  self.table[index]
# #             while current:
# #                 if current.key == key:
# #                     current.value = value
# #                     return
# #                 current = current.ref

# #             new_node = Node(key, value)
# #             new_node.ref = self.table[index]
# #             self.table[index] = new_node
# #             self.value = self.value+1


# #     def search(self, key):
# #         index = self.hash_(key)
# #         current = self.table[index]
# #         while current:
# #             if current.key == key:
# #                 return current.value
# #             current = current.ref
# #         raise KeyError(key)



# # list = [1,2,41,2,3,421,43,54,1,53,632]
# # # for i in range(len(list)-1):
# # #     for j in range(i+1, len(list)):
# # #         if list[i]>list[j]:
# # #             list[i], list[j] = list[j], list[i]


# # for i in range(len(list)-1):
# #     for j in range(len(list)-1):
# #         if list[j]>list[j+1]:
# #             list[i], list[j] = list[j], list[i]
# # print(list)



# # def sort(list, first, last):
# #     pvot = list[last]
# #     left = first
# #     right = last-1

# #     while True:
# #         while left<=right and list[left]>=pvot:
# #             left = left+1

# #         while left<=right and list[right]<=pvot:
# #             right = right-1

# #         if left>right:
# #             break
# #         list[left], list[right] = list[right], list[left]
# #     list[left], list[last] = list[last], list[left]
# #     return left



# # def quick(list, first, last):
# #     if first<last:
# #         p = sort(list, first, last)
# #         quick(list, first, p-1)
# #         quick(list, p+1, last)


# # list = [3,53,2,1,535,24,63,1312,63,2,426,1]
# # first = 0
# # last = len(list)-1
# # quick(list, first, last)
# # # print(list)



# # def mer(list):
# #     if len(list)>1:
# #         mid = len(list)//2
# #         left_list = list[:mid]
# #         right_list = list[mid:]
# #         mer(left_list)
# #         mer(right_list)
# #         k = 0
# #         i = 0
# #         j = 0 
# #         while i<len(left_list) and j<len(right_list):
# #             if left_list[i]<right_list[j]:
# #                 list[k]=left_list[i]
# #                 k = k+1
# #                 i = i+1
# #             else:
# #                 list[k] = right_list[j]
# #                 k = k+1
# #                 j = j+1

# #         while i<len(left_list):
# #             list[k] = left_list[i]
# #             i = i+1
# #             k = k+1

# #         while j<len(right_list):
# #             list[k] = right_list[j]
# #             k = k+1
# #             j = j+1


# # list = [2,34,6756,53,745,85,33,7,27,326,7,36,4,0]
# # mer(list)
# # print(list)



# # def ins(list):
# #     for i in range(1,len(list)):
# #         current = list[i]
# #         pos = i
# #         while list[pos-1]>current and pos>0:
# #             list[pos] = list[pos-1]
# #             pos = pos-1
# #         list[pos] = current


# # list = [34,5,3,2,524,6554,2,3,45,63,252,12,156,2]
# # ins(list)
# # print(list)



# # stack = []

# # def push():
# #     if n == len(stack):
# #         print("the stack is full !!")
# #     else:
# #         val = input("Enter value: ")
# #         stack.append(val)

# # def pop():
# #     if not stack:
# #         print("The stack is empty !!")
# #     else:
# #         stack.pop()

# # def display():
# #     print(stack)


# # n = int(input("Enter the size of : "))
# # while True:
# #     print("Select process 1--> add, 2--> remove, 3--> dispay, 4--> quit")
# #     choice = input("Enter: ")
# #     if choice == '1':
# #         push()
# #     elif choice == '2':
# #         pop()
# #     elif choice == '3':
# #         display()
# #     elif choice == '4':
# #         break
# #     else:
# #         print("Select proper oprations command: ")



# # queue = []

# # def enqueue():
# #     if n == len(queue):
# #         print("the queue is full !!")
# #     else:
# #         val = input("Enter the value: ")
# #         queue.append(val)


# # def dequeue():
# #     if not queue:
# #         print("The queue is empty !!")
# #     else:
# #         val = queue.pop(0)
# #         print("The remove elements is : ", val)


# # def display():
# #     print(queue)


# # n = int(input("Enter the size of queue: "))
# # while True:
# #     print("Enter choices : 1--> add, 2--> remove, 3--> display, 4--> quit")
# #     choice = input("Enter")
# #     if choice == '1':
# #         enqueue()
# #     elif choice == '2':
# #         dequeue()
# #     elif choice == '3':
# #         display()
# #     elif choice == '4':
# #         break
# #     else:
# #         print("Select proper choices !!")



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None
# class linked_list:
#     def __init__(self):
#         self.head =  None


#     def push(self):
#         val  = input("Enter the value: ")
#         node = Node(val)
#         node.ref = self.head
#         self.head = node


#     def pop(self):
#         if self.head is None:
#             print("Empty stack !!")
#         else:
#             self.head = self.head.ref



#     def display(self):
#         if self.head is None:
#             print("Satck is empty !!")
#         else:
#             n = self.head 
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

# l1 = linked_list()
# while True:
#     print("Enter your choices 1--> add, 2--> remove, 3--> display, 4--> quit")
#     choice = input("Enter: ")
#     if choice == '1':
#         l1.push()
#     elif choice == '2':
#         l1.pop()
#     elif choice == '3':
#         l1.display()
#     elif choice == '4':
#         break
#     else:
#         print("Select proper choices !!")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def enqueue(self):
#         val = input("Enter the value: ")
#         node = Node(val)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = node


#     def dequeue(self):
#         if self.head is None:
#             print("empty queue !!")
#         else:
#             self.head = self.head.ref


#     def display(self):
#         if self.head is None:
#             print("Empty queue !!")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref




# def hashing(data):
#     return data%size


# def insert(val):
#     hc = hashing(val)
#     if ht[hc] == None:
#         ht[hc] = val
#         print("The value is inserted = ", val)
#         return
#     t = (hc+1)%size
#     while t != hc and ht[t] != None:
#         t = (t+1)%size
#     if ht[t] == None:
#         ht[t] = val
#         print("Insert val is : ", val)
#         return
#     print("hash table is Full !!")
    

# def delete(val):
#     a = search(val)
#     if a==-1:
#         print(val," is not founded in the hashtabel")
#         return
#     ht[a] = None
#     print("deleted")


# def search(x):
#     hc = hashing(x)
#     if ht[hc] == x:
#         print(x, " is founded in position ", hc)
#         return hc
#     t = (hc+1)%size
#     while hc != t and ht[hc]!=x:
#         t  = (t+1)%size
#     if ht[hc] == x:
#         print(x," is founded in position ", t)
#         return t
#     print(x, 'is not founded')
#     return -1


# def display():
#     for i in ht:
#         print(i)


# size = int(input("Enter the size of hash table: "))
# ht = [None]*size
# while True:
#     choice = input("Please select your choice 1--> add, 2--> remove, 3--> search, 4--> display, 5--> quit: ")
#     if choice == '1':
#         val =  int(input("Enter the int input: "))
#         insert(val)
#     elif choice == '2':
#         val = int(input("Witch value is removed: "))
#         print(delete(val))
#     elif choice == '3':
#         val = int(input("Witch value you search: "))
#         print(search(val))
#     elif choice == '4':
#         display()
#     elif choice == '5':
#         break
#     else:
#         print("Please select proper choices !!")


# size = int(input("Enter the size of the hash table: "))
# ht = [None]*size



# def hashcode(val):
#     return val%size


# def insert():
#     val = int(input("Enter int values : "))
#     hc = hashcode(val)
#     if ht[hc] == None:
#         ht[hc] = val
#         print("Inserted value is : ",val)
#         return
#     t = (hc+1)%size
#     while hc != t and ht[t]!=None:
#         t = (t+1)%size
#     if ht[t] == None:
#         ht[t] = val
#         print("Insert the value is : ", val)
#         return
#     print("The hashtable is Full !!")


# def search():
#     val = int(input("Witch int value is you search : "))
#     hc = hashcode(val)
#     if ht[hc] == val:
#         print(val, " is founded in ", hc+1, "position")
#         return hc
#     t = (hc+1)%size
#     while hc != t and ht[t] != val:
#         t = (t+1)%size
#     if ht[t] == val:
#          print(val, " is founded in ", t+1, "position")
#          return t
#     print("The value is not founded")
#     return -1


# def delete():
#     val =  int(input("Witch value want delete: "))
#     hc = hashcode(val)
#     if hc != -1:
#         ht[hc] = None
#         print(val,' is deleted')



# def display():
#     for i in ht:
#         print(i)


# while True:
#     choice = input("Enter your choice  1--> add, 2--> remove, 3--> search, 4--> display, 5--> quit")
#     if choice == '1':
#         insert()
#     elif choice == '2':
#         delete()
#     elif choice == '3':
#         search()
#     elif choice == '4':
#         display()
#     elif choice == '5':
#         break
#     else:
#         print("Select proper choices !!!")



# list = [43,1,42,6,3,1,6657,1,564,21]
# # for i in range(len(list)-1):
# #     for j in range(i+1, len(list)):
# #         if list[i]>list[j]:
# #             list[i], list[j] = list[j], list[i]


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
#         while left<=right and pvot>=list[left]:
#             left = left+1

#         while left<=right and pvot <= list[right]:
#             right = right-1

#         if right<left:
#             break
#         else:
#             list[left], list[right] = list[right], list[left]
#     list[first], list[right] = list[right], list[first]
#     return right



# def quick(list, first, last):
#     if first<last:
#         p = sort(list, first, last)
#         quick(list, first, p-1)
#         quick(list, p+1, last)


# list = [3,224,21,42,5,531,34125,52,21,0]
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
#         k = 0 
#         i = 0
#         j = 0

#         while i <len(left_list) and j< len(right_list):
#             if left_list[i]<right_list[j]:
#                 list[k] = left_list[i]
#                 k = k+1
#                 i = i+1

#             else:
#                 list[k] = right_list[j]
#                 k = k+1
#                 j = j+1

#         while i <len(left_list):
#             list[k] = left_list[i]
#             k = k+1
#             i = i+1

#         while j < len(right_list):
#             list[k] = right_list[j]
#             k = k+1
#             j = j+1



# list = [2,34,52,1,32,53,3,22,5,6,42,2,5,65,3,2]
# mer(list)
# print(list)



# def ins(list):
#     for i in range(1,len(list)):
#         current = list[i]
#         pos = i
#         while list[pos-1]>current and pos>0:
#             list[pos] = list[pos-1]
#             pos = pos-1
#         list[pos] = current


# list = [1,242,2,4,2,53,234,432,522,5,264,21,980,0]
# ins(list)
# print(list)


# stack = []
# stack2 = []


# def push():
#     if n == len(stack):
#         print("the stack is full !!")
#     else:
#         val = input("Enter the value: ")
#         stack.append(val)

# def pop():
#     if not stack:
#         print("stack is empty !!!")
#     else:
#         val=stack.pop()
#         stack2.append(val)

# def display():
#     print(stack)





# n = int(input("Enter the size of stack : "))
# while True:
#     choice = input("select your choice 1--> add, 2--> remove, 3--> display, 4--> quit")
#     if choice == '1':
#         push()
#     elif choice == '2':
#         pop()
#     elif choice == '3':
#         display()
#     elif choice == '4':
#         break
#     else:
#         print("Enter proper choices")



# list = [23,2,134,5,12,5,2,652,3,5,2,5,22,52,55]
# for i in range(len(list)-1):
#     for j in range(i+1, len(list)):
#         if list[i]>list[j]:
#             list[i], list[j] = list[j], list[i]

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
#         while left<=right and pvot>=list[left]:
#             left = left+1

#         while left<=right and pvot <= list[right]:
#             right = right-1
#         if right<left:
#             break
        
#         list[left], list[right] = list[right], list[left]
#     list[right], list[first] = list[first], list[right]
#     return right





# def quick(list, first, last):
#     if first<last:
#         p = sort(list, first, last)
#         quick(list, first, p-1)
#         quick(list, p+1, last)


# list = [121,1,3,53,5,23,6,3345,4653,322,52,5]
# first = 0
# last = len(list)-1
# quick(list, first, last)
# print(list)
    






# def ins(list):
#     for i in range(1,len(list)):
#         current = list[i]
#         pos = i
#         while list[pos-1]>current and pos>0:
#             list[pos] = list[pos-1]
#             pos = pos-1
#         list[pos] = current


# list = [234,23,4,2,42,4,2,54,67,4,26,85,3,6,744]
# ins(list)
# print(list)v


# stack = []
# def push():
#     if n == len(stack):
#         print("The stack is full !!")
#     else:
#         val  =  input("Enter the value: ")
#         stack.append(val)

# def pop():
#     if not stack:
#         print("The stack is empty")
#     else:
#         val = stack.pop()
#         print("The removed the value is = ",val)

# def peek():
#     print(stack[-1])

# n = int(input("Enter the size of stack: "))
# while True:
#     choice = input("Enter the choice 1--> push, 2--> pop, 3--> peek, 4--> quit")

#     if choice == '1':
#         push()
#     elif choice == '2':
#         pop()
#     elif choice == '3':
#         peek()
#     elif choice == '4':
#         break
#     else:
#         print("Enter the proper choice: ")




# size = int(input("Enter the size of hashtable: "))
# ht = [None]*size

# def hashcode(val):
#     return val%size


# def insert():
#     val = int(input("enter number : "))
#     hc = hashcode(val)
#     if ht[hc] == None:
#         ht[hc] = val
#         print("The ", val, " is inserted")
#         return
#     else:
#         t = (hc+1)%size
#         while hc != t and ht[t] != None:
#             t = (t+1)%size

#         if ht[t] == None:
#             ht[t] = val
#             print("The ", val, " is inserted")
#             return
#         print("Hashtable is full !!")


# def search():
#     val = int(input("search a number"))
#     hc = hashcode(val)
#     if ht[hc] == val:
#         print(val," is founded in ", hc+1," position")
#         return hc
#     else:
#         t = (hc+1)%size
#         while t != hc and ht[t] != val:
#             t = (t+1)%size
#         if ht[t]==val:
#             print(val," is founded in ", t+1," position")
#             return t
        
#         print("The value is not founded in the hashtable !!")


# def delete():
#     val  = int(input("Select delete number: "))
#     hc = search(val)
#     if ht[hc] == val:
#         ht[hc] = None
#         print(val, "is deleted")
#         return



# while True:
#     choice = input("Select The choice 1--> insert, 2--> search ,3--> delete")
#     if choice == '1':
#         insert()
#     elif choice == '2':
#         search()
#     elif choice == '3':
#         delete()
#     else:
#         print("Select proper choices : ")
    



# class Queue:
#     def __init__(self):
#         s1 = []
#         s2 = []

#     def enqueue(self, val):
#         while len(self.s1) != 0:
#             self.s2.append(self.s1[-1])
#             self.s1.pop()

#         self.s1.append(val)

#         while len(self.s2) != 0:
#             self.s1.append(self.s2[-1])
#             self.s2.pop()


#     def dequeue(self):
#         if len(self.s1) == 0:
#             print("Stack is empty")
#             return
#         x = self.s1[-1]
#         self.s1.pop()
#         return x
# 


# s1 = []
# s2 = []


# def enqueue(val):
#     while len(s1) != 0:
#         s2.append(s1[-1])
#         s1.pop()

#     s1.append(val)

#     while len(s2) != 0:
#         s1.append(s2[-1])
#         s2.pop()


# def dequeue():
#     if not s1:
#         print("The ")



# s1 = []
# s2 = []

# def enqueue():
#     val = input("Enter the value : ")
#     while len(s1) != 0 :
#         s2.append(s1[-1])
#         s1.pop()

#     s1.append(val)



#     while len(s2) != 0:
#         s1.append(s2[-1])
#         s2.pop()

# def dequeue():
#     if not s1:
#         print("The queue is empty")
#     else:
#         val = s1.pop()
#         print(val, " is deleted")


# for i in range(10):
#     enqueue()

# dequeue()
# dequeue()
# for i in s1:
#     print(i)







# def sort(list, first, last):
#     pvot = list[first]
#     left = first+1
#     right = last

#     while True:
#         while left<=right and pvot>=list[left]:
#             left = left+1

#         while left<=right and pvot<=list[right]:
#             right = right-1

#         if right<left:
#             break
#         list[left], list[right] = list[right], list[left]
#     list[first], list[right] = list[right], list[first]
#     return right

# def quick(list, first, last):
#     if first<last:
#         p = sort(list, first, last)
#         quick(list, first, p-1)
#         quick(list, p+1, last)


# list = [2,33,42,5,2,5,21,5,355,63,63,2,67785,2,7,4]
# first = 0
# last = len(list)-1
# quick(list, first, last)
# print(list)




# def mer(list):
#     if len(list)>1:
#         mid = len(list)//2
#         left_list = list[mid:]
#         right_list = list[:mid]
#         mer(left_list)
#         mer(right_list)
#         k = 0
#         i = 0
#         j = 0

#         while i < len(left_list) and j < len(right_list):
#             if left_list[i]<right_list[j]:
#                 list[k] = left_list[i]
#                 i = i+1
#                 k = k+1
#             else:
#                 list[k] = right_list[j]
#                 k = k+1
#                 j = j+1

#         while i < len(left_list):
#             list[k] = left_list[i]
#             i = i+1
#             k = k+1

#         while j < len(right_list):
#             list[k] = right_list[j]
#             k = k+1
#             j = j+1

# list = [12,4,2,5,6,77,9,800,7,3,2,56,87]
# mer(list)
# print(list)



# def ins(list):
#     for i in range(1, len(list)):
#         current = list[i]
#         pos = i
#         while list[pos-1] > current and pos > 0:
#             list[pos] = list[pos-1]
#             pos = pos-1
#         list[pos] = current


# list = [2312,4,2,5,1,2,5,533,2,2,55,2,65,89]
# ins(list)
# print(list)
        


# list= [5,3,2,34,6,7,45,32,8]
# for i in range(len(list)-1):
#     for j in range(len(list)-1):
#         if list[j]>list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]

# print(list)


# 


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None


# class linked_list:
#     def __init__(self):
#         self.head = None


#     def push(self):
#         val = input("Enter the value: ")
#         node = Node(val)
#         node.ref = self.head
#         node = self.head


#     def pop(self):
#         self.head = self.head.ref


#     def part(self, val):
#         self




# import heapq

# # heap = []

# list = [2,5,6,32,1,53,63,674]
# # for i in list:
# #     heapq.heappush(heap, i)
# # print(heap)
# # heapq.heappop(heap)

# heapq.heapify(list)
# heapq.heappushpop(list, 89)
# heapq.heapreplace(list, 100)
# val=heapq.nsmallest(2, list)
# print(val)
# val = heapq.nlargest(2, list)
# print(val)
# print(list)


# import heapq
# arr = [3,42,5,23,1,11,555]
# n = len(arr)

# heapq.heapify(arr)
# print(arr)


#max_heapyfy
# def max_heapfy(Arr, n, i):
#     largest = i
#     left = i*2 +1
#     right = i*2 +2

#     if n>left and Arr[largest]<Arr[left]:
#         largest=left

#     if n>right and Arr[largest]<Arr[right]:
#         largest = right

#     if largest!=i:
#         Arr[i], Arr[largest] = Arr[largest], Arr[i]

#         max_heapfy(Arr, n, largest)

# for i in range(n//2-1, -1, -1):
#     max_heapfy(arr, n, i)

# print(arr)



# import heapq

# list = [23,4,32,55,654,74,3,1]
# n = len(list)
# heapq.heapify(list)
# print(list)


# def min_heap(arr, n, i):
#     largest = i
#     left = i*2+1
#     right = i*2+2

#     if n>left and arr[largest]>arr[left]:
#         largest = left

#     if n>right and arr[largest]>arr[right]:
#         largest = right

#     if i != largest:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         min_heap(arr, n, largest)



# for i in range(n//2-1, -1, -1):
#     min_heap(list, n, i)

# print(list)


# def max_heap(arr, n, i):
#     largest = i
#     left = i*2+1
#     right = i*2+2

#     if left<n and arr[left] > arr[largest]:
#         largest = left

#     if right<n and arr[left] > arr[largest]:
#         largest = right

#     if i != largest:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         max_heap(arr, n, largest)


# list = [1,3,5,234,2,43,56]
# n = len(list)
# for i in range(n//2-1, -1, -1):
#     max_heap(list, n, i)

# print(list)



# class Trie:
#     head  = {}
#     def add(self, word):
#         cur  = self.head
#         for ch in word:
#             if ch not in cur:
#                 cur[ch]={}
#             cur = cur[ch]
#         cur['*'] = True


#     def search(self, word):
#         cur = self.head
#         for ch in word:
#             if ch not in cur:
#                 print("The word is not founded in the trie ")
#                 return
#             cur[ch] = ch
#         if "*" in cur:
#             print("The value is founded in the trie ")
#         else:
#             print("The value is not founded in the trie ")




# class trie:
#     head = {}
#     def add(self, word):
#         cur = self.head
#         for ch in word:
#             if ch not in cur:
#                 cur[ch] = {}
#             cur = cur[ch]
#         cur['*'] = True

#     def search(self, word):
#         cur = self.head
#         for ch in word:
#             if ch not in cur:
#                 print("The word is not founded in the trie")
#                 return
#             cur  = cur[ch]

#         if '*' in cur:
#             print("The value is founded in the trie ")
#         else:
#             print("The value is not founded")



# t  = trie()
# t.add("akhil")
# t.add("amal")
# t.add('shinadh')
# t.add('shahid')
# t.add('anjush')
# t.add('aswin')


# t.search('amal')
# t.search('amalu')




# class trie:
#     head = {}

#     def add(self, word):
#         cur = self.head
#         for i in word:
#             if i not in cur:
#                 cur[i]={}
#             cur = cur[i]
#         cur['*'] = True

#     def search(self, word):
#         cur = self.head
#         for i in word:
#             if i not in cur:
#                 print("The value is not founded ")
#                 return
#             cur = cur[i]
#         if '*' in cur:
#             print("The value is founded in the list")
#         else:
#             print("The value is not founded ")

# t  = trie()
# t.add("akhil")
# t.add("amal")
# t.add('shinadh')
# t.add('shahid')
# t.add('anjush')
# t.add('aswin')


# t.search('amal')
# t.search('amalu')



# def add(v):
#     global node_count
#     if v in nodes:
#         print("The value is already founded in the graph")
#     else:
#         node_count = node_count+1
#         nodes.append(v)
#         for n in graph:
#             graph.append(0)
#         temp=[]
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)


# nodes = []
# graph = []
# node_count = 0
# print(graph)
# print(nodes)
# print("After adding")
# add(10)
# print(nodes)
# print(graph)


# def add(val):
#     global node_count
#     if val in nodes:
#         print("The value already in the graph")
#     else:
#         node_count = node_count+1
#         nodes.append(val)
#         for i in graphs:
#             i.append(0)

#         temp = []
#         for i in range(node_count):
#             temp.append(0)

#         graphs.append(temp)

# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graphs[i][j], end=' ')
#         print('\n')


# nodes = []
# graphs = []
# node_count = 0
# print("Before inserting")
# print(graphs)
# print(nodes)

# print("After inserting")
# add('a')
# add('k')
# add('h')
# print(graphs)
# print(nodes)
# print('hai')
# print_graph()




# def add(val):
#     global node_count
#     if val in node:
#         print("The value is already in a node ")
#     else:
#         node_count = node_count+1
#         node.append(val)
#         for i in graph:
#             i.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)


# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j], end=' ')
#         print()



# def add_edge(v1, v2):
#     if v1 not in node:
#         print("The value is not founded in the graph")
#     elif v2 not in node:
#         print("The value is not founded in the graph")
#     else:
#         index1 = node.index(v1)
#         index2 = node.index(v2)
#         graph[index1][index2] = 1
#         graph[index2][index1] = 1





# graph = []
# node = []
# node_count = 0

# print("Before add the nodes")
# print(graph)
# print(node)
# add('a')
# add('k')
# add('h')
# add('i')
# add('l')
# add_edge('a','h')
# add_edge('k', 'l')
# print("After add the nodes")
# print(node)
# print_graph()



# graph = {}


# def add_node(val):
#     if val in graph:
#         print("The value already in the list")
#     else:
#         graph[val] = []



# add_node('a')
# add_node('k')
# add_node('h')
# add_node('i')
# add_node('l')

# print(graph)



# def add_graph(val):
#     if val in graph:
#         print("value already in the graph")
#     else:
#         graph[val] = []


# def add_edge(v1, v2, cost):
#     if v1 not in graph:
#         print(v1," The value not founded in the list")
#     elif v2 not in graph:
#         print(v2, " The value not founded in the list")
#     else:
#         list1 = [v1, cost]
#         list2 = [v2, cost]
#         graph[v1].append(list1)
#         graph[v2].append(list2)




# graph = {}
# add_graph('a')
# add_graph('k')
# add_graph('h')
# add_graph('i')
# add_graph('l')
# print(graph)
# add_edge('a', 'i', 10)
# print(graph)




# def add_node(val):
#     global node_count
#     if val in nodes:
#         print("The value already in a graph")
#     else:
#         node_count = node_count+1
#         nodes.append(val)
#         for i in graph:
#             i.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)


# def add_edge(val1, val2, cost):
#     if val1 not in nodes:
#         print(val1, " is not founded in the graph")
#     elif val2 not in nodes:
#         print(val2, " is not founde in the graph")
#     else:
#         index1 = nodes.index(val1)
#         index2 = nodes.index(val2)
#         graph[index1][index2] = cost
#         graph[index2][index1] = cost


# graph = []
# nodes = []
# node_count = 0

# print("before")
# print(graph)
# print(nodes)
# print("After")
# add_node('a')
# add_node('b')
# add_node('c')
# add_node('d')
# print(graph)
# print(nodes)
# print("add edges")
# add_edge('a', 'd', 10)
# add_edge('a', 'c', 20)
# print(graph)
# print(nodes)






# def add_node(val):
#     if val in graph:
#         print(val, ' already in graph')
#     else:
#         graph[val] = []

# def add_edge(val1, val2, cost):
#     if val1 not in graph:
#         print(val1, ' not founded in the graph')
#     elif val2 not in graph:
#         print(val2, ' is not founde in the list')
#     else:
#         list1 = [val1, cost]
#         list2 = [val2, cost]
#         graph[val1].append(list1)
#         graph[val2].append(list2)



# graph = {}

# print("Before")
# print(graph)
# print("After add node")
# add_node('a')
# add_node('b')
# add_node('c')
# add_node('d')
# print(graph)
# print("after connect edge")
# add_edge('a', 'b', 10)
# add_edge('c', 'd', 20)
# print(graph)


# def add(val):
#     global node_count
#     if val in nodes:
#         print(val, " is already in the graph")
#     else:
#         node_count =node_count+1
#         nodes.append(val)
#         for i in graph:
#             i.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)


# def edge(val1, val2):
#     if val1 not in nodes:
#         print(val1, ' not founded in the graph')
#     elif val2 not in nodes:
#         print(val2, ' not founded in the graph')
#     else:
#         index1 = nodes.index(val1)
#         index2 = nodes.index(val2)
#         graph[index1][index2] = 1
#         graph[index2][index1] = 1



# def dele(val):
#     global node_count
#     if val not in nodes:
#         print(val, " is not founded ")
#     else:
#         node_count = node_count-1
#         index1 = nodes.index(val)
#         nodes.pop(index1)
#         graph.pop(index1)
#         for i in graph:
#             i.pop(index1)


# def print_g():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j], end=" ")
#         print()

# def del_ed(val1, val2):
#     if val1 not in nodes:
#         print(val1, "not founded in the graph")
#     elif val2 not in nodes:
#         print(val2, " not founded in the graph")
#     else:
#         index1 = nodes.index(val1)
#         index2 = nodes.index(val2)
#         graph[index1][index2] = 0
#         graph[index2][index1] = 0


    



# graph = []
# nodes = []
# node_count = 0
# print("Before")
# print(nodes)
# print_g()
# add('a')
# add('k')
# add('h')
# add('i')
# add('l')
# print("After add node")
# print(nodes)
# print_g()
# print("After connect edg")
# edge("a", "i")
# edge("h", "i")
# print(nodes)
# print_g()
# print("After delete node")
# dele('h')
# print(nodes)
# print_g()
# print("After delete edge")
# del_ed('a', 'i')
# print(nodes)
# print_g()


# def add(val):
#     if val in graph:
#         print(val, " already in a graph")
#     else:
#         graph[val] = []


# def add_ed(val1, val2, cost):
#     if val1 not in graph:
#         print(val1, " not present in the graph")
#     elif val2 not in graph:
#         print(val2, ' not present in the graph')
#     else:
#         list1 = [val2, cost]
#         list2 = [val1, cost]
#         graph[val1].append(list1)
#         graph[val2].append(list2)

# def del_ed(val1, val2, cost):
#     if val1 not in graph:
#         print(val1, ' not founded in the graph')
#     elif val2 not in graph:
#         print(val2, ' not founded in the graph')
#     else:
#         list1 = [val2, cost]
#         list2 = [val1, cost]
#         if list2 in graph[val2]:
#             graph[val2].remove(list2)
#         if list1 in graph[val1]:
#             graph[val1].remove(list1kjjj)



# def delete(val):
#     if val not in graph:
#         print(val, ' not present in the list')
#     else:
#         graph.pop(val)
#         for i in graph:
#             list = graph[i]
#             if val in list:
#                 list.remove(val)

# graph ={}


# print("Before")
# print(graph)
# print("After add node")
# add('a')
# add('k')
# add('h')
# add('i')
# add('l')
# print(graph)
# print("connect edge")
# add_ed('a', 'k')
# add_ed('h', 'l')
# add_ed('i', 'a')
# print(graph)
# print("delete edge")
# del_ed('h', 'l')
# print(graph)
# print("delete node")
# delete('a')
# delete("h")
# print(graph)




# def add_node(val):
#     if val in graph:
#         print(val, " already in the list")
#     else:
#         graph[val] = []


# def add_edge(val1, val2):
#     if val1 not in graph:
#         print(val1, " not presented in the list")
#     elif val2 not in graph:
#         print(val2, ' not presented in the graph')
#     else:
#         graph[val1].append(val2)
#         graph[val2].append(val1)


# def DFS(node, visited, graph):
#     if node not in graph:
#         print("The node is note in the graph")
#         return
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for i in graph[node]:
#             DFS(i, visited, graph)
        
# def BFS(node, visited, graph):
#     if node not in graph:
#         print("The node is note in the graph")
#         return
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for i in graph[node]:
#             DFS(i, visited, graph)
        




# def BFS(node, graph):
#     visited = set()
#     if node not in graph:
#         print(node, " not founded in the graph")
#         return
#     queue = []
#     queue.append(node)
#     while queue:
#         current = queue.pop(0)
#         if current not in visited:
#             print(current)
#             visited.add(current)
#             for i in graph[current]:
#                 queue.append(i)


    


# graph = {}
# # visited = set()

# add_node('a')
# add_node('k')
# add_node('h')
# add_node('i')
# add_node('l')
# add_edge('a', 'k')
# add_edge('i', 'h')
# add_edge('h', 'l')
# add_edge('l', 'k')

# # DFS_I('a', graph)
# BFS('a', graph)

# DFS('a', visited, graph)



# def add_node(val):
#     if val in graph:
#         print("The value is already in a graph")
#     else:
#         graph[val] = []



# def add_ed(val1, val2):
#     if val1 not in graph:
#         print(val1, " not in graph")
#     elif val2 not in graph:
#         print(val2, " not in graph")
#     else:
#         graph[val1].append(val2)
#         graph[val2].append(val1)




    

    

# graph = {}



# import heapq


# def min_heap(arr, n, i):
#     largest = i
#     left = i*2+1
#     right = i*2+1

#     if left<n and arr[left]<arr[largest]:
#         largest = left

#     if right<n and arr[right]<arr[largest]:
#         largest = right

#     if i != largest:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         min_heap(arr, n, largest)


# list = [2,353,63,4,7,9,564,46]
# heapq.heapify(list)
# print(list)
# n = len(list)
# for i in range(n//2-1, -1, -1):
#     min_heap(list, n, i)
# print(list)




# def max_heap(arr, n, i):
#     largest = i
#     left = i*2+1
#     right = i*2+2
    

#     if n>left and arr[left]>arr[largest]:
#         largest = left
#     if n>right and arr[right]>arr[largest]:
#         largest = right
#     if i != largest:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         max_heap(arr, n, largest)

# list = [89,93,4,932,0,3,63,8,21,9]
# n = len(list)
# for i in range(n//2-1, -1, -1):
#     max_heap(list, n, i)
# print(list)


# class trie:
#     head = {}
#     def insert(self, word):
#         cur = self.head
#         for i in word:
#             if i not in cur:
#                 cur[i] = {}
#             cur = cur[i]
#         cur['*'] = True


#     def search(self, word):
#         cur = self.head
#         for i in word:
#             if i not in cur:
#                 print("The value not founde in the trie")
#                 return
#             cur = cur[i]
#         if '*' in cur:
#             print("The word founded in the trie")
#         else:
#             print("The value is not founded")
    
#     def pri(self):
#         self.printt(self.head, '')

#     def printt(self, node, prifix):
#         for char, child in node.items():
#             if char == '*':
#                 print(prifix)
#             else:
#                 self.printt(child, prifix+char)
    

# t = trie()
# list = ['amal', 'akhil', 'roshan', 'anu']
# for i in list:
#     t.insert(i)

# t.pri()



# class BST:
#     def __init__(self, data):
#         self.key = data
#         self.lchild = None
#         self.rchild = None
    
#     def insert(self, data):
#         if self.key is None:
#             self.key =data
#             return
#         if self.key == data:
#             self.key =data
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)
    

#     def search(self, data):
#         if self.key == data:
#             print("The value founde in the BST")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value not founde in the BST")
#         else:
#             if self.rchild:
#                 if self.rchild:
#                     self.rchild.search(data)
#                 else:
#                     print("The value is not founded in the BST")
            

# def is_BST(root, min = float('-inf'), max = float("inf") ):
#         if root is None:
#             return True
#         if min > root.key or  root.key> max:
           
#             return False
            
#         return(
#                 is_BST(root.lchild, min, root.key) and is_BST(root.rchild, root.key, max)
#         )


# list = [1,34,53,6,3,96,474,354]
# b = BST(10)
# for i in list:
#     b.insert(i)

# if is_BST(b):
#     print("Binary tree")
# else:
#     print("not binary tree")




# def add_vert(val):
#     if val in graph:
#         print("The value already in graph")
#     else:
#         graph[val] = []


# def add_edge(val1, val2):
#     if val1 not in graph:
#         print(val1, ' not presented in the graph')
#     elif val2 not in graph:
#         print(val2, 'not in graph')
#     else:
#         graph[val1].append(val2)
#         graph[val2].append(val1)


# def DFS(graph, node):
#     visited = []
#     if node not in graph:
#         print("The value not founded in the graph")
#         return
#     else:
#         stack = []
#         stack.append(node)
#         while stack:
#             val = stack.pop()
#             if val not in visited:
#                 print(val)
#                 visited.append(val)
#                 for i in graph[val]:
#                     stack.append(i)


# def del_node(v):
#     if v not in graph:
#         print("The value not presnted in the graph")

#     else:
#         graph.pop(v)
#         for i in graph:
#             list = graph[i]
#             for j in list:
#                 j.remove(j)



# def BFS(graph, node):
#     visited = []
#     if node not in graph:
#         print("The value not presented in the graph")
#         return
#     else:
#         stack = []
#         stack.append(node)
#         while stack:
#             val = stack.pop(0)
#             if val not in visited:
#                 print(val)
#                 visited.append(val)
#                 for i in graph[val]:
#                     stack.append(i)

# graph = {}

# for i in range(1, 11):
#     add_vert(i)

# print(graph)
# add_edge(2,1)
# add_edge(2,3)
# add_edge(3,4)
# add_edge(4,5)
# add_edge(5,6)
# add_edge(6,7)
# add_edge(7,8)
# add_edge(8,9)
# add_edge(9,10)
# del_node(6)
# DFS(graph, 1)
# BFS(graph, 1)




# def sort(list, first, last):
#     pvot = last
#     left = first
#     right = last-1

#     while True:
#         while left<=right and pvot >= list[left]:
#             left = left+1
#         while left<=right and pvot <= list[right]:
#             right = right-1

#         if left>right:
#             break
#         list[left], list[right] = list[right], list[left]
#     list[left], list[last] = list[last], list[left]
#     return left



# def quick(list, first, last):
#     if first<last:
#         p = sort(list, first, last)
#         quick(list, first, p-1)
#         quick(list, p+1, last)

# list = [92,43,54,24,45,112,745]
# first=0
# last = len(list)-1
# quick(list, first, last)
# print(list)

# def sort(list, first, last):
#     pvot = list[first]
#     left = first+1
#     right = last

#     while True:
#         while left<=right and pvot>=list[left]:
#             left = left+1

#         while left<=right and pvot<=list[right]:
#             right = right-1

#         if right<left:
#             break
#         list[left], list[right] = list[right], list[left]
#     list[first], list[right] = list[right], list[first]
#     return right

# def quick(list, first, last):
#     if first<last:
#         p = sort(list, first, last)
#         quick(list, first, p-1)
#         quick(list, p+1, last)


# list = [2,33,42,5,2,5,21,5,355,63,63,2,67785,2,7,4]
# first = 0
# last = len(list)-1
# quick(list, first, last)
# print(list)


# def sort(list, first, last):
#     pvot = list[first]
#     left = first+1
#     right = last

#     while True:
#         while left<=right and pvot >= list[left]:
#             left = left+1
#         while left<=right and pvot <= list[right]:
#             right = right-1

#         if left>right:
#             break
#         list [left], list[right] = list[right], list[left]
#     list[first], list[right] = list[right], list[first]
#     return right


# def quick(list, first, last):
#     if first<last:
#         p = sort(list,first,last)
#         quick(list, first, p-1)
#         quick(list, p+1, last)




# list = [2,34,5643,1,2,1246,4567,4,2352,6,346,3462425356]
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
#         k = 0
#         i = 0
#         j = 0
        
#         while i<len(left_list) and j<len(right_list):
#             if left_list[i]<right_list[j]:
#                 list[k] = left_list[i]
#                 i = i+1
#                 k = k+1

#             else:
#                 list[k] = right_list[j]
#                 k = k+1
#                 j = j+1

#         while i < len(left_list):
#             list[k] = left_list[i]
#             k = k+1
#             i = i+1

#         while j < len(right_list):
#             list[k] = right_list[j]
#             j = j+1
#             k = k+1

# list = [223,432,14,15,6344,145,44,368742,7,543,75,3,5843,2]
# mer(list)
# print(list)






# def mer(list):
#     if len(list)>1:
#         mid = len(list)//2
#         left_list = list[:mid]
#         right_list = list[mid:]
#         mer(left_list)
#         mer(right_list)
#         k = 0
#         i = 0
#         j = 0

#         while i<len(left_list) and j<len(right_list):
#             if left_list[i]<right_list[j]:
#                 list[k]=left_list[i]
#                 k =k+1
#                 i =i+1
#             else:
#                 list[k]=right_list[j]
#                 k=k+1
#                 j=j+1

#         while i<len(left_list):
#             list[k] = left_list[i]
#             i=i+1
#             k=k+1

#         while j<len(right_list):
#             list[k] = right_list[j]
#             j=j+1
#             k=k+1



# list = [34,89,7,354345,23,12]
# mer(list)
# print(list)

    # def ins(list):
    #     for i in range(1,len(list)):
    #         current = list[i]
    #         pos = i
    #         while list[pos-1]>current and pos>0:
    #             list[pos] = list[pos-1]
    #             pos = pos-1
    #         list[pos] = current


    # list = [34,2,1,5,45,57,568,34]
    # ins(list)
    # print(list)



# class Node:
#     def __init__(self, data):
#         self.ref = None
#         self.data = data

# class stack:
#     def __init__(self):
#         self.head = None

#     def push(self,data):
#         node = Node(data)
#         node.ref = self.head
#         self.head = node


#     def pop(self):
#         if self.head is None:
#             print("deletion is not posible stack is empty")
#         else:
#             self.head = self.head.ref


#     def display(self):
#         if self.head is None:
#             print("Empty stack")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref
#             print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44")

    

# s = stack()
# s.push(10)
# s.display()
# s.push(30)
# s.display()
# s.pop()
# s.display()


graph={}


def insert(val):
    if val in graph:
        print("The value is already present in graph")
    else:
        graph[val] =[]


def con_node(val1, val2):
    if val1 not in graph:
        print("The value is not founded in the graph")
        return
    if val2 not in graph:
        print("The value is not founded in the graph")
        return
    graph[val1].append(val2)



insert("A")
insert("B")
insert("C")
insert("D")


con_node("A","B")
con_node("B","C")
con_node("C","D")


def BFS(val):
    if val not in graph:
        print("The value is not founded")
    else:
        visited =[]
        queue = []

        queue.append(val)
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.append(current)
                for i in graph[current]:
                    queue.append(i)
    return visited





print(BFS("A"))