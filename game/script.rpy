# Big Rig Lovers. The game.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("[name]")
define k = Character("Kaitlin")
define c = Character("Chad")
define a = Character("Andy")
define d = Character("Mr. Anderson")
define dad = Character("Dad")
define mom = Character("Mom")





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image dad = "images/ChDad.png"
    image mom = "images/ChMom.png"


    # These display lines of dialogue.
    
    scene black
    with fade

    "Welcome to Big Rig Lovers!"
    python:
        name = renpy.input("What is your name?")
    
        name = name.strip() or "Autumn"
    
    "Hello [name]! You are new kid moving into MotorVille!"
    "You'll meet some colorful characters, and make some tough choices!"
    "Enjoy yourself!"
    
    scene bedrom
    with fade
    
    play music "home.mp3" fadeout 1
    
    show dad:
      xalign 0.25
      yalign 1.0
    
    dad "Well, what do we think? Pretty good right?"
    
    show mom:
        xalign 0.75
        yalign 1.0
    
    mom "It looks lovely dear! What do you think [name]?"
    
    menu:
        "It's okay, I guess.":
            jump choice1_neu
        
        "Not too bad honestly. I was expecting worse":
            jump choice1_pos
        
        "Ugh, why did we have to move?!":
            jump choice1_neg
        
    label choice1_neu:
        $menu_flag = True
        
        dad "I'll take it! I know moving to a new place is never easy."
        
        jump choice1_done
    
    label choice1_pos:
        $menu_flag = True
        
        dad "It'll be just like it was in Port Boat, you'll see!"
        
        jump choice1_done
        
    label choice1_neg:
        $menu_flag = True
        
        dad "I know you miss home, but this was necessary for us!"
        
        jump choice1_done

    label choice1_done:
    
    mom "Let's see, now that we're all unpacked and set up, what else do we need to do?"
    mom "Oh yeah, I'm gonna give your new school a call. Ready to become a part of MHS?"
    p "Ready as I'll ever be."
    mom "I’m going to call the school, I’ll be right back."
    hide mom
    show dad
    dad "Hey [name], I just wanted to say, thank you."
    dad "I know moving is always difficult, but with this new job, our family will be able to have more,"
    dad "and I should be home a lot more nights than I was before."
    p "I know. I’m just going to miss it a lot. It’s hard to leave everything behind."
    show mom:
        xalign 0.75
        yalign 1.0
    
    mom "I just got off the phone."
    mom "Hey, [name] would you be okay with taking a trip to the school right now?"
    mom "They said they can give you a quick tour before you start your first day of classes tomorrow!"
    p "I guess so..."
    dad "Sounds great! I’ve got to go fill out some paperwork at the new company so I’ll see both of you after."

    scene school
    with fade
    
    play music "school.mp3" fadeout 1
    
    mom "Well, this is your new school."
    p "Wow, it's huge! Much bigger than my last one."
    mom "MotorVille is a much bigger town. Well let's go in!"
    
    scene hallway
    with dissolve
    
    "Secretary" "You must be [name]. Welcome to MHS!"
    "Secretary" "I'm going to have your mother fill out some paper work."
    "Secretary" "I want you to meet Kaitlin. She'll be your tour guide!"
    
    image kaitlin_base = "images/ChKaitlinHipPose.png"
    image kaitlin_show = "images/ChKaitlinShowing.png"
    image kaitlin_explain = "images/ChKaitlinExplain.png"
    
    show kaitlin_base
    
    k "Sup, [name]! I'm Kaitlin! You're going to love it here, everyone does!"
    p "Hey, nice to meet you!"
    k "Same here! I'm excited to get to know you!"
    hide kaitlin_base
    show kaitlin_show
    k "Well, let's get this show on the road!"
    k "Here at MHS, we are a community first and foremost. You'll meet many new friends, and we all help each other out for the most part."
    hide kaitlin_show
    show kaitlin_explain
    k "Not everyone gets along, but what school has everyone be all buddy buddy all the time anyway?"
    play audio "tire.mp3"
    "You hear tires screeching, and engines revving getting closer and closer until..."
    play audio "punch.opus"
    with hpunch
    "WHAM!"
    image andy_base = "images/ChAndyAlt.png"
    show andy_base
    "You are knocked onto the floor as books and papers fly everywhere. You look up to see a pick-up truck also knocked on the ground"
    a "Oof, ouch, owie!"
    hide andy_base
    image andy_sad = "images/ChAndySad.png"
    show andy_sad
    a "Uhh... Sorry!!! So Sorry!!! I'm running late!!!"
    hide andy_sad
    image andy_blush = "images/ChAndyBlushing.png"
    show andy_blush
    hide andy_blush
    play audio "enginestart.mp3"
    "The truck picks up his books and speeds off"
    
    k "OMG! Are you alright?"
    
    menu:
        "Yeah... I think....?":
            jump choice2_neu
        
        "I'm okay considering!":
            jump choice2_pos
        
        "I can't feel my legs....":
            jump choice2_neg
        
    label choice2_neu:
        $menu_flag = True
        
        k "Phew, that's a relief."
        
        jump choice2_done
    
    label choice2_pos:
        $menu_flag = True
        
        k "You're a strong girl!"
        
        jump choice2_done
        
    label choice2_neg:
        $menu_flag = True
        
        k "Here, let me help you up!"
        
        jump choice2_done

    label choice2_done:
    
    "With Kaitlin's aid you are able to wobbly stand up"
    hide kaitlin_explain
    show kaitlin_base
    k "That is Andy Pick-Up. He's sweet, if not awkward"
    k "Anyway, the bell's about to ring so I'll show you a classroom once it clears out."
    "Bell rings, students file out of various classrooms."
    play audio "chad_rev.mp3"
    "A deafening roar can be heard"
    image chad_base = "images/ChChadAlt.png"
    image chad_angry = "images/ChChadAngry.png"
    show chad_base:
        xalign 1.0
        yalign 1.0
    
    c "Smell ya later, Mr. Anderson!!! I've got some cars to crush!!!"
    image kaitlin_annoy = "images/ChKaitlinAnnoyed.png"
    hide kaitlin_base
    show kaitlin_annoy:
        xalign 0.25
        yalign 1.0
    k "Chad! Don't make me report you to the dean!!!"
    hide chad_base
    show chad_angry:
        xalign 1.0
        yalign 1.0
    c "Please! As if Ms. Perfect would risk getting on my bad side!"
    image chad_thinking = "images/ChChadThinking.png"
    hide chad_angry
    show chad_thinking:
        xalign 1.0
        yalign 1.0
    c "Who's the fresh meat?"
    p "I'm..."
    hide chad_thinking
    show chad_happy:
        xalign 1.0
        yalign 1.0
    c "What?! Can't you hear you from up here"
    c "Smell ya later, LOSERS!!!"
    hide chad_happy
    play audio "chad_rev.mp3"
    "Chad speeds off, purposely bumping into some of the other students"
    hide kaitlin_annoy
    image kaitlin_facepalm = "images/ChKaitlinFacepalm.png"
    show kaitlin_facepalm
    k "Sorry about that. Chad, is quite a handful..."
    p "I can see that."
    k "Yeah, but we make do."
    hide kaitlin_facepalm
    show kaitlin_base
    k "Anyway, let's check out a class."
    
    scene classroom
    with dissolve
    
    show kaitlin_show:
        xalign 0.75
        yalign 1.00
    k "So this is a standard classroom! Not too different from your old school probably."
    image anderson = "ChMrAnderson.png"
    k "And this is Mr.Anderson, he teaches English, Writing, and Literature!"
    show anderson:
        xalign 0.25
        yalign 1.00
    "Slightly invading your personal space, Mr. Anderson introduces himself"
    d "Hello! David Anderson at your service! I look forward to having a new mind in my classroom!"
    hide kaitlin_show
    show kaitlin_base
    k "Well, let's get going. We've got a few more stops..."
    
    scene hallway
    with dissolve
    
    show kaitlin_base
    "The rest of the tour continues. You see various different areas until you end up back at the beginning"
    k "Well that's MHS. I'm sure there's some stuff I missed, but you'll get used to it quickly."
    k "So what do you think of MHS now?"
       
    
    menu:
        "It's got some interesting people. I'll see how it goes!":
            jump choice3_neu
        
        "I'm sold. This place looks awesome!":
            jump choice3_pos
        
        "Honestly, this place sucks in comparison to my last school.":
            jump choice3_neg
        
    label choice3_neu:
        $menu_flag = True
        
        k "You bet! And you'll only meet more of them!"
        
        jump choice3_done
    
    label choice3_pos:
        $menu_flag = True
        
        k "I'm glad! You're going to have such a great time!"
        
        jump choice3_done
        
    label choice3_neg:
        $menu_flag = True
        
        hide kaitlin_base
        show kaitlin_annoy
        
        k "Well, the tour doesn't show everything. Maybe you'll change your mind."
        
        hide kaitlin_annoy
        show kaitlin_base
        jump choice3_done

    label choice3_done:
        
    k "Hey, here's my phone number! If you need help getting around or just want someone to talk to, feel free to text me!"
    k "It was great meeting you! See you tomorrow!"
    "You exchange numbers with Kaitlin as she takes her leave"
    
    scene black
    with dissolve
    
    "You and Mom head back home for dinner, and then you get ready for bed. Tomorrow is going to be a big day"
    
    pause .7
    
    scene bedrom
    with dissolve
    
    play music "late.mp3" fadeout 1
    
    "It’s the usual bright and sunny morning"
    p "Dammit, my alarm clock is in the wrong time zone!!! I'm going to be late on the first day!!!"
    "It's the usual awful sunny morning"
    p "Crap! Crap! Crap!"
    "You get through your morning routine in record time and head off to catch the bus"
    
    scene street
    with dissolve
    
    p "Almost there, I'm gonna make it!"
    p "NO! Wait!"
    play audio "bus_depart.mp3"
    "The bus pulls away, without you"
    p "Crap! This is awful! How am I supposed to get to school now?"
    play audio "horn.mp3"
    "You hear tires screeching and horns honking"
    a "Darn, missed the bus again!!!"
    "Andy shows up out of breath. Seems he also woke up late"
    
    show andy_sad
    
    a "Oh no, I guess I'll have to burn more gas if I'm going to make it on time..."
    hide andy_sad
    show andy_blush
    "Andy notices you standing there"
    a "Hey, you're that new kid aren't you? Did you also miss the bus?"
    image andy_angry = "images/ChAndyAngry.png"
    image andy_think = "images/ChAndyThinking.png"
    menu:
        "Yeah, and on my first day too...":
            jump choice4_neu
        
        "Unfortunately. I just missed it by a second!":
            jump choice4_pos
        
        "Noooooooo, I totally didn't miss the bus at all...":
            jump choice4_neg
        
    label choice4_neu:
        $menu_flag = True
        hide andy_blush
        show andy_sad
        a "Oh....Yeah that isn't the best...."
        
        hide andy_sad
        show andy_base
        
        jump choice4_done
    
    label choice4_pos:
        $menu_flag = True
        
        hide andy_blush
        show andy_angry
        
        a "Wow, that stinks! You were so close!"
        
        hide andy_angry
        show andy_base
        
        jump choice4_done
        
    label choice4_neg:
        $menu_flag = True
        
        hide andy_blush
        show andy_think
        
        
        a "Really? Then why didn't you get on the bus?"
        
        hide andy_think
        show andy_base
        
        jump choice4_done

    label choice4_done:
    
        p "Well I guess if I'm going to be late, at least I'm not the only one late."
        hide andy_base
        show andy_blush
        a "I mean, we might not be late."
        p "What? How? We totally missed the bus and the school is too far to walk."
        "Andy's passenger side door opens"
        hide andy_blush
        show andy_base
        a "Hop in, we're making sure you aren't late on your first day!"
        p "Are you sure about this???"
        a "Yeah I'm sure! Let's go!"
        "Reluctant at first, you sit down in the passenger seat. The interior looks and smells rather plain"
        a "Buckle up!"
        "After securing yourself in the seat, Andy slams the door closed, puts the pedal to the metal and takes off!"
        
        scene school
        with dissolve
        
        "You arrive at the school with only a minute before the bell, Andy lets you out"
        image andy_happy = "images/ChAndyHappy.png"
        show andy_happy
        a "Hey we might just make it after all, what room number is your homeroom?"
        p "I'm in 105A"
        a "That's right next to my room, I'll show you the way"
        
        scene hallway
        with dissolve
        
        play music "school.mp3" fadeout 1
        
        "Hurrying, you make it to your classroom. Before going inside, you turn to Andy and say..."
        p "Thanks Andy, I super appreciate it!"
        show andy_blush
        a "Don't worry about it! Here's my phone number, in case this happens again!"
        
        scene classroom
        with dissolve
        
        "Quickly exchanging numbers, you step into the classroom, the bell rings immediately."
        show anderson
        d "Woah! Cutting it close aren't we? It's fine though. I'm sure you just got lost in the halls!"
        d "Why don't you take that empty desk over there, right next to Chad."
        play audio "chad_rev.mp3"
        "Chad starts revving his engine"
        hide anderson
        show chad_base:
            xalign 1.0
            yalign 1.0
        c "Yeah new kid, you can even sit in my driver's seat if you'd like! I save that seat for the real hotties!"
        show chad_base:
            xalign 1.00
            yalign 1.00
        show anderson:
            xalign 0.20
            yalign 1.00
        d "Chad! Do you need to stay after school for detention, again?"
        hide chad_base
        show chad_angry:
            xalign 1.00
            yalign 1.00
        c "It was just a joke, bro! Can't you guys ever take a joke?"
        "Unfortunately, you sit next to Chad"
        d "After I take attendance, if you want to introduce yourself to the class, that would be swell!"
        hide chad_angry
        show anderson
        "Mr. Anderson counts out some of the students. After about a minute, he's all done"
        d "Alrighty, that covers attendance, [name] come on up!"
        show anderson:
            xalign 0.20
            yalign 1.00
        p "Hey, I'm [name]. Nice to meet all of you!"
        d "So where are you from?"
        p "I'm from Port Boat, my dad worked for the big tug boat company down there."
        image chad_happy = "images/ChChadHappy.png"
        show chad_happy
        c "If you're half as good as your pops, maybe you could give me a tug if you catch my drift!"
        d "That's enough Chad! Speak out again and it's two days detention!"
        hide chad_happy
        image chad_po = "images/ChChadPOd.png"
        show chad_po:
            xalign 1.00
            yalign 1.00
        c "Fuck that! I didn't do nothing!!!"
        d "That's it Chad, head to the principal's office, now!"
        play audio "chad_rev.mp3"
        play audio "tire.mp3"
        "Chad drives to the front of class and starts doing donuts as he leaves the room"
        hide chad_po
        show anderson
        d "I'm so sorry, [name]. If he keeps this up feel free to reach out. We do not tolerate such behavior in this classroom."
        
    menu:
        "It’s okay. It doesn’t bother me.":
            jump choice5_neu
        
        "Thanks for comforting words":
            jump choice5_pos
        
        "It’s fine. Even though he’s a jerk, he’s kinda cute!":
            jump choice5_neg
        
    label choice5_neu:
        $menu_flag = True
        
        d "Thick skin huh? Good for you!
"
        
        jump choice5_done
    
    label choice5_pos:
        $menu_flag = True
        
        d "Always know that you can feel safe in our school!"
        
        jump choice5_done
        
    label choice5_neg:
        $menu_flag = True
        
        d "Well, er… If it ever is issue you just let me know okay?"
        
        jump choice5_done

    label choice5_done:
        "class resumes as normal. The material you're going over isn't anything too new for you"
        "The bell rings signifting the end of class. You get up, say goodbye to Mr. Anderson and head for your next class. Gym."
        
        scene hallway
        with dissolve
        
        "As you're on your way, you spot Kaitlin. She sees you and waves you down"
        show kaitlin_base
        k "Hey, [name]! How's the first day going so far?"
        p "It's going well I guess."
        k "That's good to hear! So you hear about the BIG DANCE?"
        p "No, when is it?"
        k "It's this weekend! You gotta go!"
        p "I don't know... it's only the first day..."
        k "Come on, you just gotta ask someone. Any ideas?"
    
    menu:
        "Andy seemed pretty nice.":
            jump choice6_neu
        
        "Hopefully I'm cool enough for Chad":
            jump choice6_pos
        
        "Nope, I think I'll just sit this one out.":
            jump choice6_neg
        
    label choice6_neu:
        $menu_flag = True
        
        k "Yeah and I'm sure Andy doesn't have takers. It'd be cool!"
        k "Shoot him a text and see what he says!"
        "You send Andy a text asking him about the dance"
        a "The D-Dance?! Um... sure... I guess so...."
        a "I mean, YEAH! I'd totally go with you! I'll meet you outside the school!"
        "Andy accepted your invite."
        k "See! Told you it'd work out!"
        
        jump choice6_andy_done
    
    label choice6_pos:
        $menu_flag = True
        
        hide kaitlin_base
        show kaitlin_facepalm
        
        k "Really? Chad? Well, I heard he doesn't have a date yet...."
        k "Here's his number, give him a try."
        "You send Chad a text asking him about the dance"
        c "Who is this? New kid? Well, I guess you did want some of the Chad after all."
        c "Well, I'm gonna be at school anyway because of that ass, Mr. Anderson. So why not?"
        c "I'll meet you outside before it starts. See ya nerd!"
        "Chad seemed to accept your invite"
        hide kaitlin_facepalm
        show kaitlin_explain
        k "Are you sure about this? Oh well, as long as you're going it should be fun."
        
        jump choice6_chad_done
        
    label choice6_neg:
        $menu_flag = True
        
        hide kaitlin_base
        show kaitlin_explain
        k "Are you sure? Well, I guess you're right. It might be too soon."
        
        jump choice6_alone_done
        
    label choice6_andy_done:
        show kaitlin_base
        k "Got gym class now right? Same here, let's roll!"
        "You head to the gymnasium for class."
        
        scene black
        with dissolve
        
        "The rest of your time at school seems to fly by. After a few days, it's finally time for the the day of the big dance!"
        stop music fadeout 1
        scene school
        with dissolve
        
        "You meet Andy outside the school..."
        show andy_blush
        play audio "wipers.mp3"
        a "Wow you look stunning..."
        p "Thanks Andy! Shall we go inside?"
        
        scene dance
        with dissolve
        play music "dance.mp3" fadeout 1
        
        "You head inside. The gymnasium is fully decorated, music is playing, and everyone is dancing."
        p "So... Care to dance?"
        show andy_sad
        a "I'm not a good dancer though..."
        p "Don't worry, just follow my lead..."
        
        scene black
        with dissolve
        
        "You spend the night having fun with Andy at the dance."
        "After, Andy gives you a lift home."
        jump end
        
    label choice6_chad_done:
        hide kaitlin_explain
        show kaitlin_base
        k "Got gym class now right? Same here, let's roll!"
        "You head to the gymnasium for class."
        
        scene black
        with dissolve
        
        "The rest of your time at school seems to fly by. After a few days, it's finally time for the the day of the big dance!"
        
        stop music fadeout 1
        
        scene school
        with dissolve
        
        "You meet Chad outside the school..."
        show chad_happy:
            xalign 1.0
            yalign 1.0
        c "You look totally smoking babe!"
        p "Thanks Chad! Shall we go inside?"
        
        scene dance
        with dissolve
        
        play music "dance.mp3" fadeout 1
        
        "You head inside. The gymnasium is fully decorated, music is playing, and everyone is dancing."
        p "So... Care to dance?"
        show chad_happy:
            xalign 1.0
            yalign 1.0
        c "Sure thing, but I just need to use the restroom. Gotta fuel up if you know what I mean!"
        "Chad pulls out a flask that smells like gasoline"
        p "Don't go too hard, you gotta drive me home remember?"
        "After a few minutes, Chad comes back. He takes you to the dance floor."
        
        scene black
        with dissolve
        
        "Many hours later, the dance is over and Chad gives you a lift home"
        jump end
        

        
    label choice6_alone_done:
        hide kaitlin_explain
        show kaitlin_base
        k "Got gym class now right? Same here, let's roll!"
        "You head to the gymnasium for class."
        
        scene black
        with dissolve
        
        stop music fadeout 1
                
        "The rest of your time at school seems to fly by. After a few days, it's finally time for the the day of the big dance!"
        "However, you decide to stay home..."
        

        
        scene bedrom
        with dissolve
        
        play music "home.mp3" fadeout 1

        p "Well, as much fun as the dance would be if I knew people... I've got some series I need to binge!"
        "You pull out your laptop and head to Netflix.com"
        p "It may take all night, but I'll get this new season done before I can see any spoilers!"
        "Sitting with your blanket and popcorn, you prepare yourself for a night of TV!"
        
        
        scene black
        with dissolve
        
        "Many hours later, you start to get tired and decide to crash before the season finale..."
        "As you're drifting off you wonder what it'd had been like at the dance."
        jump end

        
        
        
    label end:
        "To be continued..."
        

    return
