# name="yanWen"
# print(name.upper())
# print(name.lower())

# tempDict={1:"yanwen", 2:"whatever", "idk":"wobuzhidao"}
# print(tempDict["idk"])

# tempDict1={2:"blue",4:"pink",8:"whatever8"}
# print(tempDict1[4])

# animalTuple=(4,2,"tiger","lion","giraffe","whateveranimal","tiger")
# print(animalTuple[3])
# print(animalTuple.count("tiger"))

# print(list(range(5)))

# a=[245,62,1]
# b=tempDict1
# c=[a,b]
# print(c)
# print(list(animalTuple))

# from collections import namedtuple
# a=namedtuple("yanwen","ade, chen")
# s=a("data", "python")
# print(s) #yanwen(ade='data', chen='python')

# from collections import deque
# a=["s","r","s","p","o"]
# d=deque(a)
# print(d) #deque(['s', 'r', 's', 'p', 'o'])
# d.appendleft("python")
# print(d) #deque(['python', 's', 'r', 's', 'p', 'o'])
# d.pop()
# print(d) #deque(['python', 's', 'r', 's', 'p'])
# d.popleft()
# print(d) #deque(['s', 'r', 's', 'p'])

# from collections import ChainMap
# a={1:"yanwen",2:"python"}
# b={3:"leetcode",4:"makeIt"}
# ab=ChainMap(a,b)
# print(ab) #ChainMap({1: 'yanwen', 2: 'python'}, {3: 'leetcode', 4: 'makeIt'})

# from collections import Counter
# a=[3,2,6,1,3,5,2,2,7,25,6,4,34,1,3]
# c=Counter(a)
# print(c) #Counter({3: 3, 2: 3, 6: 2, 1: 2, 5: 1, 7: 1, 25: 1, 4: 1, 34: 1})
# print(list(c.elements())) #[3, 3, 3, 2, 2, 2, 6, 6, 1, 1, 5, 7, 25, 4, 34] 
# print(c.most_common()) #(3, 3), (2, 3), (6, 2), (1, 2), (5, 1), (7, 1), (25, 1), (4, 1), (34, 1)]
# sub={2:1,6:1}
# print(c.subtract(sub)) #None
# print(c.most_common()) #[(3, 3), (2, 2), (1, 2), (6, 1), (5, 1), (7, 1), (25, 1), (4, 1), (34, 1)] 

# from collections import OrderedDict
# d=OrderedDict()
# d[1]="y"
# d[2]="a"
# d[3]="n"
# d[4]="w"
# d[5]="e"
# d[6]="n"

# print(d) #OrderedDict([(1, 'y'), (2, 'a'), (3, 'n'), (4, 'w'), (5, 'e'), (6, 'n')]) 
# print(d.keys()) #odict_keys([1, 2, 3, 4, 5, 6]) 

# from collections import defaultdict
# d=defaultdict(int)
# d[1]="yanwen"
# d[2]="python"
# d[3]="utube"
# d[4]="tictok"
# d[5]="idk"
# d[6]="shoptify"
# print(d[7]) #0

# from collections import UserDict
# from collections import UserList
# from collections import UserString

# a=[2,4,5]
# print(len(a)) #3
# a.append(4)
# print(a) #[2, 4, 5, 4]
# a.extend([2,5,7,9,3,6])
# print(a) #[2, 4, 5, 4, 2, 5, 7, 9, 3, 6]
# a.insert(2,8)
# print(a) #[2, 4, 8, 5, 4, 2, 5, 7, 9, 3, 6]
# a.pop()
# print(a) #[2, 4, 8, 5, 4, 2, 5, 7, 9, 3]
# a.pop(2)
# print(a) #[2, 4, 5, 4, 2, 5, 7, 9, 3]
# a.pop(-1)
# print(a) #[2, 4, 5, 4, 2, 5, 7, 9]
# a.remove(4)
# print(a) #[2, 5, 4, 2, 5, 7, 9]

# b=[1,2,3,4,5,6,7,8]
# c=[3,4,5,6,7,8,9]
# d=b+c
# print(d) #[1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8, 9]

# print(b[3:]) #[4, 5, 6, 7, 8]
# print(b[:3]) #[1, 2, 3]
# print(b[:-2]) #[1, 2, 3, 4, 5, 6]

# print(d[::-1]) #[9, 8, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 3, 2, 1]

# e=[1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8, 9]
# for x in e[:-3]:
#     print(x)
    
# temp=0
# while temp<e[-2]:
#     print(e[temp])
#     temp=temp+1

# tempDict={"yanwen":"001","Noran":"002","Shawn":"003"}
# tempDict1={"employer":{"yanwen":{"ID":"001","Salary":"20000"},
#                        "haha":{"ID":"002","Salary":"10000"}}}
# print(tempDict1)
# print(tempDict1.get("employer")) #{'Yanwen': {'ID': '001', 'Salary': '20000'}, 'Haha': {'ID': '002', 'Salary': '10000'}}
# for x,y in tempDict.items():
#     print(x,y)
#     '''
#     yanwen 001
#     Noran 002
#     Shawn 003
#     '''
# tempDict["yanwen"]="000"
# tempDict["chen"]="007"
# print(tempDict) #{'yanwen': '000', 'Noran': '002', 'Shawn': '003', 'chen': '007'}

# print(tempDict.pop("Noran")) #002
# print(tempDict.popitem()) #('chen', '007')

# import pandas as pd
# tempDict1={"employer":{"yanwen":{"ID":"001","Salary":"20000"},
#                         "haha":{"ID":"002","Salary":"10000"}}}

# df=pd.DataFrame(tempDict1["employer"])
# print(df)
# '''
#        yanwen   haha
# ID        001    002
# Salary  20000  10000
# '''

# x=10
# y=2
# print(x+y) #12
# print(x**y) #100

# list1=[10,20,30]
# list2=[10,20,30]
# list3=[10,50,30]

# print(list1 in list2)
# print(list1 not in list3)
# print("banana" in list1)
# print(list1 is list2)
# '''
# >>> print(list1 in list2)
# False
# >>> print(list1 not in list3)
# True
# >>> print("banana" in list1)
# False
# >>> print(list1 is list2)
# False
# '''

# print(10 & 12) #8
# '''
# 10: 1010
# 12: 1100
# 1010 & 1100 == 1000, only 1 and 1 will be 1, this is &
# so 1000 == 8 so it will print 8
# '''
# print(10 | 12) #14
# '''
# 10: 1010
# 12: 1100
# 1010 & 1100 == 1110, this is |
# so 1110 == 14 so it will print 14 
# '''

# print(10 >> 2) #2
# '''
# 10: 1010
# right shift 2 places: 0b10
# gonna be 2
# '''
# print(10 << 2) #40
# '''
# 10: 1010
# left shift 2 places: 101000
# '''

# '''
# bitwise operators:
# & AND, both of them are 1
# | OR, one of them is 1
# ^ XOR, if and only if one of the bits is 1
# ~ NOT, inverts all bits
# << Left shift, fill with 0 while shifting left
# >> Right shift, cut off the parts while shifting right
# '''

# count =0
# while count<9:
#     print("number: ",count)
#     count+=1

# print("the end")

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import LinearSegmentedColormap

# # Julia set function
# def julia(c, z, max_iter):
#     for n in range(max_iter):
#         if abs(z) > 2:
#             return n
#         z = z * z + c
#     return max_iter

# # Image size (pixels)
# width, height = 800, 800

# # Plot window (real and imaginary axis)
# re_min, re_max = -2, 2
# im_min, im_max = -2, 2

# # Maximum number of iterations
# max_iter = 256

# # Create an empty image
# image = np.zeros((height, width))

# # Julia set constant
# c = complex(-0.8, 0.156)

# # Generate Julia set fractal
# for y in range(height):
#     for x in range(width):
#         re = x * (re_max - re_min) / (width - 1) + re_min
#         im = y * (im_max - im_min) / (height - 1) + im_min
#         z = complex(re, im)
#         image[y, x] = julia(c, z, max_iter)

# # Create a custom pink colormap
# cmap = LinearSegmentedColormap.from_list("pink", ["black", "pink"])

# # Plot and display the fractal

# plt.imshow(image, cmap=cmap, extent=(re_min, re_max, im_min, im_max))
# plt.colorbar()
# plt.title("Julia Set Fractal")
# plt.show()

# n,m=0,"abc"
# n+=1

# if 
# elif 
# else

# and, or

# for i in range(5):
#     print(i) # 0 1 2 3 4
    
# for i in range(2,6):
#     print(i) # 2 3 4 5
    
# for i in range(5,1,-1):
#     print(i) # 5 4 3 2

# for i in range(5,1,-2):
#     print(i) # 5 3

# #// will go down
# print(5/2) #2.5
# print(5//2) #2
# print(-3/2) #-1.5
# print(-3//2) #-2
# print(int(-3//2)) #-2

# print(10%3) #1
# print(-10%3) #2

# import math
# print(math.floor(3/2))
# print(math.ceil(3/2))
# print(math.sqrt(3/2))
# print(math.pow(2,3))
# '''
# 1
# 2
# 1.224744871391589
# 8.0
# '''

# float("inf")
# float("-inf")

# import math
# print(math.pow(2,200))
# print(math.pow(2,200)<float("inf"))
# '''
# 1.6069380442589903e+60
# True
# '''

# arr=[1,2,3,9,3,8]
# print(arr)

# arr.append(4)
# print(arr)

# arr.pop()
# print(arr)

# arr.insert(1,7)
# print(arr)

# arr[0]=0
# arr[3]=0
# print(arr)

# '''
# [1, 2, 3, 9, 3, 8]
# [1, 2, 3, 9, 3, 8, 4]
# [1, 2, 3, 9, 3, 8]
# [1, 7, 2, 3, 9, 3, 8]
# [0, 7, 2, 0, 9, 3, 8]
# '''

# n=5
# arr=[1]*n
# print(arr) #[1, 1, 1, 1, 1]

# arr=[1,2,3]
# print(arr[-1]) #3
# print(arr[-2]) #2

# arr=[1,2,3,4]
# print(arr[1:3]) #[2, 3]

# a,b,c=[1,2,3]
# print(a,b,c) #1 2 3

# nums=[1,2,3]

# for i in range(len(nums)):
#     print(nums[i])

# for n in nums:
#     print(n)
    
# for i,n in enumerate(nums):
#     print(i,n)
# '''
# 1
# 2
# 3
# 1
# 2
# 3
# 0 1
# 1 2
# 2 3
# '''

# nums1=[1,3,5]
# nums2=[2,4,6]
# for n1, n2 in zip(nums1,nums2):
#     print(n1,n2)
# '''
# 1 2
# 3 4
# 5 6
# '''

# arr=[2,3,8,2,5,8,4,3,2,30]
# arr.sort()
# print(arr) # [2, 2, 2, 3, 3, 4, 5, 8, 8, 30]
# arr.sort(reverse=True)
# print(arr) #[30, 8, 8, 5, 4, 3, 3, 2, 2, 2]

# arr=["adelina","yanwen","alice","jane","lisa"]
# arr.sort()
# print(arr)
# # sort by length of string
# arr.sort(key=lambda x:len(x))
# print(arr)
# '''
# ['adelina', 'alice', 'jane', 'lisa', 'yanwen']
# ['jane', 'lisa', 'alice', 'yanwen', 'adelina']
# '''

# arr=[i for i in range(5)]
# print(arr) #[0, 1, 2, 3, 4]
# arr=[i+i for i in range(5)]
# print(arr) #[0, 2, 4, 6, 8]
# #then each array will be unique, different from arr=[[0]*4]*4, that case cannot change individually
# arr=[[0]*4 for i in range(4)]
# print(arr) #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# strings=["ab","cd","ef"]
# print("".join(strings)) #abcdef

# from collections import deque
# queue=deque()
# queue.append(1)
# queue.append(2)
# print(queue)

# queue.popleft()
# print(queue)

# queue.appendleft(1)
# print(queue)

# queue.pop()
# print(queue)

# '''
# deque([1, 2])
# deque([2])
# deque([1, 2])
# deque([1])
# '''

# #hashset
# mySet=set()
# mySet.add(1)
# mySet.add(2)
# print(mySet)
# print(len(mySet))
# print(1 in mySet)
# print(2 in mySet)
# print(3 in mySet)
# mySet.remove(2)
# print(2 in mySet)
# '''
# {1, 2}
# 2
# True
# True
# False
# False
# '''

# #hashmap (ada dict)
# myMap={}
# myMap["alice"]=88
# myMap["Bob"]=66
# print(myMap)
# print(len(myMap))

# myMap["alice"]=80
# print(myMap)

# print("alice" in myMap)
# myMap.pop("alice")
# print("alice" in myMap)
# myMap={"alice":90,"bob":70}
# print(myMap)
# '''
# {'alice': 88, 'Bob': 66}
# 2
# {'alice': 80, 'Bob': 66}
# True
# False
# {'alice': 90, 'bob': 70}
# '''

# myMap={i:2*i for i in range(3)}
# print(myMap) #{0: 0, 1: 2, 2: 4}

# myMap={"alice":90,"bob":70}
# for key in myMap:
#     print(key,myMap[key])

# for val in myMap.values():
#     print(val)
    
# for key,val in myMap.items():
#     print(key,val)

# '''
# alice 90
# bob 70
# 90
# 70
# alice 90
# bob 70
# '''

# #tuple: like array but immutable
# tup=(1,2,3)
# print(tup) #(1,2,3)
# print(tup[0]) #1
# print(tup[-1]) #3
# tup[0]=0 #TypeError: 'tuple' object does not support item assignment

# #can be sed as key for hash map/set
# myMap={(1,2):3}
# print(myMap[(1,2)]) #3

# mySet=set()
# mySet.add((1,2))
# print((1,2) in mySet) #True

# import heapq
# minHeap=[]
# heapq.heappush(minHeap,3)
# heapq.heappush(minHeap,2)
# heapq.heappush(minHeap,4)
# print(minHeap) #[2,3,4]
# print(minHeap[0]) #2

# while len(minHeap):
#     print(heapq.heappop(minHeap))
#     '''
#     2
#     3
#     4
#     '''

# import heapq
# maxHeap = []
# heapq.heappush(maxHeap,-3)
# print(maxHeap) #[-3]
# heapq.heappush(maxHeap,-2)
# print(maxHeap) #[-3, -2]
# heapq.heappush(maxHeap,-4)
# print(maxHeap) #[-4, -2, -3]

# print(-1*maxHeap[0]) #4

# while len(maxHeap):
#     print(-1*heapq.heappop(maxHeap))
# '''
# 4
# 3
# 2
# '''

# def myFun(n,m):
#     return n*m
# print(myFun(3,7))

# def double(arr,val):
#     def helper():
#         for i,n in enumerate(arr):
#             arr[i]*=2
#         nonlocal val
#         val *=2
#     helper()
#     print(arr,val)

# nums=[1,2]
# val=3
# print(double(nums,val))  

# class MyClass:
#     def __init__(self,nums):
#         self.nums=nums
#         self.size=len(nums)
        
#     def getLength(self):
#         return self.size
    
#     def getDoubleLength(self):
#         return 2*self.getLength() 

