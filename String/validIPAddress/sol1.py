# Since we know that the input size will be at most 12
# at most 2^32 ip address
# O(1) time | O(1) space


def validIPAddresses(string):
    result = []
    for i in range(1, min(len(string), 4)):
        current_ip_address = ["", "", "", ""]
        current_ip_address[0] = string[:i]
        print(current_ip_address[0])
        if not is_valid(current_ip_address[0]):
            continue
        for j in range(i + 1, i + min(len(string) - i, 4)):
            print(i, j)
            current_ip_address[1] = string[i:j]
            print(current_ip_address[1])
            if not is_valid(current_ip_address[1]):
                continue
            for k in range(j + 1, j + min(len(string) - j, 4)):
                current_ip_address[2] = string[j:k]
                print(current_ip_address[2])
                current_ip_address[3] = string[k:]
                print(current_ip_address[3])
                if is_valid(current_ip_address[2]) and is_valid(current_ip_address[3]):
                    result.append(".".join(current_ip_address))

    return result


def is_valid(string):
    int_string = int(string)
    if int_string > 255:
        return False
    return len(string) == len(str(int_string))


test = "1921680"
print(validIPAddresses(test))
