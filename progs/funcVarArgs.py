# Function definition is here
def printinfo( arg1, *vartuple, **keyargs ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   print vartuple
   print keyargs
   for key in keyargs:
       print key, keyargs[key]
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
printinfo( 70, 60, 50, a = 100, b = "aaa" )
