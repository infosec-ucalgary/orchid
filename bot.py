import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


_ = load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=";", intents=intents)


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


@bot.command(name="rules")
async def rules(ctx: commands.Context):
    channel = ctx.message.channel
    if (not isinstance(channel, discord.DMChannel)) and channel.name == "rules":
        try:
            if ctx.author.guild_permissions.administrator:
                title = ""
                response = (
                    "**This server is the only official University of Calgary Cyber Security Discord server. The following rules are in place for everybody’s sake. Please follow them if you wish to stay.**\n\n"
                    "**Behaviour**\n"
                    "- Be respectful: No harassment, intimidation, or making people feel uncomfortable, unwelcome, or afraid.\n\n"
                    "**Ethical Conduct**\n"
                    "- Use your powers for good: Be ethical. No sharing malicious software, links, or harmful content.\n\n"
                    "**Positive Community**\n"
                    "- Be awesome and excellent: Help each other, be welcoming, and always start by assuming the best intentions in others.\n\n"
                    "If you feel someone has boken these rules or you are being targeted, please message one of the <@&658585773007699980>. "
                    "People who break the rules get one warning as a chance to improve, and any other issues will result in removal.\n\n"
                    "**If you didn't get a role after doing the Rules Screening, message one of the <@&658585773007699980> to get the <@&722641525854699570> role.**"
                )
                embed = discord.Embed(title=title, description=response, color=0xF42535)
                _ = embed.set_author(
                    name="University of Calgary Cyber Security Club",
                    icon_url="https://cdn.discordapp.com/attachments/623226375142244363/1285799788456972298/logo.png?ex=66eb95de&is=66ea445e&hm=df2475d8dc73d6650b23bb225d79cc3e870470d77a427148c5f16ce0bc0700d2&",
                )
                _ = await ctx.send(embed=embed)
        except Exception as e:
            _ = await ctx.send(
                f"There was an error using this command. Make sure you are using it in an appropriate server: {e}"
            )


def main() -> None:
    if not TOKEN:
        print("TOKEN doesnt exist??? Check .env file.")
        return
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
