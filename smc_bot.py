import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv('TOKEN')
print(f"🤖 Bot iniciado com TOKEN: {TOKEN[:10]}...")

application = Application.builder().token(TOKEN).build()

async def start(update, context):
    menu = """
🤖 **SMC VIDEO BOT LIVE!** 🎉

**MENU PRINCIPAL:**
/start - Menu principal
/video - Análise SMC em vídeo
/status - Status do bot

**Status:** ✅ Online 24/7 (Render)
    """
    await update.message.reply_text(menu, parse_mode='Markdown')

application.add_handler(CommandHandler("start", start))
print("✅ Handlers registrados: /start")

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET', 'HEAD'])
def webhook():
    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), None)
        if update:
            print(f"📨 Update recebido: {update.message.text[:20] if update.message else 'sem texto'}")
            application.process_update(update)
        return 'OK'
    elif request.method == 'GET':
        return 'Bot is running ✅'
    return 'OK'

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    print(f"🚀 Iniciando Flask na porta {port}")
    print(f"🌐 URL: https://smc-videobot.onrender.com")
    app.run(host='0.0.0.0', port=port, debug=False)
