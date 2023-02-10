import discord
import random
import time
import os
from discord.ext import tasks, commands

from bot import util

config = util.discord_config

class AdminCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.check(util.is_owner)
    @commands.group(name='admin')
    async def admin(self, ctx):
        if ctx.invoked_subcommand is None:
            await util.send_embed(ctx, util.standard_embed(ctx, f'Use \"admin reload\" to reload the site.'))
    
    @commands.check(util.is_owner)
    @admin.group(name='reload')
    async def place_start(self, ctx):
        os.system('git pull')
        os.system('rm -rf site/public')
        os.system('cd site && hugo')
        await util.send_embed(ctx, util.success_embed(ctx, f'Reloaded Site.'))


async def setup(bot: commands.Bot):
    await bot.add_cog(AdminCog(bot))