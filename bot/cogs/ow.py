from discord.ext import commands
from sqlalchemy.orm import sessionmaker
from models import Battletags, db_connect, create_battletag_table
from utils import get_average_stats, get_most_stats, \
                      most_played, get_average_comp, get_most_comp, \
                      get_hook, get_dva


ERROR = "Could not retrieve stats. Battletag is Case Sensitive\n" \
        "Use !cb 'your_battletag' command to fix your Battletag"


engine = db_connect()
create_battletag_table(engine)
Session = sessionmaker(bind=engine)
session = Session()


class OverWatch:
    """Overwatch related stat commands"""

    def __init__(self, bot):
        """ Initialize the bot"""
        self.bot = bot

    async def parse_gen(self, generator):
        """Parses the generator function to allow the bot
            to display the data in the channel """
        try:
            for descr, stat in generator:
                await self.bot.say(descr + '  |  ' + stat)
                # If results are empty raise error
                if not descr:
                    raise Exception
        except Exception:
            await self.bot.say(ERROR)

    @commands.command(pass_context=True)
    async def b(self, ctx, battletag):
        """Enters a new user battletag into db """
        raw_user = ctx.message.author
        bt = str(battletag)
        user = str(raw_user)

        # Search db to see if battletag already exists
        record = session.query(Battletags).filter_by(disc_name=user).first()

        if record is None:
            # If no record exists create a database entry
            record = Battletags(
                disc_name=user,
                battletag=bt
            )
            # Save record to database
            session.add(record)
            session.commit()

            await self.bot.say("Battletag Added")

        else:
            await self.bot.say("Your Battletag is already logged")

    @commands.command(pass_context=True)
    async def cb(self, ctx, battletag):
        """ Changes an existing db record's battletag """
        raw_user = ctx.message.author
        bt = str(battletag)
        user = str(raw_user)

        # Search db to see if battletag already exists
        record = session.query(Battletags).filter_by(disc_name=user).first()

        if record:
            record.battletag = bt
            await self.bot.say("Battletag succesfully updated")

    @commands.command(pass_context=True)
    async def average(self, ctx):
        """ Retrieves Average Overwatch Stats """
        raw_user = ctx.message.author
        user = str(raw_user)
        try:
            record = session.query(Battletags).filter_by(disc_name=user).first()

            if record:
                battletag = record.battletag

                await self.bot.say(battletag + '\n' + '---------------')
                await self.parse_gen(get_average_stats(battletag))

            else:
                raise Exception

        except Exception:
            await self.bot.say("Error: Battletag is not registered\n"
                               "Use !b 'your_battletag' command to log it")

    @commands.command(pass_context=True)
    async def averagecom(self, ctx):
        """ Retrieves Average Competitive Overwatch Stats """
        raw_user = ctx.message.author
        user = str(raw_user)
        try:
            record = session.query(Battletags).filter_by(disc_name=user).first()

            if record:
                battletag = record.battletag

                await self.bot.say(battletag + '\n' + '---------------')
                await self.parse_gen(get_average_comp(battletag))

            else:
                raise Exception

        except Exception:
            await self.bot.say("Error: Battletag is not registered\n"
                               "Use !b 'your_battletag' command to log it")

    @commands.command(pass_context=True)
    async def most(self, ctx):
        """Retrieves Most In Game/Best Overwatch Stats"""
        raw_user = ctx.message.author
        user = str(raw_user)
        try:
            record = session.query(Battletags).filter_by(disc_name=user).first()

            if record:
                battletag = record.battletag

                await self.bot.say(battletag + '\n' + '---------------')
                await self.parse_gen(get_most_stats(battletag))

            else:
                raise Exception

        except Exception:
            await self.bot.say("Error: Battletag is not registered\n"
                               "Use !b 'your_battletag' command to log it")

    @commands.command(pass_context=True)
    async def mostcom(self, ctx):
        """Retrieves Most In Game/Best Competitive Overwatch Stats"""
        raw_user = ctx.message.author
        user = str(raw_user)
        try:
            record = session.query(Battletags).filter_by(disc_name=user).first()

            if record:
                battletag = record.battletag

                await self.bot.say(battletag + '\n' + '---------------')
                await self.parse_gen(get_most_comp(battletag))

            else:
                raise Exception

        except Exception:
            await self.bot.say("Error: Battletag is not registered\n"
                               "Use !b 'your_battletag' command to log it")

    @commands.command(pass_context=True)
    async def play(self, ctx):
        """ Retrieves Heroes Most Played Stats """
        raw_user = ctx.message.author
        user = str(raw_user)
        try:
            record = session.query(Battletags).filter_by(disc_name=user).first()

            if record:
                battletag = record.battletag

                await self.bot.say(battletag + '\n' + '---------------')
                await self.parse_gen(most_played(battletag))

            else:
                raise Exception

        except Exception:
            await self.bot.say("Error: Battletag is not registered\n"
                               "Use !b 'your_battletag' command to log it")

    @commands.command(pass_context=True)
    async def hooks(self, ctx):
        """ Retrieves Those Mad Hook Stats """
        raw_user = ctx.message.author
        user = str(raw_user)
        try:
            record = session.query(Battletags).filter_by(disc_name=user).first()

            if record:
                battletag = record.battletag

                await self.bot.say(battletag + '\n' + '---------------')
                await self.parse_gen(get_hook(battletag))

            else:
                raise Exception

        except Exception:
            await self.bot.say("Error: Battletag is not registered\n"
                               "Use !b 'your_battletag' command to log it")

    @commands.command(pass_context=True)
    async def dva(self, ctx):
        """Retrieves Dva Self-Destructs """
        raw_user = ctx.message.author
        user = str(raw_user)
        try:
            record = session.query(Battletags).filter_by(disc_name=user).first()

            if record:
                battletag = record.battletag

                await self.bot.say(battletag + '\n' + '---------------')
                await self.parse_gen(get_dva(battletag))

            else:
                raise Exception

        except Exception:
            await self.bot.say("Error: Battletag is not registered\n"
                               "Use !b 'your_battletag' command to log it")


def setup(bot):
    bot.add_cog(OverWatch(bot))
