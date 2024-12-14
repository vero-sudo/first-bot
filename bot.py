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

    # Command: !datarequest [username] [data change type] [optional extra info]
    if message.content.startswith('!datarequest'):
        # Split the command into arguments
        args = message.content.split(' ', 3)  # Split into 4 parts max

        # Ensure the command has the required arguments
        if len(args) < 3:
            await message.channel.send("Please provide the Discord username, data change type, and optional extra info.")
            return

        # Extract the arguments
        discord_username = args[1]
        data_change_type = args[2]
        extra_info = args[3] if len(args) > 3 else "No extra info provided"  # Default message if no extra info

        # Create the ticket message
        ticket_message = (
            f"**Ticket Request:**\n"
            f"**Username:** {discord_username}\n"
            f"**Data Change Type:** {data_change_type}\n"
            f"**Extra Info:** {extra_info}"
        )

        # Get the channel where the ticket will be posted (replace 'public-general' with your desired channel name)
        channel = discord.utils.get(message.guild.text_channels, name="public-general")
        if channel:
            await channel.send(ticket_message)
            await message.channel.send(f"Ticket created for {discord_username} in {channel.mention}.")
        else:
            await message.channel.send("Could not find the 'public-general' channel.")

# Run the bot with the token
client.run(TOKEN)
