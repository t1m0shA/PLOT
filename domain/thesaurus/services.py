
from domain.thesaurus.repository import WordRepository
from domain.thesaurus.entities import Word, Example, Synonym, Definition, Sentence
import json

class WordService:
    """
    Provides CRUD operations for word-management
    """
    def __init__(
        self, 
        word_repo: WordRepository
        
    ) -> None:
        self.word_repo = word_repo
        

    def create_word(
        self, 
        word_text: str, 
        examples: list[str], 
        synonyms: list[str], 
        definitions_sentences: dict[str, list[str]]
    ):
        """
        Create a word with all its examples, synonyms, definitions and sentences
        """
        word = Word(word=word_text)
        for ex in examples:
            example = Example(example=ex)
            word.add_example(example)
        for syn in synonyms:
            synonym = Synonym(synonym=syn)
            word.add_synonym(synonym)
        for defin, sentences in definitions_sentences.items():
            definition = Definition(definition=defin)
            for sen in sentences:
                sentence = Sentence(sentence=sen)
                definition.add_sentence(sentence)
            word.add_definition(definition)
        self.word_repo.create(word)
        return word
    
    def retrieve_word(self, word_uuid: str, json_format=False):
        """
        Get a word with its examples, synonyms, definitions and sentences
        """
        word = self.word_repo.retrieve(word_uuid)
        if json_format:
            return json.loads(word.model_dump_json())
        return word
    
    def update_word(self, word_uuid: str, new: str):
        """
        Modify the text of a word
        """
        word = self.word_repo.retrieve(word_uuid)
        self.word_repo.modify_value(word, new)
        word.word = new
        return word

    def delete_word(self, word_uuid: str):
        """
        Delete a word and all its examples, synonyms, definitions and sentences
        """
        word = self.word_repo.retrieve(word_uuid)
        self.word_repo.remove(word)
        return word



