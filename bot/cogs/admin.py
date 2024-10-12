import discord
import random
import docker
import time
import os
from discord.ext import tasks, commands

import util

docker_client = docker.from_env()

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
    async def reload(self, ctx):
        docker_client.containers.get('website-hugo-blog-1').exec_run('hugo --minify')
        await util.send_embed(ctx, util.success_embed(ctx, f'Reloaded Site.'))


async def setup(bot: commands.Bot):
    await bot.add_cog(AdminCog(bot))