def merge(n1, n2):
    # the lists of numbers must be sorted for arithmetic comparison
    n1s = sorted(n1)
    n2s = sorted(n2)

    # my algo requires that we loop through the larger list
    if len(n1s) >= len(n2s):
        return combine(n1s, n2s)
    else:
        return combine(n2s, n1s)

def combine(l1, l2):
    """Loop through the larger list.
    Compare the current l1 value with the value in position item of l2.

    Add the l1 value if it is lte or, there are no more l2 values.
    Add the l2 value otherwise.
    """
    item = 0
    interlace = []

    for num in l1:
        less_than = True
        while less_than:
            if num in interlace: 
                continue
            else:
                if item < len(l2):
                    if num < l2[item]:
                        interlace.append(num)
                        less_than = False
                    elif num == l2[item]:
                        interlace.append(num)
                        item += 1
                        less_than = False
                    else:
                        interlace.append(l2[item])
                        item += 1
                else:
                    interlace.append(num)
                    less_than = False

    interlace.extend(l2[item:])

    return interlace
