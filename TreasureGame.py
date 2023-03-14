print("RUN AWAY FROM THE WEREWOLF!")
print("""
***************************************************
                    ( ;`~v/~~~ ;._
                 ,/'"/^) ' < o\  '".~"11\--,
               ,/",/W  u '`. ~  >,._..,   )'
              ,/'  w  ,U^v  ;//^)/')/^\;~)'
           ,/"'/   W` ^v  W |;         )/'
         ;''  |  v' v`" W }  11
         "    .'\    v  `v/^W,) '\)\.)\/)
                    `\   ,/,)'   ''')/^"-;'
                        \  
                            '". _
                             1
**********************************************
""")
decision = input("right or left way? right or left?\n").upper()
if decision == "RIGHT":
    decision = input("cross the bridge or enter to the cave? bridge or cave?\n").upper()
    if decision == "BRIDGE":
        decision = input("Go to the car or to the street? car or street?\n").upper()
        if decision == "CAR":
            print("Bad luck, the car is broken\n")
            print("""
                  _.--,_
               .-'      '-.   
              /            1
             '          _.  '
             \      "" /  ~(
              '=,,_ =\__ `  &
                    "  "'; 111
            """)
        elif decision == "STREET":
            print("Nice, someone helped you to run away\n")
            print("""
              ___________
             '._==_==_=_.'
             .-\:      /-.
            | (|:.     |) |
             '-|:.     |-'
               \::.    /
                '::. .'
                  ) (
                _.' '._
                1111111
            """)
        else:
            print("GAME OVER, YOU WROTE SOMETHING WRONG :(")
    elif decision == "CAVE":
        print("oh no!, there are more werewolf here\n AHHHH!!!\n")
        print("""
              _.--,_
           .-'      '-.   
          /            1
         '          _.  '
         \      "" /  ~(
           '=,,_ =\__ `  &
                 "  "'; 111
              """)
    else:
        print("GAME OVER, YOU WROTE SOMETHING WRONG :(")
elif decision == "LEFT":
    print("oh no!, there are no way to run!\n YOU DIE\n")
    print("""
           _.--,_
        .-'      '-.   
      /            1
     '          _.  '
     \      "" /  ~(
      '=,,_ =\__ `  &
            "  "'; 111
    """)
else:
    print("GAME OVER, YOU WROTE SOMETHING WRONG :(")

