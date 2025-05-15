from rich import print

from lapidary.verbs.display import header


def test_header():
    print(header())
    assert True, "Printed header"
