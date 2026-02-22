import os
while True:
      print("show running processes")
      print("kill a process")
      print("show system usage")
      print("exit")

      choice = int(input("enter the process no- "))
 
      if  choice==1 :
            os.system("top")
      elif choice==2 :
            n=input("enter pid no")
            os.system("kill " + n)
      elif choice == 3:
            os.system("df -h")
      elif choice == 4:
            print("exiting")
      break
else:
    print("invalid choice")



    
