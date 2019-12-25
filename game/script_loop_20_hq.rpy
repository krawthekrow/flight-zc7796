default persistent.loop_20_babelgram_house_examined = 0

default persistent.loop_20_desks_searched = 0
default persistent.loop_20_workbench_seen = 0
default persistent.loop_20_mice_seen = 0
default persistent.loop_20_chat_found = 0

default persistent.loop_20_basement_door_examined = 0
default persistent.loop_20_basement_door_listen = 0
default persistent.loop_20_basement_entered = 0
default persistent.loop_20_lockpicking_ability = 0

default persistnet.loop_20_pulse_felt = 0
default persistent.loop_20_allie_purged_initial = 0
default persistent.loop_20_access_terminal_seen = 0
default persistent.loop_20_access_terminal_desc_seen = 0
default persistent.loop_20_start_menu = 0
default persistent.loop_20_command_history_read = 0
default persistent.loop_20_allie_known = 0

default persistent.loop_20_allie_pacified = 0

default persistent.loop_20_time_loop_resets = 0

label loop_20_display_command_history:
    term "conf -reset -profile default"
    term "conf -match $ALLIE_PREF* -set mode:direct -set detune:abs,-10"
    term "transfer -override -match $ALLIE_PREF*"
    term "conf -match $ALLIE_PREF* -set mode:direct -set detune:abs,-300"
    term "transfer -overide -match $ALLIE_PREF*"
    term "transfer -override -match $ALLIE_PREF*"
    term "conf -match $ALLIE_PERF* -set mode:direct -set detune:abs,-28800"
    term "transfer -override -match $ALLIE_PREF*"
    return

label loop_20_outside_babelgram_hq_begin:
    scene bg outside_hq

    narr "The Babelgram HQ looks like an ordinary office."
    narr "It's protected by a glass security door with a magnetic lock."

    menu loop_20_outside_babelgram_hq:
        "What should I do?"

        "Look around the building." if persistent.loop_20_babelgram_house_examined == 0:
            narr "Hmm..."
            narr "There's also a window here. It looks like a completely normal window."
            narr "Heh, I guess that's an entry point."
            $ persistent.loop_20_babelgram_house_examined = 1
            jump loop_20_outside_babelgram_hq

        "Hack the alarm system." if loop_20_rf_transmitter == 1 and loop_20_jammer_up == 0:
            narr "I turn my laptop on, connect the RF tranceiver, and download the hacking program."
            narr "...Yeah, no need to write your own hacks when someone else already did it for you."
            narr "After a few seconds, the program reports that the alarm system has been disabled."
            $ loop_20_jammer_up = 1
            jump loop_20_outside_babelgram_hq

        "Smash the window." if loop_20_hq_open == 0 and persistent.loop_20_babelgram_house_examined == 1:
            if loop_20_hammer == 0:
                narr "I whack the window with my fists."
                narr "..."
                narr "It's no use."
                narr "Maybe if I had a tool of some sort."
                jump loop_20_outside_babelgram_hq
            elif loop_20_jammer_up == 1:
                narr "I smash the window with the hammer, then unlock it from the inside."
                narr "No alarm sounds this time."
                narr "I guess I'm good."
                narr "..."
                $ loop_20_hq_open = 1
                jump loop_20_babelgram_hq_begin
            elif persistent.loop_20_security_system_seen == 1:
                narr "Not before disabling the alarm system!"
                jump loop_20_outside_babelgram_hq
            elif loop_20_jammer_up == 0:
                narr "I smash the window with the hammer."
                narr "The window crumbles into pieces."
                narr "I reach my hand in to unlock it, when..."
                narr "{i}BEEP. BEEP. BEEP.{/i}"
                narr "Yikes, an alarm system!"

                narr "..."

                narr "The police were here in no time."
                narr "I didn't bother running away. They're just gonna forget it all by the next loop anyway."
                narr "But I did get the make and model of the alarm system."
                narr "A quick Internet search revealed that it can be easily hacked."
                narr "I just need an RF transmitter to send the right frequencies..."
                narr "..."
                $ persistent.loop_20_security_system_seen = 1
                jump loop_20_end

        "Break the door." if loop_20_hq_open == 0:
            if loop_20_hammer == 0:
                narr "I whack the door with my fists."
                narr "..."
                narr "It's no use."
                narr "Maybe if I had a tool of some sort."
                jump loop_20_outside_babelgram_hq
            else:
                narr "I whack the door with the hammer."
                narr "{i}BANG! BANG! BANG!{/i}"
                narr "Spider-web cracks form on the door, but it doesn't break."
                narr "Goddamn security glass."
                narr "Maybe it'd be easier to attack the lock directly. What could I use to destroy a magnet?"
                jump loop_20_outside_babelgram_hq

        "Blowtorch the magnet lock." if loop_20_hq_open == 0 and loop_20_blowtorch == 1:
            if loop_20_blowtorch_used == 1:
                narr "My blowtorch is out of fuel."
                jump loop_20_outside_babelgram_hq
            else:
                narr "I use the remaining fuel in the blowtorch to destroy the magnet."
                narr "Before long, the door swings open."
                $ loop_20_blowtorch_used = 1
                $ loop_20_hq_open = 1
                jump loop_20_babelgram_hq_begin

        "I'm done here.":
            narr "Okay."

            jump loop_20_sf

label loop_20_babelgram_hq_begin:
    scene bg hq

    narr "So this is the Babelgram HQ."
    narr "Two rows of messy desks, a hardware workbench, a cage of... mice?"
    if persistent.loop_20_basement_entered == 0:
        narr "...and an unmarked door."
    else:
        narr "...and a door to the basement."

label loop_20_babelgram_hq:
    scene bg hq
    $ door_name = "basement door" if persistent.loop_20_basement_entered == 1 else "unmarked door"
    $ allow_pick = persistent.loop_20_basement_door_examined == 1 and loop_20_basement_lock_open == 0

    menu loop_20_babelgram_hq_menu:
        "What shall I do?"

        "Search the desks." if persistent.loop_20_desks_searched == 0:
            narr "They are packed with computers, prototype Babelgrams and all sorts of personal items."
            narr "...Nope, no paper documents about how Babelgram actually works."
            $ persistent.loop_20_desks_searched = 1
            jump loop_20_babelgram_hq

        "Boot up a computer." if persistent.loop_20_desks_searched == 1:
            if persistent.loop_20_chat_found == 0:
                narr "..."
                narr "Damn, these computers are new. The drives are auto-encrypted."
                narr "...Guess I'll have to make do with a guest account."
                narr "..."
                narr "Oh hey, FastTalk!"
                narr "Wasn't there something about FastTalk storing their caches in a public directory?"
                narr "...Aha! Here it is."
                $ persistent.loop_20_chat_found = 1
            menu loop_20_babelgram_chat:
                ".cache.48550b.FRAG":
                    term "□witch to quantum□"
                    term "app theres 5x spedup for ccz what do you think□"
                    term "39a0a1|It's very expensive.□"
                    term "118ba0|hm? same price as reg server □https://quboid.com/products/servers/6f7f1d7c5e660396_484b?uid=119□□"
                    term "30a0a1|Sent you a document.□"
                    term "The cost on the website does not include thermals and power management.□"
                    term "Total with tax would be 20x as much.□"
                    term "118ba0|oic□"
                    term "fuckig hidden costs□"
                    jump loop_20_babelgram_chat
                ".cache.488cd2.FRAG":
                    term "□hy i have to kep saying this, but STOP RNRING CUSTOMERS!!□"
                    term "its COLD NR or DEATH. rnr is NO LONGER AN OPTION□□"
                    term "like if read□□□□□"
                    term "39a0a1|Jack said that the customer explicitly requested rNR.□"
                    term "118ba0|that doesnt change anything!!!□"
                    term "cust can still sue even with writen consent□□"
                    term "39a0a1|Wfh today.□"
                    term "440f17|boba?□□□□"
                    jump loop_20_babelgram_chat
                ".cache.48a119.FRAG":
                    term "□y I have a problem□"
                    term "Npd isnt working□"
                    term "440f17|try -override□"
                    term "783bad|Alr did, no effect□"
                    term "440f17|what you doing□"
                    term "783bad|Restoring backup to mouse□"
                    term "Tried like 5 times. Still not moving□"
                    term "440f17|is it still alive□"
                    term "783bad|Oh no it isn't□"
                    term "440f17|wtf did we leave the mice on blank for too long agn□"
                    jump loop_20_babelgram_chat
                "Back.":
                    jump loop_20_babelgram_hq

        "Look at the workbench." if persistent.loop_20_workbench_seen == 0:
            narr "There's a bunch of soldering stations here, and a 3D printer."
            narr "Also, all sorts of electrical tools, such as pliers and wire cutters."
            $ persistent.loop_20_workbench_seen = 1
            jump loop_20_babelgram_hq

        "Look at the mice." if persistent.loop_20_mice_seen == 0:
            narr "They're all wearing tiny helmets on their heads. Mini-Babelgrams?"
            narr "They also all seem to be sleeping."
            narr "I give one a poke."
            narr "..."
            narr "Looks like he's very fast asleep."
            narr "That, or... nah, I don't wanna think about it."
            $ persistent.loop_20_mice_seen = 1
            jump loop_20_babelgram_hq

        "Open the [door_name]." if not allow_pick:
            if loop_20_basement_lock_open == 1:
                jump loop_20_basement_begin
            elif persistent.loop_20_basement_door_examined == 0:
                narr "Huh."
                narr "The door's locked."
                narr "Nothing fancy, though. Just a pin tumber lock."
                $ persistent.loop_20_basement_door_examined = 1
                jump loop_20_babelgram_hq
            else:
                narr "I can't. It's locked."
                jump loop_20_babelgram_hq

        "Listen through the unmarked door." if persistent.loop_20_basement_door_examined == 1 and persistent.loop_20_basement_entered == 0 and persistent.loop_20_basement_door_listen == 0:
            narr "I'm not sure what I expect to hear, but..."
            narr "Huh? There seems to be a faint thumping noise."
            $ persistent.loop_20_basement_door_listen = 1
            jump loop_20_babelgram_hq

        "Pick the lock on the [door_name]." if allow_pick:
            if loop_20_basement_lock_jam == 1:
                narr "I can't. The lock's jammed."
                narr "I don't think there's any way to unjam a lock."
                narr "...Not in this loop, anyway."
                jump loop_20_babelgram_hq
            elif loop_20_paperclips == 0:
                narr "I don't have anything to pick the lock with."
                if persistent.loop_20_lockpicking_ability == 0:
                    narr "I tried using the wires on the workbench, but they're too flexible."
                else:
                    narr "Didn't I have a pair of paperclips last time?"
                jump loop_20_babelgram_hq
            elif persistent.loop_20_lockpicking_ability == 0:
                narr "{i}Clickity-clack. Clickity-clack.{/i}"
                narr "This is way harder than the wikihow article made it look."
                narr "{i}Click-click. Clickity-clack.{/i}"
                narr "...Maybe because I'm making do with a pair of goddamn paperclips."
                narr "{i}Clack-{/i}"
                narr "Ugh! Finger slipped!"
                narr "Stupid, stupid..."
                narr "..."
                narr "{i}Clickity-clack. Clickity-clack.{/i}"
                narr "Also, the lock's a little old."
                narr "{i}Clickity-clack. Click-click. {/i}"
                narr "And the tension wrench doesn't fit very well..."
                narr "{i}Clickity-clack. Clickity-clack.{/i}"
                narr "I don't ever want to do this again."
                narr "{i}Click-click. Click-{/i}"
                narr "..."
                narr "I did it!"
                narr "I picked the lock...!"
                narr "..."
                narr "Why isn't the door opening?"
                narr "..."
                narr "Oh, I picked it the wrong way..."
                narr "Fuck, fuck, fuck. Fuck!"
                narr "A plug spinner? Where am I supposed to find something like that?"
                narr "Screw this. I'll just pick it again."
                narr "..."
                narr "{i}Clickity-clack. Clickity-clack.{/i}"
                narr "{i}Clickity-clack. Clickity-{/i}"
                narr "Huh?"
                narr "..."
                narr "The rake broke."
                narr "Fuck."
                narr "Now the lock's jammed."
                $ loop_20_basement_lock_jam = 1
                $ persistent.loop_20_lockpicking_ability = 1
                jump loop_20_babelgram_hq
            elif persistent.loop_20_lockpicking_ability == 1:
                narr "Okay, I'll make sure to pick it the {i}right{/i} way this time."
                narr "{i}Clickity-clack. Clickity-clack.{/i}"
                narr "..."
                narr "{i}Clickity-clack. Click-{/i}"
                narr "..."
                narr "{i}Clickity-clack. Clickity-clack.{/i}"
                narr "..."
                narr "{i}Click-click-click-{/i}"
                narr "I did it!"
                narr "And it only took me half an hour!"
                $ loop_20_basement_lock_open = 1
                $ persistent.loop_20_lockpicking_ability = 2
                jump loop_20_basement_begin
            elif persistent.loop_20_lockpicking_ability == 2:
                narr "{i}Clickity-clack. Click-{/i}"
                narr "..."
                narr "{i}Clickity-clack. Clickity-clack.{/i}"
                narr "..."
                narr "{i}Click-click-click-{/i}"
                narr "I did it!"
                narr "And it only took me ten minutes!"
                $ loop_20_basement_lock_open = 1
                $ persistent.loop_20_lockpicking_ability = 3
                jump loop_20_basement_begin
            elif persistent.loop_20_lockpicking_ability == 3:
                narr "{i}Clickity-clack. Click-{/i}"
                narr "..."
                narr "{i}Click-click-click-{/i}"
                narr "I did it!"
                narr "And it only took me two minutes!"
                $ loop_20_basement_lock_open = 1
                $ persistent.loop_20_lockpicking_ability = 4
                jump loop_20_basement_begin
            elif persistent.loop_20_lockpicking_ability == 4:
                narr "{i}Click-click-click-{/i}"
                narr "I did it!"
                narr "And it only took me 30 seconds!"
                $ loop_20_basement_lock_open = 1
                jump loop_20_basement_begin

        "I'm done here.":
            narr "I exit the building."

            jump loop_20_sf

label know_allie:
    if persistent.loop_20_allie_known == 0:
        narr "(Well, I guess I know that's Allie now.)"
        $ persistent.loop_20_allie_known = 1
    return

label loop_20_allie_cube:
    narr "Allie's lying motionless on the floor."
    narr "...There's a small, metallic cube on her tongue."
    narr "Embossed on its top face is a five-pointed star."
    $ persistent.loop_20_allie_purged_initial = 1

    menu:
        "What do I do with the cube?"

        "Eat it.":
            narr "I eat the cube."
            narr "I feel it melt in my mouth and wash through my skull."
            narr "And then..."
            narr "A massive headache."
            scene black
            stop music fadeout 1.0
            narr "As I lie on the floor, the burning sensation in my head only grows stronger."
            narr "I can almost feel the two nanoswarms duking it out over my brain."
            narr "As the last of my consciousness fades away..."
            narr "My only thought is..."
            narr "..."
            narr "..."
            narr ""
            $ loop_20_allie_cube_on_tongue = 0
            $ loop_20_dead = 1
            jump loop_20_end

        "Keep it.":
            narr "I keep the cube."
            $ loop_20_allie_cube_on_tongue = 0
            $ loop_20_allie_cube = 1
            jump loop_20_basement

label loop_20_basement_begin:
    if persistent.loop_20_basement_entered == 0:
        narr "I carefully open the door."
        narr "Behind it is a flight of stairs leading down into a basement."
        narr "I descend with trepidation."

        scene black
        stop music fadeout 1.0
        narr "..."
        call play_track_5 from _call_play_track_5_1
        scene bg basement

        med "Ah!-"
        narr "I smother my scream."
        narr "Is that..."
        med "Allie?"
        if persistent.loop_20_allie_pacified == 0:
            allieq "Bwa-wa. Bwa-wa."
            narr "{i}Thump. Thump.{/i}"
            allieq "Ba-wa?"
        narr "At least, I {i}think{/i} that's her..."
        narr "...going by the few pictures I saw of her when I did my research on Babelgram."
        if persistent.loop_20_allie_pacified == 0:
            narr "Whoever this is, she's lying on the floor, thumping the ground methodically with her fists."
            narr "...and she doesn't seem to respond to \"Allie\"."
        else:
            narr "..."
            narr "...Is she dead?"

        $ persistent.loop_20_basement_entered = 1
    else:
        narr "I enter the basement."
        scene black
        narr "..."
        scene bg basement

label loop_20_basement:
    scene bg basement
    menu loop_20_basement_menu:
        "What shall I do?"

        "Feel for Allie's pulse." if persistent.loop_20_allie_pacified == 1 and persistent.loop_20_pulse_felt == 0:
            narr "..."
            narr "Nope, still alive."
            $ persistent.loop_20_pulse_felt = 1
            jump loop_20_basement

        "Look at Allie." if loop_20_allie_cube_on_tongue:
            jump loop_20_allie_cube

        "Look around.":
            if loop_20_allie_cube_on_tongue:
                jump loop_20_allie_cube

            $ allie_with_q = "Allie(?)" if (persistent.loop_20_allie_known == 0) else "Allie"
            if persistent.loop_20_allie_pacified == 0:
                narr "[allie_with_q] is on the floor, thumping the ground methodically with her fists."
            else:
                narr "[allie_with_q] is lying motionless on the floor."
            narr "There's also a giant metal box here, complete with an access terminal."
            narr "A glass panel reveals its contents – a mess of complicated machinery and piping that I don't pretend to understand."
            $ persistent.loop_20_access_terminal_seen = 1
            jump loop_20_basement

        "Use the access terminal." if persistent.loop_20_access_terminal_seen == 1:
            if persistent.loop_20_access_terminal_desc_seen == 0:
                narr "Whatever's in that box seems to be running an ancient version of Windows."
                narr "There's a program open, which looks like a thin GUI wrapper around some command-line interface."
                $ persistent.loop_20_access_terminal_desc_seen = 1
            else:
                scene bg basement
            jump loop_20_basement_terminal

        "Go back upstairs.":
            narr "I don't think there's anything left to do outside this basement..."
            narr "But okay, I'll go back upstairs."

            scene black
            narr "..."

            jump loop_20_babelgram_hq

    menu loop_20_basement_terminal:
        "What shall I do?"

        "Open the start menu." if persistent.loop_20_start_menu == 0:
            narr "There seems to be a few other programs installed."
            term "npd (Neural Pattern Database)"
            term "rNR (Remote Nanoswarm Removal)"
            narr "Hmm..."
            $ persistent.loop_20_start_menu = 1
            jump loop_20_basement_terminal

        "Read command history.":
            if persistent.loop_20_command_history_read == 0:
                call loop_20_display_command_history from _call_loop_20_display_command_history
                narr "..."
            narr "The typos..."
            narr "...Was it a {i}typo{/i} that created my time loop?"
            $ persistent.loop_20_command_history_read = 1
            jump loop_20_basement_terminal

        "conf -reset -profile default" if persistent.loop_20_command_history_read == 1 and loop_20_machine_disabled == 0:
            $ loop_20_understand_command = persistent.loop_20_time_loop_resets >= 2
            if loop_20_understand_command:
                system "So, it looks like this kills the time loop."
                system "Jim doesn't actually know this, because he only ever gets to try it once."
                system "But he's not going to like it if the loop ends like this."
                system "He just committed a whole range of crimes, and he's still trapped in [persistent.youname!c]'s body."
                system "Just sayin'."
                system "Proceed anyway?"
                menu:
                    "Yes.":
                        system "Okay. Don't say I didn't warn you."
                    "No.":
                        jump loop_20_basement_terminal
            narr "I carefully type the command into the console."
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
            narr "...Huh, did that do anything?"
            narr "Maybe I shouldn't be typing in commands I don't understand."
            $ loop_20_machine_disabled = 1
            $ persistent.loop_20_time_loop_resets += 1
            jump loop_20_basement_terminal

        "Run npd (Neural Pattern Database)." if persistent.loop_20_start_menu == 1:
            term "Searching for targets..."
            if loop_20_allie_purged:
                term "No targets found."
                narr "Hmm."
                jump loop_20_basement_terminal
            else:
                term "One target active."
                term "Select profile to restore."
                jump loop_20_basement_backup_start

        "Run rNR (Remote Nanoswarm Removal)." if persistent.loop_20_start_menu == 1:
            term "WARNING: May cause stroke, migraines, and possibly nausea."
            term "Unauthorized use on human subjects is PUNISHABLE BY LAW."
            term "If human nanoswarm removal is necessary, prefer CNRP procedures where applicable."
            narr "..."
            term "Select target."
            jump loop_20_basement_removal_start

        "Step away from the terminal.":
            narr "Alright, I step away from the terminal."
            jump loop_20_basement

label loop_20_basement_removal_start:
    python:
        youname_id = persistent.youname.replace(" ", "_")
    menu loop_20_basement_removal:
        "usr_[youname_id]":
            stop music fadeout 1.0
            narr "Immediately after I hit the button, a searing pain tears through my head."
            narr "I fall to the ground, overcome by a sudden weakness."
            narr "And then the whole room collapses into flashes of light."
            narr "As I lie on the floor convulsing, I feel a small cube form at the tip of my tongue and fall onto the floor."
            narr "But the pain does not stop. I feel faint, very faint."
            narr "And around me, the room is spinning."
            narr "I summon the last of my strength and consider my options."

            menu:
                "Eat my cube.":
                    narr "I reach out and shove my cube back into my mouth."
                "Eat Allie's cube." if loop_20_allie_cube == 1:
                    narr "I reach into my pocket and shove Allie's cube into my mouth."
                    $ loop_20_allie_cube_eaten = 1
                "Lie and wait.":
                    narr "I do nothing."
                    $ loop_20_self_purged = 1

            narr "And, just like that, I black out."
            jump loop_20_end
                
        "adm_alliec" if loop_20_allie_purged == 0:
            if persistent.loop_20_allie_pacified == 0:
                narr "A scream echoes behind me."
                narr "I turn to see Allie, convulsing on the floor."
                call know_allie from _call_know_allie
                narr "Slowly, the convulsing stops, and she coughs a cube out onto the floor."
                narr "...But before I can grab it, she laps it right off the floor with her tongue."
                narr "...Hmm."
                narr "Maybe I should find a way to pacify her first."
            else:
                term "..."
                term "Procedure complete."
                if persistent.loop_20_allie_purged_initial == 0:
                    narr "..."
                    narr "...Did anything happen?"
                $ loop_20_allie_cube_on_tongue = 1
                $ loop_20_allie_purged = 1
            jump loop_20_basement
        "Ctrl-C.":
            term "Process exited with status 130"
            jump loop_20_basement_terminal

label loop_20_basement_backup_start:
    menu loop_20_basement_backup:
        "80c9b4_allie_chen":
            narr "..."
            stop music fadeout 1.0
            allie "Wha... Who are you?"
            call know_allie from _call_know_allie_1
            med "I'm... uh..."
            narr "I stare at Allie, unsure what to reply."
            narr "Am I Jim?"
            narr "...Or am I [persistent.youname!c]?"
            allie "This is bad. This is so, so, so bad."
            narr "She's typing things into the access terminal."
            allie "What did you do to my SPAC?"
            med "Nothing, I just restored your... profile, or something like that."
            allie "What?!"
            med "When I arrived, I found you thumping the floor. I think you lost your mind somehow."
            med "...so I restored you. I think you ought to thank me for that."
            allie "Why are you even here in the first place?!"
            med "I was... inspecting a Babelgram-induced time loop."
            allie "A what?!"
            med "A time loop! Uhh... it's like, when..."
            narr "Allie doesn't seem to be listening."
            allie "...because as far as I can tell, {i}you{/i} came into this room and reset my brain!"
            med "I didn't! Don't you have cameras around here?"
            allie "Argh, I {i}knew{/i} we should've fixed the cameras right away..."
            med "What?! How long have they been broken for?"
            allie "..."
            allie "It doesn't matter! You're coming with me."
            narr "And with that, she grabs my arm and leads me out of the basement."

            scene black
            narr "..."

            call play_track_4_halfway from _call_play_track_4_halfway_1
            narr "It took me too long to figure out where she was leading me."
            narr "By the time we reached the police station, it was already too late."
            narr "There was footage of me breaking and entering, but no footage of me saving Allie's life."
            narr "It was then, while trying to comprehend what had happened, when I noticed the midday sun shining through the window."
            narr "..."
            narr "I had escaped my time loop."
            narr "But faced with a long jail term and a career in shambles..."
            narr "...not to mention still being trapped in [persistent.youname!c]'s body..."
            narr "..."
            narr "...I'm not sure this was quite the escape I was looking for."
            scene black
            narr "{b}Normal Ending.{/b}"
            $ reset_to_loop_1()
            return

        "*** BLANK *** [[danger!!!]":
            term "Restoring..."
            narr "..."
            if persistent.loop_20_allie_pacified == 1:
                narr "...Nothing happens."
            else:
                narr "The thumping noise stops."
                narr "I turn to see Allie, now lying motionless on the floor."
                call know_allie from _call_know_allie_2
                if persistent.loop_20_pulse_felt == 0:
                    narr "Is she... dead?"
                $ persistent.loop_20_allie_pacified = 1
            jump loop_20_basement

        "Cancel.":
            term "Operation cancelled."
            jump loop_20_basement_terminal

label loop_20_unconscious_end:
    scene black
    narr "..."
    call play_track_4_halfway from _call_play_track_4_halfway_2
    narr "I wake up in a jail cell."
    narr "My charges are read to me."
    narr "Trespassing, murder, unauthorized Wish Fulfillment..."
    narr "...separately, hijacking and unauthorized computer access."
    narr "As I sit dazed, trying to remember what got me into this mess..."
    narr "A clock on the wall catches my attention."
    narr "I..."
    narr "I escaped the time loop."
    narr "..."
    narr "But then again, if {i}this{/i} was what escaping entailed..."
    narr "...I'd much rather not have escaped at all."
    narr "It wasn't until a while later when I realized that I'm still trapped in [persistent.youname!c]'s body."
    narr "..."
    scene black
    narr "{b}Normal Ending.{/b}"
    $ reset_to_loop_1()
    return

label loop_20_machine_disabled_end:
    scene black
    stop music fadeout 1.0
    narr "..."
    narr "...Huh."
    narr "I look at my watch."
    narr "I... escaped! I escaped the time loop!"
    narr "I walk down the streets of San Francisco, overcome by euphoria."
    narr "The streets are busy now. The sun has risen, and people are going to work."
    narr "And then it occurs to me."
    call play_track_4_halfway from _call_play_track_4_halfway_3
    narr "I just hacked into a plane and broke into multiple buildings..."
    narr "...and I didn't put any effort into hiding my tracks."
    narr "Also, I'm still trapped in [persistent.youname!c]'s body."
    narr "..."
    narr "I'm fucked."
    narr "..."
    scene black
    narr "{b}Normal Ending.{/b}"
    $ reset_to_loop_1()
    return

label loop_20_end:
    if loop_20_self_purged:
        jump loop_20_unconscious_end
    if loop_20_allie_cube_eaten:
        if loop_20_machine_disabled:
            jump loop_20_unconscious_end
        else:
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_20_allie_pacified = 0
            $ persistent.loop = 30
            $ persistent.character = 3
            $ persistent.loop_30_unlocked = 1
            return
    if loop_20_dead == 1:
        scene black
        narr "{b}Bad Ending.{/b}"
        $ reset_to_loop_1()
        return
    if loop_20_machine_disabled:
        jump loop_20_machine_disabled_end
    scene black
    narr "{b}Bad Ending.{/b}"
    if loop_20_allie_purged:
        $ persistent.loop_20_allie_pacified = 0
    return
