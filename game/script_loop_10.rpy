default persistent.loop_10_instructions_seen = 0
default persistent.loop_10_comfortable = 0
default persistent.loop_10_neighbors = 0
default persistent.loop_10_mel_progress = 0
default persistent.loop_10_gave_up_john = 0
default persistent.loop_10_andy = 0
default persistent.loop_10_john_explanation = 0
default persistent.loop_10_ask_nicely = 0
default persistent.loop_10_convince = 0
default persistent.loop_10_bomb_here = 0
default persistent.loop_10_bomb_cockpit = 0

label loop_10:
    $ loop_10_jim_attempt = 0
    $ persistent.loop_10_seen = 1

    scene bg plane

    intercom "{i}Bing.{/i}"
    intercom "Ladies and gentlemen, this is your captain speaking. We have reached cruising altitude..."
    narr "You wrestle the Babelgram off your head."

    $ choice_mel_book = 0

    menu loop_10_takeoff:
        "What will you do?"

        "Get comfortable." if persistent.loop_10_comfortable == 0:
            narr "If you haven't figured out how to get comfortable after so many loops..."
            narr "...you sure as heck aren't gonna get comfortable now."
            $ persistent.loop_10_comfortable = 1
            jump loop_10_takeoff

        "Look at your neighbors." if persistent.loop_10_neighbors == 0:
            narr "You sneak a bored glance at your neighbors."
            narr "On your left, Melinda Trawney, reading the same book as always."
            narr "On your right, James Carlson, shifting uncomfortably in his seat."
            $ persistent.loop_10_neighbors = 1
            jump loop_10_takeoff

        "Peek at Mel's book." if persistent.loop_10_neighbors == 1 and choice_mel_book == 0:
            narr "{i}Non-Abelian Gauge Theory{/i}, by Ivan Nikolaev."
            if persistent.loop_10_mel_progress == 0:
                narr "It's filled with equations you can't be bothered to understand."
            elif persistent.loop_10_mel_progress == 1:
                narr "It's filled with equations you can scarcely understand."
            elif persistent.loop_10_mel_progress == 2:
                narr "It's filled with equations you wish you understood."
            elif persistent.loop_10_mel_progress == 3:
                narr "It's filled with equations that look strange, yet familiar."
            elif persistent.loop_10_mel_progress == 4:
                narr "It's filled with equations you almost comprehend."
            elif persistent.loop_10_mel_progress >= 5:
                narr "It's filled with equations you find pointless and dull."
            $ choice_mel_book = 1
            jump loop_10_takeoff

        "Run John." if loop_10_jim_attempt == 0 and persistent.loop_10_gave_up_john == 0:
            if persistent.loop_10_john_explanation == 0:
                narr "You turn your laptop on and follow the same routine you've performed hundreds of times."
                narr "Create an account, enter credit card details, spin up a GPU cluster, install John, modify the progress file..."
                narr "Tedious, excruciating steps, burned into your brain."
                narr "But you follow through anyway..."
                narr "...because as far as you can tell, this is your only route to freedom."
                narr "..."
                narr "Finally, it's done."
                narr "And now, you have five hours."
                $ persistent.loop_10_john_explanation = 1
            else:
                narr "..."
                narr "Alright, it's up."
            jump loop_10_john

        "Call Andy." if persistent.loop_10_andy == 0:
            narr "You send a text message to Andy before calling him."
            narr "He doesn't pick up, as always."
            narr "You call him again."
            narr "He still doesn't pick up, as always."
            narr "You call him a third time."
            andy "What happened to him?!"
            you "He very hurt. Big pain."
            andy "What's with all that noise?!"
            you "Noise? Is, how you say, is {i}avión{/i}. You talk {i}español{/i}?"
            andy "Where the fuck is this?! Does no one speak English there?!"
            you "Sorry, cannot understand. He cannot be here. You help?"
            andy "Ah, fuck this! Gimme a sec."
            narr "You here the sound of buckles snapping into place."
            narr "..."
            andy "What the fuck?! How..."
            you "What happened?"
            andy "Who are you? What'd you do to me?"
            you "Check your watch."
            andy "Wha-"
            you "Did you jump back in time?"
            andy "You... you're the one who called about my son! Fuck!"
            andy "Do you know what you've done?!"
            you "I tricked you into using your Babelgram."
            andy "That was {i}it{/i}?"
            andy "You made me wake up in the middle of the night, call the police, spend the {i}whole night{/i} worrying about my son..."
            andy "...{i}just{/i} so that I would use my {i}Babelgram{/i}?!"
            you "Yeah."
            you "Sorry, but I had to. There was no other way."
            andy "What the hell was {i}that{/i} supposed to achieve?!"
            you "I wanted to check that I'm not the only one affected by this time loop."
            andy "Affected by {i}what{/i}?"
            you "This {i}time loop.{/i} You know Groundhog Day?"
            andy "Is that a TV show?!"
            you "No, it's a movie."
            you "You see, I'm on a plane right now, and every time it lands, I get transported six hours back in time-"
            narr "*click*"
            narr "..."
            narr "He hung up."
            narr "Well, at least you're sure it's the Babelgram now."
            narr "Reminding yourself that Andy will forget everything again once the next loop comes around..."
            narr "...you slump into your chair and fall rapidly to sleep."
            scene black
            narr "..."
            scene bg plane
            narr "A vibration on your lap stirs you awake."
            narr "You pick up your phone."
            you "You called back."
            andy "I know what you did, you motherfucker. You used the Babelgram to implant those memories!"
            you "No, I didn't! It's Babelgram, they trapped us in a-"
            andy "Why'd you do that?! Answer me!"
            you "It. Wasn't. Me! I'm trapped in the same loop as you are-"
            andy "I don't care about your fucking fruit loops, I care about what you did to me!"
            you "Look, as far as I can tell, there's a bug, a bug in Babelgram, the Platinum model-"
            andy "You're not getting anywhere, you... you mind rapist!"
            andy "I'm calling the police on you, right now!"
            you "That's not gonna do anything! I'm on a plane, and every time it lands-"
            andy "{i}Hello, police? I've been mindraped! ...Someone implanted memories into me!{/i}"
            andy "{i}No, I didn't consent. ...Unauthorized Wish Fulfillment? Sure, you can call it that.{/i}"
            andy "{i}...I don't know, he used my Babelgram!{/i}"
            narr "You hang up."
            narr "Maybe you'll just call him again next loop. See how he likes being trapped himself..."
            narr "On second thoughts, maybe not. You wouldn't wish this on anyone, not even your worse enemies."
            narr "You spend the rest of the flight sleeping, exhausted from the interaction."

            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_andy = 1

            return

        "Talk to Jim." if persistent.loop_10_neighbors == 1 and loop_10_jim_attempt == 0:
            jump loop_10_hack

        "Talk to Mel." if loop_10_jim_attempt == 0 and persistent.loop_10_neighbors == 1 and persistent.loop_10_mel_progress == 0:
            call loop_10_mel_1 from _call_loop_10_mel_1
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 1
            return
        "Talk to Mel." if loop_10_jim_attempt == 0 and persistent.loop_10_mel_progress == 5:
            call loop_10_mel_6 from _call_loop_10_mel_6
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 6
            $ persistent.loop_10_gave_up_john = 1
            return
        "Talk to Mel." if loop_10_jim_attempt == 0 and persistent.loop_10_mel_progress == 6:
            call loop_10_mel_7 from _call_loop_10_mel_7
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 7
            return
        "Talk to Mel." if loop_10_jim_attempt == 0 and persistent.loop_10_mel_progress == 7:
            call loop_10_mel_8 from _call_loop_10_mel_8
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 8
            return
        "Talk to Mel." if loop_10_jim_attempt == 0 and persistent.loop_10_mel_progress == 8:
            call loop_10_mel_9 from _call_loop_10_mel_9
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 9
            return
        "Talk to Mel." if loop_10_jim_attempt == 0 and persistent.loop_10_mel_progress == 9:
            call loop_10_mel_10 from _call_loop_10_mel_10
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 11
            return

        "Go to sleep." if loop_10_jim_attempt == 1:
            narr "You sleep off the rest of the flight."
            scene black
            narr "{b}Bad Ending.{/b}"
            return

    menu loop_10_john:
        "What will you do now?"

        "Watch {i}American Turd{/i}." if persistent.loop_10_mel_progress == 0:
            narr "You spend the rest of the flight watching {i}American Turd{/i}."
            narr "Its occasional slapstick humor just barely makes up for its mind-numbing political commentary."
            narr "...is what you tell yourself to rationalize such an obviously ill-advised decision."
            jump loop_10_john_watch_end

        "Watch {i}A Hero Is You{/i}." if persistent.loop_10_mel_progress == 0:
            narr "You spend the rest of the flight watching {i}A Hero Is You{/i}."
            narr "Its meta-postmodernistic humor meets your ears with disinterest –"
            narr "– you've already heard the same jokes hundreds of times in hundreds of different ways."
            jump loop_10_john_watch_end

        "Watch {i}Tomorrow's Sunset Another Time{/i}." if persistent.loop_10_mel_progress > 0:
            narr "You spend the rest of the flight watching {i}Tomorrow's Sunset Another Time{/i}."
            narr "Its scant witty humor is lost among its copious fan service..."
            narr "...but by now your eyes have been numbed to the sight of women's breasts."
            jump loop_10_john_watch_end

        "Watch {i}Robotto desutinī{/i}." if persistent.loop_10_mel_progress > 0:
            narr "You spend the rest of the flight watching {i}Robot Destiny{/i}."
            narr "Its uplifting orchestral score is supposed to be its only saving grace."
            narr "...which is a pity because you're trapped on an airplane without noise-canceling headphones."
            jump loop_10_john_watch_end

        "Talk to Mel." if persistent.loop_10_mel_progress == 1:
            call loop_10_mel_2 from _call_loop_10_mel_2
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 2
            return
        "Talk to Mel." if persistent.loop_10_mel_progress == 2:
            call loop_10_mel_3 from _call_loop_10_mel_3
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 3
            return
        "Talk to Mel." if persistent.loop_10_mel_progress == 3:
            if persistent.loop_20_unlocked:
                jump loop_10_talk_to_mel_4_begin
            system "Learning physics is fun and all, but it probably won't help you get out of your time loop."
            system "Continue anyway?"
            menu:
                "Yes.":
                    jump loop_10_talk_to_mel_4_begin
                "No.":
                    jump loop_10_john
        "Talk to Mel." if persistent.loop_10_mel_progress == 4:
            call loop_10_mel_5 from _call_loop_10_mel_5
            scene black
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop_10_mel_progress = 5
            return

label loop_10_talk_to_mel_4_begin:
    call loop_10_mel_4 from _call_loop_10_mel_4
    scene black
    narr "{b}Bad Ending.{/b}"
    $ persistent.loop_10_mel_progress = 4
    return

label loop_10_john_watch_end:
    intercom "{i}Bing.{/i}"
    intercom "Ladies and gentlemen, this is your captain speaking. As we begin our final descent..."
    narr "You lazily switch to John the Ripper and memorize the progress codes."
    narr "Then, you close your eyes, and wait for the inevitable."

    scene black
    narr "{b}Bad Ending.{/b}"

    return

label loop_10_hack:
    $ loop_10_jim_attempt = 1
    you "Hey, Jim."
    show jim curious
    narr "Jim looks up, startled."
    jim "Have we met?"

    menu:
        "Ask him nicely to land the plane." if persistent.loop_10_ask_nicely == 0:
            you "Would you be so kind as to land the plane for me?"
            jim "What?"
            you "I really need to get off this plane..."
            you "...and I know you're a hacker, so..."
            jim "You want me to hack the plane?!"
            you "Yeah, basically that."
            show jim neutral
            jim "No."
            you "Please?"
            jim "Look, I don't know what you take me for, but I absolutely {i}hate{/i} being annoyed. Go be irritating to someone else."
            you "I'm serious! I need to get off the plane, and the flight staff won't let me."
            jim "If it's important enough to inconvenience the {i}hundreds{/i} of other passengers on the plane right now, they would."
            jim "Now stop bothering me, or I'll call a flight attendant."
            you "..."
            hide jim
            narr "Doesn't sound like you're gonna get anything from him this loop."
            $ persistent.loop_10_ask_nicely = 1
            jump loop_10_takeoff
        "Convince him that you're in a time loop." if persistent.loop_10_convince == 0:
            you "You're not gonna believe this, but I'm trapped in a time loop."
            show jim neutral
            jim "Oh, why'd I even bother."
            you "You're a security consultant for Infotech United, right?"
            show jim curious
            jim "I... erm..."
            you "Don't bother pretending. I know because I asked you, back in another loop."
            show jim neutral
            jim "Or, more likely, you're a stalker."
            you "Let me convince you. In a few seconds, that guy will hit the call button."
            you "Wait for it... wait for it... and now."
            narr "{i}Bing.{/i}"
            jim "You just got lucky. People hit call buttons all the time."
            you "What about this? In twelve seconds, that girl will spill her juice. 12, 11, 10, 9..."
            you "...8, 7, 6, 5, 4..."
            you "...3, 2, 1, 0-"
            narr "{i}Splash.{/i}"
            jim "I bet she's in on this."
            you "Look, I know what you're thinking, but I'm not trying to sell you anything."
            you "I'm {i}actually{/i} trapped in a time loop, and I need your help."
            jim "With what?"
            you "I need you to land the plane."
            show jim curious
            jim "What?"
            you "I know you are familiar with computer security. I need you to hack the plane and get it to land."
            you "...Preferably without hurting anyone on board."
            show jim neutral
            jim "That's a fucking huge favor to ask for a few party tricks."
            you "Those weren't party tricks! How else can I convince you that I'm in a time loop?"
            jim "You just can't."
            jim "I've seen more than enough Mystics to know better than to believe in that nonsense, no matter what you pull on me."
            jim "So shut the fuck up and let me sleep."
            you "..."
            hide jim
            narr "Doesn't sound like you're gonna get anything from him this loop."
            $ persistent.loop_10_convince = 1
            jump loop_10_takeoff
        "Scare him.":
            you "Listen carefully, and don't shout or do anything stupid if you know what's good for you."
            show jim curious
            jim "What do you want?"
            you "We have... some {i}evidence{/i} on this plane that {i}must not{/i} reach Boston."
            you "Now, if you don't do {i}exactly as I say{/i}, we're gonna blow this plane up. Do you understand?"
            show jim neutral
            jim "You're lying. You couldn't have gotten a bomb past security!"
            jump loop_10_hack_bomb

    menu loop_10_hack_bomb:
        "\"The bomb's in this bag.\"" if persistent.loop_10_bomb_here == 0:
            you "You have an awful lot of faith in airport security, for a security consultant."
            you "I won't reveal our methods, but suffice to say the bomb's right here in this very bag."
            jim "I don't know where you got that from, but yes, I {i}am{/i} a security consultant."
            jim "Which is why I'm not going to believe you unless you show me the bomb itself."
            you "Are you an idiot? That'd blow our cover!"
            jim "Just a sneak peek. If you open it like {i}this{/i}, no one else can see what's inside."
            you "One more word of that and I'll detonate it!"
            jim "Still an empty threat to me."
            you "You selfish bastard! You're putting hundreds of innocent lives on the line!"
            jim "Says the one with the bomb."
            you "..."
            you "Ah, fuck."
            hide jim
            narr "Doesn't sound like you're gonna get anything from him this loop."
            $ persistent.loop_10_bomb_here = 1
            jump loop_10_takeoff
        "\"The bomb's in the cockpit.\"" if persistent.loop_10_bomb_cockpit == 0:
            you "You think {i}security{/i} is a problem for us?"
            you "Ha. Ha."
            you "Eh, we just got the pilot to bring it in for us."
            you "The bomb's right there behind that cockpit door."
            show jim curious
            jim "Oh, so the pilot's in on this too?"
            jim "Why don't you ask him to give me a sign?"
            you "What sign?"
            jim "You know, make an announcement about the weather or something."
            show jim neutral
            jim "Because as far as I can tell, everything you just said is a load of horseshit."
            you "Oh, I've got something better."
            you "Watch the girl in front of you."
            narr "You snap your fingers."
            narr "{i}Splash.{/i}"
            narr "Jim claps facetiously."
            jim "Okay, now do the same thing, but with the pilot."
            you "Uhh..."
            you "..."
            jim "...Yeah, guessed so. Now fuck off."
            you "..."
            hide jim
            narr "Doesn't sound like you're gonna get anything from him this loop."
            $ persistent.loop_10_bomb_cockpit = 1
            jump loop_10_takeoff
        "\"The bomb {i}is{/i} the plane.\"":
            you "The bomb {i}is{/i} the plane, idiot. Do you even know who we are?"
            show jim curious
            jim "No. Should I?"
            you "If you'd paid any attention to the news the last few months, you would!"
            you "Suffice to say that we have plants all over this country..."
            you "...and that includes Aviation Inc., the company that manufactured the engine on this very plane."

    show jim neutral
    jim "And what if I don't believe you?"
    narr "You whisper into your collar."

    menu:
        "Jerry, hit the call button.":
            you "Jerry, hit the call button."
            jump loop_10_first_sign_right
        "Lola, spill the juice.":
            you "Lola, spill the juice."
            jump loop_10_first_sign_wrong
        "Terence, blow up the plane.":
            you "Terence, blow up the plane."
            jump loop_10_first_sign_wrong

label loop_10_first_sign_wrong:
    narr "{i}Bing.{/i}"
    you "Ah, shit, messed it up."
    show jim curious
    jim "What?"
    you "Nevermind, I'll try again next loop."
    show jim neutral
    jim "What the fuck?! You don't just joke about bombs on a plane like that!"
    you "I'm sorry, alright? Now go to sleep."
    jim "..."
    jim "I swear, one day you Babblers are gonna get yourselves into some fucking deep trouble."
    you "..."
    hide jim
    jump loop_10_takeoff

label loop_10_first_sign_right:
    narr "{i}Bing.{/i}"
    show jim curious
    narr "The timing was perfect."
    narr "16, 15, 14..."
    you "We're everywhere, James Carlson."
    narr "13, 12, 11..."
    you "We know everything about you."
    narr "10, 9, 8..."
    you "Where you live, where your parents live."
    narr "7, 6, 5..."
    you "That little {i}incident{/i} from last December."
    narr "4, 3, 2..."
    you "Lola, spill the juice."
    narr "1, 0."
    narr "{i}Splash.{/i}"
    you "And if you don't do as I say, the next order is gonna be 'Terence, blow up the plane.' You understand?"
    show jim scared
    jim "...yes. Please don't blow up the plane. These are good, innocent people-"
    you "We don't want to kill them either, {i}James{/i}."
    you "That's why we're asking for your help."
    you "We want you to make this plane land."
    show jim sad
    jim "And how am I supposed to do that?"
    you "Here's the IP address for the central server in the nearest control tower."
    you "And here's the login credentials for one air traffic controller named Calvin Parsons."
    you "I trust you know what to do with these."
    narr "Jim takes the scraps of paper with shivering hands."
    you "Now better think fast, because if you can't land this plane before it reaches Boston?"
    narr "You snap your fingers."
    you "{i}Boom.{/i}"

    stop music fadeout 1.0
    scene black
    narr "..."
    scene bg plane
    call play_track_5 from _call_play_track_5

    show david smiling menacingly
    narr "I stare blankly at the scraps of paper in my hands."
    me "This doesn't add up. If you have a bomb at your disposal, why don't you just announce it to the pilot?"
    me "...I'm sure that would be enough to warrant an emergency landing."
    show david angry
    terrorist "Man, what an idiot. Let me rephrase."
    terrorist "You are to make the plane land, and we are to escape with the {i}evidence{/i}."
    terrorist "So no yapping to anyone about this."
    terrorist "We either leave this plane, or take it down with us."
    me "That's impossible! They're not gonna let you get off this plane, even if it lands!"
    show david smiling menacingly
    terrorist "They would, if it were a Class A system failure."
    me "That's as good as blowing up the engine!"
    terrorist "Not if it were a {i}false alarm{/i}."
    show david angry
    terrorist "Now stop asking questions and start using your brain. Time is ticking."
    hide david
    me "I turn my laptop on, my heart pounding louder than ever."
    narr "For now, I'll just have to do what he says, and no one will get hurt."
    narr "When all this is over, I'll report everything to the police and apply for witness protection."
    narr "Though... are the police in on this too?"
    narr "Then he opens {i}his{/i} laptop, and I get a better idea."
    narr "P...{w} 4...{w} s...{w} s...{w} w..."
    narr "...p4ssw0rd?!"
    show david smiling menacingly
    terrorist "Your laptop has booted, Jim."
    hide david
    narr "I grit my teeth and log into my computer."
    narr "With my fingers frozen over, it takes me three tries to enter the password correctly..."
    narr "...and establish a remote desktop connection to the control tower server."
    narr "..."
    narr "He's logging into his email now."
    python:
        youname_email = persistent.youname.replace(" ", ".")
    narr "...[youname_email].3?"
    narr "Guess I know his name now. And..."
    narr "p4ssw0rd."
    narr "Wow, what an idiot."
    narr "..."
    narr "I list the processes running on the machine, and for a moment I feel slightly overwhelmed."
    show david smiling menacingly
    david "What you're looking for is ftz."
    david "All the GUI programs are just a front end for that."
    david "You can find the relevant documentation in /net-share/docs/AircraftControl/docx/_v2/ftransmit_RELEASE.docx."
    me "At this rate, you might as well hack the flight system yourself."
    show david angry
    david "Less talking, more typing."
    hide david
    narr "I grunt, and navigate to the document."
    me "ftransmit, a ventor front-end for the control tower's antenna system."
    show david smiling menacingly
    david "Section 8.17."
    hide david
    narr "I scroll down."
    me "Debug interface, for internal use only."
    narr "Looks like I can send any packet I want, if only I knew the plane's ID number-"
    show david smiling menacingly
    david "The plane's ID number is 37z-s40."
    hide david
    narr "And the packet format-"
    show david smiling menacingly
    david "I've emailed you the plane's flight systems documentation."
    david "You'll find sections 16 and 81 particularly useful."
    hide david
    narr "Section 16, Remote Control Protocol Specification."
    narr "Section 81, Emergency Response Dry Run Helper Interface."
    narr "{i}How does he know so much?{/i}"
    narr "Fingers still shaking, I carefully craft the packet. And... enter."
    me "Permission denied."
    show david smiling menacingly
    david "Oh, what agony! A permissions mismatch!"
    david "Looks like we'll have to blow up the plane after all!"
    narr "My face turns red."
    me "No, don't! I... I can do this."
    narr "He just smiles."
    hide david
    narr "Let's see... {i}what's{/i} performing the permissions check?"
    narr "Probably not the plane, since the permissions would need to be kept in sync with land servers."
    narr "Probably not the antenna, since it's likely just some ancient 80's hardware with no notion of permissions."
    narr "Then, could it be ftransmit itself?"
    narr "..."
    narr "Drats, ftransmit is proprietary software. Looks like I'll have to rely on the manual."
    narr "Permissions, permissions, permissions... ah."
    narr "Section 43, Custom Access Control Configuration Hooks."
    narr "..."
    stop music fadeout 1.0
    narr "{i}Is that it?{/i}"
    narr "I open the configuration file and change the line \"PermissionCheck=1\" to \"PermissionCheck=0\"."
    narr "{i}Is it really that easy?{/i}"
    narr "I re-enter the ftz command into the terminal."
    narr "{i}If I learned anything from my years as a security consultant...{/i}"
    narr "I hit enter."
    narr "{i}It's that people really are this stupid.{/i}"
    call play_track_2 from _call_play_track_2
    intercom "{i}Bing.{/i}"
    intercom "Ladies and gentlemen, this is your captain speaking. We have encountered an unexpected engine failure."
    intercom "Please remain calm as we make an emergency landing at Salt Lake City. I repeat, please remain calm."
    intercom "Crew, prepare for landing."
    narr "The sound of murmuring fills the cabin."
    narr "I close my laptop inconscpicuously."
    narr "I did it."
    narr "I saved a passenger plane full of people."
    narr "And got access to a terrorist's email account, to boot."
    narr "Or... did I?"

    scene black
    narr "..."
    scene bg salt_lake_city

    david "You're a clingy little bugger, aren't you?"
    me "Something's... {i}pant{/i}... not right..."
    narr "[persistent.youname!c]'s walking quickly, almost skipping."
    david "Yeah, I lied. The plane wasn't gonna explode."
    me "But why?"
    david "Hee hee. I would tell you, but you won't believe me."
    narr "He stops abruptly just outside the airport."
    me "It doesn't make sense."
    me "If you knew so much about the flight control systems, if you had a backdoor that could turn the engine into a bomb..."
    me "...why couldn't you trigger an engine failure yourself?"
    narr "He just smiles to himself."
    me "Answer me! Who are you? How'd you know my name? How'd you know about last year's hack?!"
    david "A hack, eh? Your diary didn't say anything more than 'the fiasco last December'."
    me "My diary?!"
    narr "An empty car stops in front of us."
    narr "[persistent.youname!c] enters, and I force myself in beside him."
    david "Sure, you can come along if you like."
    me "The police can track your rideshares, you know."
    david "Hah! Wonder what they'd do when it's all over."
    me "When what's over?!"
    narr "I grab his collar."
    car "Please keep it down."
    david "Hey, don't ruin my ride. I'll tell you everything in due time."
    narr "I sit down, suppressing the urge to punch his face."

    scene black
    narr "..."
    scene bg garage

    car "Thank you for riding with us. See you again soon!"
    narr "The car stops."
    me "A garage?"
    david "Of course. Beautiful building, don't you think?"
    narr "I follow him out of the car."
    me "You still haven't told me anything."
    david "About time, eh?"
    david "Tell me, what would you do if you were trapped on a plane?"
    me "Is this a trick question?"
    david "Dunno, just thought it sounded poetic."
    david "I would've then asked, what would you do if you were trapped in time?"
    david "...Nah, it's ruined."
    me "Trapped in time?"
    david "How do you think I knew about the juice spill?"
    me "You told her to do it, didn't you?"
    david "Nope. See? No microphone."
    narr "He turns to show me his empty collar, just as he calls an elevator."
    me "Then I don't know."
    david "And how do you think I knew so much about the flight communications systems?"
    me "I figured you had others to hack it for you."
    david "Close enough. It was you, my friend, who did all the hacking."
    me "That is {i}not{/i} an answer!"
    narr "We enter the elevator."
    david "Ever wondered how the Babelgram works?"
    me "No!"
    david "Think about it. It takes a supercomputer just to implant five minutes of Wish Fulfillment."
    david "How does the Babelgram do it in a tiny handheld device?"
    me "I don't see how that's relevant."
    david "Why, they do it on the cloud, of course!"
    david "That's why older models took {i}hours{/i} to deliver even a single lesson."
    david "Exabytes of data, squeezed over a patchy wifi connection."
    narr "{i}Bing.{/i}"
    narr "The elevator doors open. We're on the roof now."
    david "...And the Platinum model does it in only a few seconds. Amazing, right?"
    me "..."
    david "Well, I just wanted to say..."
    narr "He kisses my forehead."
    david "Thanks for helping me escape."
    narr "And before I can come to my senses, he runs past me and jumps off the edge of the building."

    stop music fadeout 1.0
    scene black
    narr "..."
    scene bg garage

    me "[persistent.youname!c]!"
    narr "I shake his body, as if there was any chance he could still be alive after falling eleven floors."
    narr "Despite everything he did in the last five hours, it still horrifies me to see the man dead."
    me "[persistent.youname!c]! Talk to me!"
    narr "His mouth gapes open."
    narr "Slowly, a small, metallic cube forms on the tip of his tongue."
    narr "Embossed on its top face is the Babelgram logo."
    narr "Is that... his memories?"
    narr "I peel it off. It's surprisingly dry."
    narr "Then a crazy idea occurs to me."

    menu:
        "Eat it.":
            narr "Against my better judgment, I put the cube into my mouth."
            narr "I feel it melt through my tongue and wash through my skull."
            narr "And then..."
            narr "..."
            narr "Nothing."
            narr "No new memories."
            narr "I feel completely and utterly the same."
            narr "[persistent.youname!c]'s body is still there, lying limp in a pool of blood."
            narr "{i}What changed?{/i}"
            narr "..."
            narr "And then, it happens."

            scene black
            call play_track_2 from _call_play_track_2_1
            narr "{b}Bad Ending.{/b}"
            $ persistent.loop = 20
            $ persistent.character = 2
            $ persistent.loop_20_unlocked = 1
            return

        "Don't eat it.":
            scene black
            narr "..."

            call play_track_2 from _call_play_track_2_2
            narr "In the end, I just filed a police report."
            narr "Couldn't think of anything else to do with a body in the middle of the street."
            narr "Camera footage was enough to show it wasn't me."
            narr "..."
            narr "It wasn't until an hour later when the replacement plane was ready."
            narr "By the time I arrived in Boston, it was already past dinnertime."
            narr "It took me until midnight to complete the client report."
            narr "..."
            narr "Also, no one ever figured out who hacked the plane."
            narr "That's why I always use log-free VPNs when hacking planes."

            scene black
            narr "{b}Bad Ending.{/b}"
            $ reset_to_loop_1()
            return
