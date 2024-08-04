BACKSPACE = "← Backspace"
ENTER = "↵ Enter"
SHIFT = "⇧ Shift"
SPACE = "␣ Space"

CHARS: dict[str, list[list[str]]] = {
    "UK": [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", BACKSPACE],
        ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\"],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", ENTER],
        [SHIFT, "\\", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", SPACE],
    ],
    "TH": [
        ["ๅ", "/", "-", "ภ", "ถ", "ุ", "ึ", "ค", "ต", "จ", "ข", "ช", BACKSPACE],
        ["ๆ", "ไ", "ำ", "พ", "ะ", "ั", "ี", "ร", "น", "ย", "บ", "ล", "ฃ"],
        ["ฟ", "ห", "ก", "ด", "เ", "้", "่", "า", "ส", "ว", "ง", ENTER],
        [SHIFT, "ฃ", "ผ", "ป", "แ", "อ", "ิ", "ื", "ท", "ม", "ใ", "ฝ", SPACE],
    ],
    "TH_": [
        ["+", "๑", "๒", "๓", "๔", "ู", "฿", "๕", "๖", "๗", "๘", "๙", BACKSPACE],
        ["๐", '"', "ฎ", "ฑ", "ธ", "ํ", "๊", "ณ", "ฯ", "ญ", "ฐ", ",", "ฅ"],
        ["ฤ", "ฆ", "ฏ", "โ", "ฌ", "็", "๋", "ษ", "ศ", "ซ", ".", ENTER],
        [SHIFT, "ฅ", "(", ")", "ฉ", "ฮ", "ฺ", "์", "?", "ฒ", "ฬ", "ฦ", SPACE],
    ],
    "TR": [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "-", BACKSPACE],
        ["q", "w", "e", "r", "t", "y", "u", "ı", "o", "p", "ğ", "ü", ","],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ş", "i", ENTER],
        [SHIFT, ",", "z", "x", "c", "v", "b", "n", "m", "ö", "ç", ".", SPACE],
    ],
    "TR_": [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "-", BACKSPACE],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Ğ", "Ü", ";"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ş", "İ", ENTER],
        [SHIFT, ";", "Z", "X", "C", "V", "B", "N", "M", "Ö", "Ç", ":", SPACE],
    ],
}


def find_mapped_char(char: str, language: str) -> str:
    chars: list[list[str]] = CHARS["UK"]
    for i in range(len(chars)):
        for j in range(len(chars[i])):
            if chars[i][j] == char:
                return CHARS[language][i][j]
    return ""


def char_location(char: str) -> tuple[int, int] | None:
    chars: list[list[str]] = CHARS["UK"]
    for i in range(len(chars)):
        for j in range(len(chars[i])):
            if chars[i][j] == char:
                return i, j
    return None
