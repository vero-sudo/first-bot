import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from the .env file (if you're running locally)
load_dotenv()

# Fetch the token from environment variables (GitHub Secrets for deployment)
TOKEN = os.getenv("DISCORD_TOKEN")

# Check if the token is properly loaded
if not TOKEN:
    raise ValueError("No DISCORD_TOKEN found in environment variables")

# Create a bot instance using commands.Bot (slash commands require this)
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.members = True  # Enable member intent if needed

bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot has connected to the server
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Slash Command: /datarequest [target] [data_change_type] [modified_to]
@bot.tree.command(name="datarequest", description="Create a data request ticket")
async def datarequest(interaction: discord.Interaction, 
                      target: str, data_change_type: str, modified_to: str):  # Fixed parameter names

    # Create the embed message
    embed = discord.Embed(
        title="**Ticket Request**",
        description=f"A request for data modification has been created.",
        color=discord.Color.blue()  # Set the embed color
    )
    embed.add_field(name="**Username**", value=target, inline=False)
    embed.add_field(name="**Data Change Type**", value=data_change_type, inline=False)
    embed.add_field(name="**Modified To**", value=modified_to, inline=False)

    # Get the channel where the ticket will be posted (replace 'public-general' with your desired channel name)
    channel = discord.utils.get(interaction.guild.text_channels, name="public-general")
    if channel:
        await channel.send(embed=embed)
        await interaction.response.send_message(f"Ticket created for {target} in {channel.mention}.")
    else:
        await interaction.response.send_message("Could not find the 'public-general' channel.")

# Sync the commands with Discord
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot is ready and synced.")

# Run the bot with the token
bot.run(TOKEN)
