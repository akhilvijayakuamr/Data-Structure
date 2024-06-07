# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class Linked_list:
#     def __init__(self):
#         self.head = None

#     def add_beg(self, data):
#         node = Node(data)
#         node.ref = self.head
#         self.head = node


#     def add_end(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#             return
#         n = self.head
#         while n.ref is not None:
#             n = n.ref
#         n.ref = node

#     def add_after(self, data, val):
#         if self.head is None:
#             print("Empty linkedlist")
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
#             node.ref  = n.ref
#             n.ref = node


#     def add_before(self, data, val):
#         if self.head is None:
#             print("Empty linked list")
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
#             print("The value is not founde in the linkedlist")
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
#         else:
#             n = self.head
#             while n.ref.ref is not None:
#                 n = n.ref
#             n.ref = n.ref.ref


#     def del_val(self, val):
#         if self.head is None:
#             print("Empty linked list")
#             return
#         if self.head.data == val:
#             self.head = self.head.ref
#             return
#         n = self.head
#         while n.ref is not None:
#             if n.ref.data == val:
#                 break
#             n = n.ref
#         if n.ref is None:
#             print("The value is not founde in the linkedlist")
#         else:
#             n.ref = n.ref.ref






# def fact(data):
#     if data == 1:
#         return 1
#     else:
#         return data*fact(data-1)
    
# print(fact(5))



# list = [1,2,3,4,5,6,67]
# left = 0
# right = len(list)-1





# def hash(val):
#     return val%size


# def insert(val):
#     hc = hash(val)
#     if ht[hc] == None:
#         ht[hc] = val
#         print("The value is inserted")
#     else:
#         t = (hc+1)%size
#         while t != hc and ht[t] != None:
#             t = (t+1)%size
#         if ht[t] == None:
#             ht[t] = val
#             print("The value is inserted")
#         else:
#             print("the hashtable is Full")

# def search(val):
#     hc = hash(val)
#     if ht[hc] == val:
#         print("The value is founded in the linkedlist")
#         return hc
#     else:
#         t = (hc+1)%size
#         while t != hc and ht[t] != val:
#             t = (t+1)%size
#         if ht[t] == val:
#             print("The value is founded in the hash tabel")
#             return t
#         else:
#             print("The value not founded in the hash table")
#             return -1


# def delete(val):
#     index = search(val)
#     if index == -1:
#         print("The value is not founded in the hash table")
#     else:
#         ht[index] = None
#         print("The value is deleted")


# def display():
#     print(ht)


# size = int(input("Enter the size of the hashtable: "))
# ht = [None]*size

# while True:
#     print("1 is Insert , 2 is Display", "3 is Stop oprations", "4 Search value", "5 Delete value")
#     op = int(input("Selct any option: "))
#     if op == 1:
#         val = int(input("Enter value"))
#         insert(val)
#     elif op == 2:
#         display()
#     elif op == 3:
#         break
#     elif op == 4:
#         val = int(input("Enter the search value"))
#         search(val)
#     elif op == 5:
#         val = int(input("Enter delete value"))
#         delete(val)
#     else:
#         print("Select valid oprations")


# class BST:
#     def __init__(self, data):
#         self.data = data
#         self.rchild = None
#         self.lchild = None

#     def insert(self, data):
#         if self.data is None:
#             self.data = data
#             return
#         elif self.data == data:
#             self.data = data
#             return
#         elif self.data > data:
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
#         if self.data == data:
#             print("The value is founded in the BST")
#         elif self.data > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value is not founded in the BST")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The value is not founded in the BST")

#     def pre_order(self):
#         print(self.data)
#         if self.lchild:
#             self.lchild.pre_order()
#         if self.rchild:
#             self.rchild.pre_order()


#     def in_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         print(self.data)
#         if self.rchild:
#             self.rchild.in_order()



#     def post_order(self):
#         if self.lchild:
#             self.lchild.post_order()
#         if self.rchild:
#             self.rchild.post_order()




#     def delete(self, data, cur):
#         if self.data is None:
#             print("The BST is empty")
#             return
#         if self.data > data:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data, cur)
#             else:
#                 print("The value is not founded in the BST")

#         elif self.data<data:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data, cur)
#             else:
#                 print("The value is not founded in the BST")
#         else:
#             if self.rchild is None:
#                 temp = self.lchild
#                 if data == cur:
#                     self.data = temp.data
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
            
#             if self.lchild is None:
#                 temp = self.rchild
#                 if data == cur:
#                     self.data = temp.data
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
            
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.data = node.data
#             self.rchild = self.rchild.delete(node.data, cur)
#         return self



# def count(root):
#     if root is None:
#         return 0
#     else:
#         return 1+count(root.lchild)+count(root.rchild)
    


# b = BST(10)
# b.insert(23)
# b.insert(34)
# b.insert(2)
# b.insert(43)
# b.in_order()
# b.search(342)

# if count(b):
#     b.delete(43, b.data)
# else:
#     print("Empty BST")

# b.in_order()
# 
# class Trie:
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
#                 print("The value is not Founded")
#                 return
#             cur = cur[i]
#         if "*" in cur:
#             print("The value is founded in the trie")
#         else:
#             print("The value is not founded in the trie")

#     def display(self):
#         print(self.head)


# t = Trie()
# t.insert("Akhil")
# t.insert("Amal")
# t.insert("Roshan")
# t.search("Amal")

# def add_node(val):
#     if val in graph:
#         print("The value is already in graph")
#     else:
#         graph[val] = []


# def con_node(val1, val2):
#     if val1 not in graph:
#         print(val1," Not in graph")
#         return
#     if val2 not in graph:
#         print(val2, " Not in graph")
#         return
#     graph[val1].append(val2)



# def BFS(node):
#     if node not in graph:
#         print("the node is not founded in the graph")
#     else:
#         visited = []
#         queue = []
#         queue.append(node)
#         while queue:
#             current = queue.pop(0)
#             if current not in visited:
#                 visited.append(current)
#                 for i in graph[current]:
#                     queue.append(i)
#     print(visited)



# def DFS(node):
#     if node not in graph:
#         print("The is not Founded in the graph")
#     else:
#         visited = []
#         stack = []
#         stack.append(node)
#         while stack:
#             current = stack.pop()
#             if current not in visited:
#                 visited.append(current)
#                 for i in graph[current]:
#                     stack.append(i)
#     print(visited)






# graph = {}

# add_node("A")
# add_node("B")
# add_node("C")
# add_node("D")
# add_node("E")
# con_node("A","B")
# con_node("A","C")
# con_node("C","D")
# con_node("B","E")
# con_node("E","A")
# con_node("D","B")
# BFS("A")
# DFS("B")



# import random

# choice = "0123456789"
# val = ''.join(random.choices(choice, k=6))
# print(val)

# from datetime import datetime, timedelta
# now = datetime.now()
# val = now+timedelta(days=15)
# print(val.date())

