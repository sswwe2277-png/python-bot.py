from pyrogram import Client, filters
from pyrogram.errors import InviteHashExpired, UsernameNotOccupied, UserNotParticipant

import os

# قراءة المتغيرات من Environment Variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("fund_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# القنوات المطلوبة للاشتراك
CHANNELS = [
    "https://t.me/eerrt31"       # القناة التي أرسلتها
]

# التحقق من القناة
def check(client, user_id, channel):
    try:
        client.get_chat(channel)
        client.get_chat_member(channel, user_id)
        return True
    except UserNotParticipant:
        return False
    except (InviteHashExpired, UsernameNotOccupied):
        return "invalid"
    except:
        return "invalid"

@app.on_message(filters.command("start"))
def start(client, message):
    uid = message.from_user.id

    for ch in CHANNELS:
        status = check(client, uid, ch)

        if status == "invalid":
            continue

        if status is False:
            message.reply(
                f"🔔 اشترك بالقناة:\n{ch}\nثم اضغط /start"
            )
            return

    message.reply("✅ تم التحقق! البوت شغال تمام 🎉")

app.run()
