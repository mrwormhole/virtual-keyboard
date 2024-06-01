CHARS: dict[str, list[list[str]]] = {
    "UK": [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "← Backspace"],
        ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\"],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "↵ Enter"],
        ["⇧", "\\", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "Space"],
    ],
    "TH": [
        ["ๅ", "/", "-", "ภ", "ถ", "ุ", "ึ", "ค", "ต", "จ", "ข", "ช", "← Backspace"],
        ["ๆ", "ไ", "ำ", "พ", "ะ", "ั", "ี", "ร", "น", "ย", "บ", "ล", "ฃ"],
        ["ฟ", "ห", "ก", "ด", "เ", "้", "่", "า", "ส", "ว", "ง", "↵ Enter"],
        ["⇧", "ฃ", "ผ", "ป", "แ", "อ", "ิ", "ื", "ท", "ม", "ใ", "ฝ", "Space"],
    ],
    "TH_": [
        ["+", "๑", "๒", "๓", "๔", "ู", "฿", "๕", "๖", "๗", "๘", "๙", "← Backspace"],
        ["๐", '"', "ฎ", "ฑ", "ธ", "ํ", "๊", "ณ", "ฯ", "ญ", "ฐ", ",", "ฅ"],
        ["ฤ", "ฆ", "ฏ", "โ", "ฌ", "็", "๋", "ษ", "ศ", "ซ", ".", "↵ Enter"],
        ["⇧", "ฅ", "(", ")", "ฉ", "ฮ", "ฺ", "์", "?", "ฒ", "ฬ", "ฦ", "Space"],
    ],
    "TR": [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "-", "← Backspace"],
        ["q", "w", "e", "r", "t", "y", "u", "ı", "o", "p", "ğ", "ü", ","],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ş", "i", "↵ Enter"],
        ["⇧", "<", "z", "x", "c", "v", "b", "n", "m", "ö", "ç", ".", "Space"],
    ],
    "TR_": [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "-", "← Backspace"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Ğ", "Ü", ","],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ş", "İ", "↵ Enter"],
        ["⇧", "<", "Z", "X", "C", "V", "B", "N", "M", "Ö", "Ç", ".", "Space"],
    ],
}

ACTIONABLE_CHARS = ["← Backspace", "↵ Enter", "⇧", "Space"]
