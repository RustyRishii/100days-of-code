# Day 2, Inputs

name = input("What is your name?")
print()
favFood = input( "So " + name + " What is your favourite food?")
print()
tvShow = input( "Ahhh, and your What's your favourite TV show?")
question = input("So, " + name + "You wanna have " + favFood + " And watch some " + tvShow +"?")
print()
if question == "yes":
	print("Better call saul!!")
else:
	print("Nah, I'm going to sleep")