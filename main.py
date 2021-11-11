
import turtle, pandas


def start():
    screen = turtle.Screen()
    screen.title("US States Game")
    image = "blank_states_img[1].gif"
    screen.addshape(image)
    turtle.shape(image)
    df = pandas.read_csv("50_states.csv")
    turtle_states = []
    game_is_on = True
    while game_is_on:
        answer_state = screen.textinput(title=f"Guess the state", prompt="What's the another state name?")
        df_row = df.loc[df['state'] == answer_state.title()]
        print(df_row)
        if not df_row.empty:
            tur = turtle.Turtle()
            tur.penup()
            tur.hideturtle()
            tur.goto(df_row.iloc[0]['x'],df_row.iloc[0]['y'])
            tur.write(answer_state)
            df = df.drop(df[(df['state'] == answer_state.title())].index)
        else:
            print("Enter correct state")
        print(len(df))
        # Game completed sequence
        if len(df) == 0:
            game_is_on = False

    turtle.mainloop()

if __name__ == '__main__':
    start()
