#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.

  #Answer question randomly with one of the options from your earlier list.


if __name__ == '__main__':
  main()


question = input("To use the magic 8ball, ask a question:\n")

answers = ["It is certain", "It is decidedly so", "Yes deffinitely",
           "You may rely on it", "As I see it yes", "Most Likely",
           "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
           "Ask again later", "Better not tell you now", "Cannot predict now", 
           "Concentrate and ask again", "Don't count on it", "My reply is no",
           "My sources say no", "Outlook not very good", "very doubtfull"]
length = len(answers)
r = random.random ()*length
r = int(r)
response = answers[r]
print (response)