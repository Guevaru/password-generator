import random

#define a function do shuffle all the characters of a string
def shuffle(strings):
    templist= list(strings)
    random.shuffle(templist)
    return ''.join(templist)


uppercase=chr(random.randint(65,90))
lowercase=chr(random.randint(97,122))
number=chr(random.randint(48,57))
symbol=chr(random.randint(33,47))
more_signs=chr(random.randint(60,65))
all_forms=chr(random.randint(33,126))
emojis=chr(random.randint(128151,128525))
other_forms=chr(random.randint(123,152))
arabic=chr(random.randint(153,255))

password= uppercase+lowercase+arabic+other_forms+number+symbol+more_signs+emojis+all_forms
password= shuffle(password)
print("Here is your password: " + password)
