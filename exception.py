try:
    num2 = int(input("Enter the num2:"))
    num1 = int(input("Enter the num1:"))
    print(num1**num2)
    print(num1/num2)
    print("sum is:"+num1+num2)
except ZeroDivisionError:
    print(f"num2 can't be zero...")
except ValueError:
    print(f"Please enter only numbers")
except Exception as e:
    print(f"Something went wrong")