try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as e:
    print("An error has been encountered:" + e)