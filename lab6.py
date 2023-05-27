str=input("Enter a string:")
def palindrome(a):
    if len(a)<1:
        return True
    else:
        if a[0] == a[-1]:
         return palindrome(a[1:-1])
        else:
         return False
if (palindrome(str)==True):
  print("Entered string is palindrome")
else:
  print("Entered string is not palindrome")

   
