import os

commitmessage = input("commit message")


print("commit")
os.system("git add --all")
os.system(f"git commit -m {commitmessage}")
os.system("git push")
os.system("git pull")