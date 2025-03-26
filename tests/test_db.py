from infrastructure.db import SessionLocal, init_db
from infrastructure.models.thesaurus import WordModel
from domain.thesaurus.entities import Word
import json

def test_connection():
    init_db()
    session = SessionLocal()
    
    test_word = WordModel()
    test_word.word = "TestWord"
    session.add(test_word)
    session.commit()
    
    
    retrieved_word = session.query(WordModel).filter_by(uuid=test_word.uuid).first()
    print("Retrieved word:", retrieved_word.word)
    
    
    # session.delete(retrieved_word)
    # session.commit()

    session.close()
