from discord import Intents, Client

from discord.ext import commands,tasks
import Paginator
import command
import command.TaskManagement
import command.addTask
from command.getDailyTask import *
from command.addDailyTask import *
from command.addTask import *

from command.TaskManagement import *
import command.addDailyTask
import command.getDailyTask
from command.model.DailyTask import *



intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
prefix ='.' 
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('Himari to sensei: {:.2f} ms'.format(bot.latency *1000))

@bot.command()
async def addDailyTask(ctx, *, task_info: str):
    await command.addDailyTask.addDailyTask(ctx, task_info)
    


@bot.command()
async def getDailyTask(ctx):
    await command.getDailyTask.getDailyTask(ctx)

@bot.command()
async def addTask(ctx, *, task_info: str):
    await command.addTask.addTask(ctx, task_info)

# @bot.command()
# async def getTask(ctx):
#     await command.getDailyTask.getDailyTask(ctx)    
@bot.command()
async def setchannel(ctx):
    channel = ctx.channel
    await ctx.send(f"📢 Channel set to: `{channel}`")
@tasks.loop(seconds=60)
async def loop():
    channel = bot.get_channel(1239772586452189224)
    await command.TaskManagement.check_tasks(channel,bot)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    loop.start()  



@bot.command()
async def get_channel_id(ctx):
    await ctx.send(f"📢 Channel ID: `{ctx.channel.id}`")

token = ''

@bot.command()
async def pingme(ctx):
    delay = round(bot.latency * 5000)
    await ctx.send(f'📢 User '+ f'<@{ctx.author.id}>')

bot.run(token)