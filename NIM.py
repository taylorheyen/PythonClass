piles = [12, 9, 13]
turn = 1
game_over = False

while not game_over:
    print(f"Piles: {piles}")
    move = input(f"Player {turn}, enter your move (pile, stones): ")
    pile = int(move[0])
    stones_to_move = int(move[2])
    piles[pile-1] = piles[pile-1] - stones_to_move
    if turn == 1:
        turn = 2
    else:
        turn = 1
    if piles[0] + piles[1] + piles[2] == 1:
        game_over = True
print(f"Final piles: {piles}")
print("Thanks for playing")