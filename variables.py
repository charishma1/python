"""variables"""
age = 42
name = "steve"
address = "123 sesame st"


#bad names
a = 5
thisismysuperawesomevariable = 17
# illegal names
#99red_ballons = None #cant start with num
#rad-balloon = 99 #no dash
#rad ballon = 1 #no space

#variable switching 
hungry = True
hungry = False

#dynamic typing
hungry = 7
hungry = "i am not currently hungry"

#nick naming
yell =  print
yell("hello world")

#scope
MY_AGE = 33
def yes_change():
    global MY_AGE
    MY_AGE = 45
    print("age after:", MY_AGE) 

def yes_out_change():
    outer_var = "ast"
    def inner():
        nonlocal outer_var
        outer_var = "fire_truck"
        inner_var = "spy"
        print ("i wanted to be a ", outer_var)
    inner()
    print("most kids wanted to be a firefigher")
    print("But i wanted to be a(n)", outer_var)
    try:
        print("but being a", outer_var, "could be cool")
    except:
        print("too secret for me")
    
