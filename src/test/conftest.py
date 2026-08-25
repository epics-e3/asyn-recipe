import logging
import socket
import threading
from collections.abc import Iterator
from pathlib import Path

import pytest
from p4p.client.thread import Context
from run_iocsh import IOC

LOG = logging.getLogger(__name__)

TEST_DIR = Path(__file__).absolute().parent
STARTUP_CMD = TEST_DIR / "ioc" / "st.cmd"

# Must match the port in ioc/st.cmd.
ECHO_HOST = "127.0.0.1"
ECHO_PORT = 37681


class EchoServer:
    """Byte-echo TCP peer for drvAsynIPPort."""

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self._sock: socket.socket | None = None
        self._thread: threading.Thread | None = None
        self._stop = threading.Event()

    def start(self) -> None:
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind((self.host, self.port))
        self._sock.listen(5)
        self._sock.settimeout(0.5)
        self._thread = threading.Thread(target=self._serve, daemon=True)
        self._thread.start()

    def _serve(self) -> None:
        assert self._sock is not None
        while not self._stop.is_set():
            try:
                conn, _addr = self._sock.accept()
            except TimeoutError:
                continue
            with conn:
                self._echo_client(conn)

    def _echo_client(self, conn: socket.socket) -> None:
        conn.settimeout(0.5)
        while not self._stop.is_set():
            try:
                data = conn.recv(4096)
            except TimeoutError:
                continue
            if not data:
                return
            conn.sendall(data)

    def stop(self) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=5)
        if self._sock is not None:
            self._sock.close()


@pytest.fixture(scope="module")
def echo_server() -> Iterator[EchoServer]:
    server = EchoServer(ECHO_HOST, ECHO_PORT)
    server.start()
    yield server
    server.stop()


@pytest.fixture(scope="module")
def ioc(echo_server: EchoServer) -> Iterator[IOC]:  # noqa: ARG001
    with IOC.ready(STARTUP_CMD.as_posix()) as running_ioc:
        yield running_ioc
        LOG.error("IOC output:\n%s", running_ioc.output)


@pytest.fixture(scope="module")
def ctxt(ioc: IOC) -> Iterator[Context]:  # noqa: ARG001
    with Context("pva") as context:
        yield context
