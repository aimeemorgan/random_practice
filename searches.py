# For each of these sorts:
#   * Bubble
#   * Insertion
#   * QuickSort
#   * Mergesort
# ...do the following:
#   * Implement the sort algorithm (just for array of integers)
#   * For each array lengths of 10, 100, 1000, 100,000, 1,000,000, and 100,000,000:
#     * Repeat 1,000 times:
#       * Generate an array of random integers of the current length
#       * Sort the array, timing how long it takes
#     * Average the 1,000 times
#   * Plot the results (i.e. 4 charts, with 6 data points each)
#     * Note: this can be Excel -- but bonus points for learning e.g. gnuplot or
#       a python plotting library

import time

def bubble(array):
    pass

def insertion(array):
    pass

def quicksort(array):
    pass

def mergesort(array):
    pass


def generate_array(n):
    ''' Generate and return an array of length n.'''
    pass

def test_sort(sort_function, m, n):
    '''Run m trials of the specified sort on arrays of size n. 
    Return average runtime.'''
    results = []
    for i in range(m):
        print "trial #%i" % i
        array = generate_array(n)
        start_time = time.clock()
        sort_function(array)
        end_time = time.clock()
        results.append(start_time-end_time)
    return sum(results) / float(len(results))

def plot_results(test_results):
    pass


if __name__ == "__main__":
    sorts = [bubble, insertion, quicksort, mergesort]
    array_lengths = [10,
                     100,
                     1000,
                     10000,
                     100000,
                     1000000,
                     100000000]
    for sort in sorts:
        results = []
        for length in array_length:



