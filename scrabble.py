letters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m",  "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
points = [1, 1, 3, 3, 3, 3, 2, 2, 1, 1, 4, 4, 2, 2, 4, 4, 1, 1, 8, 8, 5, 5, 1, 1, 3, 3, 4, 4, 1, 1, 3, 3, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 8, 8, 4, 4, 10, 10]

letter_to_points = dict(zip(letters, points))

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for x in word:
    if (x not in letter_to_points):
      continue
    point_total += letter_to_points[x]
  return point_total
  
brownie_points = score_word("BROWNIE")

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}


def play_word(player, word):
  value_lst = player_to_words[player]
  if (word in value_lst):
    print("Uh Oh!, You already used the word '{}'...".format(word))
    return
  value_lst.append(word)
  player_to_words[player] = value_lst
  return
  

def update_points_total():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points



print(update_points_total())

play_word("wordNerd", "HELLO")

print(update_points_total())

print(player_to_words)






















