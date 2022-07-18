# O(n^2+m) time | O(n+m) space
# n: length of string, m: length of pattern
def patternMatcher(pattern, string):
    if len(pattern) == 0 or len(pattern) > len(string):
        return []

    first_letter_a = pattern[0]
    # O(m) time
    amount_of_a, amount_of_b, first_idx_b = get_count_and_first_idx_of_b(
        first_letter_a, pattern
    )
    print(amount_of_a, amount_of_b, first_idx_b)
    if amount_of_b == 0:
        len_a = len(string) / amount_of_a
        if len_a % 1 == 0:
            string_a = string[: int(len_a)]
            match_string = "".join(
                map(
                    lambda char: string_a,
                    pattern,
                )
            )
            if string == match_string:
                return [string_a, ""] if first_letter_a == "x" else ["", string_a]
        return []
    else:
        # O(n) time
        for len_a in range(1, len(string)):
            len_b = (len(string) - len_a * amount_of_a) / amount_of_b
            if len_b <= 0 or len_b % 1 != 0:
                continue
            idx_b = first_idx_b * len_a
            string_a = string[:len_a]
            string_b = string[idx_b : idx_b + int(len_b)]
            print(len_b, len(string))
            print(string_a, string_b)
            # O(2n) time
            print(
                list(
                    map(
                        lambda char: string_a if char == first_letter_a else string_b,
                        pattern,
                    )
                )
            )
            match_string = "".join(
                map(
                    lambda char: string_a if char == first_letter_a else string_b,
                    pattern,
                )
            )
            print(match_string)
            if match_string == string:
                if first_letter_a == "x":
                    return [string_a, string_b]
                return [string_b, string_a]

    return []


def get_count_and_first_idx_of_b(first_letter_a, pattern):
    amount_of_a = 0
    amount_of_b = 0
    first_idx_b = -1
    for i in range(len(pattern)):
        if pattern[i] == first_letter_a:
            amount_of_a += 1
        else:
            amount_of_b += 1
            if first_idx_b == -1:
                first_idx_b = i

    return amount_of_a, amount_of_b, first_idx_b


pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"
print(patternMatcher(pattern, string))
