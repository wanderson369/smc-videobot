import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

if __name__ == "__main__":
    # Seu código normal do bot (Application.run_polling etc) já deve estar aqui

    # Keep‑alive server (só pra Render não dar erro de porta)
    port = int(os.getenv("PORT", 10000))
    server = HTTPServer(("", port), HealthHandler)
    print(f"Health server running on port {port}")
    server.serve_forever()
