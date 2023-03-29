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

from collections import ChainMap
a={1:"yanwen",2:"python"}
b={3:"leetcode",4:"makeIt"}
ab=ChainMap(a,b)
print(ab) #ChainMap({1: 'yanwen', 2: 'python'}, {3: 'leetcode', 4: 'makeIt'})