default persistent.loop_30_best_ending = 0
default persistent.loop_30_best_ending_restart = 0

# from https://lemmasoft.renai.us/forums/viewtopic.php?t=23852
init python:
    def word_effect(txt):
        num_frames = 5
        arr = []
        for i in range(num_frames):
            arr += [""]
        for letter in txt:
            for i in range(num_frames):
                r = renpy.random.randint(0, 2)
                if r == 0:
                    arr[i] += letter
                elif r == 1:
                    arr[i] += "{size=-1}" + letter + "{/size}"
                elif r == 2:
                    arr[i] += "{size=-2}" + letter + "{/size}"
        return arr
    dnmwt = word_effect("DO NOT MESS WITH TIME")

image dnmwt:
    Text("[dnmwt[0]]")
    pause .05
    Text("[dnmwt[1]]")
    pause .05
    Text("[dnmwt[2]]")
    pause .05
    Text("[dnmwt[3]]")
    pause .05
    Text("[dnmwt[4]]")
    pause .05
    repeat

label loop_30:
    $ loop_30_machine_disabled = 0

    scene black
    narr "..."
    scene bg basement

    if persistent.loop_30_best_ending == 1 and persistent.loop_30_best_ending_restart == 0:
        narr "...Yeah, Wish Fufillment only augments memories."
        narr "Nothing I experienced actually happened."
        narr "Well, guess I still have a world to save."
        $ persistent.loop_30_best_ending_restart = 1
    else:
        narr "I'm..."
    $ choice_around = 0
    $ choice_myself = 0
    $ choice_watch = 0

label loop_30_basement:
    scene bg basement
    menu loop_30_basement_menu:
        "Look around." if choice_around == 0:
            narr "I'm in a very familiar basement."
            narr "There's a giant metal box here, complete with an access terminal."
            $ choice_around = 1
            jump loop_30_basement

        "Look at myself." if choice_myself == 0:
            narr "I'm... in Allie's body."
            narr "..."
            $ choice_myself = 1
            jump loop_30_basement

        "Look at my watch." if choice_watch == 0:
            narr "It's... early."
            narr "Before my plane even took off."
            $ choice_watch = 1
            jump loop_30_basement

        "Look at the access terminal.":
            jump loop_30_basement_terminal

        "Go to a Wish Fulfillment center.":
            scene black
            narr "..."
            term "Matching neural pattern..."
            term "Welcome back, Allie!"
            term "Searching..."
            term "One service available -- AUTO WISH FULFILLMENT."
            term "Proceed?"
            menu:
                "Yes.":
                    $ loop_30_allie_hack = 0
                    python:
                        allie_pw = renpy.input("Enter password to continue.")
                        allie_pw = allie_pw.strip()
                        if hashlib.sha512(allie_pw).hexdigest() == "b7bd35fa137cb9b0b5a5b95faf7836ef89f0e4621e728257c946af24e9b34dbe71867dab58917af62f2601499b86d7e849a06c7edffc8364c2139dcd3b5f61a7":
                            loop_30_allie_hack = 1
                    if loop_30_allie_hack == 0:
                        term "Password incorrect."
                        jump loop_30_basement

                    term "Commencing Auto Wish Fulfillment..."
                    term "...Wish granted."
                    stop music fadeout 1.0
                    narr "..."
                    $ renpy.say(system, "Decrypting (please wait, this may take a few minutes)...", interact=False)
                    $ renpy.pause(0.1, hard=True)
                    python:
                        bg_secret_data = decrypt_secret(allie_pw, "images/bg_secret.enc")
                        bg_secret_im = im.Scale(im.Data(bg_secret_data, "bg_secret.txt"), 1280, 720)
                        track_secret_init_data = decrypt_secret(allie_pw, "audio/track-secret-init.enc")
                        audio.track_secret_init = AudioData(track_secret_init_data, "audio/track-secret-init.ogg")
                        track_secret_loop_data = decrypt_secret(allie_pw, "audio/track-secret-loop.enc")
                        audio.track_secret_loop = AudioData(track_secret_loop_data, "audio/track-secret-loop.ogg")
                    $ renpy.music.set_volume(1.0)
                    play music track_secret_init fadein 1.0
                    queue music track_secret_loop loop
                    menu:
                        "Win.":
                            pass
                    $ renpy.show("bg_secret", what=bg_secret_im)
                    narr "..."
                    narr "I..."
                    narr "I won."
                    narr "{b}Best Ending.{/b}"
                    narr ""
                    call credits from _call_credits
                    narr "..."
                    $ persistent.loop_30_best_ending = 1
                    return
                "No.":
                    term "Thank you for visiting!"
                    jump loop_30_basement

        "End the loop." if loop_30_machine_disabled == 1:
            narr "Not after all this."
            narr "Swapping bodies with a CEO is great and all, but I don't think I can survive on this little testosterone."
            narr "There has to be a better way out, I know it."
            jump loop_30_basement

label loop_30_basement_terminal:
    menu:
        "conf -reset -profile default" if persistent.loop_20_command_history_read == 1 and loop_30_machine_disabled == 0:
            narr "..."
            term "Preparing condensate..."
            term "Running pre-training tests..."
            term "All tests passed."
            term "Retraining SPAC anomaly pool..."
            term "Running post-training tests..."
            term "All tests passed."
            term "Cleanup..."
            term "Done!"
            narr "..."
            $ loop_30_machine_disabled = 1
            jump loop_30_basement_terminal

        "Run npd (Neural Pattern Database)." if persistent.loop_20_start_menu == 1:
            term "Searching for targets..."
            term "One target active."
            term "Select profile to restore."
            jump loop_30_basement_backup_start

        "Run rNR (Remote Nanoswarm Removal)." if persistent.loop_20_start_menu == 1:
            narr "..."
            narr "I have no reason to muck around with this."
            jump loop_30_basement_terminal

        "I'm done here.":
            jump loop_30_basement

label loop_30_basement_backup_start:
    menu loop_30_basement_backup:
        "80c9b4_allie_chen":
            narr "But first..."

            menu:
                "Write a note.":
                    narr "Restoring Allie's neural pattern without leaving a message would be pointless."
                    narr "In my mind, I work out a seven-paragraph essay about my time loop experience and the implications of SPAC anomalies..."
                    narr "...complete with a stern warning about the consequences of time travel."
                    narr "But it occurred to me that it'd be much more effective if I left out all but the last part."
                    narr "And so, with the words {image=dnmwt} scribbled ominously across the monitor..."
                    narr "...and after making a few cuts on my arms, just to be sure..."
                    stop music fadeout 1.0
                    narr "I hit the button."
                    narr "...and then all turns black."

            jump loop_30_epilogue

        "*** BLANK *** [[danger!!!]":
            narr "I hit the button."
            narr "...and then all turns black."
            stop music fadeout 1.0
            scene black
            narr "{b}Bad Ending.{/b}"
            $ reset_to_loop_1()
            return

        "Cancel.":
            term "Operation cancelled."
            jump loop_30_basement_terminal

label loop_30_epilogue:
    scene black
    narr ""
    narr "..."
    narr ""

    call play_track_4_halfway from _call_play_track_4_halfway_5

    david "..."
    wf_staff "How was it?"
    david "...Might be just me, but it feels like the quality's been going down."
    david "Like, I don't know. I'm still doing all the same things, and don't get me wrong, the realism is {i}stunning{/i}..."
    david "But it just doesn't feel the same, you know?"
    wf_staff "Oh! What you want is the Emotions Add-on."
    wf_staff "You can get it for just $9.99 per Wish..."
    wf_staff "Or you can become a premium member and have it included for free!"
    david "Wait, are you saying it's no longer part of the basic package?"
    wf_staff "It never was. We just throw it in as part of your first few Wishes."
    wf_staff "...Just to show what Wish Fulfillment is capable of."
    david "..."
    david "...This is rubbish."

    narr ""
    narr "..."
    narr ""

    jim "I don't think I can do this."
    ben "Why not? This is pretty big."
    ben "I mean, Babelgram itself comes to us for their security audit, and you're just gonna turn them down?"
    ben "If you don't know, hundreds of people are waiting to jump at this opportunity."
    jim "Then let them. I just don't feel comfortable working for Babelgram."
    ben "What's wrong with them? All I see is a revolutionary company with world-changing products."
    ben "My kids learn so quickly, I barely need to spend time with them at all!"
    jim "..."
    ben "Look, if you're not taking this, you're not getting your bonus this month. You know that, right?"
    jim "Yes. I think this is worth sacrificing that for."
    ben "...Okay then. And don't forget to come in tomorrow."
    ben "I know it's a Saturday, but we do have an important client meeting to prepare for."

    narr ""
    narr "..."
    narr ""

    allie "So, why do you want to join Babelgram?"
    mel "I think you guys make some really cool stuff..."
    mel "...and my strong physics background would be a valuable addition to the company."
    allie "That's awesome! Which product excites you the most?"
    mel "Heh, they're all cool. But the BabySteps line just blows my mind."
    mel "It's like we've completely eliminated infancy from the timeline of human development!"
    allie "Oh, I'm super hyped about that too!{w} Did you read the papers?"
    mel "Yeah! They use chronotopic SPAC mixtures, don't they?"
    allie "Just for communication. We had that since the Platinum days, in fact."
    mel "Wow, it's been... five years already, hasn't it?"
    mel "Funny how you guys figured it out before Wish Fulfillment."
    allie "Actually, we bought the tech {i}from{/i} them. They just couldn't figure out how to productize it."
    allie "They were too ambitious, I think, trying to use SPACs for computation."
    allie "{i}We{/i} figured we could use them for high-bandwidth data transfer."
    mel "Wait... if you've had SPAC mixtures for the last five years..."
    mel "Did anyone try sending information backwards in time?"
    mel "From what I hear, it's pretty much as simple as inverting the electric field."
    allie "Uhh..."
    allie "..."
    narr "She looks at her arms."
    allie "...I guess we just never thought it was possible."
    allie "Not until Johannes-Tanaka, anyway."
    mel "Oh, but by then..."
    mel "Sometimes it feels like we'd have conquered all of physics by now if it weren't for those darn regulations."
    allie "...Eh, I think they're for the better."
    allie "Safety's kinda important when dealing with this stuff, y'know?"
    narr "..."
    narr "{b}Good Ending.{/b}"
    narr ""
    call credits from _call_credits_1
    narr "..."
    $ persistent.game_finished = 1
    $ reset_to_loop_1()
    return

label credits:
    narr "{b}--- CREDITS ---{/b}"
    narr "Story, art, and music by Mark."
    narr "Made for CMS.618 (Interactive Narrative) at MIT."
    narr "Special thanks to Nick Monfort, and everyone who helped with playtesting."
    narr "Thanks for playing my game!"
    return
