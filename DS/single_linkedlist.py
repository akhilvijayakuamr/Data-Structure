# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.ref=None

# class linked_list:
#     def __init__(self):
#         self.head=None
#     def check(self):
#         if self.head is None:
#             print("Linked list None")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n=n.ref
#     def add_value(self, data):
#         node1=Node(data)
#         node1.ref = self.head
#         self.head = node1
# l1 = linked_list()
# l1.add_value(10)
# l1.add_value(20)
# l1.check()




# ADD begining in a linked list


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def view(self):
#         if self.head is None:
#             print("the linked list is None")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref
#     def add_beg(self, data):
#         node = Node(data)
#         node.ref = self.head
#         self.head = node

# v = linked_list()
# for i in range(10):
#     v.add_beg(i)
# v.view()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def views(self):
#         if self.head is None:
#             print("not value in linked list")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.ref
#     def add_beg(self, data):
#         node = Node(data)
#         node.ref =  self.head
#         self.head = node


# l = linked_list()
# for i in range(10):
#     l.add_beg(i)
# l.views()

# add end in linked list


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head =  None

#     def view(self):
#         if self.head is None:
#             print("linked list empty")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.ref
    
#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while(n.ref is not None):
#                 n = n.ref
#             n.ref = node

# l = linked_list()
# for i in range(10):
#     l.add_end(i)
# l.view()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None
# class linked_list:
#     def __init__(self):
#         self.head = None

#     def view(self):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.ref
#     def add_beg(self, data):
#         node = Node(data)
#         node.ref  = self.head
#         self.head = node


#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while(n.ref is not None):
#                 n = n.ref
#             n.ref = node

#     def add_after(self, data, x):
#         if self.head is None:
#             print("Empty linkedlist")
#         n = self.head
#         while n is not None:
#             if n.data == x:
#                 break
#             n = n.ref
#         if n is None:
#             print("node is not present in the list")
#         else:
#             node = Node(data)
#             node.ref = n.ref
#             n.ref = node


# l = linked_list()
# l.add_beg(10)
# l.add_end(30)
# l.add_after(20, 10)
# l.view()


# class node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def view(self):
#         if self.head is None:
#             print("Empty Linked list")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.ref
    
#     def add_before(self, data, x):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.data == x:
#             node1 = node(data)
#             node1.ref = self.head
#             self.head = node1
#             return
#         n =  self.head
#         while(n is not None):
#             if n.ref.data == x:
#                 break
#             n = n.ref

#         if n is None:
#             print('The node is note present in the list')
#         else:
#             node1 = node(data)
#             node1.ref = n.ref
#             n.ref = node1


#     def add_end(self, data):
#         node1 = node(data)
#         if self.head is None:
#             self.head = node1
#         else:
#             n = self.head
#             while(n.ref is not None):
#                 n = n.ref
#             n.ref = node1


#     def empty(self, data):
#         if self.head is None:
#             node1 = node(data)
#             self.head = node1
#         else:
#             print("The linked list empty")

# l1 = linked_list()
# l1.add_end(23)
# l1.add_end(24)
# l1.add_before(25, 24)
# l1.view()

    

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def add_beg(self, data):
#         node1 = node(data)
#         node1.ref = self.head
#         self.head =  node1

#     def delete_beg(self):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             self.head = self.head.ref

#     def delete_end(self):
#         if self.head is None:
#             print("Empty linked list")
#         elif self.head.ref is None:
#             self.head = None  
#         else:
#             n = self.head
#             while(n.ref.ref is not None):
#                 n = n.ref
#             n.ref = None

#     def delete_beg(self, data):
#         if self.head  is None:
#             print("The linked list empty")
#             return
#         if self.head.data == data:
#             self.head = self.head.ref
#         else:
#             n = self.head
#             while(n.ref is not None):
#                 if n.ref.data == data:
#                     break
#                 n = n.ref

#             if n.ref is None:
#                 print("node is not present")
#             else:
#                 n.ref = n.ref.ref
        

#     def view(self):
#         if self.head is None:
#             print("Empty linkedlist")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.ref

# l1 = linked_list()
# l1.add_beg(10)
# l1.add_beg(20)
# l1.delete_beg(10)
# # l1.delete_end()
# # l1.delete_beg()
# l1.view()



# class node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head =  None

#     def view(self):
#         if self.head is None:
#             print("Empty linkedlist")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.ref

#     def add_beg(self, data):
#         node1 = node(data)
#         node1.ref = self.head
#         self.head = node1

#     def add_end(self, data):
#         node1 =node(data)
#         if self.head is None:
#             node1 = self.head
#         else:
#             n = self.head
#             while(n.ref is not None):
#                 n = n.ref
#             n.ref = node1

#     def add_after(self, data, x):
#         if self.head is None:
#             print("empty linked list")
#         else:
#             n = self.head
#             while n is not None:
#                 if n.data == data:
#                     break
#                 n = n.ref

#             if n is None:
#                 print("The value is not in this list")
#             else:
#                 node1 = node(data)
#                 n.ref = node1

#     def add_before(self, data, x):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         if self.head.data == data:
#             node1 = node(data)
#             node1.ref = self.head
#             self.head  = node1
#             return
        
#         n = self.head
#         while(n is not None):
#             if n.ref.data == data:
#                 break
#             n = n.ref
#         if n.ref is None:
#             print("value is not present in the linkedlist")
#         else:
#             node1 = node(data)
#             node1.ref = n.ref
#             n.ref = node1

#     def add_empty(self, data):
#         if self.head is not None:
#             print("the linked list is not empty")
#         else:
#             node1 = node(data)
#             self.head = node1


#     def del_beg(self):
#         if self.head is None:
#             print("linked list empty")
#         else:
#             self.head = self.head.ref


#     def del_end(self):
#         if self.head is None:
#             print("The linked list is empty")
#             return
#         if self.head.ref is None:
#             self.head = self.head.ref
        
#         else:
#             n = self.head
#             while(n.ref.ref is not None):
#                 n = n.ref
#             n.ref = None




#     def val(self, x):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.data == x:
#             self.head = self.head.ref
#         else:
#             n = self.head
#             while(n.ref is not None):
#                 if n.ref.data == x:
#                     break
#                 n = n.ref
#             if n.ref is None:
#                 print("the value not presented in this list")
#             else:
#                 n.ref = n.ref.ref



# Doubly linked list


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.pref = None
#         self.nref = None

# class Linked_list:
#     def __init__(self):
#         self.head = None

#     def tra(self):
#         if self.head is None:
#             print("The linked list is empty")
#         else:
#             n =  self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.nref


#     def tra_rev(self):
#         if self.head is None:
#             print("Linked list empty")

#         else:
#             n = self.head
#             while(n is not None):
#                 n = n.nref

#             while(n is not None):
#                 print(n.data)
#                 n = n.pref



# class Node:
#     def __init__(self, data):
#         self.data =  data
#         self.ref =  None

# class Linked_list:
#     def __init__(self):
#         self.head =  None

#     def view(self):
#         if self.head is None:
#             print("Linkedlist is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n =  n.ref

#     def add_beg(self, data):
#         node = Node(data)
#         node.ref = self.head
#         self.head = node

#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n =  n.ref
#             n.ref = node

#     def add_after(self, data, x):
#         if self.head is None:
#             print("Empty linkedlist")
#         else:
#             n = self.head
#             while(n is not None):
#                 if n.data == x:
#                     break
#                 n = n.ref
#             if n is None:
#                 print("The value not foounded in linkedlist")
#             else:
#                 node = Node(data)
#                 node.ref = n.ref
#                 n.ref = node

#     def add_befor(self, data, x):
#         if self.head is None:
#             print("Linkedlist is empty")
#             return
        
#         if self.head.data == data:
#             node = Node(data)
#             node.ref = self.head
#             self.head = node
#             return

#         n = self.head
#         while(n.ref is not None):
#             if n.ref.data == data:
#                 break
#             n = n.ref
#         if n.ref is None:
#             print("linkedlist is Empty")
#         else:
#             node = Node(data)
#             node.ref = n.ref
#             n.ref = node


#     def add_empty(self, data):
#         if self.head is not None:
#             print("The linked list is not empty")
#         else:
#             node = Node(data)
#             self.head = node




#     def del_beg(self):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             self.head = self.head.ref



#     def del_end(self):
#         if self.head is None:
#             print("empty linkedlist")
#             return
#         if self.head.ref is None:
#             self.head = self.head.ref
#         else:
#             n = self.head
#             while(n.ref.ref is None):
#                 n = n.ref
#             n.ref = None


#     def del_val(self, data):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.data == data:
#             self.head = self.head.ref
#         else:
#             n = self.head
#             while(n.ref is not None):
#                 if n.ref.data == data:
#                     break
#                 n = n.ref
#             if n.ref is None:
#                 print("The value not found in list")
#             else:
#                 n.ref = n.ref.ref







# Doubly linked list


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.nref = None
#         self.pref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def tra(self):
#         if self.head is None:
#             print("The linkedlist is empty")
#         else:
#             n = self.head
#             while( n is not None):
#                 print(n.data)
#                 n = n.nref



#     def rev_tra(self):
#         if self.head is None:
#             print("The lisnked list is empty")
#         else:
#             n = self.head
#             while n.nref is not None:
#                 n = n.nref

#             while n is not None :
#                 print(n.data)
#                 n = n.pref


#     def empty(self, data):
#         if self.head is not None:
#             print("The linked is not empty")
#         else:
#             node = Node(data)
#             self.head= node

#     def add_beg(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             node.nref = self.head
#             self.head.pref = node
#             self.head = node

#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while(n.nref is not None):
#                 n = n.nref
#             n.nref = node
#             node.pref = n


#     def add_after(self, data, x):
#         if self.head is None:
#             print("The linked list empty")
#         else:
#             n = self.head
#             while(n is not None):
#                 if n.data == x:
#                     break
#                 n = n.nref
#             if n is None:
#                 print("The node not found in the linkedlist")
#             else:
#                 node = Node(data)
#                 node.nref = n.nref
#                 node.pref= n
#                 if n.nref is not None:
#                     n.nref.pref = node
#                 n.nref = node


#     def add_before(self, data, x):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             n =  self.head
#             while(n is not None):
#                 if n.data == x:
#                     break
#                 n = n.nref
#             if n is None:
#                 print("node is note founded in linked list")
#             else:
#                 node = Node(data)
#                 node.nref = n
#                 node.pref = n.pref
#                 if n.pref is not None:
#                     n.pref.nref = node
#                 else:
#                     self.head = node
#                 n.pref = node
        

#     def del_beg(self):
#         if self.head is None:
#             print("empty linked list")
#             return
#         if self.head.nref is None:
#             self.head = None
#         else:
#             self.head = self.head.nref
#             self.head.pref = None



#     def del_end(self):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.nref is None:
#             self.head = None
#         else:
#             n = self.head
#             while(n.nref is not None):
#                 n = n.nref
#             n.pref.nref = None

#     def del_val(self, val):
#         if self.head is None:
#             print("empty linkedlist")
#             return
#         if self.head.nref is None:
#             if self.head.data == val:
#                 self.head = None
#             else:
#                 print("the node is not founded")
#             return
#         if self.head.data == val:
#             self.head = self.head.nref
#             self.head.pref = None
#             return
#         n = self.head
#         while(n.nref is not None):
#             if n.data  == val:
#                 break
#             n = n.nref       
#         if n.nref is not None:
#             n.pref.nref = n.nref
#             n.nref.pref = n.pref
#         else:
#             if n.data == val:
#                 n.pref.nref = None
#             else:
#                 print("The node is not founded in linked list")


            
                


# l1 = linked_list()
# l1.empty(10)
# l1.add_beg(5)
# l1.add_end(20)
# l1.add_before(2, 5)
# l1.add_after(30, 20)
# l1.del_val(30)
# l1.tra()
# print("<----------------------------->")
# l1.rev_tra()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.nref = None
#         self.pref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def add_beg(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             self.head.pref = node
#             node.nref = self.head
#             self.head = node

#     def add_end()




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def add(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while n.ref is not None :
#                 n = n.ref
#             n.ref = node
#             return


#     def view(self):
#         if self.head is None:
#             print("empty linked list")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.ref

#     def remove(self):
#         if self.head is None:
#             print("empty linked list")
#         else:
#             n = self.head
#             while(n.ref is not None):
#                     if n.data == n.ref.data:
#                         n.ref = n.ref.ref
#                     else:
#                         n = n.ref

    
# l1 = linked_list()
# list = [1,2,3,3,4,5,5,6,6]
# for i in list:
#     l1.add(i)
# l1.view()
# print("<------------------------->")
# l1.remove()
# l1.view()



# list = [1,2,3,4,5,6,7,8,9]
 

# def search(arr, t):
#     left, right = 0, len(arr)-1
#     while(left <= right):
#         mid = (left+right)//2
#         if arr[mid] == t:
#             return arr[mid]
#         elif arr[mid] < t:
#             left = mid+1
#         else:
#             right = mid-1
#     return False


# print(search(list, 1))


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def search(arr, t):
#     left, right = 0, len(arr)-1
#     while(left<=right):
#         mid = (left+right)//2
#         if arr[mid] == t:
#             return arr[mid]
#         elif arr[mid]<t:
#             left = mid+1
#         else:
#             right = mid-1
#     return False


# val = search(list, 5)
# print(val)

# import sys
# print(sys.getrecursionlimit())


# def rec(val):
#     if val ==1:
#         return 1
#     return val + rec(val-1)

# print(rec(5))


# list = [1,2,3,4,5,6,7,8,9]
# left, right = 0, len(list)-1
# def rec(arr, v):
#     global left
#     global right
#     mid = (left+right)//2
#     if arr[mid] == v:
#         return arr[mid]
#     elif arr[mid]<v:
#         left = mid+1
#     else:
#         right = mid-1
#     if left <= right:
#         return rec(arr, v)
#     else:
#         return False
    
# val=rec(list, 1)
# print(val)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def add_empty(self, data):
#         if self.head is not None:
#             print("The linkedlist is not empty")
#         else:
#             node = Node(data)
#             self.head = node


#     def add_beg(self, data):
#         node = Node(data)
#         node.ref = self.head
#         self.head = node


#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node 
#         else:
#             n = self.head
#             while(n.ref is not None):
#                 n =n.ref
#             n.ref = node

#     def add_after(self, data, pos):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             n = self.head
#             while(n is not None):
#                 if n.data == pos:
#                     break
#                 n = n.ref

#             if n is None:
#                 print("The value is not present in the list")
#             else:
#                 node = Node(data)
#                 node.ref = n.ref
#                 n.ref = node


#     def add_before(self, data, pos):
#         if self.head is None:
#             print("empty linked list")
#             return
#         if self.head.data == pos:    
#                 node = Node(data)
#                 node.ref = self.head
#                 self.head = node
#         else:
#             print("the node note founded")
#         n = self.head
#         while(n.ref is not None):
#             if n.ref.data == pos:
#                 break
#             n = n.ref
#         if n.ref is None:
#             print("node is not founded in linked list")

#         else:
#             node = Node(data)
#             node.ref = n.ref
#             n.ref = node


#     def del_beg(self):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             self.head = self.head.ref
            
#     def del_end(self):
#         if self.head is None:
#             print("Empty linkedlist")
#         else:
#             if self.head.ref is None:
#                 self.head = self.head.ref
#             else:
#                 n = self.head
#                 while n.ref.ref is not None:
#                     n = n.ref
#                 n.ref = None

#     def del_val(self, val):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.ref is None:
#             if self.head.data == val:
#                 self.head = None
#             else:
#                 print("The node is not found in the list")
#         else:
#             n = self.head
#             while n.ref is None:
#                 if n.ref.data == val:
#                     break
#                 n = n.ref
#             if n.ref is None:
#                 print("the node not founded in linkedlist")
#             else:
#                 n.ref = n.ref.ref

#     def view(self):
#         if self.head is None:
#             print("Empty linkedlist")
#         else:
#             n = self.head 
#             while(n is not None):
#                 print(n.data)
#                 n = n.ref

#     def rev(self):
#         if self.head is None:
#             print("The lniked list is empty")
#         else:
#             n = self.head
#             while(n is not None):






# l1 = linked_list()
# l1.add_empty(10)
# l1.add_beg(5)
# l1.add_end(15)
# l1.add_after(12, 10)
# l1.add_before(13, 15)
# l1.view()
# print("<-------------------------------------->")
# l1.del_beg()
# l1.del_end()
# l1.del_val(12)
# l1.view()



# class list:
#     def __init__(self):
#         self.capacity = 10
#         self.size = 0
#         self.val = [None]*10


#     def insert(self, data):
#         if self.capacity == self.size:
#             self.capacity *= 2
#             new_data = [None]*self.capacity

#             for i in range(self.size):
#                 new_data[i]=self.val[i]

#             self.val = new_data
#         self.val[self.size] = data
#         self.size += 1

#     def view(self):
#         for i in range(self.size):
#             print(self.val[i])


# l = list()
# for i in range(11):
#     l.insert(i)
# l.view()


                



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref  = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def add_beg(self, data):
#         node = Node(data)
#         node.ref = self.head
#         self.head  = node

#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while(n.ref is None):
#                 n = n.ref
#             n.ref = node

#     def after_val(self, data, val):
#         if self.head is None:
#             print("linked list is empty")
#             return
#         if self.head.ref is None:
#             if self.head.data == val:
#                 node = Node(data)
#                 self.head.ref = node
#             else:
#                 print("the node is not founded in linked list")
#         else:
#             n = self.head
#             while n is not None:
#                 if n.data == val:
#                     break
#                 n = n.ref
#             if n is None:
#                 print("the node is not founded")
#             else:
#                 node = Node(data)
#                 node.ref = n.ref
#                 n.ref = node

#     def del_beg(self):
#         if self.head is None:
#             print("empty linked list")
#         else:
#             self.head = self.head.ref

#     def del_end(self):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             if self.head.ref is None:
#                 self.head = self.head.ref
#             else:
#                 n = self.head
#                 while n.ref.ref is not None:
#                     n = n.ref
#                 n.ref = n.ref.ref


#     def del_val(self, val):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.data == val:
#             self.head = self.head.ref

#         else:
#             n = self.head
#             while(n.ref is not None):
#                 if n.ref.data == val:
#                     break
#                 n = n.ref
#             if n.ref is None:
#                 print("The node is not founded")
#             else:
#                 n.ref = n.ref.ref





# 

# class search:

#     def linear_search(self, arr, val):
#         for i in arr:
#             if i == val:
#                 return i
#         return False

#     def binary_search(self,arr, val):
#         left = 0
#         right = len(arr)-1
#         while(left<=right):
#             mid = (left+right)//2
            
#             if arr[mid] == val:
#                 return arr[mid]
            
#             elif arr[mid]<val:
#                 left = mid+1
#             else:
#                 right = mid-1
#         return False


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# s = search()
# print(s.linear_search(arr, 5))
# print(s.binary_search(arr)








# def rec(data):
#     if data == 1:
#         return 1
#     else:
#         return data + rec(data-1)
    
# print(rec(5))

# def rec(val):
#     if val == 0:
#         return 0
#     elif val == 1:
#         return 1
#     else:
#         return rec(val-1)+rec(val-2)
    

# for i in range(11):
#     print(rec(i))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.nref = None
#         self.pref = None

# class linked_list:
#     def __init__(self):
#         self.head = None



#     def add_beg(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             node.nref = self.head
#             self.head.pref = node
#             self.head = node


#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while(n.nref is not None):
#                 n = n.nref
#             node.pref = n
#             n.nref = node


#     def add_after(self, data, val):
#         if self.head is None:
#             print("empty linkedlist")
#             return
#         n = self.head
#         while(n is not None):
#             if n.data == val:
#                 break
#             n = n.nref
#         if n is None:
#             print("node is not presented in the list")
#         else:
#             node = Node(data)
#             node.nref = n.nref
#             node.pref = n
#             if n.nref is not None:
#                 n.nref.pref = node
#             n.nref = node
            
        

#     def add_before(self, data, val):
#         if self.head is None:
#             print("empty linked list")
#         else:
#             n =  self.head
#             while(n is not None):
#                 if n.data == val:
#                     break
#                 n = n.nref
#             if n is None:
#                 print("the node is not founded in the list")
#             else:
#                 node =  Node(data)
#                 node.pref = n.pref
#                 node.nref = n
#                 if n.pref is not None:
#                     n.pref.nref = node
#                 else:
#                     self.head = node
#                 n.pref = node




#     def del_beg(self):
#         if self.head is None:
#             print("Empty linkedlist")
#             return
#         if self.head.nref is None:
#             self.head = None
#         else:
#             self.head  = self.head.nref
#             self.head.pref = None


#     def del_end(self):
#         if self.head is None:
#             print("The linked list is empty")
#             return
#         if self.head.nref is None:
#             self.head = None
#         else:
#             n = self.head
#             while n.nref is not None:
#                 n = n.nref
#             n.pref.nref = None



#     def del_val(self, val):
#         if self.head is None:
#             print("linkedlist is empty")
#             return
#         if self.head.nref is None:
#             if self.head.data == val:
#                 self.head = None
#             else:
#                 print("The node is not founded")
#             return
#         if self.head.data == val:
#             self.head = self.head.nref
#             self.head.pref = None
#         else:
#             n = self.head
#             while n is not None:
#                 if n.data == val:
#                     break
#                 n = n.nref
#             if n is None:
#                 print("The node not founded in the list")
#             elif n.nref is None:
#                 n.pref.nref = None
#             else:
#                 n.nref.pref = n.pref
#                 n.pref.nref = n.nref

#     def view(self):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             n = self.head
#             while(n is not None):
#                 print(n.data)
#                 n = n.nref


                

# l = linked_list()
# l.add_beg(10)
# l.add_end(20)
# l.add_after(30, 20)
# l.add_before(5, 10)
# l.view()
# print("<-------------------------------------------->")
# l.del_beg()
# l.del_end()
# l.del_val(20)
# l.view()




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.nref = None
#         self.pref = None
# class linkedlist:
#     def __init__(self):
#         self.head = None
    
#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             n = self.head
#             while(n.nref is not None):
#                 n = n.nref
#             n.nref = node
#             n.nref.pref = n


#     def view(self):
#         if self.head is None:
#             print("The linkedlist is empty")
#         else:
#             n = self.head 
#             while(n is not None):
#                 print(n.data, end='')
#                 n = n.nref

#     def rev_view(self):
#         if self.head is None:
#             print("The linkedlist is empty")
#         else:
#             n = self.head
#             while(n.nref is not None):
#                 n = n.nref

#             while(n is not None):
#                 print(n.data, end='')
#                 n = n.pref
 

#     def mid(self):
#         if self.head is None:
#             print("empty linked list")
#         else:
#             n = self.head
#             m = self.head
#             while m.nref is not None:
#                  m = m.nref.nref
#                  n = n.nref
#             print(n.data)

# def join(l1, l2):
#     if not l1:  
#         return  "first linkedlist is not founded"
#     if not l2:
#         return "second linked list is None"
#     n = l1.head 
#     while(n.nref is not None):
#         n = n.nref
#     n.nref = l2.head
#     l2.head.pref = n
#     n = l1.head
#     # while(n is not None):
#     #     print(n.data, end='')
#     #     n = n.nref
        
    

# l = linkedlist()
# s =  "akhil Vijayakumar"
# for i in s:
#     l.add_end(i)
# l.view()
# print('<----------------------------------------->')
# l.rev_view()
# print("<---------------------------------------------->")
# l.mid()
            
# l1  = linkedlist()
# l2 = linkedlist()
# firstname = 'Akhil'
# lastname = 'Vijayakumar'
# for i in firstname:
#     l1.add_end(i)

# for i in lastname:
#     l2.add_end(i)

# join(l1, l2)

# l1.view()
# print('\n')
# l2.view()
            

# from array import array

# arr = array('i', [1, 2, 3, 4, 5])
# print(arr[0])
        


# def rec(n):
#     if n == 0:
#         return 0
#     if n == 1: 
#         return 1
#     return rec(n-1)+ rec(n-2)


# for i in range(11):
#     print(rec(i))


# 




# list = [1, 3, 4, 5, 6, 9, 11, 15, 18, 21, 25]


# def binary(arr, t):
#     first = 0
#     last = len(arr)-1
#     while(first <= last):
#         mid = (first+last)//2
#         if arr[mid] == t:
#             return mid+1
#         elif arr[mid] < t:
#             first = mid+1
#         else:
#             last = mid-1
#     return "The value not founded"

# print(binary(list, 15))




# class Node:
#     def __init__(self, data):
#         self.ref = None
#         self.data = data

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         n = self.head
#         while n is not None:
#             print(n.data)
#             n = n.ref
#         print("###############################################")

#     def add_beg(self,data):
#         node = Node(data)
#         node.ref = self.head
#         self.head = node


#     def add_end(self, data):
#         node = Node(data)
#         if  self.head is None:
#             self.head = node
#             return
#         n = self.head
#         while n.ref is not None:
#             n = n.ref
#         n.ref = node


#     def add_after(self,val,data):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         n = self.head
#         while n is not None:
#             if n.data == val:
#                 break
#             n = n.ref
#         if n is None:
#             print("The value is not founded in the linked list")
#         else:
#             node = Node(data)
#             node.ref = n.ref
#             n.ref = node



#     def add_before(self, val, data):
#         if self.head is None:
#             print("E,pty linkedlist")
#             return
#         if self.head.data == val:
#             node = Node(data)
#             node.ref = self.head
#             self.head = node
#             return
#         n = self.head
#         while n.ref is not None:
#             if n.ref.data == val:
#                 break
#             n = n.ref

#         if n.ref is None: 
#             print("The value is not founded in the linked list")
#         else:
#             node = Node(data)
#             node.ref = n.ref
#             n.ref = node





#     def del_beg(self):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             self.head = self.head.ref

#     def del_end(self):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.ref is None:
#             self.head = self.head.ref
#             return
#         n = self.head
#         while n.ref.ref is not None:
#             n = n.ref
#         n.ref = n.ref.ref




#     def del_val(self, val):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.data == val :
#             self.head = self.head.ref
#         else:
#             n = self.head
#             while n.ref is not None:
#                 if n.ref.data == val:
#                     break
#                 n = n.ref 

#             if n.ref is None:
#                 print("The value is not Founded in the")
#             else:
#                 n.ref = n.ref.ref
            
            



# l1 = linked_list()
# l1.add_beg(10)
# l1.display()
# l1.add_end(29)
# l1.display()
# l1.add_after(10,20)
# l1.display()
# l1.add_before(20,15)
# l1.display()
# l1.add_beg(7)
# l1.add_beg(6)
# l1.add_beg(2)
# l1.display()
# l1.del_beg()
# l1.display()
# l1.del_end()
# l1.display()
# l1.del_val(15)
# l1.display()


# list = [32,54,233,63,62,265,672]

# def linear_search(list,val):
#     for i in list:
#         if i == val:
#             print("The value is founded in the list")
#             return
#     print("The value is not founded in the list")

# linear_search(list,0)

# def binary_search(list, val):
#     left = 0
#     right = len(list)-1
#     while left<=right:
#         mid = (left+right)//2
#         if list[mid] == val:
#             print("The value is founded in the list")
#             return
#         elif list[mid]>val:
#             right = mid-1
#         else:
#             left = mid+1
#     print("The value is not founded in the list")
#     return


# list= [1,2,3,4,5,6,7,8,9]
# binary_search(list,7)


# def factorial(val):
#     if val == 1:
#         return 1
#     else:
#         return val*factorial(val-1)
    
# val=factorial(5)
# print(val)