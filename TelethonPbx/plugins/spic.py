
from . import *

@bot.on(admin_cmd(pattern="spic"))
async def oho(event):
  if not event.is_reply:
    return await event.edit('Reply to a self distructing pic !.!.!')
  k = await event.get_reply_message()
  pic = await k.download_media()
  await bot.send_file(event.chat_id, pic, caption=f"""
  YOUR SELF distructing PIC IS HACKEd by @arshuu_69
  """)
  await event.delete()




