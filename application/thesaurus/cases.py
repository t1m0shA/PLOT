from domain.thesaurus.services import WordService
from application.thesaurus.dtos import WordDTO
from pydantic import ValidationError

class CreateWordUseCase:
    """
    A class for creating word with examples, synonyms, definitions and sentences
    """
    def __init__(self, word_service: WordService):
        self.word_service = word_service

    def execute(self, word_data):
        try:
            validated_data = WordDTO(**word_data)
            return self.word_service.create_word(
                validated_data.word,
                validated_data.examples,
                validated_data.synonyms,
                validated_data.definitions_sentences
            )
        except ValidationError as ve:
            raise ValueError(str(ve))
        
class RetrieveWordUseCase:
    """
    A class for retrieving word with examples, synonyms, definitions and sentences
    """
    def __init__(self, word_service: WordService):
        self.word_service = word_service

    def execute(self, uuid, json_format=False):
        try:
            return self.word_service.retrieve_word(uuid, json_format)
        except Exception as ve:
            raise ValueError(str(ve))
        
class RemoveWordUseCase:
    """
    A class for removing word with examples, synonyms, definitions and sentences
    """
    def __init__(self, word_service: WordService):
        self.word_service = word_service

    def execute(self, uuid):
        try:
            self.word_service.delete_word(uuid)
        except Exception as e:
            raise ValueError(str(e))