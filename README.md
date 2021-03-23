# DS-Algo
Source for Data Structures and Algorithms course work (Udemy)

********** Setup for data structures package installation (edit/dev) ***********
1. Clone repo to local directory  
    ex: User\Documents\DS-Algo\
2. Open terminal and create a virtualenv or activate an existing one where you
    are able to install dev packages in.
3. Within the now-active virtual environent, run the following command to install:  
   (yourvirtualenv) >> pip install -e \[PathtoclonedRepo]\DS-Algo  
      In the example directory from step 1, this command would be:  
          >> pip install -e \User\Documents\DS-Algo\

You may now reference the class definitions from the source files in ..\DS-Algo\Data Structures  
ex:  
from LinkedLists import LinkedList_Single_Def  
from HashTables import myHashTableDef  
myList = LinkedList_Single_Def(2)  
print(myList.head)  
testTable = myHashTableDef(15)  
