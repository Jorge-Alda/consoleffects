import consoleffects


def test_emptyformat():
    assert consoleffects.decorate('Test') == 'Test'


def test_bold():
    boldtext = consoleffects.decorate('Test', bold=True)
    assert boldtext[:4] == '\x1b[1m'
    assert boldtext[-4:] == '\x1b[0m'


def test_dim():
    boldtext = consoleffects.decorate('Test', dim=True)
    assert boldtext[:4] == '\x1b[2m'
    assert boldtext[-4:] == '\x1b[0m'


def test_it():
    boldtext = consoleffects.decorate('Test', it=True)
    assert boldtext[:4] == '\x1b[3m'
    assert boldtext[-4:] == '\x1b[0m'


def test_uline():
    boldtext = consoleffects.decorate('Test', uline=True)
    assert boldtext[:4] == '\x1b[4m'
    assert boldtext[-4:] == '\x1b[0m'


def test_blink():
    boldtext = consoleffects.decorate('Test', blink=True)
    assert boldtext[:4] == '\x1b[5m'
    assert boldtext[-4:] == '\x1b[0m'


def test_strike():
    boldtext = consoleffects.decorate('Test', strike=True)
    assert boldtext[:4] == '\x1b[9m'
    assert boldtext[-4:] == '\x1b[0m'


def test_duline():
    boldtext = consoleffects.decorate('Test', duline=True)
    assert boldtext[:5] == '\x1b[21m'
    assert boldtext[-4:] == '\x1b[0m'
