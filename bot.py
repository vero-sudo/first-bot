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

# Command: Create a ticket and post it to the "public-general" channel
@client.command()
async def ticket(ctx, *, issue: str):
    # Check if the user has the proper permissions (optional)
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("You don't have permission to create a ticket.")
        return
    
    # Find the channel where the ticket will be posted
    channel = discord.utils.get(ctx.guild.text_channels, name='public-general')
    if not channel:
        await ctx.send("The 'public-general' channel was not found.")
        return

    # Create the ticket message format
    ticket_message = f"**New Ticket Created by {ctx.author.name}**\n\nIssue: {issue}"

    # Post the ticket to the channel
    await channel.send(ticket_message)

    # Acknowledge that the ticket has been created
    await ctx.send(f"Ticket created successfully in {channel.mention}.")

# Run the bot with your token
client.run('YOUR_DISCORD_TOKEN')
