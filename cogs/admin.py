import discord
from discord.ext import commands
from cogs import checks


class Admin:
    """Administrator only Bot Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.admin_or_permissions()
    async def delete(self, ctx):
        """ Deletes up to 500 messages in current channel"""

        await self.bot.purge_from(ctx.message.channel, limit=500, check=None)

    @commands.command(no_pm=True)
    @checks.mod_or_permissions(kick_members=True)
    async def kick(self, member: discord.Member):
        """ Kicks a person from the server """

        try:
            await self.bot.kick(member)
            await self.bot.say('{} has been kicked from the server. *Beep Boop Goodbye*'.format(member))

        except discord.Forbidden:
            await self.bot.say('You do not have permission to use this command')

        except discord.HTTPException:
            await self.bot.say('Could not kick user')

    @commands.command(no_pm=True)
    @checks.admin_or_permissions(ban_members=True)
    async def ban(self, member: discord.Member):
        """ Bans the user from the server"""

        try:
            await self.bot.ban(member)
            await self.bot.say('{} has been banned'.format(member))

        except discord.Forbidden:
            await self.bot.say('You do not have permission to use this command')

        except discord.HTTPException:
            await self.bot.say("Could not ban user")


def setup(bot):
    bot.add_cog(Admin(bot))
