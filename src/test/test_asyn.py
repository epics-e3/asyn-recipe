from enum import IntEnum

from p4p.client.thread import Context
from run_iocsh import wait_for

# Macros passed to asynRecord.db in st.cmd.
ASYN_PORT = "ECHO"
RECORD_ADDR = 0
RECORD_OMAX = 80
RECORD_IMAX = 80

WRITE_READ_PAYLOAD = "hello asyn"
ASYN_RECORD_PAYLOAD = "asynRecord ping"


class ConnectState(IntEnum):
    DISCONNECT = 0
    CONNECT = 1


def test_asyn_record_template_macros(ctxt: Context) -> None:
    assert ctxt.get("TEST:asyn1.PORT") == ASYN_PORT
    assert ctxt.get("TEST:asyn1.ADDR") == RECORD_ADDR
    assert ctxt.get("TEST:asyn1.OMAX") == RECORD_OMAX
    assert ctxt.get("TEST:asyn1.IMAX") == RECORD_IMAX


def test_asyn_record_port_is_connected(ctxt: Context) -> None:
    assert ctxt.get("TEST:asyn1.CNCT") == ConnectState.CONNECT
    assert ctxt.get("TEST:asyn1.OCTETIV") == 1


def test_asyn_record_write_read_echo(ctxt: Context) -> None:
    ctxt.put("TEST:asyn1.AOUT", ASYN_RECORD_PAYLOAD)
    wait_for(lambda: ctxt.get("TEST:asyn1.TINP") == ASYN_RECORD_PAYLOAD)


def test_stringin_octet_write_read_echo(ctxt: Context) -> None:
    ctxt.put("TEST:Cmd", WRITE_READ_PAYLOAD)
    wait_for(lambda: ctxt.get("TEST:Reply") == WRITE_READ_PAYLOAD)
