from consoleffects import decorate
import pytest


def test_emptyformat():
    assert decorate('Test') == 'Test'


def test_bold():
    boldtext = decorate('Test', bold=True)
    assert boldtext[:4] == '\x1b[1m'
    assert boldtext[-4:] == '\x1b[0m'


def test_dim():
    dimtext = decorate('Test', dim=True)
    assert dimtext[:4] == '\x1b[2m'
    assert dimtext[-4:] == '\x1b[0m'


def test_it():
    ittext = decorate('Test', it=True)
    assert ittext[:4] == '\x1b[3m'
    assert ittext[-4:] == '\x1b[0m'


def test_uline():
    ulinetext = decorate('Test', uline=True)
    assert ulinetext[:4] == '\x1b[4m'
    assert ulinetext[-4:] == '\x1b[0m'


def test_blink():
    blinktext = decorate('Test', blink=True)
    assert blinktext[:4] == '\x1b[5m'
    assert blinktext[-4:] == '\x1b[0m'


def test_strike():
    striketext = decorate('Test', strike=True)
    assert striketext[:4] == '\x1b[9m'
    assert striketext[-4:] == '\x1b[0m'


def test_duline():
    dulinetext = decorate('Test', duline=True)
    assert dulinetext[:5] == '\x1b[21m'
    assert dulinetext[-4:] == '\x1b[0m'


def test_underline():
    assert decorate(
        'Test', uline=True, duline=True) == decorate('Test', uline=True)


def test_errorarg():
    with pytest.raises(TypeError):
        decorate('Test', True)


def test_combined():
    styled = decorate('Test', bold=True, uline=True)
    prefix = styled[0:6]
    assert '1' in prefix
    assert '4' in prefix
