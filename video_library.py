from library_item import LibraryItem, LibraryItemEpisode
import csv



library = {}

f = open('video.csv', 'r', encoding='utf-8')
reader = csv.reader(f)
next(reader)
now_index = 1
for row in reader:

    i = now_index
    library['0' + str(i)] = LibraryItem(row[0], row[1], row[2], row[3])
    now_index += 1


library_episode = {}

library_episode['01'] = [LibraryItemEpisode('nguyen', 'A', 3, 1), LibraryItemEpisode('duc', 'R', 3, 2)]
library_episode['02'] = [LibraryItemEpisode('nguyen', 'C', 3, 1), LibraryItemEpisode('thi', 'A', 3, 2)]



def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def list_episode(key):
    output = ''
    for episode in library_episode[key]:
        output += f'{episode.info()}\n'
    return output

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        raise KeyError(f'Can not found music with number: {key}')

def get_name_episode(key):
    try:
        item = library_episode[key]
        return item.name
    except KeyError:
        raise KeyError(f'Can not found music with number: {key}')


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        raise KeyError(f'Can not found director with number: {key}')

def get_director_episode(key):
    try:
        item = library_episode[key]
        return item.director
    except KeyError:
        raise KeyError(f'Can not found director with number: {key}')


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        raise KeyError('Invalid number')

def get_rating_episode(key):
    try:
        item = library_episode[key]
        return item.rating
    except KeyError:
        raise KeyError('Invalid number')


def update_csv():
    with open('video.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Director', 'Rating', 'ImagePath'])  # Header
        for key in library:
            item = library[key]
            writer.writerow([item.name, item.director, item.rating, item.image_path])


def set_rating(key, rating):
    try:
        rating = int(rating)
        if rating <= 0 or rating > 5:
            raise ValueError('Rating must be in the range of 1 to 5')

        try:
            item = library[key]
            item.rating = rating
            update_csv()
        except KeyError:
            raise KeyError('Invalid number')

    except ValueError:
        raise ValueError('Rating must be an integer number and in range(1,5)')

def set_rating_episode(key, rating):
    try:
        rating = int(rating)
        if rating <= 0 or rating > 5:
            raise ValueError('Rating must be in the range of 1 to 5')

        try:
            item = library_episode[key]
            item.rating = rating
            update_csv()
        except KeyError:
            raise KeyError('Invalid number')

    except ValueError:
        raise ValueError('Rating must be an integer number and in range(1,5)')


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        raise KeyError('Invalid number')

def get_play_count_episode(key):
    try:
        item = library_episode[key]
        return item.play_count
    except KeyError:
        raise KeyError('Invalid number')


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        raise KeyError('Invalid number')

def increment_play_count_episode(key):
    try:
        item = library_episode[key]
        item.play_count += 1
    except KeyError:
        raise KeyError('Invalid number')

def get_image_path(key):
    try:
        item = library[key]
        return item.image_path
    except KeyError:
        raise KeyError(f'Can not found image path for video with number: {key}')

def search_by_name(search_term):
    results = []
    for key in library:
        item = library[key]
        if search_term in item.name.lower():
            results.append(f"{key} {item.info()}")
    return "\n".join(results)

def view_by_director(search_term):
    results = []
    for key in library:
        item = library[key]
        if search_term in item.director.lower():
            results.append(f"{key} {item.info()}")
    return "\n".join(results)



