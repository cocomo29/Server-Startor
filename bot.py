from discord.ext import commands

client = commands.Bot(command_prefix = "!")

Rules = """
`1` enter your Rules in line 6 of the code
"""

Links = """
Auttaja: https://auttaja.io/
Carl: https://carl.gg/
Dank Memer: https://dankmemer.lol/ :star:
Dyno: https://dyno.gg/ :star:
Giveaway: https://giveawaybot.party/
Hydra: https://hydra.bot/
Koya: https://koya.gg/ :star:
Moosic: https://moosic.co/
Mee6: https://mee6.xyz/ :star:
OwO: https://top.gg/bot/408785106942164992 :star:
Tatsumaki: https://tatsu.gg/
Vortex: https://jagrosh.com/vortex :star:
"""

@client.event
async def on_ready():
    print('Im alive lesgooooooooo!')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        id = [server.id for server in client.guilds][0]
        memberCount = [server.member_count for server in client.guilds][0]
        server = client.get_guild(id)
        [await vc.delete() for server in client.guilds for vc in server.voice_channels]
        [await channels.delete() for server in client.guilds for channels in server.text_channels]
        [await cat.delete() for server in client.guilds for cat in server.categories]
        await server.create_voice_channel(f"Member Count : {memberCount}",perm = False)
        
        info = await server.create_category('Info')
        welcome = await server.create_text_channel('welcome',category = info)
        about = await server.create_text_channel('about',category = info)
        rules = await server.create_text_channel('rules',category = info)
        announcements = await server.create_text_channel('announcements',category = info)
        roles = await server.create_text_channel('roles',category = info)

        await client.get_channel(welcome.id).send(Links)
        await client.get_channel(rules.id).send("https://media.discordapp.net/attachments/714093644029886545/718392916858634250/rules-1.gif")
        await client.get_channel(rules.id).send(Rules)

        general = ["general chat", "media", "bot commands","bot commands 2", "spam"]
        media = ["media", "selfies", "pets", "art", "wholesome", "photography", "self promotion"]
        Server = ["help", "suggestions", "complaints","boosters", "ranks" ]
        vc = ["general vc", "general vc 2", "gaming", "waiting lounge", "hangout", "staff chat", "afk"]
        musicVc = ["music vc", "music vc 2", "private music", "private music 2"]
        staff = ["logs", "staff chat", "archieve"]
        

        cat1 = await server.create_category("General")
        [await server.create_text_channel(channel, category = cat1) for channel in general]
        cat2 = await server.create_category("Media")
        [await server.create_text_channel(channel, category = cat2) for channel in media]
        cat3 = await server.create_category("Server")
        [await server.create_text_channel(channel, category = cat3) for channel in Server]
        cat4 = await server.create_category("VC")
        [await server.create_voice_channel(channel, category = cat4) for channel in vc]
        cat5 = await server.create_category("Music")
        [await server.create_voice_channel(channel, category = cat5) for channel in musicVc]
        cat6 = await server.create_category("Staff")
        [await server.create_text_channel(channel, category = cat6) for channel in staff]

client.run('paste your token here')
