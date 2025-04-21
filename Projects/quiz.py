
# Beginning: create variables
shaq_build = 0
steph_build = 0 

# middle: ask question
# question 1
answer = input ("would you rather a) shoot the basketball, or b) dunk the basketball?")
if answer == "a":
    steph_build += 1
elif answer == "b":
    shaq_build += 1

# middle: ask question
# question 2
answer = input ("do you perfer a) chicken, or b) pasta?")
if answer == "a":
    shaq_build += 1
elif answer == "b":
    steph_build += 1 

# middle: ask question
# question 3 
answer = input ("Do you like to wear a) under Armour, or b) reebok?")
if answer == "a": 
    steph_build += 1 
elif answer == "b":
    shaq_build += 1

# middle: ask question
# question 4
answer = input ("What height to you perfer a) 7'1, or b) 6'3?")
if answer == "a": 
    shaq_build += 1 
elif answer == "b":
    steph_build += 1

# middle: ask question
# question 5
answer = input ("would you rather have big hands or normal hands a) normal hands, or b) big hands?")
if answer == "a": 
    steph_build += 1 
elif answer == "b":
    shaq_build += 1

# end: determine results
if steph_build > shaq_build:
    print("You like Stephen Curry ")
elif shaq_build > steph_build:
    print("You like Shaq")
elif shaq_build == steph_build:
    print("You like both players")
