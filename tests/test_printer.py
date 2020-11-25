from greeting import printer
from unittest import mock


def test_hello(capsys):
    printer.hello()

    captured = capsys.readouterr()

    assert captured.out == "hello\n"


@mock.patch('greeting.generator.hello')
def test_mocked_hello(mocked, capsys):
    mocked.return_value = '...'

    printer.hello()

    captured = capsys.readouterr()

    assert captured.out == "...\n"
