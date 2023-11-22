from logic import TicTacToe, HumanPlayer, BotPlayer
def main():
    mode = input("Choose mode (1 for single player, 2 for two players): ")
    player1 = HumanPlayer('X')

    if mode == '1':
        player2 = BotPlayer('O')
    else:
        player2 = HumanPlayer('O')

    game = TicTacToe(player1, player2)

    # Game loop
    while True:
        game.display_board()
        game.play_turn()
        winner = game.get_winner()
        if winner:
            print(f"Player {winner} wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
