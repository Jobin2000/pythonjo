mark=72
if mark >24:
   print("you have passed the test")
   if mark>90:
       print("you have A+")
   elif mark>80 and mark<90:
       print("you have A")
   elif mark>70 and mark<80:
       print("you have B")
   else:
       print("you have C")  
else:
    print("you have failed")
