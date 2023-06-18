import pyrogram
import asyncio
import os
from pyrogram import filters, Client as Sflix

@Client.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def report_user(bot, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        data = message.text
        command, timezone = data.split(" ")
        tz = pytz.timezone(f'{timezone}')
        today = date.today()
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        report = f"𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})" + "\n"
        report += f"𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {message.reply_to_message.link}"
        # Using latest pyrogram's enums to filter out chat administrators
        async for admin in bot.get_chat_members(chat_id=message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if not admin.user.is_bot: # Filtering bots and prevent sending message to bots | Message will be send only to user admins
                try:
                    reported_post = await message.reply_to_message.forward(admin.user.id)
                    await reported_post.reply_text(
                        text=report,
                        chat_id=admin.user.id,
                        disable_web_page_preview=True
                    )
                    success = True
                except:
                    pass
            else: # Skipping Bots
                pass
        if success:
