print("Welcome to the kitty & puppy age converter!")

#First, we will create an input field to get the age of the user's cat. 
#Since the input function will always return a string, we have to change the type of the user's input to an integer. 

cat_age = input("How old is your cat?")
cat_age = int(cat_age)

#Since the human equivalent of a cat's age is approximately seven times greater, 
#we will now have to assign the human age as the cat's age multiplied by 7.
human_age = cat_age * 7

#Now, we will call on the print function to return the user's cat's age in human years. 
#In order to concatenate the human_age number with the preceding string, we will have to convert it with the str() function.
print("Your cat's age in human years equals approx. " + str(human_age))

#To get the dog's human age, we will repeat the previous steps but replacing 7 with 15 as dogs are about double the age of cats in human years.
dog_age = input("How old is your dog?")
dog_age = int(dog_age)

human_age = dog_age * 15

print("Your dog's age in human years equals approx. " + str(human_age))