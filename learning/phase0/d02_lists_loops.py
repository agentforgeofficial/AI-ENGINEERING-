# # Exercise 01:
# student_marks = [22,84,66,36,48]
# for marks in student_marks:
#     print (marks)
# student_marks.append(58)
# student_marks.remove(22)
# student_marks.sort()
# print(student_marks[::4])

# above_50 = [student_marks for student_marks in student_marks if student_marks>50]
# print(above_50)

# # Exercise 02:
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(list[5:15])
# even = [even for even in list if even % 2 == 0]
# print(even)
# squared = [squared*squared for squared in list ]
# print(squared)

# total=0
# for sum in squared:
#     total+=sum
# print(total)

# while True:
#     x= int(input("Enter the number: "))
#     if x==0:
#         break
shopping_list=[]
while True:
    
    print("Supported commands: add, remove, show, exit")
    i = input("Enter a command: ")
    final_input = i.lower()
    
    def add_item():
        x = input("Enter the item to add: ")
        shopping_list.append(x)
        return (f"{x} is added to list.")
    
    def remove_item():
        r = input("Enter the item to remove: ")
        if r in shopping_list:
            shopping_list.remove(r)
            return (f"{r} is removed from list.")
        else:
            return("Item doesnt exist.")
            
    if "add" in final_input:
        print(add_item())
    elif "remove" in final_input:
        print(remove_item())
    elif "show" in final_input:
        print (f"Total number of items: {len(shopping_list)}")
        for item in shopping_list:
            print (item)
    elif "exit" in final_input:
        break
    else:
        print("Unknown command")
    
    


    