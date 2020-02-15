
'''
*****17t4564****
Finding the sum of all the multiples of 3 or 5 below 1000
'''

def main():
    prime = 0 
    for i in range(0,1000):
        if i%3==0 or i%5==0:
            prime+=i
    print (prime)
    
#When the main function is executed, it adds all the numbers (from 0 to 1000) that are divisible by either 3 or 5 and then prints out the total sum.

main()
