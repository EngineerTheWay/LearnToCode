#Define the lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#ZIP the lists
letters_to_points = {key:value for key, value in zip(letters, points)}

#Add a blank tile to the lists
letters_to_points[" "] = 0
print(letters_to_points)

#Define a function to count the score of a word
def score_word(word):
  print_total = 0
  for letter in word:
    print_total += letters_to_points.get(letter.upper(), 0)
  return print_total

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

players_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  players_to_points[str(player)] = player_points
