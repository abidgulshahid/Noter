## This Program is Tested on macOS 10.14.5 (18F132)
import os,sys

if len(sys.argv) < 2:
    print("Usage: python noter.py <target_name>")
    sys.exit(1)
target = str(sys.argv[1])
path = "/Users/abidkhan/Desktop/Hack_Stuffs/Programs/"+target

print("[+] Making Directory")
print("[!] Checking if There Existing Directory")
if os.path.isdir(path):
    print ("Already Existed ",target)
    print ("[!] Checking if Files Are existed or not" )
    if os.path.exists(path+'todo.txt') or os.path.exists(path+'intresting.txt'):
        print("[ All Files Already Created")
        sys.exit(1)

    else:
        todo_path = os.path.join(path,'todo.txt')
        interesting_path = os.path.join(path,'intresting.txt')
        issues_path = os.path.join(path,'issues.txt')
        

        intrest_create = open(interesting_path,"w+")
        iss_create = open(issues_path,"w+")
        todo_create = open(todo_path,"w+")
        
        
        print ("[+] Todo Created")
        print ("[+] Intresting Created")
        print ("[+] Issues Created")
        sys.exit(1)

else:
    os.mkdir(path)

    print ("[+] Folder Created " ) 
    todo_path = os.path.join(path,'todo.txt')
    interesting_path = os.path.join(path,'intresting.txt')
    issues_path = os.path.join(path,'issues.txt')
        

    intrest_create = open(interesting_path,"w+")
    iss_create = open(issues_path,"w+")
    todo_create = open(todo_path,"w+")
        
        
    print ("[+] Todo Created")
    print ("[+] Intresting Created")
    print ("[+] Issues Created")

    

## This Program is Tested on macOS 10.14.5 (18F132)
