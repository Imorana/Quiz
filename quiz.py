# created by Tivinia Mulipola Vi
# This quiz is based on Cheetahs. It tests your knowledge on how well you know your Cheetahs.

# This function is called check(). It requires 2 arguments. One list and one user input. It returns true if the user input is in the list. It returns false if the user is not in the list
def check(options, user_input):
    if user_input in options:
        return True
    else:
        return False

options = ["4"]
question_one = input("How many legs does a cheetah have? Is it 1, 2, 3, or 4?")
# print(check(options, question_one))
if check(options, question_one):
    print("Good job, you are a smart individual")
else:
    print("incorrect")

options = ["cub"]
question_two = input("What is the proper name of a cheetahs child? Is it cub, kitten, child or cheetos?")
# print(check(options, question_two))
if check(options, question_two):
    print("Good job, you are a smart individual")
else:
    print("incorrect")

options = ["7000"]
question_three = ("How many cheetahs are left in the world? Is it 6517, 6283, 8271, or 7000?")
# print(check(options, question_three))
if check(options, question_three):
    print("Good job, you are amazingly impressive today")
else:
    print("incorrect you are wrong again")    

options = ["30"]
question_four = input("How many teeth does a Cheetah have? Is it 23, 42, 17 or 30")
# print(check(options, question_four))
if check(options, question_four):
    print("Good job, you are a smart individual")
else:
    print("incorrect")

options = ["Falidae"]
question_five = input("What family is a cheetah in? Is it Falidae, Calidae, Caracal, Cat")
# print(check(options, question_five))
if check(options, question_five):
    print("Good job, You are impressively smart")
else: 
    print("incorrect")

options = ["Africa"]
question_six = input("Where are cheetahs mostly found? Is it afganistan, africa, india or iran")
# print(check(options, question_six))
if check(options, question_six):
    print("Excellent, well done keep going")
else:
    print("keep trying")

options = ["8-10"]
question_seven = input("How long can cheetahs live? Is it 7-12, 3-8, 8-11 or 8-10")
# print(check(question_seven))
if check(options, question seven):
    print("Youve improved, well done")
else:
        print("try again")

options = ["animal"]
question_eight = input("What is a cheetah? Is it mammal, animal or human")
# print(check(options, question_eight))
if check(options, question_eight)
     print("Super proud of you")
else:
     print("nearly there well done")

options = ["antelope"]
question_nine = input("What do cheetahs eat? Is it antelope, dog, bear or owl")
# print(check(question_nine))
if check(options, question_nine):
    print("well done")
else:
    print("Try again, nearly there")

options = [10-12]
question_ten = input("What are the oldest cheetahs can live? Is it 8-9, 9-10, 11-13 pr 10-12")
# print(check(options, question_ten))
if check(options, question_ten):
    print("Well done, Youve reached the end")
else:
    print("Thats ok try again")

# Thank you for playing my quiz based on Cheetahs feel free to try again.




