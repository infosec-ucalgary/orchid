import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


_ = load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=";!", intents=intents)


@bot.event
async def on_ready() -> None:
    _ = await bot.tree.sync()
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


def main() -> None:
    if not TOKEN:
        print("TOKEN doesnt exist??? Check .env file.")
        return
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
