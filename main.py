def bubblesort_incr(numlist):
    for i in range(0,len(numlist)):
        for j in range(i,len(numlist)):
            if numlist[j] < numlist[i]:
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
    print(bubblesort_incr(nums))
