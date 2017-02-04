from lib.master import *
import hashlib
from lib.actions import *
from lib.util import *
from lib.updown import *
#id/username/password/permessions/karma
credentials=[]
loggedUser="NULL"#Don't refer to this, use credentials[1]
if __name__ == "__main__":
    print("\nEzAppunti v1.0")
    ftp=connectToServer()
    if "users.txt" in ftp.nlst():
        ftp.retrbinary("RETR users.txt", open("users.txt", "wb").write)  # TODO Hide file
    print("\n===LOGIN===")
    givenUsr = input("Username: ")
    givenPsw = input("Password: ")
    with open("users.txt") as f:
        for line_terminated in f:
            data = line_terminated.split(";")
            if (data[1] == givenUsr):
                if (hashlib.sha256(givenPsw.encode('utf-8')).hexdigest() == data[2]):
                    print("\nLogged successfully to " + givenUsr)
                    loggedUser=givenUsr
                    credentials = line_terminated.split(";")
                    credentials[-1]=credentials[-1].rstrip()
                    break
                else:
                    print("Wrong password")
                    loggedUser = "WRONG_PASSWORD"
                    exitProgram()#TODO Don't exit, prompt again for password
        if (loggedUser == "NULL"):
            print("No users found for entry " + givenUsr)
            exitProgram()
    master_init(ftp)
    while True:
        print("[1] Create new note\n[2] Edit existing note\n[3] Delete note")
        inp=input("~ ")
        if(inp=="1"):
            if(data[3]=="**"or data[3]=="***"):
                v=[]
                fileName=input("How do you want to name the file? ")
                print("What do you want to write inside the file? Write exit to finish")
                i=""
                while(i!="exit"):
                    i=input("")
                    v.append(i)
                actions_create_note(fileName,v)
            else:
                print("You don't have the right to write new files\n")
    os.remove("master.txt")