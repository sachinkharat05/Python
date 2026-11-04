import threading

import pytest
from werkzeug.serving import make_server

from app import app, users


@pytest.fixture
def base_url():
    users.clear()
    server = make_server("127.0.0.1", 0, app, threaded=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join()
        server.server_close()
        users.clear()
