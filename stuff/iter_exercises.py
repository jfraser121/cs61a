# iter_exercises
# import doctest

def lowest_abs(s):
    """
    Returns the indices of all elements in s with the lowest absolute value.
    >>> lowest_abs([10, 2, 5, -2])
    [1, 3]
    >>> lowest_abs([4, 3, 2, 10, 0, 0])
    [4, 5]
    """
    # indices = []
    # lowest_abs = float('inf')
    # for i, elem in enumerate(s):
    #     if abs(elem) < lowest_abs:
    #         indices = [i]
    #         lowest_abs = abs(elem)
    #     elif abs(elem) == lowest_abs:
    #         indices.append(i)
    # return indices

    # ^^^ my solution v boring and sad
    # 2 liner from mr. denero --- damn he good
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

def max_adj(s):
    """
    Returns the maximum sum of two adjacent elements in s. You may assume len(s) > 1
    >>> max_adj([0, 1, 2, 3, 4, 5])
    9
    >>> max_adj([10, -5, 15, 5, -10])
    20
    """
    # max_sum = -float('inf')
    # for i in range(len(s[:-1])):
    #     adj_sum = s[i] + s[i+1]    # sum(s[i], s[i+1]) doesn't work as sum expects iterable as first arg, starting point as 2nd.
    #     if adj_sum > max_sum:       # so sum([s[i], s[i+1]]) would work but isn't very readable
    #         max_sum = adj_sum
    # return max_sum

    # my lame solution ^^^ vvv John's dope solution
    return max([s[i] + s[i+1] for i in range(len(s) - 1)])  # this is most comfy / intuitive right now

    # another dope fun solution
    # return max([a + b for a, b in zip(s[:-1], s[1:])])

def final_dig_dict(s):
    """
    Creates a dictionary mapping each digit d to the lists of elements in s that end with d.
    >>> final_dig_dict([5, 8, 15, 10])
    {0: [10], 5: [5, 15], 8: [8]}
    """
    # digit_dict = {}
    # for d in range(10):
    #     for elem in s:
    #         if elem % 10 == d:
    #             if d not in digit_dict:
    #                 digit_dict[d] = [elem]
    #             else:
    #                 digit_dict[d].append(elem)
    # return digit_dict

    # you know the drill by now lol. both of the below work, bottom is John's, 2nd from is mine. end is diff.
    # both prety dang long, could split last list comprehension into var called last_digits or whatever.
    # also sorta has the logic the other way around i think? like outer loop vs inner loop reversed.

    return {d: [x for x in s if x % 10 == d] for d in range(10) if d in [z % 10 for z in s]}
    # return {d: [x for x in s if x % 10 == d] for d in range(10) if any([z % 10 == d for z in s])}

def friendly_elems(s):
    """
    Returns True if every element in s equals some other element in s. Otherwise returns False
    >>> friendly_elems([1, 2, 3, 3, 2, 1])
    True
    >>> friendly_elems([1, 5, 6, -1, 5, 10])
    False
    """
    # for i, target in enumerate(s):
    #     friend = False
    #     for j, other in enumerate(s):
    #         if i != j:
    #             if target == other:
    #                 friend = True
    #     if not friend:
    #         return friend
    # return friend

    # dope as hell lol
    # return all([s[i] in s[:i]+s[i+1:] for i in range(len(s))])
    return min(s.count(x) for x in s) > 1


