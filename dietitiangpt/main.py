import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction
import config as _conf
from chatgpt_app import OpenAIResponse

diet_coach_channel_id=1230064119579938880

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())
chat_response=OpenAIResponse()

@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(f"{client.user.name} is ready")
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

async def textcoach(interaction: Interaction,diet_prompt: str):
    await interaction.response.defer()
    await interaction.followup.send(chat_response.chatgpt(diet_prompt))

@client.tree.command(name="dietcoach",description="send Diet Coach your meal screenshot and question :)")
@app_commands.describe(meal_ss="Send me your meal screenshot and I will analyze it for you. You can also ask me a question about it if you want :)")
@app_commands.describe(question="Ask me anything about diet and nutrition :)")
async def aidietitian(interaction: Interaction,meal_ss: discord.Attachment=None,question: str=""):
    
    if meal_ss is None:
        await textcoach(interaction=interaction,diet_prompt=question)
    
    else:
        await interaction.response.defer()
        image_file = await meal_ss.to_file()
        content = chat_response.visiongpt(meal_ss.url,question)
        await interaction.followup.send(content=content,file=image_file)

@client.event
async def on_message(message):
    
    if message.author==client.user:
        return

    if message.channel.id==diet_coach_channel_id:
        
        if message.attachments:
            await message.channel.send(chat_response.visiongpt(message.attachments[0].url,message.content))
        else:
            await message.channel.send(chat_response.chatgpt(message.content))
    

client.run(_conf.DIETITIAN_TOKEN)