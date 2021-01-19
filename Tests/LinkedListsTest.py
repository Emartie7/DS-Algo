###############################################################################
# File Name:    LinkedListsTest.py
# Author:       Edward Martinez
# DCreated:     01-16-2021
# Description:  This file will execute a tests to verify the functionality and
#               robustness of the linked lists defined in LinkedLists.py
# Revision History:
#   Rev 0.0         Initial Commit
###############################################################################
import LinkedLists
TestResults     = []
TestFailCt      = 0
TestPassCt      = 0
####################### Test 1 ###########################
# Description: Create a singly linked list and verify entries
# Inputs:           [14 16 188 234 9 521]
# Expected Output:  [14 16 188 234 9 521]
Expected = [14, 16, 188, 234, 9, 521]
List1 = LinkedLists.LinkedList_Single_Def()
ListOut = None

for input in Expected:
    List1.append(input)
# print("Expected results: {}".format(Expected))
ListOut = List1.ReturnList(0)

if ListOut != Expected:
    print("\nTest Case 1 failed.")
    TestResults.append(0)
else:
    TestResults.append(1)

####################### Test 2 ###########################
# Description: Create a singly linked list and verify entries
# Inputs:           [1 2 3 4 ... 200]
# Expected Output:  [1 2 3 4 ....200]
Expected    = []
ListOut     = []
List2       = LinkedLists.LinkedList_Single_Def()
for input in range(1,200):
    Expected.append(input)
    List2.append(input)
ListOut = List2.ReturnList(0)

if ListOut != Expected:
    print("\nTest Case 2 failed.")
    TestResults.append(0)
else:
    TestResults.append(1)
        
####################### Test 3 ###########################
# Description: Verify prepend functionality for the linked list
# Inputs:           append [1 2 3 4 ... 100] , prepend "200", append "300", prepend "400"
# Expected Output:  [400 200 1 2 3 4 ....100 300]
Expected    = []
ListOut     = []
List3       = LinkedLists.LinkedList_Single_Def()
Expected.append(400)
Expected.append(200)
for input in range(1,100):
    Expected.append(input)
    List3.append(input)
Expected.append(300)

List3.prepend(200)
List3.append(300)
List3.prepend(400)
ListOut=List3.ReturnList(0)
if ListOut != Expected:
    print("\nTest Case 3 failed.")
    TestResults.append(0)
else:
    TestResults.append(1)
    
####################### Test 4 ###########################
# Description: Verify prepend functionality for the linked list
# Inputs:           Prepend int [1,100], append 200
# Expected Output:  [100 99 98 98 ... 2 1 200]
Expected    = []
ListOut     = []
List4       = LinkedLists.LinkedList_Single_Def()    

for input in range(1,100):
    List4.prepend(input)
for input in reversed(range(1,100)):
    Expected.append(input)
Expected.append(200)
List4.append(200)
ListOut = List4.ReturnList(0)

if ListOut != Expected:
    print("\nTest Case 4 failed.")
    TestResults.append(0)
else:
    TestResults.append(1)

####################### Test 5 ###########################
# Description: Verify insert functionality for the linked list
# Inputs:           Prepend int [1,100], append 200
# Expected Output:  [100 99 98 98 ... 2 1 200]
Expected    = []
ListOut     = []
List5       = LinkedLists.LinkedList_Single_Def()    

for input in range(1,100):
    List5.Insert(input, input-1)
    Expected.append(input)
    
ListOut = List5.ReturnList(0)

if ListOut != Expected:
    print("\nTest Case 5 failed.")
    TestResults.append(0)
else:
    TestResults.append(1)

####################### Test 6 ###########################
# Description: Verify insert functionality for the linked list
# Inputs:           [1 2 3 ... 100],insert 200 @ idx 33, insert 300 @ idx 77
# Expected Output:  [1 2 3 ... 32 33 200 34 ... 76 300 77 78 ... 100]
# Note: list is a zero-based index 
Expected    = []
ListOut     = []
List6       = LinkedLists.LinkedList_Single_Def()    

for input in range(1,100):
    List6.append(input)
    Expected.append(input)
    
Expected.insert(33, 200)
Expected.insert(77, 300)
Expected.insert(0, 400)

List6.Insert(200, 33)
List6.Insert(300, 77)
List6.Insert(400, 0)

ListOut = List6.ReturnList(0)

if ListOut != Expected:
    print("\nTest Case 6 failed.")
    TestResults.append(0)
else:
    TestResults.append(1)

####################### Test 7 ###########################
# Description: Verify remove functionality for the linked list
# Inputs:           [1 2 3 4 5 6],remove 200 2 4 6
# Expected Output:  [1 2 3 ... 32 33 200 34 ... 76 300 77 78 ... 100]
# Note: list is a zero-based index 
Expected    = [1, 3, 5]
ListOut     = []
List7       = LinkedLists.LinkedList_Single_Def()

for input in range (1,6):
    List7.append(input)

List7.remove(1)
List7.remove(2)
List7.remove(3)

ListOut = List7.ReturnList(0
                           )
if ListOut != Expected:
    print("\nTest Case 7 failed.")
    TestResults.append(0)
else:
    TestResults.append(1)
    
####################### Test 8 ###########################
# Description: Verify append, prepend, insert, and remove functionality for the linked list
# Inputs:           [1 3 5 8 13 21], prepend 34, remove 8, insert 55 @ idx 3
# Expected Output:  [1 2 3 ... 32 33 200 34 ... 76 300 77 78 ... 100]
# Note: list is a zero-based index 
Expected    = [34, 1, 3, 55, 5, 13, 21]
ListOut     = []
List8       = LinkedLists.LinkedList_Single_Def()

List8.append(1)
List8.append(3)
List8.append(5)
List8.append(8)
List8.append(13)
List8.append(21)
List8.prepend(34)
List8.remove(4)
List8.Insert(55,3)

ListOut = List8.ReturnList(0)

if ListOut != Expected:
    print("\nTest Case 8 failed.")
    TestResults.append(0)
else:
    TestResults.append(1)    
    
####################### Test 9 ###########################
# Description: Verify append, prepend, insert, and remove functionality for the linked list
# Inputs:           [1 3 5 8 13 21], prepend 34, remove 8, insert 55 @ idx 3, append 89, remove 13,
# Expected Output:  [1 2 3 ... 32 33 200 34 ... 76 300 77 78 ... 100]
# Note: list is a zero-based index 
Expected    = [34, 1, 3, 55, 144, 5, 21, 89,]
ListOut     = []
List9       = LinkedLists.LinkedList_Single_Def()
   
List9.append(1)
List9.append(3)
List9.append(5)
List9.append(8)
List9.append(13)
List9.append(21)
List9.prepend(34)
List9.remove(4)
List9.Insert(55,3)
List9.append(89)
List9.remove(5)
List9.Insert(144, 4)
    

ListOut = List9.ReturnList(0)

if ListOut != Expected:
    print("\nTest Case 9 failed.")
    TestResults.append(0)
else:
    TestResults.append(1) 

for Result in TestResults:
  if Result == 0:
      TestFailCt += 1
  else:
      TestPassCt += 1  
      
print("\nLinked List Test Results . . .")
print("\n{}/{} test cases passed. {}/{} tests failed".format(TestPassCt,len(TestResults),TestFailCt,len(TestResults)))
# print(TestResults)1