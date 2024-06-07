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
#             self.key = data
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild  = BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)


#     def search(self, val):
#         if self.key is None:
#             print("The BST is None")
#             return
#         if self.key == val:
#             print("The value is presented in the BST")
#             return
#         if self.key > val:
#             if self.lchild:
#                 self.lchild.search(val)
#             else:
#                 print("The value is not presented in the BST")
#         else:
#             if self.rchild:
#                 self.rchild.search(val)
#             else:
#                 print("The value is not presented in the BST")



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

#     def delete(self, val, curr):
#         if self.key is None:
#             print("Empty BST")
#             return
#         if self.key > val:
#             if self.key > val:
#                 if self.lchild:
#                     self.lchild = self.lchild.delete(val, curr)
#                 else:
#                     print("The value is not founded in the BST")
#         elif self.key < val:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(val, curr)
#             else:
#                 print("The value is not founded in the BST")
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
#             while node.lchild :
#                 node  = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key,curr)
#         return self
        

# def count(root):
#     if root is None:
#         return 0
#     return 1+count(root.lchild)+count(root.rchild)


# bst = BST(10)
# bst.insert(29)
# bst.insert(12)
# bst.insert(54)
# bst.in_order()
# bst.search(12)
# if count(bst)>1:
#     bst.delete(10, bst.key)
# else:
#     print("Empty BST")
# bst.in_order()

# class trie:
#     head = {}
#     def insert(self, word):
#         cur = self.head
#         for i in word:
#             if i not in cur:
#                 cur[i]={}
#             cur = cur[i]
#         cur['*'] = True

#     def search(self, word):
#         cur = self.head

#         for i in word:
#             if i in cur:
#                 cur = cur[i]
#             else:
#                 print("The value is not founded in the trie")

#         if "*" in cur:
#             print("The value is founded in the trie")
#         else:
#             print("the value is not founde in the trie")


    


# t= trie()
# t.insert("akhil")
# t.insert("amal")
# t.insert("roshan")
# t.search("amal")


# def insert(val):
#     if val in graph:
#         print("The value is already in the graph")
#     else:
#         graph[val] = []



# def add_edge(val1, val2):
#     if val1 not in graph:
#         print(val1, 'Not presented in the graph')
#         return
#     elif val2 not in graph:
#         print(val2, "not presented in the graph")
#     else:
#         graph[val1].append(val2)
#         graph[val2].append(val1)


# def DFS(start, graph):
#     visited = []
#     stack=[]
#     stack.append(start)
#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             visited.append(current)
#             for i in graph[current]:
#                 stack.append(i)

#     return visited


# graph ={}



# insert('a')
# insert('b')
# insert('c')


# add_edge('a', 'b')
# add_edge('b', 'c')
# val = DFS('a',graph)
# print(val)


# list = [1,432,2,434,54,24,364,456,64]


# def sort(list, first, last):
#     pvot = list[first]
#     left = first+1
#     right = last

#     while True:
#         while left<=right and list[left]<=pvot:
#             left += 1

#         while left<=right and list[right]>=pvot:
#             right -= 1

#         if left > right:
#             break
#         list[left], list[right] = list[right], list[left]
#     list[first], list[right] = list[right], list[first]
#     return right


# def quick(list, first, last):
#     if first<last:
#         p = sort(list, first, last)
#         quick(list,first,p-1)
#         quick(list, p+1, last)



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

#         while i < len(left_list) and j < len(right_list):
#             if left_list[i]<right_list[j]:
#                 list[k]=left_list[i]
#                 k=k+1
#                 i=i+1
#             else:
#                 list[k] = right_list[j]
#                 j=j+1
#                 k=k+1

#         while i < len(left_list):
#             list[k] = left_list[i]
#             i=i+1
#             k=k+1

            
#         while j < len(right_list):
#             list[k] = right_list[j]
#             j =j+ 1
#             k =k+ 1



# list = [245,5,2335,5647,45,2,6,4364,5623,6,2,22,45]
# mer(list)
# print(list)


# def mer(list):
#     if len(list)>1:
#         mid = len(list)//2
#         left_list = list[mid:]
#         right_list = list[:mi
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

#         while(list[pos-1]>current and pos>0):
#             list[pos-1] = current
#             pos -= 1

#         list[pos] = current

# list=[1,23,4,546,686]
# ins(list)
# print(list)



        