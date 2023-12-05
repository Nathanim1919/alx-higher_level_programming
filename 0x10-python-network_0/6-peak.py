# a function that finds  apeak in alist of unsorted integers

def find_peak(list_of_integers):
    list_length = len(list_of_integers)

    for (i in range(1, list_lenght - 1)):
        if (list_of_integers[i - 1] <= list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]
