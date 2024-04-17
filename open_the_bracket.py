from controller import GameController

if __name__ == "__main__":

    inputs = list(reversed(list("6*(4+(5-2*4)")))
    game = GameController(inputs, ["nikhil", "sid", "brian"], 97)

    # game = GameController()
    game.play()
