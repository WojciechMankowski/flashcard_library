from dataclasses import dataclass

@dataclass
class Flashcard:
    concept: str
    definition: str

    def getConcept(self) -> str:
        return self.concept

    def getDefinition(self) -> str:
        return self.definition

    def __str__(self):
        return self.concept + " -> " + self.definition

