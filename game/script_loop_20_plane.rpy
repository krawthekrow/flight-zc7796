default persistent.loop_20_comfortable = 0
default persistent.loop_20_sleep = 0
default persistent.loop_20_neighbors = 0
default persistent.loop_20_woman = 0
default persistent.loop_20_jim = 0
default persistent.loop_20_suicide = 0

default persistent.loop_20_skip_initial = 0

default persistent.loop_20_seen = 0

label loop_20:
    python:
        loop_20_dead = 0

        loop_20_wallet = 0
        loop_20_passport = 0
        loop_20_tablet = 0
        loop_20_jewelry = 0
        loop_20_paper = 0
        loop_20_soap = 0
        loop_20_knife = 0
        loop_20_cash = 0

        loop_20_hammer = 0
        loop_20_blowtorch = 0
        loop_20_blowtorch_used = 0
        loop_20_paperclips = 0
        loop_20_rf_transmitter = 0

        loop_20_electronics_raided = 0
        loop_20_bank_raided = 0
        loop_20_hq_open = 0
        loop_20_jammer_up = 0

        loop_20_workbench_looted = 0
        loop_20_basement_lock_open = 0
        loop_20_basement_lock_jam = 0
        loop_20_machine_disabled = 0

        loop_20_david_loose = 0
        loop_20_self_purged = 0
        loop_20_allie_purged = 0
        loop_20_allie_cube_on_tongue = 0
        loop_20_allie_cube = 0
        loop_20_allie_cube_eaten = 0

        persistent.loop_20_seen = 1

    scene black
    intercom "{i}Bing.{/i}"
    scene bg plane
    intercom "Ladies and gentlemen, this is your captain speaking. We have reached cruising altitude..."
    narr "I wrestle the Babelgram off my head."

    menu loop_20_takeoff:
        "What shall I do?"

        "Get comfortable." if persistent.loop_20_comfortable == 0:
            narr "This seat isn't any more comfortable than my old one."
            narr "Can't say I'm surprised."
            $ persistent.loop_20_comfortable = 1
            jump loop_20_takeoff

        "Check out my neighbors." if persistent.loop_20_neighbors == 0:
            narr "To my left, I see a young woman, reading a physics textbook."
            narr "To my right, I see me."
            $ persistent.loop_20_neighbors = 1
            jump loop_20_takeoff

        "Talk to the young woman." if persistent.loop_20_neighbors == 1 and persistent.loop_20_woman == 0:
            narr "There's nothing I need from her."
            narr "Besides, she's pretty focused on her book. I don't think she wants to be disturbed."
            $ persistent.loop_20_woman = 1
            jump loop_20_takeoff

        "Talk to... Jim." if persistent.loop_20_neighbors == 1 and persistent.loop_20_jim == 0:
            med "Hey, Jim."
            show jim curious
            jim "Have we met?"
            med "No, but I recognize you! You're James, right?{w} Infotech United?"
            jim "Uh, yeah. Who are you?"
            med "I'm [persistent.youname!c]. Used to work under Ben too. He's a real bitch, isn't he?"
            show jim neutral
            jim "Oh, you bet. You know what he made me do today?"
            med "You need to fill out a report, same day you land?"
            show jim curious
            jim "No shit! How'd you guess?"
            med "The guy never changes, man."
            med "Take it from me. You've gotta switch jobs, pronto!"
            show jim sad
            jim "Eh, no one else would take me."
            jim "And besides, I'd be betraying myself if I did. Working in compsec has always been my dream."
            med "But {i}this{/i} kind of compsec? No one dreams of this! Tell me with a straight face you're satisfied where you are."
            jim "I don't want to think about this."
            med "But you must, or you'll always be stuck in this rut."
            med "Admit it.{w} You want to be a pen tester."
            show jim neutral
            jim "No I don't! It's way too stressful, always having to keep up-to-date with vulnerabilities."
            jim "No. I like my peaceful, stress-free life."
            med "Excuses!"
            med "Peaceful? Stress-free?"
            med "Tell me, what do you do in your free time?"
            show jim curious
            jim "I... go to the beach sometimes?"
            med "Be honest with yourself! You don't {i}have{/i} any free time..."
            med "...because that asshole gives you overtime half the week and keeps you on call for the other!"
            show jim neutral
            jim "Fuck, no! It's not {i}that{/i} bad!"
            med "It {i}is{/i} that bad!"
            med "Think about it. I bet there's {i}something{/i} you want to do."
            med "Something fun."
            med "Something that got you fired from your last job, perhaps."
            jim "What do {i}you{/i} know about my last job?"
            med "More than you think."
            med "Like the... {i}incident{/i} with Wish Fulfillment Inc. last December."
            med "Admit it, that was fun."
            jim "Wha- How'd you know about {i}that{/i}?!"
            med "You can have the best security practices in the world, but none of that's gonna matter if your boss doesn't."
            med "Remember that, Jim."
            jim "Don't you dare lay a finger on me or my boss."
            med "What? No! I'm trying to {i}help{/i} you!"
            med "Here, lemme fill out some job applications to get you started."
            jim "Don't you dare. If I'm gonna switch jobs, I'll do it myself!"
            med "Sure, you do you. But at least consider it."
            jim "Fuck off, creep."
            hide jim
            narr "He closes his eyes, but he definitely isn't falling asleep anytime soon."
            narr "I spend the rest of the flight hacking into {i}Adventure Stadium{/i} accounts..."
            narr "...culminating in an epic battle against Bonefang himself, just before my loop ends."
            narr "..."
            narr "I'm really killing this loop."
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_20_jim = 1
            return

        "Hack the plane." if persistent.loop_20_lockpicking_ability == 0:
            jump loop_20_sf_begin

        "Go to sleep." if persistent.loop_20_sleep == 0:
            narr "Great idea."
            scene black
            narr "..."
            intercom "{i}Bing.{/i}"
            scene bg plane
            intercom "Ladies and gentlemen, this is your captain speaking. As we begin our final descent..."
            narr "Ugh, my neck."
            narr "..."
            narr "Let's never do that again."
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_20_sleep = 1
            return

        "Skip to lockpicking." if persistent.loop_20_lockpicking_ability > 0 and persistent.loop_20_basement_entered == 0:
            scene black
            if persistent.loop_20_skip_initial == 0:
                narr "I repeat what I did in the previous loop."
                narr "Stealing the hammer, blowtorch, RF tranceiver and paperclips..."
                narr "...and finally breaking into the Babelgram HQ."
                narr "It's tedious, having to repeat everything again."
                narr "But I press on anyway, because I feel like I'm right on the cusp of figuring out this time loop thing, once and for all."
                $ persistent.loop_20_skip_initial = 1
            narr "..."

            call skip_lockpicking_steps from _call_skip_lockpicking_steps
            jump loop_20_babelgram_hq_begin

        "Skip to basement." if persistent.loop_20_basement_entered == 1:
            call skip_lockpicking_steps from _call_skip_lockpicking_steps_1
            $ loop_20_basement_lock_open = 1
            scene black
            narr "..."
            jump loop_20_basement

label skip_lockpicking_steps:
    python:
        loop_20_hammer = 1
        loop_20_blowtorch = 1
        loop_20_blowtorch_used = 1
        loop_20_rf_transmitter = 1
        loop_20_paperclips = 1
        loop_20_electronics_raided = 1
        loop_20_bank_raided = 1
        loop_20_hq_open = 1
        loop_20_jammer_up = 1
    return
