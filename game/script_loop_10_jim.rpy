label loop_10_jim:
    scene bg plane 

    intercom "{i}Bing.{/i}"
    intercom "Ladies and gentlemen, this is your captain speaking. We have reached cruising altitude..."
    narr "I shift uncomfortably in my seat."
    narr "You’d think over a century of commercial aviation would’ve been enough to figure out how to make a goddamn chair."

    $ choice_comfortable = 0
    $ choice_babbler = 0

    menu loop_10_jim_takeoff:
        "What shall I do?"

        "Get comfortable." if choice_comfortable == 0:
            call jim_get_comfortable_1 from _call_jim_get_comfortable_1_1
            $ choice_comfortable = 1
            jump loop_10_jim_takeoff

        "Watch {i}American Turd{/i}." if choice_comfortable == 1:
            call jim_get_comfortable_2 from _call_jim_get_comfortable_2_1
            $ choice_comfortable = 2
            jump loop_10_jim_takeoff

        "Read the in-flight magazine." if choice_comfortable == 2:
            call jim_get_comfortable_3 from _call_jim_get_comfortable_3_1
            $ choice_comfortable = 3
            jump loop_10_jim_takeoff

        "Think about work." if choice_comfortable == 3:
            call jim_get_comfortable_4 from _call_jim_get_comfortable_4_1
            $ choice_comfortable = 4
            jump loop_10_jim_takeoff

        "Check out my neighbor." if choice_babbler == 0:
            narr "A middle-aged man, dismantling his Babelgram."
            narr "Another one of those snobs, paying his way into multilingualism and shoving it into everyone's face anyway."
            $ choice_babbler = 1
            jump loop_10_jim_takeoff

        "Go to sleep.":
            narr "Great idea."

    scene black
    "..."
    "Whoever designs these headrests should be fired."
    "..."
    intercom "{i}Bing.{/i}"

    scene bg plane
    intercom "Ladies and gentlemen, this is your captain speaking. As we begin our final descent..."
    narr "Ugh."
    narr "My neck aches now and I {i}still{/i} feel like a zombie."
    narr "I sit my chair upright."
    narr "Windows open around me, letting the sun stream in from behind the clouds."
    $ randnum = renpy.random.random()
    if randnum < 0.3:
        narr "Beside me, the snob is having a lively conversation with the woman on the other side."
    else:
        narr "Beside me, the snob is turning his laptop off, muttering what sounds like numbers to himself."
    narr "Me, I just stare into the distance, trying not to think about the fact that I still have to check into the office after touchdown."
    narr "It's going to be a long day."

    scene black
    narr "{b}Bad Ending.{/b}"

    return
