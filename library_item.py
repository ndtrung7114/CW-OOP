class LibraryItem:
    def __init__(self, name, director, rating=0, image_path=None):
        if name == '':
            raise ValueError('Name can not be empty')
        if director == '':
            raise ValueError('Director can not be empty')
        try:
            rating = int(rating)
        except ValueError:
            raise ValueError('Rating must be integer number')
        if rating < 1 or rating > 5:
            raise ValueError('Rating must be in range(1, 5)')
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
        self.image_path = image_path

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars



class LibraryItemEpisode(LibraryItem):
    def __init__(self, name, director, rating, episode_number, image_path=None):
        super().__init__(name, director, rating, image_path)

        self.play_count = 0
        self.episode_number = episode_number

    def info(self):
        return f"Episode {self.episode_number}: {self.name} -  {self.stars()}"
