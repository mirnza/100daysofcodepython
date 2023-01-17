# function with output
def name_format(f_name, l_name):
    full_name = f_name +' '+ l_name
    x= full_name.title()
    return x
    
print(name_format("angela", "yu"))

# function with multiple return
def name_format(f_name, l_name):
    if f_name == "" and l_name == "":
        return
    # return basically means its the end of the function
    #  if  the both the arguments are empty string then it will just print none
    # and the later part will be scrapped
    
    full_name = f_name +' '+ l_name
    x= full_name.title()
    return x
    
print(name_format("", ""))

# docstrings
def name_format(f_name, l_name):
    ''''It takes the first name and last name and adds it as full name'''
    full_name = f_name +' '+ l_name
    x= full_name.title()
    return x
    
print(name_format("angela", "yu"))
