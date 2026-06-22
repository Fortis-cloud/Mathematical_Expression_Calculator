import logging
import pytest
from calculator import calculator

def test_verbose_logging(caplog):
    caplog.set_level(logging.DEBUG)
    result = calculator("2+3*4", verbose=True)
    assert result == 14
    assert caplog.records
    # Проверяем, что есть записи с op=* и op=+
    ops = [rec.getMessage() for rec in caplog.records]
    assert any("op=*" in msg for msg in ops)
    assert any("op=+" in msg for msg in ops)
