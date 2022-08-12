#Simple Quiz
#Matua Halafihi
#02/08/22

import time
# Create the opportunity for the player to choose to play again.
def main ():
  #Introduction, welcome message
  print("Welcome to the Pap High Coding Quiz")
  time.sleep(1)
  
  
  questions = ""
  answer_1 = "c"
  rite_ans = 0
  wrong_ans = 0
  score = (rite_ans + wrong_ans)

  print('''888
                    .8888'
                   .8888'
                   888'
                   8'
      .88888888888. .88888888888.
   .8888888888888888888888888888888.
 .8888888888888888888888888888888888.
.&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
`%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
 `00000000000000000000000000000000000'
  `000000000000000000000000000000000'
   `0000000000000000000000000000000'
     `###########################'
jgs    `#######################'
         `#########''########'
           `""""""'  `"""""' ''') 
  
  #Questions
  question_1 = input("In computer programming what is pseudocode? \na) a computer language.\nb)A card that increases the memory on your hard drive.\nc) A plan that sets out the algorithm of your program. ").lower()
  if question_1 == answer_1:
      print("Correct!")
      rite_ans += 1
      score += 1
  else:
      print("Incorrect!")
      wrong_ans -= 1
      score -= 1
  print("Score: ", score)
  time.sleep(1)
  
  answer_2 = "True"
  question_2 = input("The Boolean data type is named after a famous mathematician.TRUE or FALSE? ").lower()
  if question_2 == answer_2:
      print("Correct!")
      rite_ans += 1
      score += 1
  else:
      print("Incorrect!")
      wrong_ans -= 1
      score -= 1
  print("Score: ", score)
  time.sleep(1)
  
  answer_3 = "a"
  
  question_3 = input("In computer programming what is an Algorithm? \na) A set of instructions that are performed in order. \nb)Is the main component on the harddrive of a computer. \nc) A website that you can learn how to code. ").lower()
  if question_3 == answer_3:
      print("Correct!")
      rite_ans += 1
      score += 1
      
  else:
      print("Incorrect!")
      wrong_ans -= 1
      score -= 1
  print("Score: ", score)
  time.sleep(1)
  
  answer_4 = "True"
  question_4 = input("Google and Facebook are just some of the organisations that use python in their source code. True OR False ").lower()
  if question_4 != answer_4:
      print("Incorrect!")
      wrong_ans -= 1
      score -= 1
  else:
      print("Correct!")
      rite_ans += 1
      score += 1
  print("Score: ", score)
  time.sleep(1)
  
  answer_5 = "true"
  question_5 = input("If I want to work for RocketLab or SpaceX, will programming help me get there? True OR False ").lower()
  if question_5 == answer_5:
      print("Correct!")
      rite_ans += 1
      score += 1
  else:
      print("Incorrect!")
      wrong_ans -= 1
      score -= 1
  print("Score: ", score)
  time.sleep(1)
  print('Thank you for playing. You were incorrect ' + str(wrong_ans) + ' times, and correct ' + str(rite_ans) + ' times. Your final score is:'+ str(score) )
  replay = input('Would you like to play again? ')
  if replay == "yes":
      main()
  else:
      print("Thank you for playing. Goodbye! ")
main()  
  #Display final result to user
'''  print('Thank you for playing. You were incorrect ' + str(wrong_ans) + ' times, and correct ' + str(rite_ans) + ' times. Your final score is:', score)'''
  
