# TASK WAS TO DETERMINE WHETHER THE CODE BELOW IS CORRECT AND WILL EXECUTE PROPERLY IN PYTHON

# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# for i in "axby": if ord(i) < 100: print (i)
# for i in "axby": print (ord(i) if ord(i) < 100 else i)

# IT IS NOT A CORRECT PYTHON CODE!

# one line multiple declarations are allowed if written as so:
# PYTHON DOES NOT REQUIRE SEMICOLONS AT THE END OF THE LINE
# IF statements do not require brackets
# python if and for statements require a new line after the colon, with a tab or 4 spaces
# CORRECT CODE:
x, y = 2, 3
if x > y:
    result = x
else:
    result = y
print(result)
for i in "axby":
    if ord(i) < 100:
        print(i)
for i in "axby":
    print(ord(i) if ord(i) < 100 else i)
