# 12 question
def defsum(n):
    sum=0;
    while n:
        sum+=n%10
        n=n//10
    print (sum)
num=int(input("enter the number"))
defsum(num)
