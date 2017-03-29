import random

#-- Situation Starters that reference a moment --#
when_situation = [
    "Does anyone else remember the time that ",
    "how italians react when ",
    "mfw ",
    "mfw ",
    "tfw ",
    "tfw ",
    "the face white people make when ",
    "when ",
    "when ",
    "when ",
    "when faith hill comes on and ",
    "when someone tells you they love you and then you wake up and ",
    "when you or a loved one has been diagnosed with Mesothelioma and ",
    "when you on the phone with your mom and ",
    "when you and your girl at olive garden and ",
    "when you chillin on your phone and ",
    "when you dead inside and ",
    "when you lit af in the mcdonalds line and ",
    "when you in class and ",
    "when you in panera and ",
    "when you in the middle of being roasted and ",
    "when you meet her parent and ",
    "when you stealing out of the cleft lip donation jar at kfc and ",
    "when you're about to cum and ",
    "when you're at the store and ",
    "when you're grounded and ",
    "when you're hiding from your ex and ",
    "when you're way too high and ",
    "when your friend starts flirtin with your crush and ",
    "when your girl and ",
    "when you're hittin it from the back and ",
    "when you're trying to return something at walmart and ",
    ]
#-- Singular Nouns --#
singular_noun = [
    "a baby in a minion costume ",
    "a big group of white ppl ",
    "a doggo ",
    "a kid with a fake girlfriend and a fake pair of jordans ",
    "a minion ",
    "a neckbeard ",
    "a police officer ",
    "a soundcloud rapper ",
    "a thicc ass girl ",
    "a trump supporter ",
    "alex jones ",
    "an anime body pillow comes to life and ",
    "bernie ",
    "crazytown (band ) ",
    "dj khaled ",
    "everyone is lit af and you have a job interview tomorrow and your boy ",
    "guy fieri's band ",
    "kellyanne conway ",
    "kim il sung ",
    "los lonely boys ",
    "one tiny egg ",
    "the GOP ",
    "the whole squad ",
    "someone ",
    "your fav instagram model ",
    "the substitute teacher ",
    "trump ",
    "two stepdads ",
    "ur friend ",
    "ya boy ",
    "you nut but she keep sucking and ",
    "you're getting cyberbullied by your family and everyone pauses because one of them ",
    "your 5th grade teacher walks up behind you and covers your eyes and ",
    "your cousin ",
    "your dad's friend ",
    "your dad ",
    "your mom ",
    "your most woke friend ",
    "your principal ",
    "your scariest white friend ",
    "your youngest cousin ",
    ]
#-- Actions for Singular Nouns --#
singular_action = [
    "adds you on snapchat",
    "asks if there's anything less spicy",
    "asks if you got any games on your phone",
    "asks if you remember the 90s",
    "asks to cheat off u",
    "asks to speak to the manager",
    "assumes your gender",
    "assures you that anime isn't real",
    "avoids responsibility",
    "becomes your step parent",
    "burns one and asks if you blaze too",
    "buys a gram for $40",
    "buys clothes at ikea",
    "buys games on the ziosk",
    "calls you a bitch ass faggot",
    "calls you a snowflake",
    "calls you a thot",
    "calls you daddy",
    "changes ur bio to 'hacked at 40k!!'",
    "decides to order taco bell with a coupon",
    "destroys capitalism",
    "discusses their communist ideology",
    "does beyblade in the cvs parking lot",
    "doesn't pass the aux",
    "eats ass",
    "falls in love with a fake anna kendrick profile",
    "falls into a k-hole",
    "finds your pornhub favorites",
    "finds your reddit",
    "forgets to clear their search history",
    "gets an infection and dies",
    "gets pulled over and the cop says 'dump out your weed BOOII'",
    "gets stopped by airport security",
    "gets they c*** s****d",
    "gets too high and spooks themselves",
    "gives you that look",
    "goes ass to mouth",
    "goes on a date with their family member",
    "goes to hooters with no money",
    "has been diagnosed with Mesothelioma",
    "hit you with that third narcan",
    "incinuates that jet fuel can't melt steel beams",
    "interjects politely, yet firmly, 'oh no baby! what is you doin??'",
    "is doing laundry and reaches for that sock",
    "is entitled to a lump sum",
    "is finally single",
    "is flummoxed by everything",
    "is mean on reddit",
    "is supportive of your goals",
    "jokes about suicide",
    "kisses their dad on the lips",
    "leaves a baby in a hot car",
    "logs onto myspace",
    "makes you watch while they play overwatch",
    "overcomes adversity",
    "practices something new",
    "proudly makes a harambe joke against all odds",
    "pulls up and says 'hey it's your uber driver'",
    "puts pineapple on pizza",
    "reminds you of that time you got too high",
    "runs like naruto",
    "says 'BOIII'",
    "says 'Build That Wall'",
    "says 'don't go to school tomorrow'",
    "says 'i dont care if you're black, brown, yellow or normal'",
    "says 'please do not swear on my profile'",
    "says Jeb is a big, fat mistake",
    "says deadass",
    "says eating ass is gay",
    "says eating ass is not gay",
    "says eating ass is VERY gay",
    "says jeb is a mess",
    "says jeb is a waste",
    "says other rappers aint shit",
    "says 'Please Clap'",
    "says some racist shit",
    "says 'ice cream machine broke'",
    "says 'if you on suboxone you aint clean'",
    "screams 'JCOLE WENT PLATINUM WITH NO FEATURES'",
    "screenshots your snap story",
    "sends nudes on 'accident'",
    "sends nudes on accident ",
    "sips the bong",
    "shouts 'That's a Spicy Meataball'!",
    "states firmly 'I prefer not to specify my race'",
    "starts a pyramid scheme",
    "starts a fight in the khols parking lot",
    "starts showing you old memes",
    "starts talking about airsoft",
    "starts typing 'www.p' into your browser",
    "steals someone's phone at ultra Miami my boy's phone",
    "steals your girl",
    "steals your man",
    "still talks about how 2016 was the 'worst year ever'",
    "tags you in a weak ass meme",
    "talks about you behind your back",
    "talks shit on twitter",
    "tells you they're keeping the baby",
    "tells you they're vegan",
    "thinks about 'Go Sox!'",
    "thinks about those beans",
    "tries starting a small business",
    "tries to kiss you",
    "tries to make a meme",
    "unironically screams 'worldstar'",
    "upholds american imperialism",
    "uses a pacsun giftcard",
    "vapes fentanyl from the deep web",
    "wears different clothes",
    "whispers 'another one'",
    "whispers 'not my president'",
    ]
#-- Opinionated Starting Phrases --#
opinion = [
    "Even though ",
    "I don't really care if ",
    "Just because ",
    "Okay, well even if ",
    "So what if ",
    "Well, actually... because ",
    "While ",
    ]
#-- Someone who isn't me --#
swimmy = [
    "Americans ",
    "everyone else ",
    "everyone but me ",
    "republicans ",
    "that girl from the bathroom at the flea market ",
    "The Gays ",
    "weebs ",
    "you ",
    "you and your friends ",
    "your dad's friend ",
    ]
#-- Potentials --#
potential = [
    "are totally in love with anyone whom's  ",
    "can pretend to be ",
    "is/are ",
    "is/are desperate to be ",
    "is/are really not into people who are ",
    "is/are so judgmental of people who are ",
    "might be ",
    "seem(s) to be ",
    ]
#-- something kool to be (I am a...) --#
thing2be = [
    "a fuckin klansman",
    "a fucking cuck",
    "a lil virgin",
    "always losing on scratch tickets",
    "professional cyberbullies",
    "dating a person of color",
    "edgy",
    "going to ultra Miami",
    "into chris angel mindfreak",
    "into punk rock",
    "low key racist",
    "not into anal",
    "pansexual",
    "reddit moderator",
    "sexually attracted to Guy Fieri",
    "sexually frustrated... ",
    "shitposters",
    "sick at drawing hentai",
    "sick at eating ASS",
    "sick at fingerboarding",
    "sunburnt alcoholic dads",
    "supportive of gay shock therapy",
    "tough on the internet",
    "vegan",
    "voting against net neutrality",
    "wealthy enough to buy a gram for $40",
    ]
#-- self aggrandizing --#
selfaggrand = [
    "I always ",
    "I have to tell you that I love to ",
    "im going to make sure that i always ",
    "I'm literally out here just tryna ",
    "I'm out here makin this money while I ",
    "me and my boys are gonna sit back and ",
    "technology has enabled me to ",
    "that doesn't mean that I can't ",
    "there's a pretty good chance I will continue to ",
    "you can't FUCKIN stop me while i ",
    ]
#-- Sick shit 2 do (To Verbs)  --#
thing2do = [
    "add my sister's friends on facebook ",
    "ask to speak to the manager ",
    "ask for money on facebook ",
    "be a FUCKING virgin ",
    "become your step parent",
    "blast migos ",
    "build a trampoline for the neighborhood kids ",
    "buy apps from the ziosk at applebees",
    "buy a dildo and never use it ",
    "buy a gram for $40",
    "buy a tweety bird jacket ",
    "buy bitcoins ",
    "buy condoms online ",
    "buy dip for teenagers ",
    "buy fake instagram followers ",
    "buy my groceries at the pharmacy ",
    "call asians 'orientals' ",
    "catfish myself ",
    "comment 'Amen' and share ",
    "crack open a fukkin cold one ",
    "create a fursona ",
    "date a girl who works at old navy ",
    "demonstrate peak male performance ",
    "deny climate change ",
    "eat 40 piece(s) of chicken nugget ",
    "eat ass ",
    "eat a hungry man dinner by myself ",
    "feed birds rice ",
    "finger my girl (virtually) ",
    "fly down there and whoop your ass ",
    "fuckin do dip ",
    "get a virus from a toolbar ",
    "get addicted to a stupid drug ",
    "get called out on facebook ",
    "get dressed up to go on chatroulette ",
    "get lunch out of the TRASH ",
    "get my c*** sucked ",
    "get my fukken septum pierced ",
    "get my phone stolen ",
    "give myself a nickname ",
    "go to VANS WARP TOUR ",
    "go to a sport ball game ",
    "go to college just to watch porn in the computer lab ",
    "go to olive garden alone ",
    "go to the 99 restaurant ",
    "go to ultra in miami ",
    "go to warped tour alone ",
    "google my OWN name ",
    "hack the DNC ",
    "have a child and raise it on my own ",
    "have surgery on my left knee ",
    "invite you to games on facebook ",
    "keep calm and ",
    "leave my trash in a store ",
    "light the FUCKING blunt ",
    "like someone's oldest pic ",
    "like your pic from 800 weeks ago ",
    "listen to neutral milk hotel on vinyl ",
    "Listen to the smiths alone ",
    "masturbate on the bus ",
    "meet a girl online for SEX NOW 0.5 meters away ",
    "order ethnic food but try to do the accent ",
    "orgasm to the pledge of allegiance ",
    "pirate a movie ",
    "play bingo bash ",
    "play runescape and neglect my family ",
    "play yugioh ",
    "post memes on church facebook ",
    "post my own nudes on ANONIB ",
    "post on facebook about what I WANT to talk about ",
    "pretend to buy a house ",
    "refuse to tip ",
    "rob a child ",
    "sell mids to your parents ",
    "send your bitch a smiley ",
    "share my credit card info ",
    "share racist memes ",
    "sip the fuckin bong ",
    "sleep with an anime body pillow while linux installs ",
    "smash the patriarchy ",
    "smoke 10 weed ",
    "smoke mad dust ",
    "speak 4 languages: english, profanity, sarcasm & realshit ",
    "start a new gender ",
    "steal plastic gloves out of the hospital drawer (sexual purpose) ",
    "steal someone's phone at ultra Miami my boy's phone ",
    "suck c### ",
    "take cosplay photos ",
    "take twelve xanax ",
    "tell everyone I'm vegan ",
    "throw a ball into the air ",
    "throw a dart at a child (in a store) ",
    "throw a water bottle at a homeless person ",
    "throw an egg into the street ",
    "Try to haggle at 7-11 ",
    "use my coupon at sunglass hut ",
    "vape fentanyl from the deep web",
    "vape heavy ",
    "wear my minion costume ",
    "wear the same alphet as my profile pic ",
    "win at mafia wars ",
    ]
#-- reasons why / becauses --# 
howso = [
    "...THANK YOU VERY MUCH",
    "and that's none of your business",
    "because I can",
    "because i am a Hacker",
    "because i graduated top of my class in the navy seals",
    "because i'm fuckin american. (fuck yeah)",
    "because obama became president",
    "because you still a lil bitch",
    "becuse i said so!",
    "cuz i got it like that",
    "despite my addiction to writing furry erotic fiction",
    "even when america crumbles",
    "even when it's not that lit",
    "every damn day",
    "like a boss.",
    "like a real punk rocker",
    "so please get the FUCK off my page...",
    "so please keep your comments to yourself",
    "so stay out of mine and my husband' 's inbox !!",
    "while i get my identity stole",
    ]
def when():         #-- Situation Starters that reference a moment --#
    when1 = random.choice(when_situation)
    return when1
def sing_noun():    #-- Singular Nouns --#
    sing_noun1 = random.choice(singular_noun)
    return sing_noun1
def sing_act():     #-- Actions for Singular Nouns --#
    sing_act1 = random.choice(singular_action)
    return sing_act1
def opStart():      #-- Opinionated Starting Phrases --#
    op = random.choice(opinion)
    return op
def swim():         #-- Someone who isn't me --#
    swimlet = random.choice(swimmy)
    return swimlet
def pot():          #-- Potentials --#
    poten = random.choice(potential)
    return poten
def thing2b():      #-- something kool to be (I am a...) --#
    thing = random.choice(thing2be)
    return thing
def selfagg():          #-- Self-Aggrandizing --#
    selfaggr = random.choice(selfaggrand)
    return selfaggr
def koolshit():     #-- Sick shit 2 do (To Verbs)  --#
    kool = random.choice(thing2do)
    return kool
def whysthat():     #-- reasons why / becauses --# 
    whys = random.choice(howso)
    return whys

def meme(deep):
    meme_cat = ["when","when", "while","opinionated"] #add later  "broad", "callout", "defensive"
    meme_cat_select = random.choice(meme_cat)
    if meme_cat_select == "when":
        if deep == '1':
            meme = "::  %s%s%s" % (when(),sing_noun(),sing_act())
            print(meme)
        if deep == '2':
            meme = "::  %s%s%s and %s" % (when(),sing_noun(),sing_act(),sing_act())
            print(meme)
        if deep == '3':
            meme = "::  %s%s%s and %s and %s" % (when(),sing_noun(),sing_act(),sing_act(),sing_act())
            print(meme)
        if deep == '3':
            meme = "::  %s%s%s and %s and %s and also %s" % (when(),sing_noun(),sing_act(),sing_act(),sing_act(),sing_act())
            print(meme)
        else:
            meme = "::  %s%s%s" % (when(),sing_noun(),sing_act())
            print(meme)
            
    if meme_cat_select == "while":
        if deep == '1':
            meme = "::  %s%s%s%s, %s%s%s" % (opStart(),swim(),pot(),thing2b(),selfagg(),koolshit(),whysthat())
            print(meme)
        if deep == '2':
            meme = "::  %s%s%s%s, %s%s,and %s%s" % (opStart(),swim(),pot(),thing2b(),selfagg(),koolshit(),koolshit(),whysthat())
            print(meme)
        if deep == '3':
            meme = "::  %s%s%s%s%s%s, and %s, and %s%s" % (opStart(),swim(),pot(),thing2b(),selfagg(),koolshit(),koolshit(),koolshit(),whysthat())
            print(meme)
        else:
            meme = "::  %s%s%s%s, %s%s%s" % (opStart(),swim(),pot(),thing2b(),selfagg(),koolshit(),whysthat())
            print(meme)
            
    if meme_cat_select == "opinionated":
        if deep == '1':
            meme = "::  %s%s%s... %s%s%s" % (opStart(),sing_noun(),sing_act(),selfagg(),koolshit(),whysthat())
            print(meme)
        if deep == '2':
            meme = "::  %s%s%s, and %s... %s%s%s" % (opStart(),sing_noun(),sing_act(),sing_act(),selfagg(),koolshit(),whysthat())
            print(meme)
        if deep == '3':
            meme = "::  %s%s%s, and %s... %s%s, and %s%s" % (opStart(),sing_noun(),sing_act(),sing_act(),selfagg(),koolshit(),koolshit(),whysthat())
            print(meme)
        else:
            meme = "::  %s%s%s, %s%s%s" % (opStart(),sing_noun(),sing_act(),selfagg(),koolshit(),whysthat())
            print(meme)
def wowe():
    print()
    print("""
¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯
#--                           Meme Research Lab                            --#
#--                                                                        --#""")
    mememake = input("#--                          Generate Meme? [y/n]                          --#\n[ayy@lmao~/] $ ")
    if mememake == 'y':
        manymeme = int(input("#--                         How many you want fam?                        --#\n[ayy@lmao~/] $ "))
        deep = input("#--                     How many layers you want? [1-3]                    --#\n[ayy@lmao~/] $ ")
        print("""
¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯
#--                              k here u go                               --#
##############################################################################
""")
        print()
        for i in range(manymeme):
            meme(deep)
        wowe()
    elif mememake == 'n':
        print('ok')
        exit
    else:
        wowe()
        
wowe()


