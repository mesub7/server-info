# server-info

Server info is a small bot designed to display information about your server stats (I mean an actual server/computer and not a discord server). I made this because I couldn't find anything that was prebuilt for me to just run.

![image](https://mesub.is-ne.at/x4P7nS.png)

## Requirements

You need:
0) Python 3.8 (if you have built the wheels for discord.py for 3.9 then you _should_ be able to use that).
1) [discord.py](https://pypi.org/project/discord.py/) version 1.5.1 or later.
2) [psutil](https://pypi.org/project/psutil/)
3) [uptime](https://pypi.org/project/uptime/)

## Setting up the bot

### Part one 

0) Ensure that you have created a [bot account.](https://discord.com/developers)
1) Open `monitor_setup.py` in your editor.
2) Replace the assigned value for `CHANNEL_ID`.
3) Add your bot token in `client.run('token')`.
4) Wait for the bot to print the message ID and copy it.

### Part two

0) Ensure that you have completed part one.
1) Open `server_monitor.py`
2) Replace the values assigned to `CHANNEL_ID` and `MESSAGE_ID` with the ones that the setup script produced.
3) Start your bot!

A pm2 file (`monitor-pm2.json`) is included to keep the bot online.

## Contributing

I would call myself a "basic intermediate" user of python so my code could probably be made better. Feel free to open a PR.

## Support

For any help, you can join my [small discord server](https://discord.gg/rDpcrNCRwV)
My discord is: mesub#0556
