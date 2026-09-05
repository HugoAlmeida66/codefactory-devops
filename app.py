"""API demonstrativa para a atividade de DevOps da CodeFactory."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "0.1.0"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            "/": {"empresa": "CodeFactory Solutions", "versao": VERSION},
            "/health": {"status": "ok"},
        }
        payload = routes.get(self.path)
        body = json.dumps(payload if payload is not None else {"erro": "Rota inexistente"}).encode()
        self.send_response(200 if payload is not None else 404)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", int(os.getenv("PORT", "8000"))), Handler).serve_forever()
