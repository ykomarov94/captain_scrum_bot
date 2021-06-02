import discord
import random

guildname = 'talking scientific pizza'
intents = discord.Intents.all()
client = discord.Client(intents=intents)

sad_prefixes = ['увы, но', 'вынужден огорчить, господа, но', 'вот незадача,', 'бесконечно извиняюсь, но', 'как ни прескорбно, но', 'сожалею, но именно сегодня', 'так уж вышло, что']
joy_prefixes = ['счастливый случай выбрал {}', 'перенаправляем прожекторы... всё внимание на {}!', 'поздравляю! самый счастливый человек сегодня — {}', 'герой сегодняшнего дня — {}', 'а самый красивый голос в канале — у {}, вот послушайте', 'как ни крутись, но тут без {} не обойтись', 'победитель розыгрыша — {}', 'человек-легенда, лауреат премии "их выбрал рандом" — {}', 'случайности не случайны, {} знает это, как никто другой']


def sad_prefix():
    return random.choice(sad_prefixes)


def joy_prefix():
  return random.choice(joy_prefixes)


async def choise_random(message):
    args = message.content.split()

    if len(args) >= 2:
        channel = await get_channel_byname(message, args[1])
    else:
        channel = await get_channel(message)

    members = channel.members
    if not members:
        await message.channel.send(f'{sad_prefix()} в канале "{channel_name}" никого нет')
        return

    await message.channel.send(joy_prefix().format(random.choice(members).mention))


async def get_channel(message):
    guild = message.guild
    channel = [x for x in guild.channels if str(x.type) == 'voice' and message.author in x.members]
    if not channel:
        await message.channel.send(f'{sad_prefix()} {message.author.mention} не удалось найти ни в одном из каналов')
        return
    return channel[0]


async def get_channel_byname(message, ch_name):
    guild = message.guild
    channel = [x for x in guild.channels if x.name.lower() == ch_name and str(x.type) == 'voice']
    if not channel:
        await message.channel.send(f'{sad_prefix()} голосовой канал "{ch_name}" найти не удалось')
        return
    return channel[0]


@client.event
async def on_ready():
    global tsp
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!random') or message.content.startswith('!рандом'):
        await choise_random(message)
        

client.run('TOKEN')
