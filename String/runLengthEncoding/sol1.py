def runLengthEncoding(string):
    # Write your code here.
    if string == "":
        return ""
    output = ""
    prev = ""
    count = 1
    for char in string:
        if prev != '':
            if prev == char:
                if count == 9:
                    output += "9" + char
                    count = 1
                else:
                    count += 1
            else:
                output += str(count) + prev
                count = 1
        prev = char
    output += str(count) + prev
    return output
