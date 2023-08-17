num = int(input("Enter a number to be multiplied: "))
start = int(input("Enter a starting point for the problem: "))
end = int(input("Enter an end point for the problem: "))

for mul in range(start, end):
    if mul == 6:
        print("we're done!")
        break
    print(num * mul)
    
    
    num = [10,20,30,40,50, "we're all done"]
    for numbers in num:
        print(numbers)
        