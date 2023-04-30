from bank_server import commands
from class_bankkonto import Account


def test_commands():
    message = Account("Mira", "privatkonto", "privatkonto", "123456789")
    register = []
    assert commands(message, register) == "Account added in register"


def test_commands_1():
    message = "2"
    register = [Account("Maja", "Privatkonto", "Privatkonto", "123456789")]
    assert commands(message, register) == register


def test_commands_2():
    message = "3#025874136"
    register = [
    Account("Maja", "Privatkonto", "Privatkonto", "123456789"),
    Account("Molly", "Privatkonto", "Privatkonto", "987456123"),
    Account("Linus", "Privatkonto", "Privatkonto", "025874136")
    ]
    assert commands(message, register) == f"Requested account: {Account('Linus', 'Privatkonto', 'Privatkonto', '025874136').__str__()}"
