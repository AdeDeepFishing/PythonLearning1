#Coding Interview Preparation: Coursera, Meta
#Week 1
#The coding interview
'''
Types of interview:

Screening:
What is the role?

    What coding language does the company typically use?

    What is the interview process, what types of interviews will be conducted, and how many will there be?

    What is the nature of the project the proposed role is for?

    What is the typical makeup of the team?

    Who will be on the interview panel, and what is their role in the company?

Quiz:(The questions will be job-specific, so the content may vary. However, they will be questions that should be answered with concise, direct responses)

    How do you test for nulls in an array in a language of your choice?

    What is the space complexity for Quicksort?

    Which data structure would you use to store a list of keys and values?

    What is a collision in hashing?

    What is the syntax to select a column name using SQL?

    What testing processes are you familiar with?

Online coding assignment: LeetCode

The technical interview: will present you with a challenging problem and give you a brief period to solve it. It is always best to discuss your thoughts aloud as you engage with the challenge. these interviews are designed to demonstrate your problem-solving skills.

    How would you explain technology X to a non-technical person?

    What is your favorite technology and why?

    What databases have you worked with? 

    Tell me about a technical challenge you have overcome in a project. 

    What projects have you worked on in your spare time?

Top tips:

    Conduct your research before every interview and review each one on completion. Most companies are happy to provide feedback after your interview, so always ask for this and use the points made as a starting point to be better prepared for the following interview. Remember, practice makes perfect.


'''

'''
Communication

Clearly convey a concept

Communicate why you are suitable for the role

verbally & non-verbally

STAR method

    situation: project & challenges faced
    
    task: ur responsibilities & assignments
    
    action: rectify/address the challenges
    
    result: results/outcomes of the actions
    
'''

'''
pseudocode

    demonstrating ur ability to reason out a problem
    
    help u focus on the solution more

'''

'''
interview tips

prepare for common questions:

    Tell me about yourself.

    Why do you feel that they should hire you?

    What are your major strengths?

    Or, what are your major weaknesses?

    What pay are you expecting?

    How do your previous experiences make you suitable for this role?

    What do your friends say about you?

    Why do you want this role?

    How have you dealt with conflict in the past?
    
Dress well

Behave well (demeanor)

Virtual Interview: Find a quiet place

'''

'''
test ur solution

Take home:

    Integration test
    
    functional test
    
    regression test

Coding Interview:

    readability
    
    clear outcome: it should run as expected
    
    automation: run quickly
    
    
'''
#Intro to CS
'''
binary 

1001001 73

boolean

1true 0false

A 0100 0001
B 0100 0010
. 0010 1110
: 0011 1010

'''

'''
!x
x&&y
x||y
x^y #XOR(x,y)=1 if x and y r diff, =0 otherwise

'''

'''
memory:infos & instructions

    cache memory
    
    main memory
    
    secondary memory

RAM: read access memory

ROM: read only memory; programmable

volatile: memory lost if power is lost

non-volatile

transfer rate

'''

'''
time complexity

O(1)-constant time

    print("Yo")

O(n)-linear time

    for i in range()

O(log n)-binary search

    #猜数字，100，50，25，13，。。。

O(n^2)

    for i in range():
    
        for k in range():

in the graph: algorithm time complexity, As you can see, the best time to aim for is O(1); O(log n) is still excellent. O(n) is ok and O(n^2) is not great. 

'''

'''
space complexity

    Auxiliary space refers to the extra space or the temporary space used by an algorithm

    space complexity == input space + auxiliary space
'''

#Week 2
#Basic Data Structures

'''
basic data structures
    
    mutable, immutable
    
        u can or cannot change a string after it has been created.
    
        in python is immutable
        
        reduce memory consumption, immutable points all to the same location
    
    linear, non-linear(tree, graph)
'''

'''
strings

    \ gonna make sure the words will still be in ""
    
    e.g.: "yanwen says \"dont worry, we will make it\" to herself."

integers

booleans

arrays

objects

'''

'''
list & set

    list: ordered, mutable, duplicates
    
        linked list: each element points to the next one
    
    set: unordered, mutable, no duplicates
    
        hashing function: hash(key) = value
        
        O(1) to find an element in a set
    
    tuple: ordered, immutable, duplicates
'''

'''
stack & queue

    lifo: last in first out

    stack: LIFO, push, pop, peek(top), search, isEmpty, using in deck
    
    queue: FIFO, enqueue, dequeue
'''