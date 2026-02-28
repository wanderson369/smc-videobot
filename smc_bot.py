import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# === TEU TOKEN ===
TOKEN = os.getenv('TOKEN')

# === APPLICATION (GLOBAL) ===
application = Application.builder().token(TOKEN).build()

# === TEUS HANDLERS (igual teu código) ===
async def start(update, context):
    await update.message.reply_text("SMC Bot LIVE! 🎉

/start:

application.add_handler(CommandHandler("start", start))

# === FLASK WEBHOOK ===
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET', 'HEAD'])
def webhook():
    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), None)
        application.process_update(update)
        return 'OK'
    return 'Bot is running'  # Health check

# === MAIN ===
if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
