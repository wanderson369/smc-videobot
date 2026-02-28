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
