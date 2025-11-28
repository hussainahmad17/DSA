# intuition is that we have to find the largest index(larger value) and then swap with index
def heapifyDown(self,array,ind):
    n=len(array)
    largest_ind = ind

    leftchild_ind = 2 * ind + 1
    rightchild_ind = 2 * ind + 2

    # check if leftchild_ind is in tree and leftchild_ind vlaue is greater than index value

    if leftchild_ind < n and array[leftchild_ind] > array[largest_ind]:
        largest_ind = leftchild_ind

    # check if rightchild_ind is in tree and rightchild_ind vlaue is greater than index value

    if rightchild_ind < n and array[rightchild_ind] > array[largest_ind]:
        largest_ind = rightchild_ind


    if largest_ind != ind:
        array[largest_ind],array[ind] = array[ind],array[largest_ind]
        self.heapifyDown(array,largest_ind)