# сортировка возрастание
def bubblesort_incr(numlist):
    for i in range(0,len(numlist)):
        for j in range(i,len(numlist)):
            if numlist[j] < numlist[i]:
                temp = numlist[j]
                numlist[j] = numlist[i]
                numlist[i] = temp
    return numlist

# сортировка убывание
def bubblesort_decr(numlist):
    for i in range(0,len(numlist)):
        for j in range(i,len(numlist)):
            if numlist[j] > numlist[i]:
                temp = numlist[j]
                numlist[j] = numlist[i]
                numlist[i] = temp
    return numlist

if __name__ == '__main__':
    print('enter a quantity of numbers')
    n = int(input())
    nums = []
    print('enter all numbers')
    if n <= 0 :
        print('no numbers - no sorting')
    for i in range(0,n):
        print(f'number {i} is ',end="")
        number = float(input())
        nums.append(number)
    print('choose a mode of sorting (incrementing - incr, decrementing - decr)')
    print(f'mode is ', end="")
    mode = str(input())
    if mode.lower() == 'incr':
        print(bubblesort_incr(nums))
    elif mode.lower() == 'decr':
        print(bubblesort_decr(nums))
    else:
        print('the wrong mode')