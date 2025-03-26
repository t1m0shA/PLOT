from sqlalchemy import Column, String, Table, ForeignKey, Integer
from sqlalchemy.orm import relationship
from uuid import uuid4
from infrastructure.models.base import Base

class WordModel(Base):
    __tablename__ = 'words'
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    word = Column(String(255), nullable=False)
    examples = relationship('ExampleModel', secondary='word_example', back_populates='words', cascade='all, delete')
    synonyms = relationship('SynonymModel', secondary='word_synonym', back_populates='words', cascade='all, delete')
    definitions = relationship('DefinitionModel', secondary='word_definition', back_populates='words', cascade='all, delete')

class SynonymModel(Base):
    __tablename__ = 'synonyms'
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    synonym = Column(String(255), nullable=False)
    words = relationship('WordModel', secondary='word_synonym', back_populates='synonyms')

WordSynonymModel = Table(
    'word_synonym',
    Base.metadata,
    Column('word_uuid', String(36), ForeignKey('words.uuid')),
    Column('synonym_uuid', String(36), ForeignKey('synonyms.uuid'))
)

class ExampleModel(Base):
    __tablename__ = 'examples'
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    example = Column(String(255), nullable=False)
    words = relationship('WordModel', secondary='word_example', back_populates='examples')
    
WordExampleModel = Table(
    'word_example',
    Base.metadata,
    Column('word_uuid', String(36), ForeignKey('words.uuid')),
    Column('example_uuid', String(36), ForeignKey('examples.uuid'))
)

class DefinitionModel(Base):
    __tablename__ = 'definitions'
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    definition = Column(String(255), nullable=False)
    words = relationship('WordModel', secondary='word_definition', back_populates='definitions')
    sentences = relationship('SentenceModel', secondary='definition_sentence', back_populates='definitions', cascade='all, delete')
    
WordDefinitionModel = Table(
    'word_definition',
    Base.metadata,
    Column('word_uuid', String(36), ForeignKey('words.uuid')),
    Column('definition_uuid', String(36), ForeignKey('definitions.uuid'))
)

class SentenceModel(Base):
    __tablename__ = 'sentences'
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    sentence = Column(String(255), nullable=False)
    definitions = relationship('DefinitionModel', secondary='definition_sentence', back_populates='sentences')
    
DefinitionSentenceModel = Table(
    'definition_sentence',
    Base.metadata,
    Column('sentence_uuid', String(36), ForeignKey('sentences.uuid')),
    Column('definition_uuid', String(36), ForeignKey('definitions.uuid'))
)
