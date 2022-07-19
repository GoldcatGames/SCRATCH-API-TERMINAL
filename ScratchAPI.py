
import webbrowser
category=0
user=0
project=0
typevar=0
usertypevar=0
slash='/'
username=0
password=0
login=0
loop=0
apiconnect=0

print ('-Scratch API Terminal-')
print ('Scratch API By Scratch Team: scratch.mit.edu')
print (" ")

categoryset=input ('Enter The Category (users, projects, or studios) ')
category=categoryset
if category==("users"):
    userset=input ('Username? ')
    user=userset
    typeset=input("Type? (following, followers, projects, favorites, etc., Also Space For Blank) ")
    typevar=typeset
    categorylock=category+slash+user
    usertypevar = "{0}{1}{2}".format(categorylock,slash,typevar)
    apiconnect='https://api.scratch.mit.edu/'+usertypevar
    print ('Connecting to', apiconnect)
    webbrowser.open(apiconnect)
elif category==("projects"):
    projectset=input('Project Number? ')
    project=projectset
    typeset=input('Type? (remixes, loves, stars, comments, Also Space For Blank) ')
    typevar=typeset
    usertypevar = "{0}{1}{2}".format(category,slash,project,slash,typevar)
    apiconnect='https://api.scratch.mit.edu/'+usertypevar
    print ('Connecting to', apiconnect)
    webbrowser.open(apiconnect)
elif category==("studios"):
    projectset=input('Studio Number? ')
    project=projectset
    typeset=input('Type? (projects, managers, curators, etc., Also Space For Blank) ')
    typevar=typeset
    usertypevar = "{0}{1}{2}".format(category,slash,project,slash,typevar)
    apiconnect='https://api.scratch.mit.edu/'+usertypevar
    print ('Connecting to', apiconnect)
    webbrowser.open(apiconnect)
    
    
    
