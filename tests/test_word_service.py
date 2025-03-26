from application.thesaurus.cases import RetrieveWordUseCase
from domain.thesaurus.services import WordService
from domain.thesaurus.entities import Word
from infrastructure.repositories.thesaurus_repo import SQLAlchemyWordRepository
from infrastructure.db import SessionLocal, init_db

def test_word_service():
    init_db()
    session = SessionLocal()
    word_repository = SQLAlchemyWordRepository(session)
    word_service = WordService(word_repository)
    get_word_use_case = RetrieveWordUseCase(word_service)
    
    res = get_word_use_case.execute(
        uuid='6a3a9084-b933-49ae-9e23-140827c608a9',
    )
    assert isinstance(res, Word)
