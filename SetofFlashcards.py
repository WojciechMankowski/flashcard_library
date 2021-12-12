from Flashcard import Flashcard


class SetOfFlashcards:

    def __init__(self, name_set: str, id_user, description: str= None, image: str=None) -> None:
        self.name_set = name_set
        self.id_user = id_user
        self.description = description
        self.image = image
        id_set = 0
        self.set_flashcards: list[Flashcard] = []

    def Add_flashcard(self, flashcard: Flashcard) -> None:
        self.set_flashcards.append(flashcard)

    def __str__(self):
        return self.name_set


