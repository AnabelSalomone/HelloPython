total = 0
input_num = 0
exception_msg = "Wrong type of data"
finish_msg = "done"


while True:
    input_num = input("Enter a number: ")
    try:
        total = total + float(input_num)
    except:
        if input_num == finish_msg:
            print(total)
            break
        else:
            print("Only write numbers!")