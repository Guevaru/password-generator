import random

#create several variables for different string values each
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase='abcdefghijklmnopqrstuvwxyz'
number='1234567890'
symbol='~!@#$%^&*()+=,-./:;<=>?@{|}\[]'

#concatenate all the variables
combined=uppercase+lowercase+number+symbol

#declare a variables for the length of the password
length= 12

#make a variable password to join the module random with the function sample carrying arguements length and combined

password= "".join(random.sample(combined, length))
print("Here is your password: " + password)