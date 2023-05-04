
[Tutorial](https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-discord-connection)

- I had to install `dotenv` with `pip install python-dotenv`
- v1.5 has `Intents` which need to be specified. `discord.Intents.default()` worked if the bot was an administrator on the channel. Specify the intents in the `Client` constructor:
```    
intents = discord.Intents.default()
client = discord.Client(intents=intents)
```
- 