n = int(input("enter any number - "))
n = abs(n)
p = ["EVEN", "ODD"]
print("then given number is ",p[n%2])
# 2. positive or negative
if n > 0:
    print("the given number is positive")   
elif n < 0:
    print("the given number is negative")