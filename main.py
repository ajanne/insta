from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import enums
import instaloader

model_engine = "text-davinci-003"

app = instaloader.Instaloader()
try:
    app.login("user.035007", "saranbhuvan")
except:
    app.login("user.035006", "saranbhuvan")
    
bot = Client("DumperGPT", api_id=3769190, api_hash="e125d5abf9dadd0f9b861f774f5aae6a", bot_token="5863087473:AAHvdFs954RE-AjexU5jIPnRCXN0-7mvzUM")

START_BUTTON = JOIN_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/DumperBots")], [InlineKeyboardButton("Help", callback_data="help")], [InlineKeyboardButton("Source code", callback_data="source")], [InlineKeyboardButton("Back", callback_data="back")]])
JOIN_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/DumperBots")], [InlineKeyboardButton("Joined", callback_data="chatgpt")]])

@bot.on_message(filters.command("start") & filters.all)
async def start(bot, msg):
    reply_markup = START_BUTTON
    await msg.reply_text(text="<b>π§πΎπππ πΆπΎππΌπππΎ ππ π¨ππππΊπ₯πππ½πΎπ. π³πππ π»ππ ππππππ½πΎ π¨ππΏππππΊππππ ππΏ π¨ππππΊπππΊπ π΄ππΎπ π»π π΄ππΎπππΊππΎ.\n\nπ  π―πππ½ππΌπ ππΏ @TheDumperNetwork</b>", reply_markup=reply_markup)
    await msg.reply_text("<b>Use /find instagram_username</b>")

@bot.on_callback_query()
def callback_query(bot, CallBackQuery):
    reply_markup = START_BUTTON
    if CallBackQuery.data == "help":
        text = """
        <b>π’ππππΊππ½π π ππΊπππΊπ»ππΎ :\n/find <usernmae> - To Get Detailes of User\n\nπ€ππΊππππΎ :\n/find eminem</b>
        """
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)
    elif CallBackQuery.data == "source":
        text = "<b>π¨πΏ πππ ππΊππ ππππ π»ππ'π πππππΌπΎ πΌππ½πΎ\n\nπ’ππππΊπΌπ : @Walker_web</b>"
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)
    elif CallBackQuery.data == "back":
        text = "<b>π§πΎπππ πΆπΎππΌπππΎ ππ π¨ππππΊπ₯πππ½πΎπ. π³πππ π»ππ ππππππ½πΎ π¨ππΏππππΊππππ ππΏ π¨ππππΊπππΊπ π΄ππΎπ π»π π΄ππΎπππΊππΎ.\n\nπ  π―πππ½ππΌπ ππΏ @TheDumperNetwork</b>"
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)


@bot.on_message(filters.command("find") & filters.all)
async def chatgpt(bot, msg):
    try:
        member = await bot.get_chat_member("DumperBots", msg.from_user.id)
        is_mem = True
    except UserNotParticipant:
        reply_markup = JOIN_BUTTON
        await msg.reply_text(text="<b>πΈππ ππππ ππππ πππ π’ππΊπππΎπ ππ πππΎ ππππ ππΎππππΌπΎ</b>", reply_markup=reply_markup)
        return

    if is_mem:
        username = msg.text.replace("/find ", "")
        await bot.send_chat_action(msg.chat.id, enums.ChatAction.TYPING)
        try:
            profile = instaloader.Profile.from_username(app.context, username)
        except:
            await msg.reply_text("<b>Kindly check the provided Username is Correct!</b>")
        un = str(profile.username)
        ui = str(profile.userid)
        tp = str(profile.mediacount)
        fc = str(profile.followers)
        fp = str(profile.followees)
        bi = str(profile.biography)
        text = "<b>ππ¨ππ§π£ππ’π : " + un + "\n\nππ¨ππ§ ππΏ : <tt>" + ui + "</tt>\n\nππ€π©ππ‘ ππ€π¨π©π¨ : " + tp + "\n\nππ€π‘π‘π€π¬ππ§π¨ πΎπ€πͺπ£π© : " + fc + "\n\nππ€π‘π‘π€π¬ππ£π πΎπ€πͺπ£π© : " + fp + "\n\nπ½ππ€ :\n" + bi + "</b>"
        await msg.reply_text(text)
        
print("Bot is Running")
bot.run()
