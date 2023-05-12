from turtle import Turtle,Screen
import pandas as pd
from country import write_country

screen = Screen()
screen.title("U.S. States Game")

map = Turtle()
path_img=r"""./Quiz_map/us-states-game-start/blank_states_img.gif"""
screen.register_shape(path_img)
screen.setup(width=725,height=491)
map.shape(path_img)

us_states_path = r"""./Quiz_map/us-states-game-start/50_states.csv"""
us_states = pd.read_csv(us_states_path)

game_is_on = True
correct_ans = 0
lives = 10
correct_states = []
state_list = us_states.state.to_list()
missing_path = r"""./Quiz_map/us-states-game-start/missing_values.csv"""


while game_is_on:

    user_ask = screen.textinput(title=f"{correct_ans}/50 U.S. States",
                                prompt="What's the state?")
    user_ask = user_ask.title()
    
    if (not us_states[us_states["state"]==user_ask].empty) and (correct_ans<50) and (user_ask not in correct_states):
        correct_ans += 1
        value = us_states[us_states["state"]==user_ask]
        write_country(value.x.values[0],value.y.values[0],value.state.values[0])
        correct_states.append(value.state.values[0])

    elif us_states[us_states["state"]==user_ask].empty and user_ask != "Done":  
        lives -= 1

    if (user_ask == "Done") or (correct_ans == 50 or lives == 0):
        game_is_on = False
        missing_values = [state for state in state_list if state not in correct_states]
        states = pd.DataFrame(missing_values,columns=['Missing'])
        states.to_csv(missing_path)
        screen.bye()
    
screen.exitonclick()
    