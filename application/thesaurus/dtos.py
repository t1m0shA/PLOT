from typing import List, Dict
from pydantic import BaseModel, Field

class WordDTO(BaseModel):
    """
    An input validator for the word\n
    Verifies that the inserted word and its examples, synonyms,\n
    definitions and sentences are in the correct form
    """
    word: str = Field(..., min_length=1)
    examples: List[str] = Field(default_factory=list)
    synonyms: List[str] = Field(default_factory=list)
    definitions_sentences: Dict[str, List[str]] = Field(default_factory=dict)