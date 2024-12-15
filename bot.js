// Import the required library
const { Client, GatewayIntentBits } = require('discord.js');

// Create a new client instance with intents
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

// When the bot is ready
client.once('ready', () => {
    console.log('Bot is online!');
});

// When a message is received
client.on('messageCreate', (message) => {
    if (message.content === '!hello') {
        message.reply('Hello!');
    }
});

// Log in using your bot's token (use an environment variable for security)
client.login(process.env.DISCORD_TOKEN);  // Ensure you have the DISCORD_TOKEN set in your .env file
