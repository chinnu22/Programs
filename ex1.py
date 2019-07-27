def cast_vote(age):
    assert age>=18,f"Age shouldn't be < 18,it was:{age}"
    print("Thank you for voting......")
try:
    age = int(input("Enter the age:"))
    cast_vote(age)
except AssertionError as a:
    print(a)
else:
    print("Thank you for entering a valid age.........")
finally:
    print("End.......")