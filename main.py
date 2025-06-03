from pyrogram import Client, filters
import time
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# !اكتم: كتم العضو 10 دقائق
@app.on_message(filters.command("اكتم") & filters.group)
async def mute(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            permissions={},
            until_date=int(time.time()) + 600
        )
        await message.reply("✅ تم كتم العضو 10 دقائق")
    else:
        await message.reply("❗ يجب الرد على رسالة العضو")

# !فك: فك الكتم
@app.on_message(filters.command("فك") & filters.group)
async def unmute(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            permissions={
                "can_send_messages": True,
                "can_send_media_messages": True,
                "can_send_other_messages": True,
                "can_add_web_page_previews": True,
            }
        )
        await message.reply("✅ تم فك الكتم")
    else:
        await message.reply("❗ يجب الرد على رسالة العضو")

# !حظر: طرد العضو
@app.on_message(filters.command("حظر") & filters.group)
async def ban(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await client.kick_chat_member(message.chat.id, user_id)
        await message.reply("🚫 تم حظر العضو")
    else:
        await message.reply("❗ يجب الرد على رسالة العضو")

# !مسح: حذف الرسالة
@app.on_message(filters.command("مسح") & filters.group)
async def delete_message(client, message):
    if message.reply_to_message:
        await message.reply_to_message.delete()
        await message.delete()
    else:
        await message.reply("❗ يجب الرد على الرسالة المراد حذفها")

app.run()
