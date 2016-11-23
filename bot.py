import discord
from discord.ext import commands
import logging

from secret import token


description = '''A Discord Bot that provides Overwatch stats and basic functionality

                - To use commands type:  !b 'your_battletag'
                  ex: !b ItwasLuck#1682 '''

# These are the command cog extensions the bot will load
initial_extensions = [
    'cogs.ow',
    'cogs.admin'
]

# Initialize the bot
bot = commands.Bot(command_prefix='!', description=description)

# Load the cog extensions
for extension in initial_extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        print('Failed to load extension {}\n{}: {}'.format(extension,
                                                           type(e).__name__, e))


@bot.event
async def on_ready():
    """ Displays successful bot login in console"""
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_member_join(member):
    """ Notifies when new member has joined the server"""
    await bot.send_message(member.server, "{} joined {}".format(member,
                                                                member.joined_at))


@bot.command(pass_context=True)
async def invite(ctx):
    """ Creates an invite link for the server """
    try:
        link = await bot.create_invite(ctx.message.channel,
                                       max_age=300, max_uses=0)
        await bot.say(link)

    except discord.HTTPException:
        await bot.say("Failed to create invite")


@bot.command(pass_context=True)
async def hello(ctx):
    """ Greets the user """

    await bot.say("Hello, {}".format(ctx.message.author))


bot.run(token)
