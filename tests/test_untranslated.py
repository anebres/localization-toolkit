from toolkit.untranslated import find_untranslated

def test_find_untranslated():
    source = {
        "greet": "Hello",
        "bye": "Goodbye",
        "same": "Copy"
    }
    target = {
        "greet": "Bonjour",
        "bye": "",
        "same": "Copy"
    }
    expected = ["bye", "same"]
    assert find_untranslated(source, target) == expected