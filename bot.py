import asyncio, os
from telegram import Bot
from PIL import Image, ImageDraw

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@MAESTROTIPS_EG"

MATCHES = [
    ("Man City vs Arsenal", "BTTS Yes", "1.85"),
    ("Real vs Barca", "Over 2.5", "1.75"),
    ("Ahly vs Zamalek", "1X", "1.60"),
    ("Liverpool vs Chelsea", "Home Win", "2.10"),
    ("Bayern vs Dortmund", "BTTS Yes", "1.90"),
]

def make_img(t):
    img = Image.new('RGB', (1080,1350), (18,18,18))
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,1080,150], fill=(255,215,0))
    d.text((50,400), t, fill=(255,255,255))
    img.save("/tmp/m.jpg")
    return "/tmp/m.jpg"

async def main():
    bot = Bot(TOKEN)
    for a,b,c in MATCHES:
        cap = f"🔥 {a}\n💡 {b} | {c}\n\n📲 @MAESTROTIPS_EG"
        p = make_img(f"{a}\n{b} @ {c}")
        await bot.send_photo(CHANNEL, open(p,'rb'), caption=cap)
        await asyncio.sleep(2)

asyncio.run(main())
