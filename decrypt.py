def decrypt(text):
    pointer = 0
    result=''
    counter = 3
    while pointer < len(text):
        num = int(text[pointer:pointer+counter])
        value=0
        if num % 2 == 0:
            value = int(num /4)
        else:
            value = int(num /5)

        result += chr(value)
        pointer += counter
    return result


print(decrypt('245200255208265216275224285'))