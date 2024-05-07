import discord
from discord.ext import commands
from Config import config
from datetime import datetime
import random
import random
import sqlite3
import numpy as np



bot = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all())  
# подключение к базе данных

conn = sqlite3.connect('ratings.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ratings (
            user_id INTEGER,
            rating Float,
            number_of_ratings INTEGER,
            all_rating Float)''')
conn.commit()


class rates(discord.ui.View):
    def __init__(self, user_id):
          super().__init__()
          self.user_id = user_id


    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def rate_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        for child in self.children:
            child.disabled = True
        
        user_id = self.user_id
        result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()

        if(result == None):
            c.execute("INSERT INTO ratings (user_id, rating, number_of_ratings, all_rating) VALUES (?, ?, ?, ?)", (user_id, 1, 1, 1))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        else:
            new_rating = np.round((result[2]+1)/(result[1]+1), decimals=2)
            c.execute("UPDATE ratings SET rating = ?, number_of_ratings = ?, all_rating = ? WHERE user_id = ?", (new_rating, result[1]+1, result[2]+1, user_id))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        conn.commit()

        await interaction.response.edit_message(view=self)


    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def rate_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        for child in self.children:
            child.disabled = True
            
        user_id = self.user_id
        result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()

        if(result == None):
            c.execute("INSERT INTO ratings (user_id, rating, number_of_ratings, all_rating) VALUES (?, ?, ?, ?)", (user_id, 2, 1, 2))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        else:
            new_rating = np.round((result[2]+2)/(result[1]+1), decimals=2)
            c.execute("UPDATE ratings SET rating = ?, number_of_ratings = ?, all_rating = ? WHERE user_id = ?", (new_rating, result[1]+1, result[2]+2, user_id))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        conn.commit()
        await interaction.response.edit_message(view=self)


    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def rate_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        for child in self.children:
            child.disabled = True
            
        user_id = self.user_id
        result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()

        if(result == None):
            c.execute("INSERT INTO ratings (user_id, rating, number_of_ratings, all_rating) VALUES (?, ?, ?, ?)", (user_id, 3, 1, 3))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        else:
            new_rating = np.round((result[2]+3)/(result[1]+1), decimals=2)
            c.execute("UPDATE ratings SET rating = ?, number_of_ratings = ?, all_rating = ? WHERE user_id = ?", (new_rating, result[1]+1, result[2]+3, user_id))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        conn.commit()
        await interaction.response.edit_message(view=self)


    @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
    async def rate_4(self, interaction: discord.Interaction, button: discord.ui.Button):
        for child in self.children:
            child.disabled = True

            
        user_id = self.user_id
        result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()

        if(result == None):
            c.execute("INSERT INTO ratings (user_id, rating, number_of_ratings, all_rating) VALUES (?, ?, ?, ?)", (user_id, 4, 1, 4))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        else:
            new_rating = np.round((result[2]+4)/(result[1]+1), decimals=2)
            c.execute("UPDATE ratings SET rating = ?, number_of_ratings = ?, all_rating = ? WHERE user_id = ?", (new_rating, result[1]+1, result[2]+4, user_id))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        conn.commit()
        await interaction.response.edit_message(view=self)
 
    @discord.ui.button(label="5", style=discord.ButtonStyle.gray)
    async def rate_5(self, interaction: discord.Interaction, button: discord.ui.Button):
        for child in self.children:
            child.disabled = True
            
        user_id = self.user_id
        result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()

        if(result == None):
            c.execute("INSERT INTO ratings (user_id, rating, number_of_ratings, all_rating) VALUES (?, ?, ?, ?)", (user_id, 5, 1, 5 ))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        else:
            new_rating = np.round((result[2]+5)/(result[1]+1), decimals=2)
            c.execute("UPDATE ratings SET rating = ?, number_of_ratings = ?, all_rating = ? WHERE user_id = ?", (new_rating, result[1]+1, result[2]+5, user_id))
            result = c.execute("SELECT rating, number_of_ratings, all_rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
        conn.commit()

    #    await interaction.response.send_message(f"оценил пользователя на 5 баллов. Средняя оценка: {res_rating}")
        await interaction.response.edit_message(view=self)



class Buy(discord.ui.View):
    def __init__(self):
          super().__init__()
   
    @discord.ui.button(label="Купить?", style=discord.ButtonStyle.red)
    async def btn0(self, interaction: discord.Integration, button: discord.ui.Button):
        message = "2 .Если вы хотите отказаться от покупки нажмите ниже"
        x = random.randrange(10)
        role = await interaction.guild.create_role(name=f"{x}'s Role")
       #bot.role = interaction.guild.get_role(role)
        AD_role =  discord.utils.get(interaction.guild.roles, name='Продовец')
        await interaction.user.add_roles(role)
        chanell = await interaction.channel.guild.create_text_channel(name=f"{x}'s area")

        await chanell.set_permissions(role, send_messages = True, read_messages = True)
        await chanell.set_permissions(interaction.guild.default_role, send_messages = False, read_messages = False)
        await chanell.set_permissions(AD_role, send_messages = True, read_messages = True)
        await chanell.send(message, view=Cancel(role=role, chanell=chanell))
        self.value = 'buy'        
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)



class Cancel(discord.ui.View):
    def __init__(self, role, chanell):
          super().__init__()
          self.role = role
          self.chanell = chanell

    @discord.ui.button(label="Отказаться от покупки", style=discord.ButtonStyle.red)
    async def btn(self, interaction, button):

        #await self.role.delete() # Удалить роль
        #await self.chanell.set_permissions(name = 'Продовец', send_messages = False, read_messages = False)
      #  await interaction.user.send(view = rates(interaction.user))
        
        await interaction.send_message("Простите, но функция не работает")

@commands.has_permissions(administrator = True) 
@bot.command()
async def lm(ctx: commands.Context, member: discord.Member, user: str):
    await member.send('Здравствуйте, благодарим вас за покупку в нашем магазине, мы просим вас оценить сотрудника который вас обслуживал, спасибо !', view=rates(user))

@commands.has_permissions(administrator = True) 
@bot.command()
async def otz(ctx, user_id):
    # Создаем кнопки
    await ctx.send('Пожалуйста, оцените нашу работу:', view=rates(user_id))

@bot.command()
async def ranks(ctx, user_id):
    # Создаем кнопки
    result = c.execute("SELECT rating FROM ratings WHERE user_id = ?", (user_id,)).fetchone()
    await ctx.send(f'У этого пользователя {result}')




@bot.event
async def on_ready():
    print("I am running on " + bot.user.name)

@commands.has_permissions(administrator = True) 
@bot.command()
async def button(ctx: commands.Context):
     
      #chanel = bot.get_channel(1214154395273662464)
      try:
         await ctx.send(view=Buy())
         #await chanel.send(view=Buy())
      except Exception as errors:
        print(f"Bot Error: {errors}")

@bot.command()
async def time(ctx):
      now = datetime.now()
      current = now.strftime("%H:%M:%S")
      await ctx.send('Сейчас: ' + current)
      await ctx.send('А время работы с 14:00 до 21:00 МСК')







bot.run(config['token'])

