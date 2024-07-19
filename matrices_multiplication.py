first_matric=[[1,2,3,10],[4,1,10,5],[11,7,4,2]]
len_first_matric=len(first_matric)

for number in first_matric:
    len_number=len(number)
    len_numbers=[]
    len_numbers.append(len_number)

second_matric=[[1,4,9],[14,7,1],[2,9,14],[8,3,3]]
len_second_matric=len(second_matric)

new_matric=[]
new_matric_2=[]
sum=0
for v in len_numbers:

    if len_number==len_second_matric:
        for index,item in enumerate(first_matric):
            
            counter=0
            while counter<len(second_matric)-1:
                for i,num in enumerate(item):
                    sum=sum+num*second_matric[i][counter]
                new_matric_2.append(sum)
                sum=0
                counter+=1
                
            if len(new_matric_2)==len_first_matric:
                new_matric.append(new_matric_2)
                new_matric_2=[]

        print(new_matric)

    else:
        print("I'm sorry, but these two matrices cannot be multipilied")
        exit()
                

      



    
  

            
    


   


         


            

           
