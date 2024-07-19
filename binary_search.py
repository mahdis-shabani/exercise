def binary_search(char_list):
    char_list_2=[]
    char=input("enter:")
    counter=0

    ord_char=ord(char)
    for i in char_list:
        char_list_2.append(ord(i))
    lenght=int(len(char_list_2)/2)
    while ord_char!=char_list_2[lenght]:
        if ord_char>=char_list_2[lenght]:
                
                counter+=1
                char_list_2=char_list_2[lenght:]
                lenght=int(len(char_list_2)/2)
        else:
             counter+=1
             char_list_2=char_list_2[:lenght]
             lenght=int(len(char_list_2)/2)

             
    return counter                 
char_list=["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q"]
print(binary_search(char_list))




def binary_search(numbers_list):
    number_list_2=[]
    num=int(input("enter:"))
    counter=0
    lenght=int(len(numbers_list)/2)
    while num!=numbers_list[lenght]:
        if num>=numbers_list[lenght]:
                
                counter+=1
                number_list_2=numbers_list[lenght:]
                lenght=int(len(number_list_2)/2)
        else:
             counter+=1
             number_list_2=number_list_2[:lenght]
             lenght=int(len(number_list_2)/2)

             
    return counter                 
numbers_list=[1,5,7,8,12,14]
print(binary_search(numbers_list))

