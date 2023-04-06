def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights = sorted(redShirtHeights, reverse=True)
    blueShirtHeights = sorted(blueShirtHeights, reverse=True)
    if len(redShirtHeights) != len(blueShirtHeights):
        return False
    if redShirtHeights:
        firstRowColor = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
        for idx in range(len(redShirtHeights)):
            if firstRowColor == "RED":
                if redShirtHeights[idx] >= blueShirtHeights[idx]:
                    return False
            else:
                if blueShirtHeights[idx] >= redShirtHeights[idx]:
                    return False
    return True


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest:
        redShirtSpeeds = sorted(redShirtSpeeds)
        blueShirtSpeeds = sorted(blueShirtSpeeds, reverse=True)
    else:
        redShirtSpeeds = sorted(redShirtSpeeds)
        blueShirtSpeeds = sorted(blueShirtSpeeds)
    totalSpeed = 0
    for idx, r in enumerate(redShirtSpeeds):
        totalSpeed += max(r, blueShirtSpeeds[idx])

    return totalSpeed


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    p = linkedList
    while p and p.next:
        if p.value == p.next.value:
            p.next = p.next.next
        else:
            p = p.next

    return linkedList


def getNthFib(n):
    # Write your code here.
    if n <= 1:
        return n-1
    prev = 0
    curr = 1
    for _ in range(2, n):
        prev, curr = curr, prev + curr
    return curr


def productSum(array):
    # Write your code here.
    def helper(arr, depth = 1):
        sum = 0
        for ele in arr:
            if isinstance(ele, list):
                sum += (depth + 1) * helper(ele, depth + 1)
            else:
                sum += ele
        return sum
    return helper(array)



if __name__ == '__main__':
    b = [6, 9, 2, 4, 5]
    r = [5, 8, 1, 3, 4]

    print(classPhotos(r, b))
