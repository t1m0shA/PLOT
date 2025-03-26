from abc import ABC, abstractmethod
from domain.thesaurus.entities import Word, Definition, Sentence, Example, Synonym
from typing import TypeVar, Generic

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):
    """Base repository for any entity"""

    @abstractmethod
    def retrieve(self, uuid: str) -> T:
        """Fetch an entity by its UUID"""
        pass

    @abstractmethod
    def create(self, entity: T) -> None:
        """Save an entity"""
        pass

    @abstractmethod
    def remove(self, entity: T) -> None:
        """Delete an entity"""
        pass

    @abstractmethod
    def modify(self, old: T, new: T) -> None:
        """
        Modify an entity value
        """
        pass

    

class WordRepository(BaseRepository[Word]):
    """
    Abstract word storage access
    """
    pass


