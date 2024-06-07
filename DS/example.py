# class BST:
#     def __init__(self, data):
#         self.key = data
#         self.lchild = None
#         self.rchild = None

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             self.key = data
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
#             print("The data is founded in the list")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value is not founded")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The value is not founded")



#     def pre_order(self):
#         print(self.key)
#         if self.lchild:
#             self.lchild.pre_order()
#         if self.rchild:
#             self.rchild.pre_order()


#     def in_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         print(self.key)
#         if self.rchild:
#             self.rchild.in_order()


#     def post_order(self):
#         if self.lchild:
#             self.lchild.post_order()
#         if self.rchild:
#             self.rchild.post_order()
#         print(self.key)



#     def min(self):
#         current = self
#         while current.lchild:
#             current = current.lchild
#         print("The minimum value is :", current.key)

        

#     def max(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("The max value is ", current.key)



    # def closet(self, root, data):
    #     clo = float('inf')
    #     while True:
    #         if abs(root.key - data)<abs(clo - data):
    #             clo = root.key
    #         if data < root.key:
    #             root = root.lchild
    #         elif data > root.key:
    #             root = root.rchild
    #         else:
    #             break
    #     print("The closet value is ", clo)




#     def delete(self, val, curr):
#         if self.key is None:
#             print("BST is empty")
#             return
#         if val < self.key:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(val, curr)
#             else:
#                 print("The bst not founded in the BST")
#         elif val > self.key:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(val, curr)
#             else:
#                 print("The value not founde in the list")
#         else:
#             if self.rchild is None:
#                 temp = self.lchild
#                 if val == curr:
#                     self.key = temp.key
#                     self.rchild = temp.rchild
#                     self.lchild = temp.lchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             if self.lchild is None:
#                 temp = self.rchild
#                 if val == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(val, curr)
#         return self


# def count(root):
#     if root is None:
#         return 0
#     return 1+count(root.lchild)+count(root.rchild)





# root = BST(10)
# root.insert(24)
# root.insert(5)
# root.insert(23)
# root.insert(89)
# root.insert(26)
# root.in_order()
# root.search(23)
# if count(root)>1:
#     root.delete(10, root.key)
# else:
#     print("empty bst")
# root.in_order()





# class BST:
#     def __init__(self, data):
#         self.key  = data
#         self.lchild = None
#         self.rchild = None

    

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             self.key = data
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
#             print("The value is founded in the BST")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value is not founde in BST")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The value not founded in the BST")


#     def pre_order(self):
#         print(self.key)
#         if self.lchild:
#             self.lchild.pre_order()
#         if self.rchild:
#             self.rchild.pre_order()

#     def in_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         print(self.key)
#         if self.rchild:
#             self.rchild.in_order()


#     def post_order(self):
#         if self.lchild:
#             self.lchild.post_order()
#         if self.rchild:
#             self.rchild.post_order()


#     def min(self):
#         current = self
#         while current.lchild:
#             current = current.lchild
#         print("The min value is : ", current.key)


#     def max(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("The max value is : ", current.key)



#     def closet(self, root, val):
#         clo = float('inf')
#         while root:
#             if abs(root.key - val) < abs(clo - val):
#                 clo = root.key

#             if root.key > val:
#                 root = root.lchild

#             elif root.key < val: 
#                 root = root.rchild

#             else:
#                 break
#         print("The closet value is : ", clo)
        


#     def delete(self, val, curr):
#         if self.key is None:
#             print("The BST is empty")
#             return
#         if self.key > val:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(val, curr)
#             else:
#                 print(val ,' not founded in the BST')
#         elif self.key < val:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(val, curr)
#             else:
#                 print(val," is not founde in the BST")
#         else:
#             if self.rchild is None:
#                 temp = self.lchild
#                 if val == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             if self.lchild is None:
#                 temp = self.rchild
#                 if val == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
            
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key, curr)
#         return self
    


#     def is_bst(self, root, min_val = float("-inf"), max_val = float("inf")):
#         if root is None:
#             return True
        
#         if min_val<root.key<max_val:
#             return False
        
#         return(
#             root.is_bst(root.lchild, min_val, root.key) and root.is_bst(root.rchild, root.key, max_val)
#         )


# def count(node):
#     if node is None:
#         return 0
#     return 1+count(node.lchild)+count(node.rchild)

 



# root  = BST(10)
# root.insert(23)
# root.insert(7)
# root.insert(35)
# root.insert(21)
# root.insert(17)
# root.in_order()
# root.search(7)
# root.closet( root,26)
# root.min()
# root.max()
# if count(root)>1:
#     root.delete(10, root.key)
# else:
#     print("The BST is empty")
# root.in_order()

# if root.is_bst:
#     print("This is bst")
# else:
#     print("This is not bst")



# def min_heap(arr, n, i):
#     largest = i
#     left = i*2+1
#     right = i*2+2

#     if n>left and arr[left]<arr[largest]:
#         largest = left

#     if n>right and arr[right]<arr[largest]:
#         largest = right

#     if i != largest:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         min_heap(arr, n, largest)



# list = [5,353,6,332,1,63,7,2,45,745,2725,2336,0]
# n = len(list)
# for i in range(n):
#     min_heap(list, n, i)

# print(list)



# class trie:
#     head = {}

#     def add(self, word):
#         cur = self.head
#         for i in word:
#             if  i not in cur:
#                 cur[i] = {}
#             cur = cur[i]
#         cur['*'] = True


#     def search(self, word):
#         cur = self.head
#         for i in word:
#             if i not in cur:
#                 print("The value not founded in the trie")
#                 return
#             cur = cur[i]

#         if '*' in cur:
#             print("The value founded in the list")
#         else:
#             print("The value is not founded")
        


# class BST:
#     def __init__(self, data):
#         self.key = data
#         self.lchild = None
#         self.rchild = None

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key== data:
#             self.key = data
#             return
#         if self.key>data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = BST(data)
#         if self.key<data:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)


#     def search(self, val):
#         if self.key == val:
#             print("The value is presented in the BST")
#             return
#         if self.key > val:
#             if self.lchild:
#                 self.lchild.search(val)
#             else:
#                 print("The value not founded in the BST")
#         else:
#             if self.rchild:
#                 self.rchild.search(val)
#             else:
#                 print("The value not founded in the BST")



#     def min(self):
#         current = self
#         while current.lchild:
#             current = current.lchild
#         print("The min value is : ", current.key)



#     def max(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("The max value is: ", current.key)



#     def closet(self, root, val):
#         clo = float('inf')
#         while root:
#             if abs(root.key - val)<abs(clo - val):
#                 clo = self.key
#             if root.key > val:
#                 root = root.lchild
#             elif root.key < val:
#                 root = root.rchild
#             else:
#                 break
#         print("The closet number is : ", clo)




#     def delete(self, val, curr):
#         if self.key is None:
#             print("The node is empty")
#             return
#         if self.key>val:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(val, curr)
#             else:
#                 print("The value is not founde in the list")
#         elif self.key<val:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(val, curr)
#             else:
#                 print("The value is not founded in the list")
#         else:
#             if self.rchild is None:
#                 temp = self.rchild
#                 if val == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
            
#             if self.lchild is None:
#                 temp = self.rchild
#                 if curr == val:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key, curr)
#         return self
    


#     # def is_BST(self, root, min = float('-inf'), max = float('inf')):
#     #     if root is None:
#     #         return True
#     #     if min<root.key<max:
#     #         return False
#     #     return(root.is_BST(root.lchild, min, root.key) and root.is_BST(root.rchild, root.key, max))
    
    
#     def is_bst(self, root, min_val = float("-inf"), max_val = float("inf")):
#         if root is None:
#             return True
        
#         if min_val<root.key<max_val:
#             return False
        
#         return(
#             root.is_bst(root.lchild, min_val, root.key) and root.is_bst(root.rchild, root.key, max_val)
#         )

    


#     def in_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         print(self.key)
#         if self.rchild:
#             self.rchild.in_order()
    



# def count(root):
#     if root is None:
#         return 0
#     return 1+count(root.lchild)+count(root.rchild)


# lt= [4,5,3,63,2,75,9863,78]
# root = BST(10)
# for i in lt:
#     root.insert(i)
# root.in_order()
# root.search(2)
# if root.is_bst(root):
#     print("This is Bst")
# else:
#     print("This is not a BST")

# if count(root)>1:
#     root.delete(10, root.key)
# else:
#     print("The BST is empty")

# root.in_order()


# def min_heap(arr, n, i):
#     largest = i
#     left = i*2+1
#     right = i*2-1


#     if left<n and arr[left]<arr[largest]:
#         largest = left
    
#     if right<n and arr[right]<arr[largest]:
#         largest = right

#     if i != largest:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         min_heap(arr, n, largest)


# list = [2,3,432,53,526,264,264,9]
# n = len(list)
# for i in list:
#     min_heap(list, n, i)
# print(list)



# class trie:

#     head = {}

#     def insert(self, word):
#         cr = self.head
#         for i in word:
#             if i not in cr:
#                 cr[i] = {}
#             cr = cr[i]
#         cr['*'] = True


#     def search(self, word):
#         cr = self.head
#         for i in word:
#             if i not in word:
#                 print("The value not founded in the trie")
#                 return
#             cr = cr[i]
#         if '*' in cr:
#             print("The value is founde in trie")
#         else:
#             print("The value not founde in the trie")




# t = trie()
# t.insert("akhil")
# t.insert("amal")
# t.insert("roshan")
# t.search("amal")



# class BST:
#     def __init__(self, data):
#         self.key = data
#         self.lchild = None
#         self.rchild = None

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             self.key = data
#             return
#         if self.key>data:
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
#             print("The value presnted in the BST")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value not presented in the BST")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The value not presented in the BST")



#     def min(self):
#         current =  self
#         while current.lchild:
#             current = current.lchild
#         print("The min value is : ", current.key)


#     def max(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("The max value is : ", current.key)


#     def pre_order(self):
#         print(self.key)
#         if self.lchild:
#             self.lchild.pre_order()
#         if self.rchild:
#             self.rchild.pre_order()



#     def in_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         print(self.key)
#         if self.rchild:
#             if self.rchild:
#                 self.rchild.in_order()


#     def post_order(self):
#         if self.lchild:
#             self.lchild.post_order()
#         if self.rchild:
#             self.rchild.post_order()
#         print(self.key)



#     def closet(self, root, val):
#         clo = float('inf')
#         while root:
#             if abs(root.key - val)<abs(clo - val):
#                 clo = root.key
#             if root.key>val:
#                 root = root.lchild
#             elif root.key<val:
#                 root = root.rchild
#             else:
#                 break
#         print("The closet value is :", clo)



#     def is_bst(self, root, min = float("-inf"), max = float('inf')):
#         if root is None:
#             return True
#         if min>root.key or root.key>max:
#             return False
#         return(root.is_bst(root.lchild, min, root.key) and root.is_bst(root.rchild, root.key, max))
    

#     def delete(self, data, curr):
#         if self.key is None:
#             print("Empty BST")
#             return
#         if self.key>data:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data, curr)
#             else:
#                 print("The value not founded in the BST")
#         elif self.key<data:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data, curr)
#             else:
#                 print("The value not founde in the BST")
#         else:
#             if self.rchild is None:
#                 temp  = self.lchild
#                 if curr == data:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             if self.lchild is None:
#                 temp = self.rchild
#                 if curr == data:
#                     self.key = temp.key
#                     self.lchild =temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
            
#             node =  self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key, curr)
#         return self
    

#     def ancestor(self, val):
#         list = []
#         current = self
#         while current is not None:
#             list.append(current.key)
#             if val < current.key:
#                 current = current.lchild
#             elif val > current.key:
#                 current = current.rchild
#             else:
#                 break
#         if current is None:
#             print("The value not founde in the BST")
#         else:
#             print(list)





# def count(root):
#     if root is None:
#         return 0
#     else:
#         return 1+count(root.lchild)+count(root.rchild)


# list = [23, 75, 789, 12, 43, 867,1]  
# root = BST(10)
# for i in list:
#     root.insert(i)
# root.in_order()
# root.closet(root, 6)
# if count(root)>1:
#     root.delete(10, root.key)
# else:
#     print("Empty BST")
# root.in_order()
# root.max()
# root.min()

# if root.is_bst(root):
#     print("it is BST")
# else:
#     print("it is not BST")

# root.ancestor(43)


            

# def min_heap(list, n, i):
#     largest = i
#     left = 2*i+1
#     right = 2*i+2

#     if left<n and list[left]<list[largest]:
#         largest = left

#     if right<n and list[largest]>list[right]:
#         largest = right


#     if i != largest:
#         list[i], list[largest] = list[largest], list[i]
#         min_heap(list, n, largest)



# arr = [2, 66, 30, 5, 4, 9]
# n = len(arr)
# for i in range(n//2-1, -1, -1):
#     min_heap(arr, n, i)

# print(arr)


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

#         if "*" in cur:
#             print("The value founded in the trie")
#         else:
#             print("The value is not founded in the trie")



   




# t = trie()
# t.insert("amil")
# t.insert("amaljith")
# t.insert("akhil")
# t.insert("jaseel")
# t.insert("pranav")
# t.insert("nihal")
# t.search("akhil")
# t.display()





# def add_node(val):
#     global nodes_count
#     if val in graph:
#         print("The value already presented in the graph")
#         return
#     else:
#         nodes_count = nodes_count+1
#         nodes.append(val)
#         for i in graph:
#             i.append(0)
#         temp = []
#         for i in range(nodes_count):
#             temp.append(0)
#         graph.append(temp)



# def add_ed(val1, val2):
#     if val1 not in nodes:
#         print("The value not founded in the graph")
#     if val2 not in nodes:
#         print("The value not founded in the graph")
#         return
#     index1 = nodes.index(val1)
#     index2 = nodes.index(val2)
#     graph[index1][index2] = 1
#     graph[index2][index1] = 1



# def print_g():
#     for i in range(nodes_count):
#         for j in range(nodes_count):
#             print(graph[i][j], end=' ')
#         print()



# def delete_node(val):
#     global nodes_count
#     if val not in nodes:
#         print("The value is not founded in the ")
#         return
#     nodes_count = nodes_count-1
#     index1 = nodes.index(val)
#     nodes.pop(index1)
#     graph.pop(index1)
#     for i in graph:
#         i.pop(index1)

# def delete_ed(val1, val2):
#     if val1 not in nodes:
#         print("the value not founded in the graph")
#     elif val2 not in nodes:
#         print("The value not founded in the graph")
#     else:
#         index1 = nodes.index(val1)
#         index2 = nodes.index(val2)
#         graph[index1][index2] = 0
#         graph[index2][index1] = 0



    

    



# nodes = []
# graph = []
# nodes_count = 0

# for i in range(11):
#     add_node(i)
# add_ed(0,1)
# add_ed(2,5)
# add_ed(7,8)
# add_ed(8,9)
# delete_node(8)
# delete_ed(0,1)

# print_g()
# print(nodes)



# class BST:
#     def __init__(self, data):
#         self.key = data
#         self.lchild = None
#         self.rchild = None

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             self.key = data
#             return
#         if self.key>data:
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
#             print("The value is presented in the BST")
#             return
#         if self.key>data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value is not founded in the BST")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The values are not presneted in the BST")


#     def pre_order(self):
#         print(self.key, end=" ")
#         if self.lchild:
#             self.lchild.pre_order()
#         if self.rchild:
#             self.rchild.pre_order()


#     def in_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         print(self.key, end=" ")
#         if self.rchild:
#             self.rchild.in_order()


#     def post_order(self):
#         if self.lchild:
#             self.lchild.post_order()
#         if self.rchild:
#             self.rchild.post_order()
#         print(self.key, end=" ")




#     def delete(self, val, cur):
#         if self.key is None:
#             print("The BST is empty")
#             return
#         if self.key > val:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(val, cur)
#             else:
#                 print("The value is not presnted in the BST")
#         elif self.key < val:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(val, cur)
#             else:
#                 print("The value is not presnted in the BST")
#         else:
#             if self.lchild is None:
#                 temp = self.rchild
#                 if val == cur:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             if self.rchild is None:
#                 temp = self.lchild
#                 if val == cur:
#                     self.key= temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp  = None
#                     return
#                 self = None
#                 return temp
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key, cur)
#         return self
    

# def count(root):
#     if root is None:
#         return 0
#     else:
#         return 1+count(root.lchild)+count(root.rchild)
    
# list = [4353,64,45,678,1,78,87,32]
# root = BST(10)
# for i in list:
#     root.insert(i)
# print("pre_order")
# root.pre_order()
# print()
# print("in order")
# root.in_order()
# print()
# print("post order")
# root.post_order()
# print()
# root.search(64)
# if count(root):
#     root.delete(10, root.key)
# else:
#     print("The BST is empty")
# print("after deleteing root node")
# root.in_order()



# list = [23,2,24,53,13,643,754,21344]
# # for i in range(len(list)-1):
# #     for j in range(i, len(list)):
# #         if list[j]<list[i]:
# #             list[i], list[j] = list[j], list[i]

# # print(list)


# for i in range(len(list)):
#     for j in range(len(list)-1):
#         if list[j]>list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]

# print(list)