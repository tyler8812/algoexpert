# O(nlog(n)) time | O(1) space
# sort: O(nlog(n)) time
def classPhotos(redShirtHeights, blueShirtHeights):
    sort_red_shirt = sorted(redShirtHeights)
    sort_blue_shirt = sorted(blueShirtHeights)
    is_red_last = sort_red_shirt[0] > sort_blue_shirt[0]
    print(sort_red_shirt, sort_blue_shirt)
    if is_red_last:
        for idx in range(len(sort_red_shirt)):
            if sort_red_shirt[idx] <= sort_blue_shirt[idx]:
                return False
    else:
        for idx in range(len(sort_red_shirt)):
            if sort_blue_shirt[idx] <= sort_red_shirt[idx]:
                return False

    return True
