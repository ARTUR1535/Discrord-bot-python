import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Bot is online')


@bot.command(aliases=["возможности"])
async def ping(ctx):
    await ctx.send("Возможности: 1) >Формулы 2))>графики ")


@bot.command(aliases=["Формулы"])
async def ping1(ctx):
    await ctx.send(
        "1)>Механика 2)>Криволинейное.движение 3)>Динамика 4)>Работа.энергия.мощность  5)>Колебания.Волны 6)  >Электродинамика   "
    )


@bot.command(aliases=["Механика"])
async def ping2(ctx):
    await ctx.send(
        "1) V=S/t   2) x=x0+vt   3) a=v-v0/t   4) v=v0+at  5) s=v0t+(at^2)/2 6)  x=x0+v0t+(at^2)/2 "
    )


@bot.command(aliases=["Криволинейное.движение"])
async def ping3(ctx):
    await ctx.send("1)  v=N/t  2) T=t/N  3)  T=1/v  4)  v=2ПrV  5)  W=2П/T")


@bot.command(aliases=["Динамика"])
async def ping4(ctx):
    await ctx.send(
        "1)  a=F/m  2)  F1=-F2  3)  Fтр=MN  4)F=mg  5)Fупр=-kx  6)  F=G(m1m2)/r^2    "
    )


@bot.command(aliases=["Работа.энергия.мощность"])
async def ping5(ctx):
    await ctx.send(
        " 1)A=FSCOSa  2)A=-FS  3)  N=A/t  4)Eкин=(mV^2)/2  5)  Eпот=mgh 6)Eп=(kx^2)/2  6)E=Eк+Eп "
    )


@bot.command(aliases=["Колебания.Волны"])
async def ping6(ctx):
    await ctx.send(
        " 1)  x=Asin(wt+ф0)  2)  v=vcos(wt+ф0)  3)  a=-asin(wt+ф0)  4)  W=2Пv=2П/T  5) T=2Пsqr(m/k)  6)  T=2Пsqr(l/g)   "
    )


@bot.command(aliases=["Электродинамика"])
async def ping7(ctx):
    await ctx.send(
        " 1) F=K(q1q2)/r^2  2) E=F/q  3)E=U/d  4)W=k(q1q2)/r  5)C=q/u   ")


@bot.command(aliases=["графики"])
async def ping8(ctx):
    await ctx.send("1)>Изопроцессы  2)>Колебательные  3)>Движения")


@bot.command(aliases=["Изопроцессы"])
async def ping9(ctx):
    await ctx.send(
        " https://upload.wikimedia.org/wikipedia/ru/f/f5/Isoprocess.jpg")


@bot.command(aliases=["колебательные"])
async def ping10(ctx):
    await ctx.send(
        "https://www.examen.ru/assets/images/2014/formuly/fiz/11_03.png")


@bot.command(aliases=["Движения"])
async def ping11(ctx):
    await ctx.send("https://marina.yuha.ru/files/tabl/04d.gif")


bot.run(os.getenv("token"))