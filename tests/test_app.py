import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import urlopen
from app import Handler


class APITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_health(self):
        with urlopen(self.base + "/health", timeout=5) as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(json.load(response), {"status": "ok"})

    def test_home(self):
        with urlopen(self.base + "/", timeout=5) as response:
            self.assertEqual(response.headers.get_content_type(), "application/json")
            self.assertEqual(json.load(response)["empresa"], "CodeFactory Solutions")

    def test_missing_route(self):
        with self.assertRaises(HTTPError) as context:
            urlopen(self.base + "/inexistente", timeout=5)
        with context.exception as response:
            self.assertEqual(response.code, 404)
            self.assertEqual(json.load(response), {"erro": "Rota inexistente"})
