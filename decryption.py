from tkinter import messagebox

def decryptor(password,msg,img,c,pas):
  message = ""
  n = 0
  m = 0
  z = 0
  if password == pas:
     for i in range(len(msg)):
         message = message + c[img[n, m, z]]
         n = n + 1
         m = m + 1
         z = (z + 1) % 3
     
     return message
  else:
     messagebox.showerror("Authentication Error", "Incorrect passcode")
 
  
  



