from sqlalchemy.orm import Session, joinedload
from domain.thesaurus.entities import Word, Example, Synonym, Definition, Sentence
from infrastructure.models.thesaurus import (
    WordModel, 
    ExampleModel, 
    SynonymModel, 
    DefinitionModel, 
    SentenceModel, 
)
from domain.thesaurus.repository import WordRepository

class SQLAlchemyWordRepository(WordRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, entity):
        word_model = WordModel(uuid=entity.uuid, word=entity.word)
        for ex in entity.examples:
            example_model = self.session.query(ExampleModel).filter_by(uuid=ex.uuid).first()
            if not example_model:
                example_model = ExampleModel(uuid=ex.uuid, example=ex.example)
            word_model.examples.append(example_model)
        for syn in entity.synonyms:
            synonym_model = self.session.query(SynonymModel).filter_by(uuid=syn.uuid).first()
            if not synonym_model:
                synonym_model = SynonymModel(uuid=syn.uuid, synonym=syn.synonym)
            word_model.synonyms.append(synonym_model)
        for defin in entity.definitions:
            definition_model = self.session.query(DefinitionModel).filter_by(uuid=defin.uuid).first()
            if not definition_model:
                definition_model = DefinitionModel(uuid=defin.uuid, definition=defin.definition)
            for sen in defin.sentences:
                sentence_model = self.session.query(SentenceModel).filter_by(uuid=sen.uuid).first()
                if not sentence_model:
                    sentence_model = SentenceModel(uuid=sen.uuid, sentence=sen.sentence)
                if sentence_model not in definition_model.sentences:
                    definition_model.sentences.append(sentence_model)
            word_model.definitions.append(definition_model)
        self.session.add(word_model)
        self.session.commit()

    def retrieve(self, uuid):
        validated_uuid = str(uuid)
        definitions = []
        word = self.session.query(WordModel).options(
            joinedload(WordModel.examples),
            joinedload(WordModel.synonyms),
            joinedload(WordModel.definitions).joinedload(DefinitionModel.sentences)
        ).filter(WordModel.uuid == validated_uuid).one()
        for definition in word.definitions:
            d = Definition(uuid=definition.uuid, definition=definition.definition) 
            sentences = definition.sentences
            for sentence in sentences:
                s = Sentence(uuid=sentence.uuid, sentence=sentence.sentence)
                d.add_sentence(s)
            definitions.append(d)
        return Word(
            uuid=word.uuid,
            word=word.word,
            examples=[Example(uuid=ex.uuid, example=ex.example) for ex in word.examples],
            synonyms=[Synonym(uuid=syn.uuid, synonym=syn.synonym) for syn in word.synonyms],
            definitions=[definition for definition in definitions]
        )
        
    def remove(self, entity):
        word = self.session.query(WordModel).filter_by(uuid=entity.uuid).first()
        if word:
            self.session.delete(word)
            self.session.commit()

    def modify(self, old, new):
        pass
        
        
        