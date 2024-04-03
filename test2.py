import sys
def get_sign(x):
  if (x == 0):
    return 0
  if (x < 0):
    return -1
  else:
    return 1

if __name__ == "__main__":
    testInteger = 4
    print('integer is: ', testInteger)
    print('\nSign of integer is: ')
    print(get_sign(testInteger))
    arr = []
    for i in range(0, testInteger):
      arr[i] = get_sign(i)
    arr2 = []
    for i in range(0, testInteger):
      arr2.append(get_sign(i))
    print('the')
    print('end')
    print('.')
    sys.exit()