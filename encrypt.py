def encrypt(text):
    pointer = 0
    result = ''
    counter= 1
    odd_number = 4
    even_number = 5
    while pointer < len(text):
        if ord(text[pointer]) % 2 == 0:
            result += str(ord(text[pointer])*odd_number)
        else:
            result += str(ord(text[pointer])*even_number)
        pointer += counter
    return result
 

print(encrypt('123456789'))