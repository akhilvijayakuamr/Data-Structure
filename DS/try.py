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
#             print("The value is founded in the BST")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("The value is not founded in the BST")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("The value is not founded in the BST")



#     def min(self):
#         cur = self
#         while cur.lchild:
#             cur  = cur.lchild
#         print("The minimum value is : ", cur.lchild)
    

#     def max(self):
#         cur = self
#         while cur.rchild:
#             cur  = cur.rchild
#         print("The max value is : ", cur.rchild)


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



#     def  closet(self, root, val):
#         clo = float('inf')
#         while root:
#             if abs(root.key -  val)< abs(clo - val):
#                 clo =root.key
#             if root.key > val:
#                 root = root.lchild

#             elif root.key < val:
#                 root = root.rchild

#             else:
#                 break
#         print("The closet value is : ", clo)
    
#     def delete(self, val, cur):
#         if self.key is None:
#             print("Empty BST")
#             return
#         if self.key > val:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(val, cur)
#             else:
#                 print("The val not founded in the BST")

#         elif self.key < val:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(val, cur)
#             else:
#                 print("The value is not founded in the BST")


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
#             self.rchild = self.rchild.delete(node.key, cur)
#         return self
    

# def is_bst(root, min = float('-inf'), max = float('inf')):
#     if root is None:
#         return True
#     if min > root.key or max < root.key:
#         return False
    
#     return(
#         is_bst(root.lchild, min, root.key) and is_bst(root.rchild, root.key, max)
#     )


# def count(root):
#     if root is None:
#         return 0
#     else:
#         return 1+count(root.lchild)+count(root.rchild)
    


# root =  BST(10)
# list = [34,64,75,2,46,6754,25,6786,785,232]
# for i in list:
#     root.insert(i)

# root.in_order()

# root.search(2)

# if count(root)>1:
#     root.delete(10, root.key)
# else:
#     print("Empty BST")

# root.in_order()

# if is_bst:
#     print("This is BST")
# else:
#     print("This is not BST")

# root.closet(root, 80)



# def min_heap(arr, n, i):
#     largest = i
#     left = i*2+1
#     right = i*2+2

#     if left<n and arr[left]<arr[largest]:
#         largest = left
#     if right<n and arr[right]<arr[largest]:
#         largest=right
#     if i != largest:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         min_heap(arr, n, largest)


# list = [12,3,53,754,1,546,865]
# n = len(list)
# for i in range(n//2-1, -1, -1):
#     min_heap(list, n, i)
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
#                 print("The value not founded in the Trie")
#                 return
#             cur  = cur[i]
#         if '*' in cur:
#             print("The value founded in the trie")
#         else:
#             print("The value not founded in the trie")


#     def pr(self):
#         self.prinn(self.head, '')

#     def prinn(self , head, prefix):
#         for char, child in head.items():
#             if '*' in char:
#                 print(prefix)
#             else:
#                 self.prinn(child, prefix+char)
        

# t = trie()
# list = ['amal', 'amaljith', 'anu', 'ajith']
# for i in list:
#     t.insert(i)

# t.search('amal')
# t.pr()



