import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler

# ... teu código do bot todo igual (TOKEN, handlers, etc) ...

# === FLASK WEBHOOK CORRIGIDO ===
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET', 'HEAD'])
def webhook():
    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), None)
        application.process_update(update)  **← AQUI! application, NÃO bot**
    return 'OK'

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    server = HTTPServer(("", port), HealthHandler)
    print(f"Health server running on port {port}")
    server.serve_forever()
