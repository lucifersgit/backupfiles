# This prorgram says hello, and asks for my name

print('Hello world')
print('What is your name?') # ask for their name
#this is a user input option
myName = input () 

print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') 

#ask for age via user input

myAge = input ()

print('Your current age is ' + myAge)

print('Add a number of years to see how old you will be, then')

myAgeadd = input ()

print('You would like to add ' + myAgeadd + ' years to your current age')

myAgecombo = (int(myAge) + int(myAgeadd))

print('Here:' + (str(int(myAgecombo)))
#print('You will be' + (str(int(myAgeadd) + str(int(myAge)) ' in a year.')

#print('You will be ' + str(int(myAge) + 1)  + ' in a year.')
