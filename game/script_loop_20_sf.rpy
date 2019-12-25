default persistent.loop_20_hack_plane = 0
default persistent.loop_20_mcdonalds_explanation = 0
default persistent.loop_20_nuggs = 0
default persistent.loop_20_paperclips_asked = 0
default persistent.loop_20_paperclips_stolen = 0
default persistent.loop_20_house_explanation = 0
default persistent.loop_20_security_system_seen = 0

label loop_20_sf_begin:
    scene black
    narr "..."
    scene bg streets

    narr "Alright, I'm at San Francisco now."

    if persistent.loop_20_hack_plane == 0:
        narr "It was pretty much the same as before."
        narr "Only difference was that I had to use a different control tower."
        narr "I was fast enough, of course, that I ended up in San Francisco instead of Salt Lake City."
        narr "..."
        $ persistent.loop_20_hack_plane = 1

label loop_20_sf:
    scene bg streets

    menu loop_20_sf_menu:
        "Where should I go?"

        "The Babelgram HQ.":
            if loop_20_hq_open == 0:
                jump loop_20_outside_babelgram_hq_begin
            else:
                jump loop_20_babelgram_hq_begin

        "An electronics store." if loop_20_electronics_raided == 0 and persistent.loop_20_security_system_seen == 1:
            jump loop_20_electronics_begin

        "A bank.":
            jump loop_20_bank_begin

        "A random house." if persistent.loop_20_house_explanation == 0:
            jump loop_20_house_begin

        "An unlocked house." if persistent.loop_20_house_explanation == 1:
            jump loop_20_house_begin

        "A Wish Fulfillment center.":
            scene black
            narr "..."
            term "Matching neural pattern..."
            term "Welcome back, [persistent.youname!c]!"
            term "Sorry, after-hours services are available only to premium customers."
            term "Would you like to apply for premium membership?"

            menu:
                "Yes.":
                    narr "..."
                    $ loop_20_you_password = 0
                    python:
                        you_pw = renpy.input("Enter password to continue.")
                        you_pw = you_pw.strip()
                        if hashlib.sha512(you_pw).hexdigest() == "fe1c94d7b0ac51013b944b84cd1fd40111421684f857ebf2eaaf494014007e3068ea25ed03c4c8155b33c1271742db38dcf3059096ad2b859b44ed2b9ae5d10f":
                            loop_20_you_password = 1
                    if loop_20_you_password == 0:
                        term "Password incorrect."
                        jump loop_20_sf
                    term "Thank you for your application! We will be contacting you in 1-2 business days."
                    narr "..."
                    narr "...Drats."
                    jump loop_20_sf
                "No.":
                    term "Thank you for visiting!"
                    jump loop_20_sf

        "Just somewhere to eat." if persistent.loop_20_mcdonalds_explanation == 0:
            jump loop_20_mcdonalds_begin

        "A McDonald's." if persistent.loop_20_mcdonalds_explanation == 1:
            jump loop_20_mcdonalds_begin

        "Wait out the loop.":
            narr "I wile away the rest of the loop at a nearby McDonald's."
            jump loop_20_end

label loop_20_bank_begin:
    scene black
    narr "Alright, I'm at a bank."
    narr "It's closed, though."
    narr "The door is one of those fancy glass security doors with a magnetic lock."

    menu loop_20_bank:
        "What shall I do?"

        "Break the door." if loop_20_bank_raided == 0:
            if loop_20_hammer == 0:
                narr "I whack the door with my fists."
                narr "..."
                narr "It's no use."
                narr "Maybe if I had a tool of some sort."
                jump loop_20_bank
            else:
                narr "I whack the door with the hammer."
                narr "{i}BANG! BANG! BANG!{/i}"
                narr "Spider-web cracks form on the door, but it doesn't break."
                narr "Goddamn security glass."
                narr "Maybe it'd be easier to attack the lock directly. What could I use to destroy a magnet?"
                jump loop_20_bank

        "Blowtorch the magnet lock." if loop_20_bank_raided == 0 and loop_20_blowtorch == 1:
            if loop_20_blowtorch_used == 1:
                narr "My blowtorch is out of fuel."
                jump loop_20_bank
            else:
                narr "I use the remaining fuel in the blowtorch to destroy the magnet."
                narr "Before long, the door swings open."
                $ loop_20_blowtorch_used = 1

            narr "..."
            narr "I couldn't find any cash, apart from a few rolls of quarters."
            narr "I guess they don't actually need to store any, since everyone draws cash from ATMs now."
            narr "I did find reams of account balances and investment records, but they're basically worthless to me at the moment."
            narr "Oh, there's also a few paperclips."
            $ loop_20_paperclips = 1
            $ loop_20_bank_raided = 1
            jump loop_20_bank

        "Draw money.":
            if loop_20_cash == 0:
                narr "I use the ATM outside."
                narr "..."
                narr "Alright, I have $500 now."
                $ loop_20_cash = 1
            elif loop_20_cash == 1 and loop_20_wallet == 1:
                narr "Okay, I drew another $500 with the stolen credit card."
                narr "I wonder what I'll do with all this cash?"
                $ loop_20_cash = 2
            else:
                narr "I can't draw anymore cash today. I've reached my withdrawal limit."
            jump loop_20_bank

        "I'm done here.":
            jump loop_20_sf

label loop_20_electronics_begin:
    scene black
    narr "I wander to the front of an electronics store."
    narr "Like every other store, it's closed."
    narr "I should be able to get an RF transmitter here."

    menu loop_20_electronics:
        "What shall I do?"

        "Enter.":
            narr "I can't. The door's locked."
            jump loop_20_electronics

        "Smash a window.":
            if loop_20_hammer == 0:
                narr "I whack the window with my fists."
                narr "..."
                narr "It's no use."
                narr "Maybe if I had a tool of some sort."
                jump loop_20_electronics
            else:
                narr "I smash a window with the hammer and unlock it from the inside."
                narr "Then, I climb in clumsily."
                narr "It takes a while, but I find it eventually –"
                narr "– a USB RF tranceiver."
                $ loop_20_rf_transmitter = 1
                $ loop_20_electronics_raided = 1
                jump loop_20_sf

        "I'm done here.":
            jump loop_20_sf

label loop_20_mcdonalds_begin:
    scene black
    if persistent.loop_20_mcdonalds_explanation == 0:
        narr "It takes me a while to find a place still open at this time of day."
        narr "I end up ducking into a nearby McDonald's."
        $ persistent.loop_20_mcdonalds_explanation = 1

    menu loop_20_mcdonalds:
        "What shall I do?"

        "Ask for paperclips." if persistent.loop_20_paperclips_asked == 0 and loop_20_paperclips == 0:
            narr "The cashier just looks at me weird and asks if anyone uses paperclips anymore."
            narr "I stare back and say, yeah, apparently {i}I{/i} do."
            narr "Guess I won the argument..."
            narr "...but I didn't win any paperclips."
            $ persistent.loop_20_paperclips_asked = 1
            jump loop_20_mcdonalds

        "Order some nuggets." if persistent.loop_20_nuggs == 0:
            narr "I order 100 nuggets."
            narr "Wait, I know what you're thinking."
            narr "But no, I don't actually like nuggets that much."
            narr "I wouldn't even say I like nuggets at all."
            narr "..."
            narr "{i}nom nom nom nom nom{/i}"
            narr "..."
            $ persistent.loop_20_nuggs = 1
            jump loop_20_mcdonalds

        "Order some nuggets." if persistent.loop_20_nuggs == 1:
            narr "I order 100 nuggets."
            narr "..."
            narr "What?"
            narr "Fine. Maybe I {i}do{/i} like nuggets, just a tiny bit."
            narr "..."
            narr "A little bit."
            narr "..."
            narr "Okay, a lot! Ugh! Why do I need to be so self-conscious about my food preferences?"
            narr "..."
            narr "{i}nom nom nom nom nom{/i}"
            narr "..."
            $ persistent.loop_20_nuggs = 2
            jump loop_20_mcdonalds

        "Order some nuggets." if persistent.loop_20_nuggs == 2:
            narr "I order 100 nuggets."
            narr "..."
            narr "Yes, I know the hunger will just come back again after I jump."
            narr "You know what? I don't care."
            narr "{i}I'm{/i} trapped in a time loop, {i}I{/i} get to do whatever the fuck I want."
            narr "..."
            narr "{i}nom nom nom nom nom{/i}"
            narr "..."
            $ persistent.loop_20_nuggs = 3
            jump loop_20_mcdonalds

        "Order some nuggets." if persistent.loop_20_nuggs == 3:
            narr "I order 100 nuggets."
            narr "..."
            narr "{i}nom nom nom nom nom{/i}"
            narr "..."
            jump loop_20_mcdonalds

        "I'm done here.":
            jump loop_20_sf

label loop_20_house_begin:
    scene black
    $ loop_20_house_menu_1_empty = loop_20_wallet == 1 and loop_20_passport == 1 and loop_20_tablet == 1 and loop_20_jewelry == 1 and loop_20_hammer == 1
    $ loop_20_house_menu_2_empty = not (persistent.loop_20_paperclips_stolen == 0 and loop_20_paperclips == 0) and loop_20_paper == 1 and loop_20_soap == 1 and loop_20_blowtorch == 1
    $ loop_20_house_empty = loop_20_house_menu_1_empty and loop_20_house_menu_2_empty
    if loop_20_house_empty:
        narr "I've already stolen everything I can think to steal."
        narr "What, should I steal their garbage too?"
        jump loop_20_house_done
    if persistent.loop_20_house_explanation == 0:
        narr "No need to be random about this. I already located a few houses with unlocked back doors."
        $ persistent.loop_20_house_explanation = 1

label loop_20_house_1:
    if loop_20_house_menu_1_empty:
        jump loop_20_house_2
    menu loop_20_house_1_menu:
        "What shall I steal?"

        "Wallet." if loop_20_wallet == 0:
            narr "Okay, found a wallet."
            narr "It contains an ID card, a credit card, and a driving license."
            narr "...and a tiny bit of cash, of course."
            $ loop_20_wallet = 1

        "Passport." if loop_20_passport == 0:
            narr "Okay, found a US passport."
            narr "I wonder what I'll do with it?"
            $ loop_20_passport = 1

        "Tablet." if loop_20_tablet == 0:
            narr "Okay, found a tablet."
            narr "I wonder what I'll do with it?"
            narr "I mean, it's PIN-locked."
            narr "And I'm not going to spend a million loops guessing different combinations manually."
            $ loop_20_tablet = 1

        "Jewelry." if loop_20_jewelry == 0:
            narr "Okay, found some jewelry."
            narr "Some diamonds, I think? And a bunch of gold?"
            narr "I don't know how to tell if they're genuine."
            $ loop_20_jewelry = 1

        "Hammer." if loop_20_hammer == 0:
            narr "Okay, found a hammer."
            $ loop_20_hammer = 1

        "More...":
            jump loop_20_house_2

    jump loop_20_house_done

label loop_20_house_2:
    menu loop_20_house_2_menu:
        "What shall I steal?"

        "Paperclips." if persistent.loop_20_paperclips_stolen == 0 and loop_20_paperclips == 0:
            narr "No one seems to have any paperclips."
            narr "I mean, who uses paperclips anymore?"
            $ persistent.loop_20_paperclips_stolen = 1
            jump loop_20_house_1

        "Paper." if loop_20_paper == 0:
            narr "Okay, sure. I load up my bag with blank paper."
            $ loop_20_paper = 1

        "Soap." if loop_20_soap == 0:
            narr "Okay, here's some soap."
            narr "I wonder what I'll use it for?"
            narr "I mean, I {i}would{/i} like a shower. Even if I'll just get dirty and sweaty again when I jump."
            narr "But if any public showers exist, they probably aren't open at this time of day."
            $ loop_20_soap = 1

        "Blowtorch." if loop_20_blowtorch == 0:
            narr "Wow, this one was hard to find."
            narr "But here's one. This guy must really like to cook."
            narr "It's almost empty, though."
            $ loop_20_blowtorch = 1

        "More..." if not loop_20_house_menu_1_empty:
            jump loop_20_house_1

        "Actually, nevermind. Stealing is wrong.":
            narr "Okay."
            jump loop_20_sf

    jump loop_20_house_done

label loop_20_house_done:
    scene bg streets

    jump loop_20_sf

label loop_20_allie_house_begin:
    if persistent.loop_20_allie_house_explanation == 0:
        narr "I figured the CEO of Babelgram, if anyone, would know what's up with this time loop shenanigans."
        narr "She didn't respond to my calls and emails in the last loop, so I thought I'd pay her a visit directly."
        narr "Finding her address was easy enough."
        narr "It was right there, in an unprotected database on the Babelgram servers..."
        narr "...by which I mean the same servers that host their public website."
        $ persistent.loop_20_allie_house_explanation = 1
    narr "..."
    narr "Well, here I am."
    narr "Everything's dark, except for a faint glow from a window on the second floor."

    $ choice_kick = 0

    menu loop_20_allie_house:
        "What shall I do?"

        "Knock on the door.":
            narr "..."
            narr "No one answers."
            jump loop_20_allie_house

        "Ring the doorbell.":
            narr "..."
            narr "No one answers."
            jump loop_20_allie_house

        "Kick down the door." if choice_kick == 0:
            narr "{i}BANG! BANG! BANG!{/i}"
            narr "..."
            narr "Damn, that's one sturdy door."
            $ choice_kick = 1
            jump loop_20_allie_house

        "Kick down the door." if choice_kick == 1:
            narr "{i}BANG! BANG! BANG!{/i}"
            narr "..."
            narr "Shouldn't have skipped leg day."
            narr "Not that I gym..."
            $ choice_kick = 2
            jump loop_20_allie_house

        "Kick down the door." if choice_kick == 2:
            narr "{i}BANG! BANG! BANG!{/i}"
            narr "..."
            unknown "Hey, could you keep it down?"
            narr "Okay, that's just not gonna work. Can we try something else?"
            $ choice_kick = 3
            jump loop_20_allie_house

        "Pick the lock." if loop_20_paperclips == 1:
            narr "Without a pair of pliers, bending the paperclips into shape was difficult."
            narr "I ended up sticking them into grooves on the floor."

        "I'm done here.":
            jump loop_20_sf
