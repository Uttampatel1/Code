import datetime 

def datetime():
    return datetime.datetime.now()
    
def add_fun(client):
    if (client=='1'):
        exer_dite=int (input("Enter the number 1 for exercise and 2 for dite :\n"))
        add_item=input ("what do you want to add ?\n")
        if (exer_dite=='1'):
            with open ("uttam_exer.txt") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    item.write("%s"%item)
            print ("item successfully add")
        elif (client=='2'):
            exer_dite=int (input("Enter the number 1 for exercise and 2 for dite :\n"))
            add_item=input ("what do you want to add ?\n")
            if (exer_dite=='1'):
                with open ("uttam_exer.txt") as f:
                    add = [" [",getdate(),"] ",add_item,"\n"]
                    for item in add:
                        item.write("%s"%item)
                print ("item successfully add")
                    
                
                
    
    
    
client=int (input("enter the number 1 for uttam ,2 for ayush and 3 for dhruval :\n"))
add_retrieve=int (input("enter number 1 for add and 2 for retrieve:\n"))