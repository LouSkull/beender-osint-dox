import time
import os

def yes():
  time.sleep(2)
  print("\033[91mWARNING: TO START TOOL, START \"main_beender.py\" FILE\033[91m")
  print("\033[91mWARNING: READ LICENSE FILE!!!\033[91m")
  time.sleep(4)
  
  os.system("start main_beender.py")
  exit()
  
def no():
  time.sleep(2)
  print("\033[91mWARNING: TO START TOOL, START \"main_beender.py\" FILE\033[91m")
  print("\033[91mWARNING: READ LICENSE FILE!!!\033[91m")
  time.sleep(4)
  
  print("Bye...")
  time.sleep(1)
  exit()
  
  
os.system("cls")
os.system("title github.com/LouSkull")
os.system("color 6")
setup = ("""
███████╗███████╗████████╗██╗   ██╗██████╗ 
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
███████╗█████╗     ██║   ██║   ██║██████╔╝
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
███████║███████╗   ██║   ╚██████╔╝██║     
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
""")
print(setup)
os.system("color 6")
os.system("pip install -r main.folder\\beender_plugin.txt")
os.system("python -m nuitka --mingw64 main_beender.py")
time.sleep(2)
while True:
  os.system("cls")
  os.system("color 6")
  print(setup)
  a = input("Successfully installed, Do you wont start beender dox? (Y,N)  ")

  if a == "Y":
    yes()
    
  elif a == "y":
    yes()
    
  elif a == "n":
    no()
    
  elif a == "N":
    no()
    
  else:
    print(f"Unknown function: {a}")
    time.sleep(2)
