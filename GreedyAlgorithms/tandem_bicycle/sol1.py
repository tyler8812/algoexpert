# O(NlogN) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    answer = 0
    if fastest:
        for i in range(len(redShirtSpeeds)):
            answer += max(
                redShirtSpeeds[i], blueShirtSpeeds[len(blueShirtSpeeds) - i - 1]
            )
    else:
        for i in range(len(redShirtSpeeds)):
            answer += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return answer
