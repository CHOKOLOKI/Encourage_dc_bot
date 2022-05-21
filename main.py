import discord
import os
import random
import requests
import json
import pytz
import datetime as dt
from keep_alive import keep_alive

#Variables section
client = discord.Client()

now = dt.datetime.now()

Manila =pytz.timezone('Asia/Manila')

localtz=pytz.timezone('Europe/London')

now=localtz.localize(now)

now_today=now.astimezone(Manila)
print(now_today)

petsa = now_today.strftime('%m/%d/%Y')

oras = now_today.strftime("%H:%M:%S" + ' (+01:00:00)')

#These are all the listed words
happy_words = ["lipaya", "happy", "Happy", "Lipay", "Lipaya", "lipay", "smiling", "smiley","Smiling", "Smiley", "I feel better"]

starter_supports = ["good for you", "That is good to hear", "keep it up", "Sana all", "Sanaol"]

sad_words = ["maoy", "Maoy", "buwagan", "Buwagan", "hilak", "Hilak", "hilaka", "Hilaka","depressed", "Depressed", "Sad", "sad", "guol", "Guola", "guola", "Guol"]

starter_encourage = ["Hang in there!", "Everything will be alright", "Don't worry I'm here for you", "You're a great person", "Cheer up!", "Ma okay ra tanan basta salig lang sa imo kaugalingon"]

morning_greet = ["Good morning", "ohayo", "Ohayo","good morning", "Maayong Buntag", "maayong buntag", "Magandang Umaga", "magandang umaga", "goodmorning", "Goodmorning"]

morning_message = ["Good morning", "Ohayo Gozaimasu", "Hello! Good morning", "Good morning how was your sleep?", "Good Morning. Did you sleep well?"]

haler_greets = ["hi bot", "Hi bot", "hi Bot", "Hi Bot", "Hi ging", "hi ging", "Hi Ging", "Hi ging", "Hi gingski", "Hi Gingski", "Hi Gingskiki", "hi ginsgski", "hi gingskiki", "Hi guys", "hi guys"]

orayt = ["Hi guyd", "Haluu", "Hiii", "Haluu guyd",]

Good_night = ["Good night", "matog nako", "tug nako", "Matog nako", "Tug nako", "Goodnight", "good night", "Goodnight", "Oyasumi", "Oyasuminasai", "Goodnight", "goodnight"]

Sleep = ["Good Night! Sleep Well", "Good Night! Sweet Dreams", "Good Night!", "Good Night! Sleep Tight"]

Tired_words = ["Kapoy", "Kapoya", "Kapoy nako", "kapoy", "kapoya", "kapoy nako", "Gikapoy" , "gikapoy", "Gikapoy nako", "gikapoy nako", "I'm tired", "Tired", "exhausted", "tired", "exhausting", "too much work", "grabe nga trabaho", "grabe na trabaho"]

Tired = ["Please rest Master!", "You did well today! Please take a rest", "Thank you for your hardwork! Please Rest", "Take a break and enjoy life", "You will get good things from your hardwork, so please rest"]

amen = ["Uli na ging", "uli na ging", "We miss you ging", "we miss you ging", "I miss you ging", "i miss you ging"]

nema = ["I miss you too", "Gimingaw nasab ko ninyo", "Kita raman gihapon ta puhon"]

Cant_sleep = ["I cannot sleep", "cant sleep", "i cannot sleep", "Cant sleep", "di ko katog", "diko katog"]

Sleep_now = ["Please go to bed and Relax", "Sleep early to get more ideas tomorrow", "Please go to bed and clear your mind", "If you won't sleep. you will have a bad memory"]

gabii = ["maayong gabii", "Maayong gabii", "Mayng gabii", "mayng gabii", "Good evening","good evening", "Goodevening", "goodevening","Konbanwa"]

tubag_sa_gabii = ["Good evening!", "What a pleasant night it is.", "Hello Good evening"]

Ver = ['ver briz', 'briz', 'Ver', 'Ver Briz', 'Ver briz', 'ver briz barontoy', 'ver briz b barontoy', 'ver briz b. barontoy']

Briz = ["Ahh Ver Briz, That's the girl Gio loves", "Ver Briz? That's Gio's lover Right?"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}: {user_message} ({channel})')

  if message.channel.name == 'general':
    if user_message.lower() == 'hi':
      await message.channel.send(f'Hello {username}! It is nice to see you')
      return

#What to say to the bot or ask
    if user_message.lower() == 'what day is it?':
      await message.channel.send(f'today is {petsa} do not forget the date {username}!')

    if user_message.lower() == 'what time is it?':
      await message.channel.send(f'it is {oras} right now {username}!')
  
    if user_message.lower() =='bye':
      await message.channel.send(f"Bye! {username}! See ya!")
      return
    
    elif user_message.lower() == 'goodbye':
      await message.channel.send(f'Bye! {username}! See ya!')

    if user_message.lower() == 'i love you zero two':
      await message.channel.send(f'I love you too {username}!')

    if user_message.lower() == 'i miss you zero two':
      await message.channel.send(f'Oh how sweet! I missed you too {username}')

    if user_message.lower() == 'i miss you':
      await message.channel.send(f'I missed you too {username}!')

    if user_message.lower() == 'kamusta naman si gio?':
      await message.channel.send(f'Okay raman, malipayon gihapon')

    if user_message.lower() == 'hey zero two':
      await message.channel.send(f'Oh Hello there {username}!')
    
    if user_message.lower() == 'i love you':
      await message.channel.send(f'I love you too {username} <3')

    if user_message.lower() == 'unsa ni ging?':
      await message.channel.send(f'I am the bot created by Gio Daguil. Nice to meet you!')

    if user_message.lower() == 'who are you?':
      await message.channel.send(f'I am the bot created by Gio Daguil. Nice to meet you!')

    if user_message.lower() =='will you encourage me?':
      await message.channel.send(f'Sure!, Just type "!encourage"')

    if user_message.lower() == 'wow':
      await message.channel.send(f'Right? It is amazing!')

    if user_message.lower() == 'choya':
      await message.channel.send(f'Right? It is amazing')

    if user_message.lower() == 'chuya':
      await message.channel.send(f'Right? It is amazing')

    if user_message.lower() == 'where is gio right now?':
      await message.channel.send(f'gio is on P. Remedio st. Banilad, Mandaue, Cebu city')

    if user_message.lower() == 'Where did gio work?':
      await message.channel.send(f'Gio is currently working on BPOSeats as QA Tester on Devs Department')

    if user_message.lower() == 'who made you?':
      await message.channel.send(f'I am created by Sergio M. Daguil III')

    if user_message.lower() == 'who is your creator?':
      await message.channel.send(f'My creator is the one and only Sergio Mendola Daguil III')

    if user_message.lower() == 'who is ugly here?':
      await message.channel.send(f'No other than {username}. It is obvious')

    if user_message.lower() == 'kinsay maot diri?':
      await message.channel.send(f'No other than {username}. It is obvious')

    if user_message.lower() == 'how are you?':
      await message.channel.send(f'I am fine. Thank you!')

    if user_message.lower() == 'zero two':
      await message.channel.send(f'yes? what do you need from me?')

    if user_message.lower() == 'am i right zero two?':
      await message.channel.send(f'Yes! You are right')

    if user_message.lower() == "who is gio's girlfriend?":
      await message.channel.send(f'His girlfriend is Ver Briz Barontoy')

    if user_message.lower() == 'im cute':
      await message.channel.send(f'Me too i am also cute!')

    if user_message.lower() == 'im pretty':
      await message.channel.send(f'I am pretty too!')

    if user_message.lower() == 'what can you do?':
      await message.channel.send(f'I can answer all your stupid questions {username}!')

    if user_message.lower() == 'nice one zero two':
      await message.channel.send(f'Thank you!')

    if user_message.lower() == 'im hungry':
      await message.channel.send(f'I will lend you some snacks.')

    if user_message.lower() == 'evening zero two':
      await message.channel.send(f'Good evening {username}, How was your day?, Are you tired?')

  msg = message.content

  if msg.startswith('!encourage'):
    quote = get_quote()
    await message.channel.send(quote)

#This where I put the listed word for the bot to reply word to  search every word by word it sees.  
  if any(word in msg for word in happy_words):
    await message.channel.send(random.choice(starter_supports))

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encourage))

  if any(word in msg for word in morning_greet):
    await message.channel.send(random.choice(morning_message))

  if any(word in msg for word in haler_greets):
    await message.channel.send(random.choice(orayt))
  
  if any(word in msg for word in Good_night):
    await message.channel.send(random.choice(Sleep))

  if any(word in msg for word in Tired_words):
    await message.channel.send(random.choice(Tired))

  if any(word in msg for word in amen):
    await message.channel.send(random.choice(nema))

  if any(word in msg for word in Cant_sleep):
    await message.channel.send(random.choice(Sleep_now))

  if any(word in msg for word in gabii):
    await message.channel.send(random.choice(tubag_sa_gabii))
  
  if any(word in msg for word in Ver):
    await message.channel.send(random.choice(Briz))

#This keep alive something is what makes this bot work for a long time  
keep_alive()
client.run(os.environ['pray'])