from pydantic import BaseModel, field_validator
import re

UUID_REGEX = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.IGNORECASE
)

class StringValidationMixin(BaseModel):
    """
    Provides common validation methods for string fields in all entities.
    """

    @field_validator("*")
    @classmethod
    def no_whitespaces_or_linebreaks(cls, value):
        if isinstance(value, str) and not UUID_REGEX.match(value):
            if value != value.strip():
                raise ValueError("The string must not have any leading or trailing spaces")
            if "\n" in value or "\r" in value:
                raise ValueError("The string must not contain any newline or carriage return characters")
        return value

    @field_validator("*")
    @classmethod
    def validate_start_with_capital(cls, value):
        if isinstance(value, str) and value and not UUID_REGEX.match(value):
            if not value[0].isupper():
                raise ValueError("The string must start with a capital letter")
        return value 