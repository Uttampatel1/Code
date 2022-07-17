# Health Management System
# Total 6 Files, 3 For exercise and 3 For for diet
# 3 clients - Harry, Rohan and Hammad
# write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client

import datetime

def getdate():
    return datetime.datetime.now()

def add_func(client):
    if client == "1":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("uttam_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("uttam_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")          
    elif client == "2":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("ayush_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("ayush_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")         
    elif client == "3":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("dhruv_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("dhruv_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added") 
            
            
def retrive_func(client):
    if client == "1":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("uttam_exer.txt",) as f:
                    for i in (f.readlines()) :
                       print (i)
                       
            except:
                print("Items does not retrieve. Please add some items in file")        
        elif exer_diet == "2":
            try:
                with open("uttam_diet.txt",) as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i) 
            except:
                print("Items does not retrieve. Please add some items in file")                
    elif client == "2":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("ayush_exer.txt",) as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
        elif exer_diet == "2":
            try:
                with open("ayush_diet.txt") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
    elif client == "3":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("dhruv_exer.txt") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
        elif exer_diet == "2":
            try:
                with open("dhruv_diet.txt") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")          

client = input("Enter number 1 for uttam, 2 for ayush and 3 for dhruv : ") 
add_retrieve = input("Enter number 1 for Add and 2 for Retrieve : ")

if add_retrieve == "1":
    add_func(client)
elif add_retrieve == "2":
    retrive_func(client)