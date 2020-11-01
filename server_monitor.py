import discord
import asyncio
import psutil
from discord.ext import tasks
from datetime import datetime
from uptime import uptime


intents = discord.Intents.default()
client = discord.Client(intents=intents)

CHANNEL_ID = 12345678910 # Insert channel ID here
MESSAGE_ID = 10987654321 # Insert message ID here

def b2h(n):
    symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


@client.event
async def on_ready():
    print("Online!")

@tasks.loop(minutes=1)
async def useful():
        await client.wait_until_ready()
        message = await client.get_channel(CHANNEL_ID).fetch_message(MESSAGE_ID)
        while not client.is_closed():
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            net = psutil.net_io_counters()
            await asyncio.sleep(1)
            net2 = psutil.net_io_counters()
            if net.bytes_recv > net2.bytes_recv:
                current_in = 0
            else:
                 current_in = net2.bytes_recv - net.bytes_recv
            if net.bytes_sent > net2.bytes_sent:
                current_out = 0
            else:
                current_out = net2.bytes_sent - net.bytes_sent
            delta_uptime = uptime()
            hours, remainder = divmod(int(delta_uptime), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)
            newEmbed = discord.Embed(title='Server information.', colour=discord.Colour.green())
            newEmbed.add_field(name="CPU infomation", value=f"{cpu}/100%")
            newEmbed.add_field(name="RAM information", value=f"{b2h(ram.used)}/{b2h(ram.total)}. Percentage: {ram.percent}%")
            newEmbed.add_field(name="Network information", value=f"Bytes sent: {b2h(current_out)} Bytes recieved: {b2h(current_in)} \nBytes sent in total: {b2h(net.bytes_sent)}. Bytes recieved in total: {b2h(net.bytes_recv)}")
            newEmbed.set_footer(text=f"Server online for: {days}d, {hours}h, {minutes}m, and {seconds}s")
            await message.edit(embed = newEmbed)
            await asyncio.sleep(30)

useful.start()

client.run('token')
