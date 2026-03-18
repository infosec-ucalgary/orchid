
## Orchid UCalgary Cyber Security Club Discord Bot ##

A Discord bot for the University of Calgary Cyber Security Club that automatically assigns roles to new members and provides server rules.

# How It Works: 
The bot automatically assigns the "Member" role to users who complete Discord's membership screening.  It also includes : 
    - /ping command - to check latency
    - ;rules command (admin-only) - for posting formatted server rules in the #rules channel.

# How Deployment Works:
To run the bot, install dependencies (discord.py and python-dotenv), create a .env file with your bot token, and run python bot.py. The bot will stay online as long as the script is running.

# Creating and Setting Up the Token:
# Step 1: Create Discord Bot
    1. Go to the Discord Developer Portal (https://discord.com/developers/applications/)
    2. Click “New Application” if it doesn't exist.
        - Enter the bot name: "orchid" , and click create
        - Add a description and icon to personalize the bot
        - Save changes 
    3. Add a bot user
       - Go to the "Bot" tab (puzzle piece icon). Click "Add Bot" → "Yes, do it!"
    4. Retrieve the Token
       - Click "Reset Token" or "Copy" under the Token section and save it
        ⚠️ Never share this token publicly!

# Step 2: Add Orchid Bot to Server
    1. Navigate to OAuth2 → URL Generator
       - Select scopes:
            • bot
            • Applications.commands
       - Select bot permissions
            • Manage Roles
            • Send Messages
            • Embed Links
            • Read Message History
    2. Copy the generated URL
    3. Open the URL in a browser
    4. Select the desired server
    5. Complete the captcha.  The bot will be successfully added to the server

# Step 3: Running the Bot
    1. Install dependencies: pip install discord.py python-dotenv
    2. Create a .env file in the root directory and add : TOKEN=bot_token_here
    3. Run the bot: python bot.py 
    4. Upon successful completion, we get “ We have logged in as Orchid and synced commands!”
