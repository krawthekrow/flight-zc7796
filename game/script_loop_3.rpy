default persistent.youname_locked = 0

label loop_3:
    scene bg plane

    intercom "{i}Bing.{/i}"
    intercom "Ladies and gentlemen, this is your captain speaking. We have reached cruising altitude..."
    narr "I shift uncomfortably in my seat."
    narr "You’d think over a century of commercial aviation would’ve been enough to figure out how to make a goddamn-"

    menu:
        "\"Hey, Jim.\"":
            show david neutral
            babbleru "Hey, Jim."

    narr "Shit, a Babbler? I'm not in the mood for this."
    me "Have we met?"
    babbler "No less than thirty-seven times. You're not gonna believe this, but I'm trapped in a time loop."
    me "Oh, why'd I even bother."
    babbler "You're a security consultant for Infotech United, right?"
    me "I... erm..."
    show david neutral
    babbler "Don't bother pretending."
    babbler "I know because I asked you, back in another loop."
    me "Or, more likely, you're a stalker."
    babbler "Let me convince you. In a moment, that guy will hit the call button."
    narr "..."
    me "It's not happening."
    menu:
        "It's coming...! I think...!":
            babbler "It's coming...! I-"
        "Wait a few seconds.":
            babbler "Wait a few seconds-"
        "Huh. Did I get it wrong?":
            babbler "Huh, did I get it-"
    narr "{i}Bing.{/i}"
    me "You just got lucky. People hit call buttons all the time."
    babbler "I knew you'd say that."
    babbler "Well, what about this? The girl in front of you is gonna spill her juice in..."
    menu:
        "Twenty seconds.":
            babbler "...twenty seconds! 19, 18, 17..."
            babbler "...16, 15, 14, 13, 12..."
            babbler "...11, 10, 9, 8-"
        "Fifteen seconds.":
            babbler "...fifteen seconds! 14, 13, 12..."
            babbler "...11, 10, 9, 8, 7..."
            babbler "...6, 5, 4, 3-"
        "Ten seconds.":
            babbler "...ten seconds! 9, 8, 7, 6..."
            babbler "...5, 4, 3, 2..."
            babbler "...1, 0!"
            babbler "..."
            babbler "Uh-"
    narr "{i}Splash.{/i}"
    me "That was twelve seconds."
    show david sad
    babbler "Twelve, okay. Twelve, twelve..."
    me "And I bet she's in on this."
    show david angry
    babbler "{i}Why would she?!{/i}"
    me "Because you're trying to sell me something or another. What'd it be this time, Mystic Pills?"
    babbler "I told you, I'm stuck in a time loop!"
    me "Not interested."
    show david neutral
    babbler "What if I told you..."
    show david smiling menacingly
    babbler "...that it might have something to do with Babelgram?"
    me "Then you deserve it."
    show david neutral
    babbler "Think about it. If we can prove that Babelgram did cause the time loop, then we can sue them."
    me "And how the hell will that benefit me?"
    babbler "I know you don't like Babelgram."
    me "It's the users I don't like, not the company."
    babbler "That's not true. You also detest the company and all it stands for, because it symbolizes the commodification of learning."
    narr "Wait, that line..."
    me "Did you read my diary?!"
    show david angry
    babbler "No! I told you, I'm in a time loop!"
    show david neutral
    babbler "And in one loop, we had a pretty intriguing conversation about Babelgram and Wish Fulfillment..."
    babbler "...and what you call the technocratic backfire effect."
    narr "I don't know what could've convinced me to talk about {i}that{/i} to the likes of him, but-"
    narr "Wait, am I starting to believe him?"
    me "Look, I still don't trust you, but- what's a time loop, anyway?"
    show david sad
    babbler "I'd ask if you've watched Groundhog Day, but I know you haven't."
    me "Never heard."
    show david neutral
    babbler "Okay. So in six – no – five and a half hours, the plane's gonna land, right?"
    me "Right."
    babbler "Well, just before it lands, I get transported six hours into the past."
    babbler "...Around the time, and probably exactly when, I used my Babelgram."
    me "Okay..."
    show david sad
    babbler "Then I’d sit through this whole flight again..."
    show david neutral
    babbler "...and I'd keep getting transported back, over and over, {i}ad infinitum{/i}."
    babbler "It's been at least thirty-seven loops so far – more than that, actually, since I only started counting partway through."
    me "And what do {i}I{/i} have to do with it?"
    babbler "I need your help."
    babbler "I need you to hack the Babelgram servers."

    scene black
    narr "For a while, I say nothing."
    narr "A time loop?"
    narr "That sounds like something straight out of {i}Tim and the Machine{/i}, or whatever kids watch these days."
    narr "All things considered, I'd say he's either insane or a really bad prankster."
    narr "But..."
    narr "...something about him gives me pause."
    narr "His tone of voice, maybe?"
    narr "It didn't sound like he was {i}trying{/i} to earn my trust."
    narr "He just sounded..."
    extend " tired."
    extend " Resigned."
    extend " Like..."
    narr "{i}Like he's been through this same conversation over thirty-seven times.{/i}"
    narr "And maybe it wasn't even that."
    narr "Because deep down inside, I really want what he said to be true."
    narr "Because deep down inside, I really want an excuse to {i}hurt{/i} Babelgram."
    narr "It isn't just because I despise the company and all it stands for."
    narr "It's because, after all these years, working as a security consultant in some faceless corporation,"
    narr "telling people for the {i}millionth{/i} time to change their default admin password..."
    narr "It feels like I finally got the chance to do something meaningful."
    narr "And so I say it."

    scene bg plane
    show david neutral

    me "I'll do it."
    show david happy
    narr "The Babbler's face brightens up considerably."
    babbler "You... you said yes."
    me "That I did."
    babbler "Thank you. You don't know how much this means to me."
    me "So what do you need, exactly?"
    babbler "To start with, I want to know how the Babelgram actually works."
    me "Why, of course. And I must've forgot, but what's your name again?"

label loop_3_enter_name:
    if persistent.youname_locked == 0:
        python:
            youname_input = renpy.input("Enter your name.")
            youname_input = youname_input.strip()
            youname_valid_chars = all(c.isalpha() or c.isspace() for c in youname_input)
            youname_valid_empty = len(youname_input) > 0
            youname_valid_len = len(youname_input) <= 20
            youname_conflict = youname_input == "jim"
        if not youname_valid_chars:
            narr "Sorry, I can't understand that."
            narr "Please enter a name with only letters and spaces."
            jump loop_3_enter_name
        elif not youname_valid_empty:
            narr "Come again?"
            jump loop_3_enter_name
        elif not youname_valid_len:
            narr "Please use a shorter name. (max 20 characters)"
            jump loop_3_enter_name
        elif youname_conflict:
            narr "That would make things confusing."
            narr "Could you choose a different name?"
            narr "It doesn't have to be your real name."
            jump loop_3_enter_name
        else:
            $ persistent.youname = youname_input
    david "I'm [persistent.youname!c]. And you're James Carlson. Nice to meet you."

    scene black
    narr "..."
    scene bg plane
    show david surprised

    $ persistent.youname_locked = 1

    david "They {i}what{/i}?!"
    me "They left their admin interface accessible to the wider Internet, and at a default port, too."
    me "And... guessed it. They didn't change their password."
    david "Is this normal?!"
    me "For FastNet users, yes."
    me "They force you to change it in v2, but most companies are still stuck at v1."
    me "...Too many breaking API changes."
    david "So what you're saying is, anyone with a smidgen of computer knowledge can just log into this system..."
    david "...and screw with my brainwaves?!"
    narr "I smile."
    me "Don't panic just yet."
    me "This isn't the system that deals with – what was it again? – neural patterning."
    me "It's just where they store customer data."
    david "You mean, like my username and password?"
    me "And your credit card number, address, and medical references, yes."
    show david neutral
    david "I'm not sure that's any less discomforting."
    me "I'm hoping we can use this as a stepping stone. Recognize any of the names here?"

    $ choice_you = 0
    $ choice_andy = 0

    menu loop_3_names:
        "\"[persistent.youname!c]! That's me!\"" if choice_you == 0:
            show david happy talking
            david "[persistent.youname!c]! That's me!"
            narr "{i}What a narcissist.{/i}"
            me "From the timestamp, it looks like you only got your Babelgram this morning?"
            david "Yeah! Flew all the way here just to get it."
            me "Man, have you never heard of online shopping?"
            show david angry
            david "Hey, this isn't just any old Babelgram, alright."
            show david happy talking
            david "It's a {i}Platinum{/i} Babelgram!"
            david "Only ten of these babies exist anywhere in the world right now."
            me "Only ten? Is this some sort of early access thing?"
            david "Yeap! I was lucky enough to be one of the first few to pre-order."
            me "..."
            me "Well, you're not the person I'm looking for here."
            show david neutral
            me "Try again."
            $ choice_you = 1
            jump loop_3_names
        "\"Allie Chen! That's their CEO!\"":
            show david happy talking
            david "Allie Chen! That's their CEO!"
        "\"Uhh... Andy Hurwitz?\"" if choice_andy == 0:
            david "Uhh... Andy Hurwitz?"
            me "You know him?"
            david "No, but it says he bought the Platinum model too."
            me "What's so special about that?"
            david "You know how Babelgrams used to take, like, 3 hours just to deliver a single lesson?"
            david "The Platinum model does it in a matter of minutes."
            david "That's why I could do it just now, during takeoff."
            me "Hmph. It just gets easier, doesn't it?"
            show david happy talking
            david "Yeah! Isn't it great?"
            david "Soon we'll be teaching babies to walk in a matter of seconds!"
            me "..."
            me "Well, that's not the person I'm looking for."
            show david neutral
            me "Try again."
            $ choice_andy = 1
            jump loop_3_names

    me "Indeed. Now I'll just take her password..."
    term "E6C36718DFFAAAFA85E611D9D0FD41A7"
    show david neutral
    david "Wow, that's a pretty complicated password."
    me "It's hashed. With MD5, because {i}of course{/i} it is."
    me "And if I were to guess, I bet they didn't salt it either."
    david "Is that bad?"
    me "Ohoho. Just you watch."
    narr "I check the password against an online rainbow table."
    me "Damn, not gonna be that easy, eh."
    me "Let's see... lowercase alphanumeric, minimum length 8."
    david "What are you doing?"
    me "Running it through John the Ripper. It's a password cracker."
    show david surprised
    david "Wow, just like in the movies! How long would it take?"
    me "Depending on how strong the password is, it might take anywhere from a few days..."
    me "...to a couple hundred years."
    david "{i}A couple hundred years?!{/i} But we only have-"
    narr "He looks at his watch."
    david "-four hours!"
    me "Huh? Oh, right, your time loop thing."
    show david neutral
    david "Fuck, fuck, fuck, fuck, fuck. Isn't there anything else you can do?"
    me "Well, it's unlikely, but... lemme check."

    scene black
    narr "..."
    scene bg plane
    show david angry

    david "{i}Adventure Stadium?!{/i}"
    david "I want to know how the Babelgram works, not steal people's monees!"
    show david happy
    david "...though I wouldn't mind if you got me a few hundred million. It'd be fun to try my hand at Bonefang himself."
    show david neutral
    me "Heh, you wish. No, that's not what I'm going for."
    david "What then?"
    me "Adventure Stadium had a plaintext password breach last month, and the torrent's still up."
    me "And if her blog's any indication, Allie Chen {i}does{/i} play the game..."
    me "...so her password {i}might{/i} be in there somewhere."
    show david happy
    david "Oh, that's smart! Then we can use it to log into the Babelgram servers!"
    me "..."
    me "...you use the same password for everything too, don't you."
    david "Uh... no, I don't, heh. Why... would I?"
    narr "I grep his name in the Adventure Stadium dump."
    show david neutral
    me "p4ssw0rd, eh."
    david "..."
    me "You truly {i}are{/i} an idiot."
    show david sad
    david "Not that it matters. My loop's ending in three-and-a-half hours."
    me "In any case, looks like we're out of luck."
    me "Allie probably made her account after they migrated to the new server."
    show david neutral
    david "Ah, shit. Is there anything else we can try?"
    david "Like..."

    $ choice_ddos = 0
    $ choice_db = 0
    $ choice_direct = 0

label loop_3_other_hacks_begin:
    if choice_ddos == 1 and choice_db == 1 and choice_direct == 1:
        jump loop_3_other_hacks_end
    menu loop_3_other_hacks:
        "Could we DDOS the Babelgram servers?" if choice_ddos == 0:
            david "Could we... uh... DDOS the Babelgram servers?"
            david "I think I read about something like that the other day..."
            me "No, a denial-of-service attack isn't going to get you any information, it just makes Babelgram unusable for everyone else."
            david "...Oh, damn."
            $ choice_ddos = 1
            jump loop_3_other_hacks_begin
        "Can we find her password somewhere else?" if choice_db == 0:
            david "Can we find her password somewhere else?"
            me "Nowhere I can think of."
            me "There may be other dumps floating around somewhere, but I don't have any, uh, contacts."
            david "Contacts?"
            me "..."
            david "...Oh."
            $ choice_db = 1
            jump loop_3_other_hacks_begin
        "Can't we hack into Babelgram's servers directly?" if choice_direct == 0:
            david "Can't we hack into Babelgram's servers directly?"
            me "Already did that, remember?"
            me "Besides, do you even know what you mean when you say 'Babelgram servers'?"
            david "Huh?"
            david "Yeah, I mean, they {i}have{/i} to store their blueprints {i}somewhere{/i}, right?"
            me "Pssh, no. This is a {i}startup{/i} we're talking about."
            me "Think about it. If you and I were to start a company {i}right now{/i}, where would we draft our design documents?"
            david "Uhh... oh. We'd just use Google Docs."
            me "Or send it to each other over email."
            david "...So that's what we're after."
            me "And there's no way in hell we'd be able to hack those services directly..."
            me "...So we'll just have to suck it up and find her password."
            $ choice_direct = 1
            jump loop_3_other_hacks_begin

label loop_3_other_hacks_end:
    narr "..."
    david "Shit. Guess all we can do now is sit around and hope that your Jack the Ripper finds the password before the plane lands."
    me "Well, there {i}is{/i} a way to make it faster."
    david "How?"
    me "I could run it on a GPU cluster."
    me "It'd cost quite a bit, though, and I'm not sure I'd be willing to throw that much money at our little game."
    show david angry
    david "So you think this is a game, eh."
    narr "He opens his wallet."
    show david neutral
    david "Here's my credit card. Use as much as you please."
    narr "I gape in horror."
    me "You're really not joking about the time loop, are you."
    show david angry
    david "Of course I'm not! I'm {i}trapped{/i} on this plane, goddammit. This is worse than death!"
    me "Alright, fine, I'll use it."
    me "But whatever happens, even if you {i}do{/i} escape your time loop, you're not getting any of that money back."
    show david neutral
    david "Of course."
    me "Write that here, sign it, and send me a picture of yourself holding it up to the camera."
    david "Fine, and fuck you."
    narr "I grin."

    scene black
    narr "..."
    scene bg plane
    show david sad

    david "This is it, I guess, the final hour."
    narr "[persistent.youname!c] rests his head on the chair in front of him."
    david "I'm kinda looking forward to the next loop, actually."
    david "My neckache disappears every time I jump."
    narr "He leans back again and rubs his forehead."
    narr "..."
    show david neutral
    david "Hey, Jim. I was thinking. You said John works by trying different passwords until something works, right?"
    me "Yeah, pretty much."
    david "You think we could run it across multiple loops?"
    me "What do you mean?"
    david "Well, let's say we know that John has tried all passwords starting with the letter 'a'."
    david "Then in the next loop, we can tell John to try all passwords starting with the letter 'b'."
    david "That way, we just have to keep doing this over and over again, and eventually we'll find the password."
    me "Hmm, that's an idea. I'm not sure if John supports that, but lemme check."
    narr "I take another look at the documentation."
    me "Oh, hey! Looks like it {i}does{/i} support pause and resume."
    me "And it dumps its state in a human-readable format, too."
    show david happy
    david "Awesome! Where's it at now?"
    me "Uhhh... here."
    narr "I turn my laptop to [persistent.youname!c]."
    show david surprised
    david "{i}Thirty numbers?!{/i} Fuck, it'd take me {i}forever{/i} to memorize that!"
    me "Can't you write it on your arm or something?"
    show david neutral
    david "No, nothing physical carries over in the jump."
    david "It's just my mind, as far as I can tell."
    me "Hmm..."
    me "Maybe only the first few numbers are important."
    me "Like if you just set the rest to zero, maybe you'd lose some progress, but not that much."
    david "Is that true?"
    me "I'll need to look at the source code to be sure."
    show david sad
    david "Great. I'll see how much I can memorize in the meantime."

    scene black
    narr "..."
    scene bg plane

    show david happy
    me "...And then you just type this in, and hit enter."
    narr "[persistent.youname!c] hits the enter key, his face beaming."
    show david happy talking
    me "I did it! This is {i}my{/i} John the Ripper, running on {i}my{/i} virtual GPU cluster!"
    narr "I've never seen anyone so excited about setting up a cluster before."
    narr "Perhaps when you're trapped on a plane for eternity, you learn to treasure every small victory."
    david "I did it I did it I did it! Babelgram, here I come!"
    me "Heh. For a non-programmer, you do learn pretty fast-"
    hide david
    show david neutral
    intercom "{i}Bing.{/i}"
    intercom "Ladies and gentlemen, this is your captain speaking. As we begin our final descent..."
    stop music fadeout 1.0
    narr "[persistent.youname!c] gulps."
    show david sad
    david "...Ten minutes. In ten minutes, I'll jump, and..."
    narr "A tear appears at the corner of his eye."
    david "...I'll lose you, Jim. I mean, you'll still be here, but..."
    david "...everything. Everything we did together, it'll become nothing but a memory.{w} My memory."
    david "To you, I'll become just another asshole Babbler again."
    narr "Asshole Babbler?"
    me "I'm sorry. I don't know what I said to you in the other loops..."
    me "...I don't know if it even makes {i}sense{/i} to apologize for things I said in other loops, but –"
    me "– thanks to you, I definitely won't be seeing Babelgrammers the same way again."
    narr "..."
    narr "[persistent.youname!c] looks down at his Babelgram."
    show david neutral
    david "Jim, I have something to confess."
    me "Yeah?"

    menu:
        "It was fun hacking with you.":
            show david happy
            david "...It was fun hacking with you."
            me "Would you say you'd do it all over again if you could?"
            narr "He laughs weakly."
            david "Yeah, maybe I would."
            narr "..."
        "I read your diary.":
            david "I {i}did{/i} read your diary."
            me "What?! How?"
            david "Back in another loop. I took your phone while you were sleeping."
            me "And how'd you guess the password?"
            david "By watching you type it, over and over again, across many different loops."
            me "I... I don't know what to say."
            david "Well, I'm sorry. I really didn't know what else to do."
            me "It's okay, I guess."
            me "There's nothing really sensitive in there..."
            me "...and anything more than a week old is stored on a different machine."
            david "Thanks. If only you were {i}this{/i} forgiving every loop."
            me "What?"
        "I love you.":
            david "I love you."
            show david happy
            david "Like, romantically."
            me "..."
            david "..."
            me "..."
            david "..."
            show david neutral
            me "..."
            david "..."
            show david sad
            narrex "..."

    call play_track_4_halfway from _call_play_track_4_halfway_4
    scene black
    narr "{b}Bad Ending.{/b}"

    $ persistent.loop = 10
    $ persistent.change_character_enabled = 1

    return
