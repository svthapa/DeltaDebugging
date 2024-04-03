Main File:
- deltaDebugging.py is the main python file that outputs the result

Test Code Files:
- test1.py is the original get_sign code. 
- test2.py is the code after 8 changes are made
- Changes can be seen with diff test1.py test2.py 

Bug introduced and Changes Made:
- The bug is at line 17, where arr[i] = get_sign() is called, which gives error:
    IndexError: list assignment index out of range
- Other changes made are: created new array and added get_sign through a loop, added print functions.

Patches:
- patches are created using patch function 
- patches are from patch1 to patch8
- each patch contains line number and the change made from the original test1.py


How to Run the DeltaDebugging:
- The deltaDebugging.py takes input the original file and the 8 patch files.
- Input to cmd is as follows:
    python3 deltaDebugging.py test1.py patch1.patch patch2.patch patch3.patch patch4.patch patch5.patch patch6.patch patch7.patch patch8.patch 

- output is the minimum list of patch files that causes the bug.
- patches can be inputted in any order, the main file manages the ordering of the patch automatically.
- input must contain the original file and 8 patch files.


Thoughts, Findings, and Insights:
- The delta debugging is a recursive process (modification of binary search) to find 
    minimum set of patches that causes the bug.
- When using patches with line number and changes as input, I found it is a must to make sure
    the patches are ordered so the earlier line changes comes first when using patch function, 
    or else patching is not succesful.
- It is a nlogn algorithm, as I had to sort out of the patches first, then conduct the recursive search.


Running Configuration:

Step    Ci      Configuration     Test

1       C1       1 2 3 4          Fail
2       C2       1 2              Pass
3       C3           3 4          Fail
4       C4           3            Pass
5       C5             4          Fail

Patch 4 is found.