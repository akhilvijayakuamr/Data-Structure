# class BST:
#     def __init__(self, key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None


# b1 = BST(10)
# print(b1.key)
# print(b1.lchild)
# print(b1.rchild)
# b1.lchild = BST(20)
# print(b1.lchild.key)
# print(b1.lchild.lchild)
# print(b1.lchild.rchild)



# class BST:
#     def __init__(self, key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             return
#         if self.key > data:
#             if self.lchild :
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = BST(data)

#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)

# root = BST(10)
# list = [2,32,42,5,2,4,242,4,12]
# for i in list:
#     root.insert(i)



# class BST:
#     def __init__(self, key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None


#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
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
#             print("The node is founded ")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The node is not founded")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The data is not founded")

#     def pre_order(self):
#         print(self.key, end=" ")
#         if self.lchild:
#             self.lchild.pre_order()
#         if self.rchild:
#             self.rchild.pre_order()



#     def in_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         print(self.key, end=' ')
#         if self.rchild:
#             self.rchild.in_order()

#     def post_order(self):
#         if self.lchild:
#             self.lchild.post_order()
#         if self.rchild:
#             self.rchild.post_order()
#         print(self.key, end=' ')


#     def delete(self, data):
#         if self.key is None:
#             print("Tree is empty")
#             return
#         if data < self.key:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data)
#             else:
#                 print("The value is not founded ")

#         elif data > self.key:
#             if self.rchild:
#                 self.rchild  = self.rchild.delete()
#             else:
#                 print("The value is not founded")

#         else:
#             if self.lchild is None:
#                 temp = self.rchild
#                 self = None
#                 return temp
#             if self.rchild  is None:    
#                 temp = self.lchild
#                 self = None
#                 return temp
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key)
#             return self






# root = BST(10)
# list = [2,3,42,5,6,678,3,32,6,7]
# for i in list:
#     root.insert(i)

# root.search(100)

# print("PreOrder")
# root.pre_order()
# print()
# print("Inorder")
# root.in_order()
# print()
# print("Postorder")
# root.post_order()

# class BTS:
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
#                 self.lchild = BTS(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BTS(data)


#     def search(self, data):
#         if self.key == data:
#             print("The value is founded in the list ")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value is not founded in the list")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("THe value is not founded in the list")




#     def pre_order(self):
#         print(self.data, end=' ')
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


#     def search(self,val):
#         if self.key == val:
#             print("The value is founded")
#             return
#         if self.key > val:
#             if self.lchild:
#                 self.lchild.search(val)
#             else:
#                 print("The value is not founded in the tree")
#         else:
#             if self.rchild:
#                 self.rchild.search(val)
#             else:
#                 print("The value is not founded in the tree")



#     def pre_order(self):
#         print(self.key)
#         if self.lchild:
#             self.lchild.pre_order()
#         if self.rchild:
#             self.rchild.pre_order()



#     def inn_order(self):
#         if self.lchild:
#             self.lchild.inn_order()
#         print(self.key)
#         if self.rchild:
#             self.rchild.inn_order()



#     def post_order(self):
#         if self.lchild:
#             self.lchild.post_order()
#         if self.rchild:
#             self.rchild.post_order()
#         print(self.key)
        


#     def delete(self, val, curr):
#         if self.key is None:
#             print("Empty tree")
#             return
#         if self.key > val:
#             if self.lchild:
#                 self.lchild=self.lchild.delete(val, curr)
#             else:
#                 print("The value is not founded")

#         elif self.key<val:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(val, curr)
#             else:
#                 print("The value is not founded")

#         else:
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
            
#             node = self.rchild

#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key, curr)
#         return self
    



#     def min(self):
#         current =self
#         while current.lchild:
#             current = current.lchild

#         print("The min value is ", current.key)
        

#     def max(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("The max value is ", current.key)
      

# def count(node):
#     if node is None:
#         return 0
#     return 1+count(node.lchild)+count(node.rchild)




# b = BST(15)
# list = [1,2,3,4]
# for i  in list:
#     b.insert(i)


# if count(b)>1:
#     b.delete(15, b.key)
# else:
#     print("The tree is empty ")


# b.pre_order()
# b.inn_order()
# b.post_order()


# print()
# print()
# b.inn_order()
# print()
# print()
# b.max()
# b.min()

    



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
#             print("The value is founded")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value not founded")

#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The value is not founded ")



#     def min(self):
#         current = self
#         while current.lchild:
#             current = current.lchild
#         print("The min value is ", current.key)



#     def max(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("The max value is ", current.key)



#     def delete(self, data, curr):
#         if self.key is None:
#             print("Empty tree")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data, curr)
#             else:
#                 print("The value is not founde in the bst")
#         elif self.key < data:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data, curr)
#             else:
#                 print("The value is not founded in the bst ")
            
#         else:
#             if self.rchild is None:
#                 temp = self.lchild
#                 if data == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             if self.lchild is None:
#                 temp  = self.rchild
#                 if data == curr:
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
#             self.rchild = self.rchild.delete(data, curr)
#         return self
        



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
#             print("The value is founded ")
#             return
#         if self.key>data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value is not founded ")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The value is not founded")
    

#     def min(self):
#         current = self
#         while current.lchild:
#             current = current.lchild
#         print("The min value is ",current.key)


#     def max(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("Thr max value is founded ", current.key)



#     def pre_order(self):
#         print(self.key, end=' ')
#         if self.lchild:
#             self.lchild.pre_order()
#         if self.rchild:
#             self.rchild.pre_order()



#     def in_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         print(self.key, end=' ')

#         if self.rchild:
#             self.rchild.in_order()



#     def post_order(self):
#         if self.lchild:
#             self.lchild.in_order()
#         if self.rchild:
#             self.rchild.in_order()
#         print(self.key, end=' ')




#     def delete(self, data, curr):
#         if self.key is None:
#             print("Empty BST")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data, curr)
#             else:
#                 print("The value is founded in the list")
#         elif self.key < data:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data, curr)
#             else:
#                 print("The value is founde in the list")
#         else:
#             if self.rchild is None:
#                 temp = self.lchild
#                 if data == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             if self.lchild is None:
#                 temp = self.rchild
#                 if data == curr:
#                     self.key = temp.key
#                     self.rchild = temp.rchild
#                     self.lchild = temp.lchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(data, curr)
#         return self
    



#     # def find_closest_value(self, root, target):
#     #     closest = float('inf')  # Initialize with positive infinity
#     #     while root:
#     #         if abs(root.key - target) < abs(closest - target):
#     #             closest = root.key
#     #         if target < root.key:
#     #             root = root.lchild
#     #         elif target > root.key:
#     #             root = root.rchild
#     #         else:
#     #             break  # Target value found, no need to search further
#     #     return closest





#     def closet(self, root, tar):
#         cls = float('inf')
#         while root:
#             if abs(root.key - tar)<abs(cls - tar):
#                 cls = root.key
#             if tar < root.key:
#                 root = root.lchild
#             elif tar > root.key:
#                 root = root.rchild
#             else:
#                 break
#         return cls





# root = BST(10)
# list = [2,3,5]
# for i in list:
#     root.insert(i)


# root.post_order()
# print()
# root.search(6)

# def count(node):
#     if node is None:
#         return 0
#     else:
#         return 1+count(node.lchild)+count(node.rchild)
    

    
# if count(root)>1:
#     root.delete(10, root.key)
# else:
#     print("The tree is empty ")

# root.in_order()
# print()
# print(root.closet(root, 24))
    



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
#             print("The value is founded ")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value is not founded ")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The value is not founded")


#     def pre_order(self):
#         print(self.key, end=' ')
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
#         print(self.key, end=' ')



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




#     def closet(self, root, data):
#         clo = float('inf')
#         while root:
#             if abs(root.key - data)<abs(clo - data):
#                 clo = root.key

#             if data < root.key:
#                 root = root.lchild

#             elif data > root.key:
#                 root = root.rchild

#             else:
#                 break
#         print("The closet value is : ", clo)




#     def delete(self, data, curr):
#         if self.key is None:
#             print("The BST is empty")
#             return
#         if data < self.key:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data, curr)
#             else:
#                 print("The value is not in BST")

#         elif data > self.key:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data, curr)
#             else:
#                 print("The value is not founded ")

#         else:
#             if self.rchild is None:
#                 temp = self.lchild
#                 if data == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
            
#             if self.lchild is None:
#                 temp = self.rchild
#                 if data == curr:
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
    

# def isBST(root, min_value=float('-inf'), max_value=float('inf')):
#     if root is None:
#         return True

#     if not (min_value < root.key < max_value):
#         return False

#     return (
#     isBST(root.lchild, min_value, root.key) and
#     isBST(root.rchild, root.key, max_value)
#     )



# def count(node):
#     if node is None:
#         return 0
#     else:
#         return 1+count(node.lchild)+count(node.rchild)
    


# root = BST(1)
# list = [32,4,64,7,8,34]
# for i in list:
#     root.insert(i)

# root.in_order()
# print()
# root.search(8)
# root.closet(root, 20)
# root.max()
# root.min()
# if count(root)>1:
#     root.delete(4, root.key)
# else:
#     print("The tree is empty")
# root.in_order()
# print()
# if isBST(root):
#     print("The tree is a Binary Search Tree.")
# else:
#     print("The tree is not a Binary Search Tree.")







# import heapq
# heap = []
# heapq.heappush(heap, 2)
# heapq.heappush(heap, 56)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 8)
# print(heap)
# heapq.heappop(heap)
# print(heap)