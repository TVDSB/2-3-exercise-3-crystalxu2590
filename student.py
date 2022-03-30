def main():
    #your code goes here
    usersnumber = int(input("Please enter a number:\n"))
    if usersnumber % 3 == 0 and usersnumber % 5 == 0:
        print("fizzbuzz")
    elif usersnumber % 3 == 0:
        print("fizz")
    elif usersnumber % 5 == 0:
        print("buzz")
    else:
        print(usersnumber)
    print("0")

if __name__ =='__main__':
    main()
