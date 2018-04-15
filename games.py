import discord
from discord.ext import commands
from random import randint


class Games():
    
    def __init__(self, bot):
        self.bot = bot


    #atirar um dado com 20 faces
    @commands.command(pass_context=True)
    async def roll(self, ctx):
        await self.bot.say('You rolled a ' + str(randint(1,20)))
    
    
    #atirar moeda ao ar (com easteregg)
    @commands.command(pass_context=True)
    async def flip(self, ctx):
        n = randint(0,10000)
        line = 'WTF the coin landed upright!'
        if(n<5000): line = 'You got tails'
        elif(n<10000): line = 'You got heads'
    
        await self.bot.say(line)
    
    
    #escolher uma carta
    @commands.command(pass_context=True)
    async def pick(self, ctx):
        simbolo = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
        naipe = ['paus', 'ouros', 'copas', 'espadas']
        await self.bot.say(simbolo[randint(0,12)] + ' de ' + naipe[randint(0,3)])
    
    
    #pedra papel tesoura
    @commands.command(pass_context=True)
    async def rps(self, ctx, player):
        if(player == 'rock' or player == 'paper' or player == 'scissors'  or player == 'r' or player == 'p' or player == 's'):
            cpu = getRPS()
            player = simpRPS(player)
            result = "**JBB won!**" #assume que o JBB ganha
            if (player == cpu):
                result = "**It´s a tie!**"
            if (player == "rock" and cpu == "scissors"):
                result = "**You won!**"
            if (player == "paper" and cpu == "rock"):
                result = "**You won!**"
            if (player == "scissors" and cpu == "paper"):
                result = "**You won!**"
            await self.bot.say('You played ' + player + '\nJBB played ' + cpu + '\n' + result)
        else:
            await self.bot.say('*Invalid*')


def getRPS():
    n = randint(0,2)
    if(n == 0):
        return "rock"
    if(n == 1):
        return "paper"
    return "scissors"


def simpRPS(hand):
    if (hand == "r"):
        hand = "rock"
    if (hand == "p"):
        hand = "paper"
    if (hand == "s"):
        hand = "scissors"
    return hand


def setup(bot):
    bot.add_cog(Games(bot))