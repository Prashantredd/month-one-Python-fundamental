with open("details.txt","r") as file :
    d=file.read()
    print(d)
with open("details.txt","a") as file:
    name=input()
    age=int(input())
    classs=input()
    file.write(f" {name}\t {age}\t {classs}\n")
with open("details.txt","r") as f:
    print(f.read())    
        