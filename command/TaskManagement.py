import datetime
import discord
from discord.ext import commands, tasks
import command.db
from command.db import *
from command.model.Task import Task
from datetime import datetime, timedelta


async def check_tasks(channel,bot):
    now = datetime.now()
    now_time = now.strftime("%H:%M") 
    
    days_of_week = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
        "Friday": 4, "Saturday": 5, "Sunday": 6
    }

    print(f"🕒 Current time: {now_time}, Weekday: {now.weekday()}")  # Debug
    tasksList = command.db.get_tasks()
    for task in tasksList:
        userid = task["userid"]
        task_name = task["name"]
        task_description = task["description"]
        task_time = task["time"]  
        task_status = task["status"]
        task_dotw = task["dotw"] 
        dotw = days_of_week[task_dotw]
        if now.weekday() == dotw and now_time == task_time and task_status == "False":
            await send_noti(channel,userid,task_name,task_description,bot)
        else:
            print("❌ Task is not due.")

async def send_noti(channel, userid, task_name, task_description, bot):
    user = await bot.fetch_user(userid)
    embed = discord.Embed(
        title="Your task is due!",
        description=f"<@!{user.id}>\n```{task_name} - {task_description}```",
        colour=0xd4add7,
        timestamp=datetime.now()
    )
    embed.set_author(name=user.name)
    embed.set_thumbnail(url=user.avatar)
    embed.set_footer(icon_url="https://i.imgur.com/fumd8iG.jpeg")

    await channel.send(embed=embed, allowed_mentions=discord.AllowedMentions(users=True))


