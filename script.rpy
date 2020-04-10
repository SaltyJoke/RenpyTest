# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kanna")
define m = Character("Mishima")
define s = Character("Sou")
define ku = Character("Kugie")
define n = Character("Naomichi")
define a = Character("Anzu")
define fourth = Character("Fourth Wall")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg rubble:
        xzoom 1.75 yzoom 1.75

    show kanna smile
    k "There you guys are."
    hide kanna
    show mishima frown
    m "Ah, Miss Kanna, what a pleasant surprise." (multiple=3)
    m "I would invite you to join us, but where is miss Mai? If she is not nearby, you may be endangering her." (multiple=3)
    s "..." (multiple=3)
    hide mishima
    show kanna angry
    k "She's powered off, you snake ass. Now let Anzu and Kugie go before I rip out your fucking stomach. I'll let you bleed out everywhere and I'll make sure no one will want to help you."
    hide kanna
    show mishima frown
    m "That is very unbecoming language for a girl of your age, miss Kanna. I am not here to harm a child."
    m "Miss Kugie, please calm her down."
    hide mishima
    show kanna smile
    k "Now for you, Sou, give back the scarf. NOW."
    s "Not this again..."
    show kanna angry2
    k "Give. It. Back. It's the only thing I have left of Alice and I. Give it back."
    s "You seem to have taken a lot more from Alice, Kanna."
    s "Frankly, I don't think I influenced you as much as {i}him{/i}."
    show kanna bucket2
    k "{color=#a00}Give it back and no one will die in this room.{/color}"

    scene bg black
    show sou scared
    s "..."

    menu:
        "Give Kanna the scarf":
            jump give
        "Don't give Kanna the scarf":
            jump dont
    label give:
        hide sou
        show kugie one
        ku "Sou, don't."
        s "..."
        hide kugie
        jump dont
    label dont:
        show sou deadpan
        s "{color=#595}For Gin's sake...{/color}"

    scene bg rubble:
        xzoom 1.75 yzoom 1.75
    show kanna bucket2
    k "Good. I got it from you fair last time, and you stole it back like the rat you are."
    k "Now give it, or your stomach will be on the floor."
    hide kanna
    show kugie one
    ku "Kanna... That's enough."
    hide kugie
    show kanna angry
    k "NO!"
    k "I will kill you too if you get in my way! I can tell Mishima is trying to sway you to his side and use you to kill us. I will kill you and everyone here!"
    show kanna bucket
    k "...Well, besides Anzu. She's nice."
    hide kanna
    show naomichi neutral
    n "You guys should probably just listen. Wouldn't want this to get any more violent than it needs to be."
    hide naomichi
    show mishima angry
    m "{size=+10}Miss Kanna, ENOUGH IS ENOUGH!{/size}"
    m "{size=+5}I am trying my best here to protect everyone, including yourself, but your cruelty has gotten in the way!{/size}"
    m "{size=+5}I won't let you hurt anybody anymore, understand me!{/size}"
    m "{size=+5}I want to believe in your good side, but your actions make it harder to do! Just know that I am doing all of this to protect you, to protect as many people as possible!{/size}"
    m "{size=+5}Now you can continue to bitch around and cause chaos, or you can cooperate and apologize for your misdeeds!{/size}"
    m "{size=+5}I'm sorry for what I did to Alice, but it was for the greater good!{/size}"
    hide mishima
    show naomichi sweatgrin
    n "Looks like he's finally living up to his title as the mad science teacher."
    s "..."
    hide naomichi
    show mishima angry
    m "Just remember this, Kanna, I will never give up on you, even if it costs me my damn {color=#a00}life!{/color}"
    hide mishima
    show kanna smile
    k "Heh. Maybe now you are starting to understand the pain we feel."
    show kanna bucket2
    k "No... You're using me for something, I know it."
    show kanna bucket
    k "Maybe if you fall to your knees and cry, I might think about it."
    fourth "{color=#595}{size=-5}(Dear player, please ignore the fact that Kugie has exactly one sprite right now){size=-5}{/color}"
    hide kanna
    show kugie one # TODO: give Kugie more sprites
    ku "I'm not killing anyone. I won't kill for you OR Mishima!"
    ku "We're supposed to work together. You told me you were going to kill just Mishima. But now you're trying to kill Sou, Gin, and your own sister!"
    ku "How could you do or say such things? What happened to the Kanna I used to know!? The Kanna that would rely on her big sister or the adults no matter what!?"
    ku "Even if you KILL me! I'm not giving up on you; I still value you and your life as a big sister should. Even if you don't value mine..."
    s "{color=#595}So noisy...{/color}"
    hide kugie
    show mishima angry
    m "{size=+5}This is fucking absurd!{/size}"
    show mishima think
    m "..."
    m "Miss Kugie, I was not going to ask you to kill anybody. I was simply going to ask you to protect Miss Kanna before the doll targeting her tries to kill her."
    m "Yes, I said it. Every doll has been assigned a target to be killed."
    hide mishima
    show anzu dark
    a "..."
    s "{color=#595}Anzu...{/color}"
    hide anzu
    show kanna angry2
    k "Everyone left me, Kugie. No one wants to help me. I have no one to rely on besides myself and Alice at this point. It's clear all of you have turned your back on me by killing the one I trusted."
    show kanna smile
    k "Now all of you will pay. Every single one of you filthy mortals will pay with your {color=#a00}blood!{/color}"
    hide kanna
    show anzu dark
    s "{color=#595}Anzu is getting closer to Mishima...{/color}"
    s "M... Miss Anzu..."
    fourth "{color=#595}{size=-5}(Silox: \"Why do I hear boss music?\" Also, please forgive Kugie again.){/size}{/color}"
    hide anzu
    show kugie one
    ku "I've never left you! Every move I made, I thought of YOU, Kanna! I was hesitant to trust anyone because of them betraying you and killing Alice."
    ku "But that was just my failure as a big sister. If I didn't fail my first trial... you wouldn't feel alone."
    ku "Kanna, PLEASE! Please let me make it up to you. Stop this and stay by my side... I'll protect you, I'll help you. Just stop trying to murder everyone!"
    hide kugie
    show kanna angry
    k "No... No no no no no no no no! If you care, let me help you dummies and kill all the humans!"
    s "{color=#595}You should get going, then.{/color}"
    hide kanna
    show naomichi smile
    n "Let me know if I should punch someone, Kanna. I'm going into withdrawal over here."
    hide naomichi
    show mishima angry
    m "Get out now! We don't need any more bad influences for Kanna!"
    hide mishima
    show naomichi neutral
    n "Bad influence? This whole situation is your fault, so don't blame anyone but yourself."
    hide naomichi
    show sou deadpan
    s "...Kurumada? What are you saying?"
    hide sou
    show mishima frown
    m "Miss Kanna's situation is everybody's fault, but you're just making it worse. Please leave."
    s "{color=#595}Anzu is right behind him...{/color}"
    hide mishima
    show kugie one
    ku "...Kanna, please listen... We can work a way past this without a murder. You're just a kid; you can't and shouldn't murder anyone."
    ku "I don't know if I'm going to be able to murder. I'm just a high schooler, Kanna. How could I have the right to take away lives when I'm the one who threw mine away?"
    hide kugie
    show kanna angry2
    k "It's my fault you died. And I know that..."
    hide kanna
    show anzu dark
    a "..."
    s "{color=#595}She's raising a hand with something in it...{/color}"
    hide anzu
    show mishima frown
    m "I trust everybody in this room to do the right thing. {color=#a00}No blood needs to be shed.{/color}"
    hide mishima
    show kanna angry2
    k "Mishima, most of this shit is your fault. Don't play innocent, Mr. protector of the peace."
    hide kanna
    show sou stressed
    s "{color=#595}What should I do? Nothing is getting better...{/color}"
    s "{color=#595}But Anzu is...{/color}"
    show sou yell
    s "{size=+5}PROFESSOR! BEHIND YOU!"
    hide sou
    show kanna smile
    k "Do it! Now!"
    hide kanna
    show mishima worried
    "...!"
    hide mishima
    show kanna smile
    k "Mishima! Accept your fate and die for your {color=#a00}\"greater good!\"{/color}"
    hide kanna
    show kugie one
    ku "K-Kanna... Anzu...! Don't! He's not worth it!"
    hide kugie
    show mishima frown
    m "{color=#a00}Nobody move.{/color}"
    s "{color=#595}He... He got Anzu into a chokehold...{/color}"
    s "{color=#595}The professor must be really buff...{/color}"
    hide mishima
    show naomichi neutral
    n "You aren't gonna do shit."
    hide naomichi
    show kanna bucket
    k "..."
    hide kanna
    show kugie one
    s "Kugie. You knew about this, didn't you!?"
    k "I-I'm sorry..."
    hide kugie
    show mishima worried
    m "I... trusted you, miss Anzu. Why me? Isn't your target miss Reko?"
    hide mishima
    show anzu stressed
    a "J-Just clowning around..."
    hide anzu
    show mishima worried
    m "What is going on? This does not have to end this way! Everybody, please put aside your primitive instincts!"
    hide mishima
    show kanna angry
    k "{size=+5}{cps=25}{color=#a00}DIE YOU PIECE OF UTTER SHIT!!!{/color}{/cps}{/size}{nw}"
    hide kanna
    show mishima pain
    m "{size=+5}{cps=25}{color=#a00}AAAAAAAACK!!{/color}{/cps}{size=+5}{nw}"

    # This ends the game.

    return

    # https://discordapp.com/channels/598728377360187414/605722060920193044/692506373799411792
