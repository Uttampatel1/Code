try :
    num = int(input("Enter the number:\n"))

    table =[num*i for i in range(1,11)]
    print (table)
    
    with open ("tables.txt","a") as f:
        f.write(str(table))
        f.write("\n")
except Exception as e:
    print ("please check the number")
    
    