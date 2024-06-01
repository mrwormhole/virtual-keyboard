import pytest

from characters import CHARS, find_mapped_char


def test_characters_layout_len():
    layout_lens: dict[str, str] = {}  # "UK" -> "13-12-13-13"
    for language, keyboard_layout in CHARS.items():
        for i, row in enumerate(keyboard_layout):
            if layout_lens.get(language) is None:
                layout_lens[language] = str(len(row))
            else:
                layout_lens[language] += "-" + str(len(row))
    want_layout_len: str = layout_lens.get("UK")
    for language, layout_len in layout_lens.items():
        assert want_layout_len == layout_len


def test_find_mapped_char():
    assert find_mapped_char("k", "TH") == "า"
    assert find_mapped_char("'", "TH") == "ง"
    assert find_mapped_char(";", "TH_") == "ซ"
    assert find_mapped_char("\\", "TH_") == "ฅ"

    assert find_mapped_char(";", "TR") == "ş"
    assert find_mapped_char("\\", "TR") == ","
    assert find_mapped_char("'", "TR_") == "İ"
    assert find_mapped_char(".", "TR_") == "Ç"


if __name__ == "__main__":
    pytest.main()
