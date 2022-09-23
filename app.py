import discord
import random
import os
from sentiment_analysis import sentiment_analysis
from dotenv import load_dotenv
load_dotenv()
bot = discord.Client()

token = os.getenv('DISCORD_CLIENT_TOKEN')

# Add your positive, negative and neutral responses in the lists:
responses_pos = []
responses_neg = []
responses_neu = []

@bot.event
async def on_ready():
    guild_count = 0
    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")
        # INCREMENTS THE GUILD COUNTER
        guild_count = guild_count + 1
        # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(msg):
    message = msg.content
    if(msg.author.bot == False): 
        #Use isGreeting from sentiment_analysis.py
        if(message in ['yo', 'hi', 'hello', 'greetings', 'hey', 'sup', 'whatsup', 'whatsup', 'heyy', 'heyyy', 'heyyyy', 'heyyyyy']):
            await msg.reply("um hi")
        else:  
            if(sentiment_analysis(message) == 'NEUTRAL'):
                await msg.reply(responses_neu[random.randint(0, len(responses_neu)-1)])
            if(sentiment_analysis(message) == 'POSITIVE'):
                await msg.reply(responses_pos[random.randint(0, len(responses_pos)-1)])
            if(sentiment_analysis(message) == 'NEGATIVE'):
                await msg.reply(responses_neg[random.randint(0, len(responses_neg)-1)])

# bot.run(os.environ.get('CLIENT_TOKEN'))
bot.run(token)
