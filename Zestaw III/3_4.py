while True:
    try:
        a = input("Write a number or stop to quit the program: ")

        if a.lower() == 'stop':
            break

        a = float(a)
        print(pow(a, 3))

    except ValueError:
        print("It is not a number!")
print("Thanks for using the program!")
