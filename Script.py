class script(object):
    START_TXT = """π·π΄π»πΎ {},
πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>, πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ π"""
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """β― πΌπ π½π°πΌπ΄: <a href=https://t.me/M_autofilter_bot>{}</a>
β― π²ππ΄π°ππΎπ: <a href=https://t.me/VysakhXR>ππππ°πΊπ· α‘§</a>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β― π±πΎπ ππ΄πππ΄π: π·π΄ππΎπΊπ
β― π±ππΈπ»π³ πππ°πππ: v1.0.1 [ π±π΄ππ° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and π»πππ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. π»πππ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- π»πππ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. π»πππ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/M_autofilter_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of π»πππ

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    
    REPORT_TXT = """β€ πππ₯π©: Rα΄α΄α΄Κα΄ β οΈ
    
ππππ πππππππ πππππ π’ππ ππ ππππππ π πππππππ ππ π ππππ ππ πππ ππππππ ππ πππ ππππππππππ πππππ. π³ππ'π ππππππ ππππ πππππππ.

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ/report ππ @admins - π³π ππΎππππ πΊ πππΎπ ππ πππΎ πΊπ½ππππ (ππΎπππ ππ πΊ ππΎπππΊππΎ)."""
    
    VIDEO_TXT ="""π·π΄π»πΏ ππΎπ ππΎ π³πΎππ½π»πΎπ°π³ ππΈπ³π΄πΎ π΅ππΎπΌ ππΎππππ±π΄
    
β’ Usage 
 You can download any video from YouTube 

How to use 
β’ ππΊπ±π¦ /video or /mp4 ππ―π₯ (https://youtu.be/kB9TkCs8cX0)
β’ ππΉπ’π?π±π­π¦:
<code>/mp4 https://youtu.be/kB9TkCs8cX0</code>
<code>/video https://youtu.be/kB9TkCs8cX0</code>"""
 
    SONG_TXT = """<b>ππΎπ½πΆ π³πΎππ½π»πΎπ°π³ πΌπΎπ³ππ»π΄</b>
    
<b>ππΎπ½πΆ π³πΎππ½π»πΎπ°π³ πΌπΎπ³ππ»π΄, π΅πΎπ ππ·πΎππ΄ ππ·πΎ π»πΎππ΄ πΌπππΈπ². ππΎπ π²π°π½ πππ΄ ππ·πΈπ π΅π΄π°πππ΄ π΅πΎπ π³πΎππ½π»πΎπ°π³ π°π½π ππΎπ½πΆ ππΈππ· πππΏπ΄π π΅π°ππ ππΏπ΄π΄π³.ππΎππΊπ πΎπ½π»π πΎπ½ πΆππΎππΏπ../</b>

<b>π²πΎπΌπΌπ°π½π³π</b>

βΊβΊ  /song ππΎπ½πΆ π½π°πΌπ΄ 

ππΎππΊπ πΎπ½π»π πΎπ½ πΆππΎππΏ""" 
    
    TELEGRAPH_TXT = """<b>β«οΈHELP: TelegraphβͺοΈ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

π€§ /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

β’ ππππ π²ππππππ πΈπ π°ππππππππ ππ πππππ πππ ππ
β’ ππππ π²ππππππ π²ππ ππ ππππ ππ’ πππππ’πππ"""

    YTTHUMB_TXT = """π·π΄π»πΏπ ππΎ π³πΎππ½π»πΎπ°π³ π°π½π ππΎππππ±π΄ ππΈπ³π΄πΎ ππ·ππΌπ±π½π°πΈπ»
    
β­How to use

β Type /ytthumb [video Link]

β’ Example  
<code>/ytthumb https://youtu.be/UyzJ9KEoU0w</code>""" 
    
    HEROKUSTATUS_TXT = """Send /status for getting bot and heroku status"""
    
    RESTRIC_TXT = """β€ πππ₯π©: Mα΄α΄α΄ π«
    
πππππ πππ πππ ππππππππ π πππππ πππππ πππ πππ ππ ππππππ πππππ πππππ ππππ πππππππππππ’

βͺ/mute: π³π ππππΎ πΊ πππΎπ ππ πππΎ πππππ 
βͺ/unmute: π³π ππππππΎ πΊ πππΎπ ππ πππΎ πππππ 
βͺ/tmute: π³π ππΎπππππΊππππ ππππΎ πΊ πππΎ

β€ π­πππΎ:
πΆππππΎ πππππ /tmute πππ ππππππ½ πππΎπΌππΏπ πππΎ ππππΎ ππππ
βπ€ππΊππππΎ: /tmute 2π½
πΈππ πΌπΊπ πππΎ ππΊπππΎπ: π/π/π½
 β’ π = ππππππΎπ
 β’ π = πππππ 
 β’ π½ = π½πΊππ"""
 
    FILE_TXT = """β€ πππ₯π©: ππ’π₯π ππ­π¨π«π ππ¨ππ?π₯π.. 
    
<b>π±π πππΈπ½πΆ ππ·πΈπ πΌπΎπ³ππ»π΄ ππΎπ π²π°π½ πππΎππ΄ π΅πΈπ»π΄π πΈπ½ πΌπ π³π°ππ°π±π°ππ΄ π°π½π³ πΈ ππΈπ»π» πΆπΈππ΄ ππΎπ π° πΏπ΄ππΌπ°π½π΄π½π π»πΈπ½πΊ  ππΎ π°π²π²π΄ππ ππ·π΄ ππ°ππ΄π³ π΅πΈπ»π΄π.πΈπ΅ ππΎπ ππ°π½π ππΎ π°π³π³ π΅πΈπ»π΄π π΅ππΎπΌ π° πΏππ±π»πΈπ² π²π·π°π½π½π΄π» ππ΄π½π³ ππ·π΄ π΅πΈπ»π π»πΈπ½πΊ πΎπ½π»π  πΎπ ππΎπ ππ°π½π ππΎ π°π³π³ π΅πΈπ»π΄π π΅ππΎπΌ π°  πΏππΈππ°ππ΄ π²π·π°π½π½π΄π» ππΎπ πΌπππ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½ πΎπ½ ππ·π΄ π²π·π°π½π½π΄π» ππΎ π°π²π²π΄ππ π΅πΈπ»π΄π...//</b>

βͺΌ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π βΊ

βͺ /plink βΊβΊ <b>ππ΄πΏπ»π ππΎ π°π½π πΌπ΄π³πΈπ° ππΎ πΆπ΄π π»πΈπ½πΊ</b>
βͺ /pbatch βΊβΊ <b>πππ΄ ππΎππ πΌπ΄π³πΈπ° π»πΈπ½πΊ ππΈππ· ππ·πΈπ π²πΎπΌπΌπ°π½π³</b>
βͺ /batch βΊβΊ <b>ππΎ π²ππ΄π°ππ΄ π»πΈπ½πΊ π΅πΎπ πΌππ»ππΈπΏπ»π΄ π΅πΈπ»π΄π</b>

βͺΌ ππ±ππ¦π©π₯π βΊ

<code>/batch https://t.me/MWUpdatez/3 https://t.me/MWUpdatez/8</code>"""
    
    STICKER_TXT = """ππΎπ π²π°π½ πππ΄ ππ·πΈπ πΌπΎπ³ππ»π΄ ππΎ π΅πΈπ½π³ π°π½π πππΈπ²πΊπ΄ππ πΈπ³

β’ πππππ 
To Get Sticker ID 

β­How to use

 β Reply To Any Sticker /stickerid"""
   
    NEXXT_TXT = """π·π΄π {},
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π"""
    
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
