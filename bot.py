import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

_ = load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = 912856141862678530

intents = discord.Intents.default()
intents.guilds = True


bot = commands.Bot(command_prefix=";", intents=intents)

@bot.event
async def on_ready() -> None:
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)
    print(f"We have logged in as {bot.user} and synced commands!")


@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    if before.pending and not after.pending:
        guild = bot.get_guild(before.guild.id)
        if not guild:
            print("Member isn't in a server??")
            return

        member = guild.get_member(before.id)
        if not member:
            print("Member doesn't exist??")
            return

        role = discord.utils.get(before.guild.roles, name="Member")
        if not role:
            print("Member role doesn't exist??")
            return

        await member.add_roles(role)


@bot.tree.command(name="ping", description="Get the bot's latency.")
async def ping(inter: discord.Interaction) -> None:
    await inter.response.send_message(f"Pong! ({round(bot.latency * 1000)}ms)")


@bot.tree.command(name="rules", description="Embed rules.")
async def rules(inter: discord.Interaction):
    if not inter.user.guild_permissions.administrator:
        await inter.response.send_message("Only administrators can use this command.",ephemeral=True)
        return
    
    channel = inter.channel
    if channel and channel.name != "rules":
        await inter.response.send_messages("This command can only be used in #rules.", ephemeral=True)
        return
    
    response = (
        ":warning: **This server is the only official University of Calgary Cyber Security Discord server. "
        "The following rules are in place for everybody’s sake. Please follow them if you wish to stay.**\n\n"
        "**Behaviour**\n"
        "- Be respectful: No harassment, intimidation, or making people feel uncomfortable.\n\n"
        "**Ethical Conduct**\n"
        "- Be ethical. No sharing malicious software or harmful content.\n\n"
        "**Positive Community**\n"
        "- Help each other and assume good intentions.\n\n"
        "If someone breaks the rules contact <@&658585773007699980>."
    )

    embed = discord.Embed(description=response, color=0xF42535)

    embed.set_author(
        name="University of Calgary Cyber Security Club",
        icon_url="https://cdn.discordapp.com/attachments/623226375142244363/1285799788456972298/logo.png"
    )

    await inter.response.send_message(embed=embed)


def main() -> None:
    if not TOKEN:
        print("TOKEN doesnt exist??? Check .env file.")
        return
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
