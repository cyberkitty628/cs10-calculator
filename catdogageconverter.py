print("Welcome to the kitty & puppy age converter!")

#First, we will create an input field to get the age of the user's cat. 
#Since the input function will always return a string, we have to change the type of the user's input to an integer. 

cat_age = input("How old is your cat?")
cat_age = int(cat_age)

#Since the human equivalent of a cat's age is approximately seven times greater, 
#we will now have to assign the human age as the cat's age multiplied by 7.
human_age = cat_age * 7