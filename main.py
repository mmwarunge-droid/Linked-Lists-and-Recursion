from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    ll = LinkedList()
    

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)

    # TODO: 3) Display the list to verify insertion
    ll.display()

    # TODO: 4) Call recursive_sum and print the result
    print("Sum:", ll.recursive_sum())

    # TODO: 5) Call recursive_search with a target and print result
    print("Search 2:", ll.recursive_search(2))
    print("Search 4:", ll.recursive_search(4))

    # TODO: 6) Call recursive_reverse, then display the reversed list
    ll.recursive_reverse()
    ll.display()

    


# 