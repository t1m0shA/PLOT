from pydantic import Field
from typing import List
from domain.thesaurus.validation import StringValidationMixin
from uuid import uuid4

class Sentence(StringValidationMixin):
    """
    Represent a sentence for the definition
    """
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    sentence: str = Field(..., min_length=1)

class Definition(StringValidationMixin):
    """
    Represent a definition for the word
    """
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    definition: str
    sentences: List[Sentence] = Field(default_factory=list)
    
    def add_sentence(self, sentence: Sentence):
        if sentence in self.sentences:
            raise ValueError(
                f"Sentence {sentence.sentence} already exists for definition {self.definition}."
            )
        self.sentences.append(sentence)

class Example(StringValidationMixin):
    """
    Represent an example for the word
    """
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    example: str

class Synonym(StringValidationMixin):
    """
    Represent a synonym for the word
    """
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    synonym: str

class Word(StringValidationMixin):
    """
    Represent a word
    """
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    word: str
    definitions: List[Definition] = Field(default_factory=list)
    examples: List[Example] = Field(default_factory=list)
    synonyms: List[Synonym] = Field(default_factory=list)

    def add_definition(self, definition: Definition):
        if definition in self.definitions:
            raise ValueError(
                f"Definition {definition.definition} already exists for word {self.word}."
            )
        self.definitions.append(definition)

    def add_example(self, example: Example):
        if example in self.examples:
            raise ValueError(
                f"Example {example.example} already exists for word {self.word}."
            )
        self.examples.append(example)
        
    def add_synonym(self, synonym: Synonym):
        if synonym.synonym.lower() == self.word.lower():
            raise ValueError(f"A word {self.word} cannot be its own synonym.")
        if synonym in self.synonyms:
            raise ValueError(
                f"Synonym {synonym.synonym} already exists for word {self.word}."
            )
        self.synonyms.append(synonym)

# word = Word(word="Come")

# definition_1 = Definition(definition="Come word definition 1")
# sentence_1_1 = Sentence(sentence="Sentence 1 for Come definition 1")
# definition_1.add_sentence(sentence_1_1)

# definition_2 = Definition(definition="Come word definition 2")
# sentence_2_1 = Sentence(sentence="Sentence 1 for Come definition 2")
# sentence_2_2 = Sentence(sentence="Sentence 2 for Come definition 2")
# definition_2.add_sentence(sentence_2_1)
# definition_2.add_sentence(sentence_2_2)

# word.add_definition(definition_1)
# word.add_definition(definition_2)

# synonym_1 = Synonym(synonym="Ssssss")
# word.add_synonym(synonym_1)

# example = Example(example="Example for word Come")
# word.add_example(example)

# print(word.model_dump_json())