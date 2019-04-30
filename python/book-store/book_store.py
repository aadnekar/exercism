def calculate_total(books):
    """ Two base cases: either zero books or one book """
    if len(books) == 0:
        return 0
    elif len(books) == 1:
        return 800

    # books = sorted(books)
    book_dict = {}
    for _ in range(1, 6):
        book_dict[_] = books.count(_)
    
    # No discount for any of the books.
    price = 800 * len(books)
    
    for _ in range(2, 6):
        # Have to initiate a new dictionary each time, or else it changes the values in the ordinary dictionary.
        temp_dict = book_dict.copy()
        temp = iterate_purchase(_, temp_dict)
        price = min(temp, price)

    return price

def calculate_subtotal(num_books):
    """ returns the price of the number of books being purchased with the
        the discount accounted for. """
    discount = [0, 1, 0.95, 0.90, 0.80, 0.75]
    return 800 * num_books * discount[num_books]

def iterate_purchase(max_books_discount, book_dict):
    ''' Greedy method:
        Sort the list in descending order
        Calculate the price every time you reach max_books_discount or there are no more unique books
        Iterate until there are no books left '''
    price = 0
    while sum(book_dict.values()) > 0:
        num_books = 0
        for key, value in sorted(book_dict.items(), key = lambda book_dict: book_dict[1], reverse=True):
            if value > 0:
                num_books += 1
                book_dict[key] -= 1
            if num_books == max_books_discount:
                break
        price += calculate_subtotal(num_books)
    return price