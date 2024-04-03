import sys
import subprocess
import difflib
from difflib import Differ
import re

def DD(original, changeSet, changeRemain):
    if len(changeSet) == 1:
        if applyRun(original, changeSet, changeRemain):
            return changeSet
        else:
            return []
    
    mid = len(changeSet) // 2

    if applyRun(original, changeSet[:mid], changeRemain):
        return DD(original, changeSet[:mid], changeRemain) 

    elif applyRun(original, changeSet[mid:], changeRemain):
        return DD(original, changeSet[mid:], changeRemain)
    
    lr1 = DD(original, changeSet[:mid], changeRemain + changeSet[mid:])

    lr2 = DD(original, changeSet[mid:], changeRemain + changeSet[:mid])

    return lr1 + lr2


def applyRun(original, changeSet, changeRemain):
    # if len(changeSet) == 1:
    #     subprocess.run(f'patch {original} {changeSet[0]} -o output.py', shell = True)

    # if (len(changeSet) >= 1 and len(changeRemain) == 0):
    #     changeSet.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    #     patch = mergeFiles(changeSet)
    #     #print(patch)
    #     subprocess.run(f'patch {original} {patch} -o output.py', shell = True)
    
    
    #if (len(changeRemain) != 0):
    totalChange = changeSet + changeRemain
    totalChange.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    patch = mergeFiles(totalChange)
    subprocess.run(f'patch {original} {patch} -o output.py', shell = True)

    out = subprocess.run('python3 output.py', shell = True)
    if out.returncode == 0:
        return False
    else:
        return True
    

def mergeFiles(fileSet):
    
    with open('mergePatch.patch', 'w') as file:
        for f in fileSet:
            with open(f, 'r') as infile:
                file.write(infile.read())
        file.write('\n')  
    return 'mergePatch.patch'
        


if __name__ == "__main__":
    original = sys.argv[1]
    changeSet = []
    for i in range(2,9):
        changeSet.append(sys.argv[i])

    print(DD(original, changeSet, []))



    # subprocess.run(f'patch {original} {changeSet[0]} -o output.py', shell = True)
    # out = subprocess.run('python3 output.py && echo "success"', shell = True)
    # if out.returncode == 0:
    #     print('true')
    # else:
    #     print('false')


    # with open(fpath_original,'r') as file1:
    #     file1_info = file1.readlines()
    # with open(fpath_change,'r') as file2:
    #     file2_info = file2.readlines()
   
    # diff = difflib.unified_diff(file1_info, file2_info, fromfile=fpath_original,
    #     tofile=fpath_change, lineterm='')
   
    # for lines in diff:
    #     print(lines)
    
