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
    
for Result in TestResults:
    if Result == 0:
        TestFailCt += 1
    else:
        TestPassCt += 1
print("\nLinked List Test Results . . .")
print("\n{}/{} test cases passed. {}/{} tests failed".format(TestPassCt,len(TestResults),TestFailCt,len(TestResults)))
# print(TestResults)1