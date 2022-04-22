import discord
from discord.ext import commands
import datetime
from Settings import fetch_setting

intents = discord.Intents().default()
intents.members = True
intents.voice_states = True
intents.message_content = True

def prefix(bot, message):
    return fetch_setting(message.guild.id, 'prefix')

bot = commands.Bot(command_prefix=prefix, description="Robo Barista for The Gayming Café!", intents=intents, help_command=None, case_insensitive=True, strip_after_prefix=True)

bot_version = '0.4.1'

last_start_time = datetime.datetime.utcnow()

unverifiedRole = {
    811369107181666343 : 811453152061685760,
    866160840037236736 : 901649824963784705,
    622592295065354241 : 959675399393124402
}

verifyChannel = {
    811369107181666343 : 811492489230942259
}

bumpRole = {
    811369107181666343 : 830842531490431027,
    866160840037236736 : 921192640580558919
}

ageRoleList = { 
    811369107181666343 : [
        811443057018142740,
        811451993645908068,
        811452000624967692,
        811452006971211797,
        811452013585891342,
        811452018387451914,
        877785052640059442,
        877787715163258890
    ],
    866160840037236736 : [
        901649904357752833
    ]
}

pronounRoleList = { 
    811369107181666343 : [
        811443833832734750,
        811443883304419328,
        811443152857989120,
        877789173086564422,
        811443911582548018,
        864251359636881408,
        864642630684377098

    ],
    866160840037236736 : [
        901649866999087125
    ]
}

tooOldRole = { 
    811369107181666343 : 811452704617922590,
    866160840037236736 : 901649931432001726,
    622592295065354241 : 959673591899750471
}

tooYoungRole = { 
    811369107181666343 : 959673604562358272,
    622592295065354241 : 959673635008831572
    
}

verifiedRole = {
    811369107181666343 : 811442483115720706,
    866160840037236736 : 901650947405672479,
    622592295065354241 : 959676031613149255
}

logChannel = {
    811369107181666343 : 811498382211284992
}

roleChannel = {
    811369107181666343 : 811396496774922240
}

welcomeChannel = {
    811369107181666343 : 811386285876445184,
    866160840037236736 : 866160840037236739
}

numberEmoteList = [
            "<:gh_1:856557384071512065>",
            "<:gh_2:856557978383155200>",
            "<:gh_3:856557993030189096>",
            "<:gh_4:856558007352950795>",
            "<:gh_5:856558030836990002>",
            "<:gh_6:856558055138394169>",
            "<:gh_7:856558070069723146>",
            "<:gh_8:856558533814124544>",
            "<:gh_9:856558551547510794>",
            "<:gh_10:856558568986771466>"
        ]

joinChannel = {
    811369107181666343 : 811386285876445184,
    764385563289452545 : 764385563813871618,
    866160840037236736 : 866160840037236739
    }

botRole = {
   811369107181666343 : 811452026150977576,
   866160840037236736 : None
}

loadedInventories = {}

bumpChannel = {
    811369107181666343 : 812166022073024552
}

code_contributors = [
    243759220057571328,
    332653982470242314
]

gif_contributors = [
    253286336264536070,
    332653982470242314,
    456051303823441920,
    634097307327135750,
    505116146467602432
]
