default persistent.in_force_afm = False
default persistent.old_afm_enable = False
default persistent.old_afm_time = 20

label loop_1:
    scene bg plane 

    intercom "{i}Bing.{/i}"
    intercom "Ladies and gentlemen, this is your captain speaking. We have reached cruising altitude..."
    narr "I shift uncomfortably in my seat."
    narr "You’d think over a century of commercial aviation would’ve been enough to figure out how to make a goddamn chair."

    $ choice_comfortable = 0
    $ choice_babbler = 0

    menu loop_1_takeoff:
        "What shall I do?"

        "Get comfortable." if choice_comfortable == 0:
            call jim_get_comfortable_1 from _call_jim_get_comfortable_1
            $ choice_comfortable = 1
            jump loop_1_takeoff

        "Watch {i}American Turd{/i}." if choice_comfortable == 1:
            call jim_get_comfortable_2 from _call_jim_get_comfortable_2
            $ choice_comfortable = 2
            jump loop_1_takeoff

        "Read the in-flight magazine." if choice_comfortable == 2:
            call jim_get_comfortable_3 from _call_jim_get_comfortable_3
            $ choice_comfortable = 3
            jump loop_1_takeoff

        "Think about work." if choice_comfortable == 3:
            call jim_get_comfortable_4 from _call_jim_get_comfortable_4
            $ choice_comfortable = 4
            jump loop_1_takeoff

        "Check out my neighbor." if choice_babbler == 0:
            narr "A middle-aged man, wearing a Babelgram."
            narr "He's staring at his feet, a grim look on his face."
            narr "Damn, he doesn't look good. Does Babelgramming take that much out of you?"
            $ choice_babbler = 1
            jump loop_1_takeoff

        "Check out the Babelgrammer." if choice_babbler == 1:
            narr "I've always taken Babblers for mere assholes, gloating to themselves over their misplaced pride."
            narr "But what if they're driven by something darker?"
            narr "A crippling fear, perhaps, of falling behind in a society where knowledge is your only commodity?"
            narr "Well, then they'd still be assholes, anyway."
            $ choice_babbler = 2
            jump loop_1_takeoff

        "Go to sleep.":
            narr "Great idea."

    scene black
    "..."
    "Whoever designs these headrests should be fired."
    "..."
    stop music fadeout 1.0
    unknown "Eeeeeyaaaa!"
    scene bg plane

    narr "My eyes jump open."
    narr "It takes me a second to realize what's happening."
    show david choking at shake_transform
    babbler "..."
    narr "The Babbler is convulsing, his face blue."
    unknown "Is anyone here a medical professional?!"
    unknown "Do the Heimlich!"
    unknown "You beside him, unbuckle his seatbelt!"
    narr "That's... that's me! I reach for his seatbelt..."
    narr " Is he pushing me away?"
    unknown "Do it!"
    narr "The girl on the other side is restraining him now."
    narr "My eyes glazing, I snap open his seatbelt."
    narr "..."
    narr "He's still struggling. but his energy has waned."
    narr "It takes no less than one flight attendant and two other passengers to get him into position, and..."
    narr "{i}Pop!{/i}"
    narr "A spit-covered stress ball bounces against the carpeted floor."
    show david struggling at shake_transform
    babbler "AAAAAAAAAAAAAAA-"
    fa "Hey. Hey."
    babbler "-AAAAAAAAAAAAAA-"
    fa "Listen to me. Look at me. Hey!"
    babbler "-AAAAAAAAAAAAAA-"
    fa "Please! You have to stop!"
    babbler "JUST LET ME DIE ALREADY!"
    fa "Sit down. Please! You'll be alright."
    babbler "-FUCK FUCK FUCK FUCK FUCK-"
    fa "Ow!"
    afa "Sit him down!"
    fa "I'll get the cuffs-"
    afa "Please, calm down! We don't want to hurt you!"
    fa "Can you hold him down for me? I need to tell the pilot-"
    hide david
    narr "..."

    call play_track_4_halfway from _call_play_track_4_halfway
    narr "There goes the rest of the day, I guess."
    narr "I can already see it happening."
    narr "They'll make an emergency landing, I'll arrive late, and I won't even have time for a snack before checking in at the office."
    narr "I close my eyes."

    scene black
    narr "It's going to be a long day."
    narr "{b}Bad Ending.{/b}"

    $ persistent.loop = 2

    return

