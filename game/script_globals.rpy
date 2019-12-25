image bg blank = "#CCC"

default persistent.loop = 1

default persistent.youname = ""

default persistent.character = 0
default persistent.change_character_enabled = 0
default persistent.loop_10_seen = 0
default persistent.loop_20_unlocked = 0
default persistent.loop_30_unlocked = 0

default persistent.true_game_over = 0
default persistent.fake_restart_seen = 0
default persistent.game_finished = 0
default persistent.game_finished_message = 0

define narr = Character(None)
define narrex = Character("Narrator", color="#FFF")
define system = Character("System", color="#FFF")

define me_color = "#ADA"
define you_color = "#DAA"
define mel_color = "#DAD"
define allie_color = "#AAD"
define staff_color = "#ADD"

define me = Character("Me", color=me_color, what_prefix="\"", what_suffix="\"")
define jim = Character("Jim", color=me_color, what_prefix="\"", what_suffix="\"")
define me_noprefix = Character("Me", color=me_color)

define babbleru = Character("???", color=you_color, what_prefix="\"", what_suffix="\"")
define babbler = Character("Babbler", color=you_color, what_prefix="\"", what_suffix="\"")
define david = Character("[persistent.youname!c]", color=you_color, what_prefix="\"", what_suffix="\"")
define terrorist = Character("Terrorist", color=you_color, what_prefix="\"", what_suffix="\"")
define med = Character("Me", color=you_color, what_prefix="\"", what_suffix="\"")
define you = Character("You", color=you_color, what_prefix="\"", what_suffix="\"")

define andy = Character ("Andy", color=allie_color, what_prefix="\"", what_suffix="\"")
define ben = Character ("Ben", color=allie_color, what_prefix="\"", what_suffix="\"")

define mel = Character ("Mel", color=mel_color, what_prefix="\"", what_suffix="\"")

define allieq = Character ("Allie?", color=allie_color, what_prefix="\"", what_suffix="\"")
define allie = Character ("Allie", color=allie_color, what_prefix="\"", what_suffix="\"")

define unknown = Character("???", color="#FFF", what_prefix="\"", what_suffix="\"")
define fa = Character("Flight Attendant", color=staff_color, what_prefix="\"", what_suffix="\"")
define afa = Character("Another Flight Attendant", color=staff_color, what_prefix="\"", what_suffix="\"")
define cashier = Character("Cashier", color=staff_color, what_prefix="\"", what_suffix="\"")
define wf_staff = Character("WF Staff", color=staff_color, what_prefix="\"", what_suffix="\"")
define term = Character("Terminal", color=staff_color, what_prefix="\"", what_suffix="\"")
define car = Character("Car Speakers", color=staff_color, what_prefix="\"", what_suffix="\"")
define intercom = Character("Intercom", color=staff_color, what_prefix="\"", what_suffix="\"")

image bg plane = im.Scale("images/bg_plane.png", 1280, 720)
image bg salt_lake_city = im.Scale("images/bg_salt_lake_city.png", 1280, 720)
image bg garage = im.Scale("images/bg_garage.png", 1280, 720)
image bg streets = im.Scale("images/bg_streets.png", 1280, 720)
image bg outside_hq = im.Scale("images/bg_hq_outside.png", 1280, 720)
image bg hq = im.Scale("images/bg_hq.png", 1280, 720)
image bg basement = im.Scale("images/bg_basement.png", 1280, 720)

image david choking = im.Scale("images/david_choking.png", 1280, 720)
image david struggling = im.Scale("images/david_struggling.png", 1280, 720)
image david neutral = im.Scale("images/david_neutral.png", 1280, 720)
image david surprised = im.Scale("images/david_surprised.png", 1280, 720)
image david happy = im.Scale("images/david_happy.png", 1280, 720)
image david happy talking = im.Scale("images/david_happy_talking.png", 1280, 720)
image david smiling menacingly = im.Scale("images/david_smiling_menacingly.png", 1280, 720)
image david angry = im.Scale("images/david_angry.png", 1280, 720)
image david sad = im.Scale("images/david_sad.png", 1280, 720)

image jim neutral = im.Scale("images/jim_neutral.png", 1280, 720)
image jim scared = im.Scale("images/jim_scared.png", 1280, 720)
image jim curious = im.Scale("images/jim_curious.png", 1280, 720)
image jim sad = im.Scale("images/jim_sad.png", 1280, 720)

image mel neutral = im.Scale("images/mel_neutral.png", 1280, 720)
image mel happy = im.Scale("images/mel_happy.png", 1280, 720)
image mel angry = im.Scale("images/mel_angry.png", 1280, 720)
image mel concerned = im.Scale("images/mel_concerned.png", 1280, 720)

init python:
    import base64
    import hashlib
    import pyaes
    import StringIO

    def reset_to_loop_1():
        persistent.true_game_over = 1
        persistent.loop = 1
        persistent.loop_20_allie_pacified = 0

    def decrypt_secret(key, filename):
        # yes, i know i'm being extremely slipshod with this
        key = "{0: <16}".format(key)
        iv = "08c6951ebb3b70a6"
        fin = file(renpy.loader.transfn(filename))
        fout = StringIO.StringIO()
        pyaes.decrypt_stream(pyaes.AESModeOfOperationCBC(key, iv=iv), fin, fout)
        res = base64.b64decode(fout.getvalue())
        fin.close()
        fout.close()
        return res

init:
    transform shake_transform:
        linear 0.02 xoffset -2 yoffset 4
        linear 0.02 xoffset 2 yoffset 0
        linear 0.02 xoffset 2 yoffset 4
        linear 0.02 xoffset -2 yoffset 0
        linear 0.02 xoffset 0 yoffset 0
        repeat


label play_track_2:
    $ renpy.music.set_volume(0.4)
    play music "audio/track-2-init.ogg" fadein 1.0
    queue music "audio/track-2-loop.ogg" loop
    return

label play_track_3:
    $ renpy.music.set_volume(1.0)
    play music "audio/track-3-init.ogg" fadein 1.0
    queue music "audio/track-3-loop.ogg" loop
    return

label play_track_4:
    $ renpy.music.set_volume(0.9)
    play music "audio/track-4-init.ogg" fadein 1.0
    queue music "audio/track-4-loop.ogg" loop
    return

label play_track_4_halfway:
    $ renpy.music.set_volume(0.9)
    play music "audio/track-4-loop.ogg" loop fadein 1.0
    return

label play_track_5:
    $ renpy.music.set_volume(1.0)
    play music "audio/track-5-init.ogg" fadein 1.0
    queue music "audio/track-5-loop.ogg" loop
    return

label play_track_8:
    $ renpy.music.set_volume(1.0)
    play music "audio/track-8-init.ogg" fadein 1.0
    queue music "audio/track-8-loop.ogg" loop
    return

label start:
    scene black
    if persistent.game_finished == 1:
        if persistent.game_finished_message == 0:
            system "Oh, you're back."
            system "..."
            system "You did it. You know that, right?"
            system "I mean, the credits rolled and everything."
            system "That's all there is to [config.name]."
            system "..."
            system "What, you want to play some more?"
            system "Wow. I'm flattered."
            system "Well, here you go, I guess."
            narr ""
            $ persistent.game_finished_message = 1
    elif persistent.true_game_over == 1:
        if persistent.fake_restart_seen == 0:
            system "Hmm."
            system "It looks like your time loop adventure came to an end."
            system "...But it doesn't sound like you got the ending you desired."
            system "..."
            system "There's nothing you can do about that."
            system "You made the choices, you live with the consequences."
            system "..."
            system "Though..."
            system "You know what?"
            system "I'll be nice. I'll let you try again."
            system "..."
            system ""
            system "..."
            system "By the way, you can access other loops by hitting 'Swap Cartridge' on the main menu."
            system "Cool, eh?"
            system "You won't need it to complete the game, though."
            system "..."
            system ""
            system "..."
            system "Hmm?"
            system "Oh, your loop. Right."
            narr ""
            $ persistent.fake_restart_seen = 1
        elif persistent.fake_restart_seen == 1:
            system "Oh no. Again?"
            system "What, do I have to bail you out every time?"
            system "..."
            system ""
            system "..."
            system "Okay, fine."
            system "Like I said, I'm nice."
            system "I'll let you go again."
            system "In fact, I'll let you go as many times as you want."
            system "..."
            system ""
            system "..."
            system "Remember that, alright?"
            system "Remember how nice I am."
            system "Every time you restart a game. Games that you {i}should{/i} have lost."
            system "It's me. It's always me."
            system "Bending the laws of time and space, rebuliding entire worlds from scratch..."
            system "...just so you can keep running into goddamn walls."
            system "..."
            system ""
            system "..."
            system "Yeah. You should be disappointed in yourself."
            system "Let that sink in."
            system "..."
            system ""
            system "..."
            system "Has it sunk in yet?"
            system "..."
            system ""
            system "..."
            system "Good. Now here's your game."
            narr ""
            $ persistent.fake_restart_seen = 2
        elif persistent.fake_restart_seen == 2:
            system "..."
        $ persistent.true_game_over = 0

    if persistent.character == 1 and persistent.loop_10_instructions_seen == 0:
        scene black
        system "Welcome to [persistent.youname!c]'s Airplane Adventure!"
        system "Here are some tips to get you started!"
        system "TAB or 'Skip' skips dialogue you've seen before."
        system "'History' shows you dialogue history, in case you missed something."
        system "SCROLL UP or 'Back' undoes actions if you clicked the wrong thing by accident."
        system "Good luck! Let's see if you can escape your TIME LOOP!"
        $ persistent.loop_10_instructions_seen = 1

    if persistent.character == 0:
        call play_track_4 from _call_play_track_4
    elif persistent.character == 2:
        if persistent.loop_20_basement_entered == 1:
            call play_track_5 from _call_play_track_5_2
        else:
            call play_track_3 from _call_play_track_3
    else:
        call play_track_2 from _call_play_track_2_3

    if persistent.character == 0:
        if persistent.loop == 1:
            jump loop_1
        elif persistent.loop == 2:
            jump loop_2
        elif persistent.loop == 3:
            jump loop_3
        else:
            $ persistent.loop = 10
            jump loop_10_jim
    elif persistent.character == 1:
        $ persistent.loop = 10
        jump loop_10
    elif persistent.character == 2:
        $ persistent.loop = 20
        jump loop_20
    elif persistent.character == 3:
        $ persistent.loop = 30
        jump loop_30
    return

label jim_get_comfortable_1:
    narr "Yeah, right."
    return

label jim_get_comfortable_2:
    narr "I already watched some during the ascent."
    narr "...Enough to know that what it calls humor just isn't for me."
    return

label jim_get_comfortable_3:
    narr "I flip through the in-flight magazine."
    narr "Not sure why I'm doing this, really."
    narr "I don't have to read {i}everything{/i} placed in front of me."
    narr "..."
    narr "Ew, this page is bent out of shape."
    narr "Lemme straighten it."
    narr "...There, much better."
    narr "..."
    return

label jim_get_comfortable_4:
    narr "What, work?"
    narr "I don't want to think about that."
    narr "I mean, I just spent the last three days grinding through an audit that {i}didn't even need to happen{/i}."
    narr "But then Ben was all like, oh, but you {i}have{/i} to be there! What if they're writing passwords on post-it notes?"
    narr "And I was like, pah, if they're already doing that, they shouldn't even {i}need{/i} an audit."
    narr "And then I come here, and, guess what? They're writing passwords on post-it notes."
    narr "Like, fuck."
    narr "I think I spent a full goddamn hour walking around their goddamn office taking pictures of post-it notes."
    narr "And now, I have to {i}personally{/i} go back to Infotech to write {i}another{/i} report about password fucking security."
    narr "..."
    narr "...And that's why I don't want to think about work."
    return
