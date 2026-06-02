import discord
import random
from discord.ext import commands

# Configuração do Bot
TOKEN = "Aqui vai o meu token"

# Permissão herdada: padrão.
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Base de dados simples para o bot
# Lista
lixo_reciclavel = [
    "lata", "saquinho", "plastico"
]

lixo_comum = [
    "fralda", "restos de comida"
]

descarte_especial = [
    "pilha", "remédio"
]


@bot.command()
async def lixo(ctx, *, item=None):
    if item is None:
        await ctx.send("Use assim: !lixo lata")
        return
    
    item = item.lower() 

    if item in lixo_reciclavel:
        await ctx.send(f'{item} deve ir para a reciclagem.')
    
    elif item in lixo_comum:
        await ctx.send(f'{item} deve ir para lixo comum.')

    # Falta criar mais uma codição
    # Falta criar o else caso o item não exista


bot.run(TOKEN)