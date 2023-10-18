#program that formats 1,2,3 digit numbers into 3 digit format
def format_number(num):
    if num < 10:
        return f'00{num}'
    elif num < 100:
        return f'0{num}'
    else:
        return str(num)

numbers = [5, 23, 102, 7, 456]

for num in numbers:
    formatted_number = format_number(num)
    print(formatted_number)