try :
    num = float(input("Enter the SGPA Number:\n"))
    if num<=10:
         result = (num*10)-7.5
         print (f"🥳 your percentage is = {result}%")
    else :
        print ("please Enter lower then 10 SGPA Number!")
except Exception as e :
    print ("🤖check the number! ")
    print (e)