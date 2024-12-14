import os
import discord
from dotenv import load_dotenv

# Load environment variables from the .env file (if you're running locally)
load_dotenv()

# Fetch the token from environment variables (GitHub Secrets for deployment)
TOKEN = os.getenv("DISCORD_TOKEN")

# Check if the token is properly loaded
if not TOKEN:
    raise ValueError("No DISCORD_TOKEN found in environment variables")

# Create a client instance for the bot
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.members = True  # Enable member intent if needed

client = discord.Client(intents=intents)


# Event: Bot has connected to the server
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event: Respond to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Don't let the bot reply to itself

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello, {message.author.name}!')

# Run the bot with the token
client.run(TOKEN)
