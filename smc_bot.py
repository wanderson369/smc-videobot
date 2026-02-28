import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SMC Bot is running")

# DEPOIS do application.run_polling()
if __name__ == "__main__":
    # Seu bot roda aqui normalmente...
    
    # Health server pro Render (NÃO APAGA!)
    port = int(os.getenv("PORT", 10000))
    server = HTTPServer(("", port), HealthHandler)
    print(f"Health server on port {port}")
    server.serve_forever()
    # TEU CÓDIGO ATUAL (mantém 100%)
imports...
load_dotenv()
TOKEN = os.getenv('TOKEN')

# SÓ ADICIONA ISSO AQUI 👇 (logo após TOKEN)
WEBHOOK_URL = "https://smc-videobot.onrender.com" 
requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}")
print("✅ Webhook configurado!")

# resto do teu código IGUAL...
