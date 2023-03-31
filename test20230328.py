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

x=10
y=2
print(x+y) #12
print(x**y) #100




