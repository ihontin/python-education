"""quick_sort """

# from random import randint


def quick_sort(sortlist):
    """
    Quick-sort algorithm.
    """
    index_list = list()
    two_indx = (0, len(sortlist) - 1)
    index_list.append(two_indx)
    for two_indx in index_list:
        val_indx = two_indx[0]
        base_indx = two_indx[1]
        while base_indx > val_indx:
            base = sortlist[base_indx]
            value = sortlist[val_indx]
            if value > base:
                sortlist[base_indx] = value
                sortlist[val_indx] = sortlist[base_indx - 1]
                sortlist[base_indx - 1] = base
                base_indx -= 1
            else:
                val_indx += 1
        boundar_low = two_indx[0]
        boundar_high = two_indx[1]
        if base_indx > 1 and boundar_low < base_indx - 1:
            index_list.append((boundar_low, base_indx - 1))
        if base_indx < len(sortlist) - 1 and base_indx + 1 < boundar_high:
            index_list.append((base_indx + 1, boundar_high))

    return sortlist


# a = [randint(1, 100) for i in range(15)]
# b = quick_sort(a)
