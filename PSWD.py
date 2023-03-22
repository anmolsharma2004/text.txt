# the function is to check whether the password met all the conditions or not ?
# the verification is done by the already present function called (RE) Reading expressions
def pswd_check(pswd):
   specharlist = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
   # the list is for
   #the special characters
   alphalist = re.compile('[a-z]')
   #this list is for
   # the lowercase letter
   Alphalist = re.compile('[A-Z]')
   #this list is for
   # the uppercase letter
   numlist = re.compile('[0-9]')
   # this list is for 
   # the numbers  

   # the if conditions further check that the 
   #provided output either have the required input value or not
   if(alphalist.search(pswd) == None):
        print("The password need at least one lowercase alphabet to proceed")
        return 0# if it doesn"t have the value it returns false
   else:
       pass

   if(Alphalist.search(pswd) == None):
        print("The password needs at least one uppercase letter to proceed")
        return 0 
   else:
       pass # else it goes onto the next condition

   if(numlist.search(pswd) == None):
       print("The password needs atleast one number to proceed")
       return 0
   else:
       pass

   if(specharlist.search(pswd) == None):
       print("The password needs atleast one special character to proceed")
       return 0  
   else:
       pass

   return 1 # if all the conditions are meant it returns true


            if pswd_confirmation == 1:# if the random generated password is confirmed
               print("Your account has been created succesfully")
               # if the sign up is succesful with the required password 
               print("Now you can signin in your",PORTAL.upper(),"using this login credentials")
               exit()
            if pswd_confirmation == 2:#if user want a new random generatewd password
               continue
            if pswd_confirmation == 3:# if they want to manually type the pasword
               num = 1
               break
