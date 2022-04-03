# O(4^n * n) time | O(4^n * n) space
def phoneNumberMnemonics(phoneNumber):
    mnemonicFound = []
    currentMnemonic = ["0"] * len(phoneNumber)
    helper(0, phoneNumber, currentMnemonic, mnemonicFound)

    return mnemonicFound


def helper(idx, phoneNumber, currentMnemonic, mnemonicFound):
    print(idx)
    if idx == len(phoneNumber):
        mneonic = "".join(currentMnemonic)
        mnemonicFound.append(mneonic)
    else:
        letters = phone_letters[phoneNumber[idx]]
        for letter in letters:
            print(currentMnemonic)
            currentMnemonic[idx] = letter

            helper(idx + 1, phoneNumber, currentMnemonic, mnemonicFound)


phone_letters = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}
