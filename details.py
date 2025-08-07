def add():
    with open("contact.txt","a") as f:
        name=input("enter name : ")
        number=input("enter number : ")
        gmail=input("enter the gmail : ")
        f.write(f"{name},{number},{gmail}\n")
def view() :       
   with open("contact.txt","r") as f:
     print(f.read())  

def search():
    p=input("enter number or name :").lower()
    found=False
    try :
        with open("contact.txt","r") as f:
            for i in f:
                name,number,gmail=i.strip().split(",")
                if p in name.lower() or p in number.lower():
                    print(f"{name},{number},{gmail}")
                    found=True
                    break
            if not found:
                print("not found")    
    except FileNotFoundError:
        print("file not found error") 
while True:            
 choice=input(" enter the option :")
 if choice=="add":
    print(add())
 elif choice=="view":
    print(view())
 elif choice=="search":
    print(search())
 elif choice=="exit":
     break                                   
