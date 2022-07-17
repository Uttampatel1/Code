# Health Management System
client_list = {1:"uttam", 2:"ayush", 3:"dhruv"}
lock_list = {1:"Exercise", 2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("\nSelect Client Name:\n")
    for key, value in client_list.items():
        print("Press", key, "for", value)
    client_name = int(input())
        
    print("Selected Client :", client_list[client_name],"\n")

    print("Press 1 for add")
    print("Press 2 for Retrieve")
    op = int(input())

    if op==1:
        for key, value in lock_list.items():
            print("Press", key, "to add ", value)
        lock_name =  int(input())
        print("Selected Job :", lock_list[lock_name],"\n")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'
        while(k != "n"):
            print("Enter", lock_list[lock_name])
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:\n")
            continue
        f.close()
    elif op == 2:
        for key, value in lock_list.items():
            print("Press", key, "to retrieve", value)
        lock_name =  int(input())
        print(client_list[client_name], "-", lock_list[lock_name], "Report :","\n", end="")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", )
        contents = f.readlines()
        for line in contents:
            print(line,end="") 
        f.close() 
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("\n🤖Wrong Input🤯 !!!")
    
