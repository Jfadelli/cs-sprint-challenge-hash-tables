def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    storage = {}

    for i in range(length):
        diff = limit - weights[i]
        # print('diff -> ', diff)
        current =  weights[i]
        # print('weights -> ', weights)
        if diff in storage:
            return (i, storage[diff])
        else:
            storage[current] = i
    return None
