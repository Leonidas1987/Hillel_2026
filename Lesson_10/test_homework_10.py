import logging
from homework_10 import log_event


def test_log_event_success(caplog):
    with caplog.at_level(logging.INFO, logger="log_event"):
        log_event("Leon", "success")

    assert "Username: Leon, Status: success" in caplog.text
    assert caplog.records[-1].levelno == logging.INFO


def test_log_event_expired(caplog):
    with caplog.at_level(logging.WARNING, logger="log_event"):
        log_event("Leon", "expired")

    assert "Username: Leon, Status: expired" in caplog.text
    assert caplog.records[-1].levelno == logging.WARNING


def test_log_event_failed(caplog):
    with caplog.at_level(logging.ERROR, logger="log_event"):
        log_event("Leon", "failed")

    assert "Username: Leon, Status: failed" in caplog.text
    assert caplog.records[-1].levelno == logging.ERROR