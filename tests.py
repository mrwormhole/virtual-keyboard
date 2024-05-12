import pytest
from characters import CHARACTERS


def test_characters_layout_len():
    layout_lens: dict[str, str] = {}  # "UK" -> "13-12-13-13"
    for language, keyboard_layout in CHARACTERS.items():
        for i, row in enumerate(keyboard_layout):
            if layout_lens.get(language) is None:
                layout_lens[language] = str(len(row))
            else:
                layout_lens[language] += "-" + str(len(row))
    want_layout_len: str = layout_lens.get("UK")
    for language, layout_len in layout_lens.items():
        assert want_layout_len == layout_len


if __name__ == "__main__":
    pytest.main()
