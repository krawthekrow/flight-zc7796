label loop_2:
    scene bg plane

    intercom "{i}Bing.{/i}"
    intercom "Ladies and gentlemen, this is your captain speaking. We have reached cruising altitude..."
    narr "I shift uncomfortably in my seat."
    narr "You’d think over a century of commercial aviation would’ve been enough to figure out how to make a goddamn chair."

    $ choice_comfortable = 0
    $ choice_babbler = 0

    menu loop_2_takeoff:
        "What shall I do?"

        "Get comfortable." if choice_comfortable == 0:
            call jim_get_comfortable_1 from _call_jim_get_comfortable_1_2
            $ choice_comfortable = 1
            jump loop_2_takeoff

        "Watch {i}American Turd{/i}." if choice_comfortable == 1:
            call jim_get_comfortable_2 from _call_jim_get_comfortable_2_2
            $ choice_comfortable = 2
            jump loop_2_takeoff

        "Read the in-flight magazine." if choice_comfortable == 2:
            call jim_get_comfortable_3 from _call_jim_get_comfortable_3_2
            $ choice_comfortable = 3
            jump loop_2_takeoff

        "Think about work." if choice_comfortable == 3:
            call jim_get_comfortable_4 from _call_jim_get_comfortable_4_2
            $ choice_comfortable = 4
            jump loop_2_takeoff

        "Check out my neighbor." if choice_babbler == 0:
            narr "A middle-aged man, wearing a Babelgram."
            narr "He’s staring into nowhere, a stunned look on his face."
            $ choice_babbler = 1
            jump loop_2_takeoff

        "Check out the Babelgrammer." if choice_babbler == 1:
            narr "I’ve heard first-time Babblers describe the experience as mind-blowing – I guess they weren’t exaggerating after all."
            narr "...Not that it makes them any less reprehensible."
            $ choice_babbler = 2
            jump loop_2_takeoff

        "Check out the Babbler." if choice_babbler == 2:
            narr "I mean, seriously?"
            narr "Back in the day, we used to spend {i}weeks{/i} banging through flash cards and conversational exercises..."
            narr "...and we'd still trip up over the {i}simplest{/i} of grammatical mistakes!"
            narr "And now you want to reduce it to a click of a button?"
            narr "That's not how language works!"
            narr "Language is {i}supposed{/i} to be difficult."
            narr "Meritocratic."
            narr "{i}Organic.{/i}"
            narr "One day, we'd be paying to teach our kids to walk!"
            $ choice_babbler = 3
            jump loop_2_takeoff

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

    menu:
        "\"Hey.\"":
            babbler "Hey."
    narr "The Babbler? What business does he want with me?"
    narr "Still looking forward – no need to give him the privilege of eye contact – I reply."
    me "Hey."
    babbler "Did... did you feel something?"
    me "You mean, other than profoundly tired?"
    babbler "No, more like... a sense of {i}déjà vu{/i}."
    narr "He's not just a Babbler, but a Mystic too? Thank goodness this plane is landing soon."
    me "Whatever you're trying to sell me, I'm not interested."
    babbler "I'm not trying to sell you anything!"
    me "That's what you fuckers always say."
    babbler "Please, listen to me. I... I'm scared."
    me_noprefix "*sigh*"
    show david neutral
    narr "I turn to face him."
    me "What do you want?"
    show david sad
    babbler "...Huh. I don't actually know what to ask for."
    me "Figures."
    show david neutral
    babbler "I mean, it's just that..."
    babbler "...something really weird happened, and I thought maybe you felt it too."
    babbler "But I guess you would've said so by now if you had."
    narr "I claw at my pants."
    me "Fine, tell me what happened."
    me "But if this is another scheme to sell me your new-age gizmos or whatever, well, fuck you in advance."
    show david angry
    babbler "Look, it's not-"
    narr "He winces."
    show david sad
    babbler "I- I think I saw the future. Like a while back, when we were still taking off."
    show david neutral
    babbler "I thought it was a dream at first, but..."
    babbler "You know how dreams sorta fade away as time passes?"
    babbler "Well, this... *vision*... it got more vivid, the more I thought about it."
    me "Uh huh."
    babbler "You know how that girl spilled her juice?"
    me "I was sleeping."
    babbler "Well, she did."
    babbler "Thing is, I remember it. From the vision, I mean."
    me "And now you're gonna write about it on your personal blog and gain twenty new followers. Congratulations."
    show david angry
    babbler "Hey! I know it sounds dumb, but it really happened!"
    me "..."
    babbler "..."
    me "..."
    show david sad
    narr "He sags into his chair."
    babbler "I wouldn't believe myself either, if I were you."
    narr "I look at him sternly."
    me "You want to know what I think?"
    me "I think you should cut down on whatever drugs you're taking."
    me "...and also the Babelgramming. I don't know what you Babblers get out of-"
    show david surprised
    babbler "Why, of course! The-"
    scene black
    narr "{b}Bad Ending.{/b}"

    $ persistent.loop = 3

    return
