// bot.js
const { Client, GatewayIntentBits } = require('discord.js');
require('dotenv').config();  // To load the token from .env

// Create a new client instance
const client = new Client({ 
    intents: [
        GatewayIntentBits.Guilds, 
        GatewayIntentBits.GuildMessages, 
        GatewayIntentBits.MessageContent 
    ] 
});

// When the bot is ready
client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

// Listen for messages and respond
client.on('messageCreate', (message) => {
    if (message.content === '!hello') {
        message.channel.send(`Hello, ${message.author.username}!`);
    }
});

// Log in to Discord with the token from the environment
client.login(process.env.DISCORD_TOKEN);
