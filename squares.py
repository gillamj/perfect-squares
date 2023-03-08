from math import sqrt as sr

print("Pick a number to count up to. This will return all perfect square roots up to your number!")


def get_squares():
    x = input("Please enter your number here. If you do not wish to continue, please type \"end\":")
    z = 0
    if x == "end":
        print("Goodbye!")
        return
    try:
        y = float(x)
        while z <= y:
            if float(sr(z)) - int(sr(z)) == 0:
                print(str(int(sr(z))) + " is the perfect square root of " + str(z) + "!")
                z += 1
            else:
                z += 1
        return get_squares()
    except ValueError:
        print("The input was not a valid number.")
        return get_squares()


user_number = get_squares()



