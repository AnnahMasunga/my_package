
"""Return the top n item in an array , in descending order.

Args: 
    items(array): list or array-like object
    n(int):num of items to return

Return:
    array: top n item , in decending order

Egs:
     >>>top-n([8 , 3 , 2 , 7, 4], 3)
     [8,7,3]


"""
def top_n(items, n):
    """
    docstring goes here
    """

    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # If this item is bigger than next the item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!

    # Get last two items
    top_n = items[-n:]

    # Return in descending order
    return top_n[::-1]
