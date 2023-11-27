from library_item import LibraryItem


def test_library_item_creation_valid():

    item = LibraryItem('Movie Name', 'Director', 3)
    assert item.name == 'Movie Name'
    assert item.director == 'Director'
    assert item.rating == 3
    assert item.play_count == 0

def test_library_item_creation_invalid_name():
    try:
        item = LibraryItem('', 'Director', 3)
    except ValueError as err:
        assert str(err) == 'Name can not be empty'




def test_library_item_creation_invalid_director():
    try:
        item = LibraryItem('Movie Name', '', 3)
    except ValueError as err:
        assert str(err) == 'Director can not be empty'

def test_library_item_creation_invalid_rating_type():
    try:
        item = LibraryItem('Movie Name', 'Director', 'four')
    except ValueError as err:
        assert str(err) == 'Rating must be integer number'

def test_library_item_creation_invalid_rating_range_low():
    try:
        item = LibraryItem('Movie Name', 'Director', 0)
    except ValueError as err:
        assert str(err) == 'Rating must be in range(1, 5)'

def test_library_item_creation_invalid_rating_range_high():
    try:
        item = LibraryItem('Movie Name', 'Director', 6)
    except ValueError as err:
        assert str(err) == 'Rating must be in range(1, 5)'

def test_library_item_info():
    item = LibraryItem("Movie Name", "Director", 3)
    assert item.info() == "Movie Name - Director ***"