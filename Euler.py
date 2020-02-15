#g18m6734
# This is my solution to Even Fibonacci numbers
# Greatest solution ever
def fib(): # For creating the fibonacci sequence
    nums = [1]
    num1 = 1
    num2 = 1
    num3 = 0
    while nums[-1] < 4000000:
        num3 = num1 + num2
        nums.append(num3)
        num1 = num2
        num2 = num3
    return nums
def even(alist): # finding the even numbers 
    cnt = 0
    data = []
    while cnt != len(alist):
        if (alist[cnt]%2) == 0:
            data.append(alist[cnt])
        cnt += 1
    return data
def add(alist): # adds all the even numbers 
    cnt = 0
    for i in alist:
        cnt += i
    return cnt
def main(): # main function for calling the other ones 
    dat = fib()
    get = even(dat)
    a = add(get)
    print (a)
main()