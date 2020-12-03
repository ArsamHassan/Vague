import discord
from discord.ext import commands
import math
import random
import asyncio

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='v.', help_command=None)



@client.event
async def on_ready():
    print("Vague is now online!")
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="v.help | been helping since the Vietnam War"))


# Welcoming Command:


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("v.hello"):
        await message.channel.send("Hello, how are you doing today!")
    await client.process_commands(message)




@client.command()
async def kill(ctx):
    await ctx.send('Who do you wanna kill?')

    def check(msg):
        return ctx.author == msg.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    victim = msg.content

    option = [' with a bomb', ' with a water gun', ' by video calling', " by summoning a cringe bot like Equinox", " with a nuke"]
    real_option = random.choice(option)

    if victim == 'Vague':
        await ctx.send('Bruh you know Im the killer right?')
    else:
        await ctx.send(ctx.author.mention + ' killed ' + str(victim) + real_option)





@client.command()
async def hi(ctx):
    await ctx.send("Hello there! How are you doing today? Good, Fine, Bad?")

    def check(msg):
        return ctx.author == msg.author and msg.channel == ctx.channel and msg.content in ['Good', 'Fine', 'Bad']

    msg = await client.wait_for("message", check=check)
    if msg.content == 'Good':
        await ctx.send('Awesome! I hope you have an amazing day!')
    elif msg.content == 'Fine':
        await ctx.send('Hope you feel better!')
    elif msg.content == 'Bad':
        await ctx.send('Well, try playing some of my games, or use v.commands to see what other fun things I can do for you!')


# Wisdom comand

@client.command()
async def advice(ctx):
    total_sentences = [
        'Take time to know yourself. "Know thyself" said Aristotle. When you know who you are, you can be wise about your goals, your dreams, your standards, your convictions. Knowing who you are allows you to live your life with purpose and meaning.',
        'A narrow focus brings big results. The number one reason people give up so fast is because they tend to look at how far they still have to go instead of how far they have come. But its a series of small wins that can give us the most significant success.',
        'Show up fully. Dont dwell on the past, and dont daydream about the future, but concentrate on showing up fully in the present moment.',
        'Dont make assumptions. If you dont know the situation fully, you cant offer an informed opinion.',
        'Be patient and persistent. Life is not so much what you accomplish as what you overcome. ',
        'In order to get, you have to give. If you support, guide, and lead others, if you make contributions to their lives, you will reap the best rewards.',
        'Luck comes from hard work. Luck happens when hard work and timing and talent intersect.']
    wisdom = random.choice(total_sentences)
    await ctx.send(wisdom)


# Math Commands:

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@client.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a - b)


@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)


@client.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)


@client.command()
async def ptg(ctx, a: int, b: int):
    c_squared = (a ** 2) + (b ** 2)
    c = round(math.sqrt(c_squared), 2)
    await ctx.send(c)


@client.command()
async def help(ctx):
    embed = discord.Embed(title="***Vague Command List***",description=" ***Welcome*** :handshake: \n ``v.hello`` | ``v.hi`` \n ***Life*** :peace: \n  ``v.advice`` | ``v.kill`` \n ***Math*** :nerd: \n ``v.add`` | ``v.subtract`` | ``v.divide`` | ``v.multiply`` | ``v.ptg`` \n ***Games*** :video_game: \n ``v.fight`` | ``v.beef`` | ``v.hangman`` | ``v.galaxo``" , color=0x3498db)
    await ctx.send(embed=embed)




@client.command(name="fight")
async def fight(ctx):
    global times_used
    await ctx.send(f"You want smoke with me huh? Yes / No")

    # This will make sure that the response will only be registered if the following
    # conditions are met:
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
               msg.content in ["Yes", "No"]

    msg = await client.wait_for("message", check=check)
    if msg.content == "Yes":
        user2_hp = 100
        user1_hp = 100
        while True:

            await ctx.send(msg.author.mention + " **Do you want to**  ``Punch``, ``Defend`` or ``End``!")

            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["Punch", "Defend","End"]

            msg = await client.wait_for("message", check=check)
            if msg.content == "Punch":
                power = (random.randint(20, 60))
                ap = random.randint(20, 60)
                user2_hp = user2_hp - power if user2_hp - power > 0 else 0
                user1_hp = user1_hp - ap if user1_hp - ap > 0 else 0
                await ctx.send("You dealt " + str(power) + " damage! Vague is now left with " + str(user2_hp) + "hp!")
                if user2_hp <= 0:
                    break
                await asyncio.sleep(2)
                await ctx.send(f"Vague hit you for {ap}. You are now left with {user1_hp} hp")
                if user1_hp <= 0:
                    break
            elif msg.content == "Defend":
                bruh = random.randint(5, 45)
                user1_hp = int(user1_hp) + bruh
                if user1_hp >= 150:
                    user1_hp = 150
                    await ctx.send("You're now at max shield limit! Your HP: " + str(user1_hp))
                else:
                    await ctx.send('You increased by ' + str(bruh) + (" hp! Now you're at " + str(user1_hp) + '!'))

                await asyncio.sleep(2)
                if user2_hp <= 50:
                    bruh = random.randint(5, 45)
                    user1_hp = int(user2_hp) + bruh
                    await ctx.send("Vague healed by " + str(bruh) + " hp! He is now at " + str(user2_hp + bruh) + "!")
                else:
                    ap = random.randint(18, 65)
                    await ctx.send(f"Vague hit you for {ap}. You are now left with {user1_hp - ap} hp")


            elif msg.content == "End":
                await ctx.send(msg.author.mention + " hah! chicken! :chicken:.")
                break
        if user2_hp <= 0:
            await ctx.send(msg.author.mention + ' **You WON** :crown: \n*Vague is dead!* :skull:')
        elif user1_hp <= 0:
            await ctx.send('**You LOST** :skull_crossbones: \n*Vague WON* :crown:!')

    elif msg.content == "No":
        await ctx.send(msg.author.mention + " What a wimp.")


@client.command(name="hangman")
async def hangman(ctx):
    word_list = ['apple', 'banana', 'orange', 'school', 'vague', 'king', 'anime', 'home', 'minecraft', 'python']
    word = random.choice(word_list)
    word.upper()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    await ctx.send("Welcome to Hangman! You will have six tries to guess the correct answer! Enjoy!")
    hangman_word = "⎯ " * len(word_completion)
    await ctx.send(hangman_word)

    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author



    while not guessed and tries > 0:
        guess = await client.wait_for('message', check=check)
        guess = guess.content
        guess = str(guess)

        if guess == 'hint':
            await ctx.send('Word starts with ' + word[0])

        elif guess == word:
            guessed = True
            break

        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                await ctx.send("You already tried '" + guess + "'!")
            elif guess not in word:
                await ctx.send("'" + guess + "', isn't in the word!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                await ctx.send(("Nice, '" + guess + "' is in the word!"))
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                await ctx.send("You already tried " + guess + "!")
            elif guess != word:
                await ctx.send("Sorry, " + guess + " is not the word!")
                tries -= 1
                guessed_words.append(guess)



    if guessed:
        await ctx.send("Good Job! You Guessed the Word!")
    else:
        await ctx.send("I'm sorry, but you ran out of tries. The word was " + word + ". Maybe next time!")

'''
@client.command()
async def rule_book(ctx):
    rulebook = ['1. You can Punch, Defend, Kick, Special or End \n 2. "Kick" will deal x3 damagae, if userHP is below 30"]
'''




@client.command()
async def beef(ctx, member: discord.Member):
    await ctx.send(f"{member.mention}, what is your response ``Yes`` / ``No`` !")
    fighter_2 = ctx.author
    fighter = member
    user1ab = 1
    user2ab = 1
    round = 0
    round2 = 0
    def check(msg):
        return msg.author == member and msg.channel == ctx.channel and \
               msg.content in ["Yes", "No"]

    msg = await client.wait_for('message', check=check)

    if msg.content == 'Yes':
        def check(msg):
            return msg.author

        await ctx.send("The fight is ON! Both of you will go face to face, attacking and defending turn by turn! Type **'rulebook'** for the list of rules and actions! \n **Contestants:** \n \n \n Offender:" + ctx.author.mention + " \n Victim: " + member.mention + " \n \n**Begin!**")

        await asyncio.sleep(3)

        user1_hp = 100
        user2_hp = 100

        while user1_hp > 0 or user2_hp > 0:

                if member == msg.author:
                    await ctx.send(fighter_2.mention + " **Do you want to**  ``Punch``, ``Kick``, ``Defend``, ``Special`` or ``End``!")
                    round2 += 1

                if fighter_2 == msg.author:
                    await ctx.send(fighter.mention + " **Do you want to**  ``Punch``, ``Kick``, ``Defend``, ``Special`` or ``End``!")
                    round += 1



                msg = await client.wait_for("message", check=check)
                if msg.content == "Punch":
                    power = (random.randint(20, 60))
                    ap = random.randint(20, 60)

                    if msg.author == fighter_2:
                        user2_hp = user2_hp - power if user2_hp - power > 0 else 0
                        await ctx.send(fighter_2.mention + " dealt " + str(power) + " damage!" + fighter.mention + " is now left with " + str(user2_hp) + " hp!")
                        if user2_hp <= 0:
                            break
                    else:
                        user1_hp = user1_hp - ap if user1_hp - ap > 0 else 0
                        await ctx.send(fighter.mention + " dealt " + str(power) + " damage!" + fighter_2.mention + " is now left with " + str(user1_hp) + " hp!")
                        if user1_hp <= 0:
                            break

                elif msg.content == "Defend":
                    bruh = random.randint(18, 65)

                    if msg.author == fighter_2:
                        user1_hp = int(user1_hp) + bruh
                        if user1_hp >= 150:
                            user1_hp = 150
                            await ctx.send("You're now at max shield limit! Your HP: " + str(user1_hp))
                        else:
                            await ctx.send('You increased by ' + str(bruh) + (" hp! Now you're at " + str(user1_hp) + '!'))

                    else:
                        user2_hp = int(user2_hp) + bruh
                        if user2_hp >= 150:
                            user2_hp = 150
                            await ctx.send("You're now at max shield limit! Your HP: " + str(user2_hp))
                        else:
                            await ctx.send('You increased by ' + str(bruh) + (" hp! Now you're at " + str(user2_hp) + '!'))

                elif msg.content == 'Kick':
                    kik = random.randint(35, 45)


                    if msg.author == fighter_2:

                        if user1_hp == 150:
                            kik = kik * 2

                        user2_hp = user2_hp - kik if user2_hp - kik > 0 else 0
                        await ctx.send(fighter_2.mention + " dealt " + str(kik) + " damage!" + fighter.mention + " is now left with " + str(user2_hp) + " hp!")
                        if user2_hp <= 0:
                            break
                    else:
                        if user2_hp == 150:
                            kik = kik * 2

                        user1_hp = user1_hp - kik if user1_hp - kik > 0 else 0
                        await ctx.send(fighter.mention + " dealt " + str(kik) + " damage!" + fighter_2.mention + " is now left with " + str(user1_hp) + " hp!")
                        if user1_hp <= 0:
                            break

                elif msg.content == 'Special':
                    if msg.author == fighter_2:
                        if user1ab == 1:
                            if round2 >= 3:
                                boom = random.randint(60, 100)
                                user2_hp = int(user2_hp) - int(boom) if user2_hp - boom > 0 else 0
                                user1_hp = int(user1_hp) - 40 if user1_hp - boom > 0 else 0
                                await ctx.send(fighter_2.mention + " dealt " + str(boom) + " damage!" + fighter.mention + " is now left with " + str(user2_hp) + " hp!")
                                user1ab -=1
                                if user2_hp <= 0:
                                    break
                                elif user1_hp <=0:
                                    break
                            else:
                                await ctx.send('You can only use special on round 3 and after!')
                        elif user1ab == 0:
                            await ctx.send('You already used your special power! You have 0 left!')

                    elif msg.author == fighter:
                        if user2ab == 1:
                            if round >= 3:
                                boom = random.randint(60, 100)
                                user1_hp = int(user1_hp) - int(boom) if user1_hp - boom > 0 else 0
                                user2_hp = int(user2_hp) - 40 if user2_hp - boom > 0 else 0
                                await ctx.send(fighter.mention + " dealt " + str(boom) + " damage!" + fighter_2.mention + " is now left with " + str(user1_hp) + " hp!")
                                user2ab -=1
                                if user1_hp <= 0:
                                    break
                                elif user2_hp <= 0:
                                    break
                            else:
                                await ctx.send('You can only use special on round 3 and after!')
                        elif user2ab == 0:
                            await ctx.send('You already used your special power! You have 0 left!')


                elif msg.content == "End":
                    await ctx.send(msg.author.mention + " hah! chicken! :chicken:.")
                    break


        if user2_hp <= 0:
            await ctx.send(fighter_2.mention + ' **You WON** :crown: \n' + fighter.mention + ' is dead! :skull:')
        elif user1_hp <= 0:
            await ctx.send(fighter.mention + ' **You WON** :crown: \n' + fighter_2.mention + ' is dead! :skull:')

    elif msg.content == 'No':
        await ctx.send(msg.author.mention + ' never knew such cowards existed in this universe... :chicken:')
    else:
        await ctx.send(msg.author.mention + ' Invalid response!')


@client.command()

async def galaxo(ctx):
    global times_used
    await ctx.send(f"Welcome to galaxo! In this game you will be fighting against enemies at different levels! Final Boss level is 5! Each level, a new and stronger enemy will appear! You have only 1 life to defeat all the enemies, each round your hp will reset! Type 'ready' to start or 'no' to stop.")


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
               msg.content in ["ready", "no"]

    msg = await client.wait_for("message", check=check)
    if msg.content == "no":
        await ctx.send(msg.author.mention + ' left the game.')

    elif msg.content == 'ready':
        boss1 = 100
        boss2 = 155
        boss3 = 170
        boss4 = 225
        boss5 = 300
        userhp = 100
        special1 = 1
        special2 = 1
        special3 = 1
        special4 = 1
        special5 = 1

        while True:
            await ctx.send(ctx.author.mention + "Welcome to round 1, in this round you will be up against the first boss! \nName: Boss1 \nAttack: 30 - 50 \nHP: 100\n\n Shall we begin? `yes` / `no` \n\n If you want to choose levels type 'yes' and then in the next prompt, 'BossLevel(x)'")
            round = 1
            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel and \
                       msg.content in ["yes", "no"]

            msg = await client.wait_for("message", check=check)
            if msg.content == "no":
                break
            elif msg.content == 'yes':
                while round == 1:

                    await ctx.send(msg.author.mention + " **Do you want to**  ``Punch``, ``Defend`` or ``End``!")

                    def check(msg):
                        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["Punch","Defend","End", "BossLevel(2)", "BossLevel(3)", "BossLevel(4)", "BossLevel(5)", "GameHack"]

                    msg = await client.wait_for("message", check=check)

                    if msg.content == "GameHack":
                        await ctx.send("You have 9999 HP and your on the last level, enjoy!")
                        userhp = 9999
                        round += 4

                    if msg.content == "BossLevel(2)":
                        userhp = 125
                        round += 1
                        await ctx.send(ctx.author.mention + ' Congratulations! Welcome to round 2! In this round you will be up against a mighty boss! Additionally your HP has been increased to 125hp! \n\nName: Boss2\nAttack: 40 - 60\nHP: 125')

                    elif msg.content == "BossLevel(3)":
                        userhp = 135
                        round += 2
                        await ctx.send(ctx.author.mention + " Welcome to round 3, WOW you've reallly made it this far huh? Well your next opponent is tough, and you're hp is increased to 135, Good Luck! \n\nName: Boss3 \nAttack: 50 - 70\nHP: 150")

                    elif msg.content == "BossLevel(4)":
                        userhp = 135
                        round += 3
                        await ctx.send(ctx.author.mention + " Okay, wow! This is really impressive! However I think this will be the last round for you... Your hp is maxed out now, at 135 hp, and your next opponent is very notorious!\n\n Name:Boss4\nAttack: 50 - 70\nHP: 175")
                    elif msg.content == "BossLevel(5)":
                        userhp = 135
                        round += 4
                        await ctx.send("Formidable! You are one of a kind, onlu 0.001% of people reach this level! You are about to face the final boss, and I have to tell you even if you lose you did an awsome job!")


                    elif msg.content == "Punch":
                        power = (random.randint(20, 60))
                        ap = random.randint(30, 50)
                        boi = ap
                        boss1 = boss1 - power if boss1 - power > 0 else 0
                        userhp = userhp - ap if userhp - ap > 0 else 0
                        await ctx.send(
                            "You dealt " + str(power) + " damage! Boss1 is now left with " + str(boss1) + "hp!")
                        if boss1 <= 0:
                            round += 1
                            await ctx.send(msg.author.mention + ' **You WON** :crown: \n\nBoss1 is dead! :skull: \n\n You will now move on to round 2!')
                            userhp = 125
                            await ctx.send(ctx.author.mention + ' Congratulations! Welcome to round 2! In this round you will be up against a mighty boss! Additionally your HP has been increased to 125hp! \n\nName: Boss2\nAttack: 40 - 60\nHP: 125')
                            break
                        await asyncio.sleep(2)
                        await ctx.send(f"Boss 1 hit you for {ap}. You are now left with {userhp} hp")
                        if userhp <= 0:
                            round += 1
                            await ctx.send('**You LOST** :skull_crossbones: \n*Boss 1 WON* :crown:! \n\n You will have to restart from round 1, sorry!')
                            break
                    elif msg.content == "Defend":
                        bruh = random.randint(5, 45)
                        userhp = int(userhp) + bruh
                        if userhp >= 125:
                            userhp = 125
                            await ctx.send("You're now at max shield limit! Your HP: " + str(userhp))
                        else:
                            await ctx.send('You increased by ' + str(bruh) + (" hp! Now you're at " + str(userhp) + '!'))

                        await asyncio.sleep(2)
                        if boss1 <= 80:
                            bruh = random.randint(5, 45)
                            boss1 = int(boss1) + bruh
                            await ctx.send("Boss1 healed by " + str(bruh) + " hp! He is now at " + str(boss1 + bruh) + "!")
                        else:
                            ap = random.randint(30, 50)
                            await ctx.send(f"Boss1 hit you for {ap}. You are now left with {userhp - ap} hp")


                    elif msg.content == "End":
                        await ctx.send(msg.author.mention + " left the game. Your progress was not saved.")
                        break




                while round == 2:
                    await ctx.send(msg.author.mention + " **Do you want to**  ``Punch``, ``Defend`` or ``End``!")

                    def check(msg):
                        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["Punch","Defend", "End"]

                    msg = await client.wait_for("message", check=check)
                    if msg.content == "Punch":
                        power = (random.randint(30, 70))
                        ap = random.randint(40, 60)
                        boss2 = boss2 - power if boss2 - power > 0 else 0
                        userhp = userhp - ap if userhp - ap > 0 else 0
                        await ctx.send("You dealt " + str(power) + " damage! Boss2 is now left with " + str(boss2) + "hp!")
                        if boss2 <= 0:
                            round += 1
                            await ctx.send(msg.author.mention + ' **You WON** :crown: \n\nBoss2 is dead! :skull: \n\n You will now move on to round 3!')
                            userhp = 135
                            await ctx.send(ctx.author.mention + " Welcome to round 3, WOW you've reallly made it this far huh? Well your next opponent is tough, and you're hp is increased to 135, Good Luck! \n\nName: Boss3 \nAttack: 50 - 70\nHP: 150 ")
                            break
                        await asyncio.sleep(2)
                        await ctx.send(f"Boss2 hit you for {ap}. You are now left with {userhp} hp")
                        if userhp < 0 or userhp == 0:
                            await ctx.send('**You LOST** :skull_crossbones: \n*Boss 2 WON* :crown:!')
                            break
                    elif msg.content == "Defend":
                        bruh = random.randint(5, 45)
                        userhp = int(userhp) + bruh
                        if userhp >= 125:
                            userhp = 125
                            await ctx.send("You're now at max shield limit! Your HP: " + str(userhp))
                        else:
                            await ctx.send('You increased by ' + str(bruh) + (" hp! Now you're at " + str(userhp) + '!'))

                        await asyncio.sleep(2)
                        if boss2 <= 90:
                            bruh = random.randint(30, 60)
                            boss2 = int(boss2) + bruh
                            await ctx.send("Boss2 healed by " + str(bruh) + " hp! He is now at " + str(boss2 + bruh) + "!")
                        else:
                            ap = random.randint(40, 60)
                            await ctx.send(f"Boss2 hit you for {ap}. You are now left with {userhp - ap} hp")


                    elif msg.content == "End":
                        await ctx.send(msg.author.mention + " left the game. Your progress was not saved.")
                        break

                while round == 3:
                    await ctx.send(msg.author.mention + " **Do you want to**  ``Punch``, ``Defend`` or ``End``!")

                    def check(msg):
                        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["Punch","Defend","End"]

                    msg = await client.wait_for("message", check=check)
                    if msg.content == "Punch":
                        power = (random.randint(40, 80))
                        ap = random.randint(50, 70)
                        boss3 = boss3 - power if boss3 - power > 0 else 0
                        userhp = userhp - ap if userhp - ap > 0 else 0
                        await ctx.send(
                            "You dealt " + str(power) + " damage! Boss3 is now left with " + str(boss3) + "hp!")
                        if boss3 <= 0:
                            round += 1
                            await ctx.send(msg.author.mention + ' **You WON** :crown: \n\nBoss3 is dead! :skull: \n\n You will now move on to round 4!')
                            await ctx.send(msg.author.mention + "Welcome to round 3, WOW you've reallly made it this far huh? Well your next opponent is tough, and you're hp is increased to 135, Good Luck! \n\nName: Boss3 \nAttack: 50 - 70\nHP: 150")
                            break
                        await asyncio.sleep(2)
                        await ctx.send(f"Boss3 hit you for {ap}. You are now left with {userhp} hp")
                        if userhp < 0 or userhp == 0:
                            await ctx.send('**You LOST** :skull_crossbones: \n*Boss 2 WON* :crown:!')
                            break
                    elif msg.content == "Defend":
                        bruh = random.randint(5, 45)
                        userhp = int(userhp) + bruh
                        if userhp >= 125:
                            userhp = 125
                            await ctx.send("You're now at max shield limit! Your HP: " + str(userhp))
                        else:
                            await ctx.send(
                                'You increased by ' + str(bruh) + (" hp! Now you're at " + str(userhp) + '!'))

                        await asyncio.sleep(2)
                        if boss3 <= 90:
                            bruh = random.randint(30, 60)
                            boss3 = int(boss3) + bruh
                            await ctx.send(
                                "Boss3 healed by " + str(bruh) + " hp! He is now at " + str(boss3 + bruh) + "!")
                        else:
                            ap = random.randint(50, 70)
                            await ctx.send(f"Boss3 hit you for {ap}. You are now left with {userhp - ap} hp")


                    elif msg.content == "End":
                        await ctx.send(msg.author.mention + " left the game. Your progress was not saved.")
                        break

                while round == 4:
                    await ctx.send(msg.author.mention + " **Do you want to**  ``Punch``, ``Defend`` or ``End``!")

                    def check(msg):
                        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["Punch","Defend", "End"]

                    msg = await client.wait_for("message", check=check)
                    if msg.content == "Punch":
                        power = (random.randint(40, 65))
                        ap = random.randint(60, 80)
                        boss4 = boss4 - power if boss4 - power > 0 else 0
                        userhp = userhp - ap if userhp - ap > 0 else 0
                        await ctx.send("You dealt " + str(power) + " damage! Boss4 is now left with " + str(boss4) + "hp!")
                        if boss4 <= 0:
                            round += 1
                            await ctx.send(msg.author.mention + ' **You WON** :crown: \n\nBoss4 is dead! :skull: \n\n You will now move on to the final round!')
                            userhp = 135
                            await ctx.send(ctx.author.mention + " Okay, wow! This is really impressive! However I think this will be the last round for you... Your hp is maxed out now, at 135 hp, and your next opponent is very notorious!\n\nName:Boss4\nAttack: 50 - 70\nHP: 175")
                            break
                        await asyncio.sleep(2)
                        await ctx.send(f"Boss4 hit you for {ap}. You are now left with {userhp - int(ap)} hp")
                        if userhp < 0 or userhp == 0:
                            await ctx.send('**You LOST** :skull_crossbones: \n*Boss 2 WON* :crown:!')
                            break
                    elif msg.content == "Defend":
                        bruh = random.randint(5, 45)
                        userhp = int(userhp) + bruh
                        if userhp >= 125:
                            userhp = 125
                            await ctx.send("You're now at max shield limit! Your HP: " + str(userhp))
                        else:
                            await ctx.send('You increased by ' + str(bruh) + (" hp! Now you're at " + str(userhp) + '!'))

                        await asyncio.sleep(2)
                        if boss4 <= 90:
                            bruh = random.randint(40, 70)
                            boss4 = int(boss4) + bruh
                            await ctx.send("Boss4 healed by " + str(bruh) + " hp! He is now at " + str(boss4 + bruh) + "!")
                        else:
                            ap = random.randint(50, 70)
                            await ctx.send(f"Boss4 hit you for {ap}. You are now left with {userhp - ap} hp")


                    elif msg.content == "End":
                        await ctx.send(msg.author.mention + " left the game. Your progress was not saved.")
                        break

                while round == 5:
                        await ctx.send(msg.author.mention + " **Do you want to**  ``Punch``, ``Defend`` or ``End``!")

                        def check(msg):
                            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["Punch","Defend","End"]

                        msg = await client.wait_for("message", check=check)
                        if msg.content == "Punch":
                            power = (random.randint(40, 65))
                            ap = random.randint(70, 90)
                            boss5 = boss5 - power if boss5 - power > 0 else 0
                            userhp = userhp - ap if userhp - ap > 0 else 0
                            await ctx.send("You dealt " + str(power) + " damage! Boss5 is now left with " + str(boss5) + "hp!")
                            if boss5 <= 0:
                                await ctx.send(msg.author.mention + ' **You WON** :crown: \n\nBoss5 is dead! :skull: \n\n :partying_face: YOU HAVE COMPLETED THE GAME! FANTASTIC JOB! :partying_face:')
                                break
                            await asyncio.sleep(2)
                            await ctx.send(f"Boss5 hit you for {ap}. You are now left with {userhp} hp")
                            if userhp <= 0:
                                await ctx.send('**You LOST** :skull_crossbones: \n*Boss 2 WON* :crown:!')
                                break
                        elif msg.content == "Defend":
                            bruh = random.randint(5, 45)
                            userhp = int(userhp) + bruh
                            if userhp >= 125:
                                userhp = 125
                                await ctx.send("You're now at max shield limit! Your HP: " + str(userhp))
                            else:
                                await ctx.send(
                                    'You increased by ' + str(bruh) + (" hp! Now you're at " + str(userhp) + '!'))

                            await asyncio.sleep(2)
                            if boss5 <= 90:
                                bruh = random.randint(60, 80)
                                boss5 = int(boss5) + bruh
                                await ctx.send("Boss5 healed by " + str(bruh) + " hp! He is now at " + str(boss5 + bruh) + "!")
                            else:
                                ap = random.randint(60, 80)
                                await ctx.send(f"Boss5 hit you for {ap}. You are now left with {userhp - ap} hp")


                        elif msg.content == "End":
                            await ctx.send(msg.author.mention + " left the game. Your progress was not saved.")
                            break

                if userhp == 0:
                    await ctx.send('Sorry! You lost, good try though, you can start the game again using the same `v.galaxo` command! Thanks for playing!')
                    break
                else:
                    break

client.run('Nzc0NDY3MTI3NjYyODcwNTQw.X6YMuA.ME3-zCbi2EgiwyLCzw8POyg5F00')



