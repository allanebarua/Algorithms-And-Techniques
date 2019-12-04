from algorithms.insertion_sort import do_insertion_sort


def test_do_insertion_sort():
    # Already sorted list
    elements = [1,2,3,4,5]
    do_insertion_sort(elements)
    # do_insertion_sort takes a mutable object as an argument and
    # modifies it.
    assert elements == [1,2,3,4,5]

    # Shuffle elements
    elements = [1,3,2,5,4]
    do_insertion_sort(elements)
    assert elements == [1,2,3,4,5]
