from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json, time
from pathlib import Path
ROOT = Path(__file__).parent / "static"

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def do_GET(self):
        if self.path.startswith("/api/action"):
            start = time.perf_counter()
            time.sleep(0.025)  # retardo fijo para hacer visible la medición en esta PoC
            elapsed = (time.perf_counter() - start) * 1000
            body = json.dumps({"ok": True, "message": "Acción procesada", "server_ms": round(elapsed, 2)}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

if __name__ == "__main__":
    print("PoC activa en http://127.0.0.1:8000")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
