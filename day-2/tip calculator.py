print("welcome to the tip calculator")
a=int(input("what was the total bill "))
b=int(input("how much tip would you like to give? 10,12or15 "))
c=int(input("how many people to split the bill?"))
print("each person should pay")
ans = ((b/100+1)*a)/c
print(round(ans, 2))