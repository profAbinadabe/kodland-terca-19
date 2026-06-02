import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

# Área para funções
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']  


# Comandos/Ações do bot
@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    # Mostra quando um membro específico entrou no servidor.
    data_formatada = member.joined_at.strftime("%d/%m/%Y")
    await ctx.send(f"Boas-vindas! O usuário {member.name} entrou no servidor no dia {data_formatada}.")

    # "O usuario " + usuario + " "
    # "O usuario", usuario, " "
    # f"O usuario {usuario} "

@bot.command()
async def meme(ctx):
    # pegar todos os arquivos dentro da pasta imagens
    images = os.listdir('img')

    # escolher imagem aleatoria
    img_name = random.choice(images)

    # abrir imagem escolhida e enviar para o discord 
    with open(f"img/{img_name}", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file = picture)


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("O TOKEN SECRETO FICA AQUI")
