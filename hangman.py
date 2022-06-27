import random as r

#choose a word from list randomly
word_list = ["aardvark", "baboon", "camel"]
word_choice_num = r.randint(0,len(word_list)-1)
word_choice = word_list[word_choice_num]

# #set array for each word with underscores
word_length = len(word_choice)

print(f"The word is {word_choice} and it has {word_length} characters.")
# #create underscore for length of word
display=[]

# # number of player lives is in variable 
lives = 6 

# #art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# #set initial display of underscores with length of word
for i in range(0,word_length):
    display.append("_")

print(f"Your word is {display}")
print(f"You have {lives} choices left.")

#loop through the underscores and replace the letter if the user guesses it correctly
end_of_game = False

while end_of_game != True:
  guess = input("Guess a letter: ").lower()

  #check guessed letter
  for i in range(0,word_length):
    if guess == word_choice[i]:
      display[i] = word_choice[i]
  print("Good guess!")
    
  #if guess is not in word
  #then reduce lives by one
  # if lives = 0, game should stop and print "you lose"
  if guess not in display:
    lives = lives - 1
    if lives == 0:
      print("You ran out of lives. You lose!")
      end_of_game = True
    elif lives > 0:
      print(f"Wrong guess. You have {lives} lives left.")
  print(display)
  print(stages[lives])

  #Win condition
  if display.count("_") == 0:
    end_of_game = True
    print("You Win")

