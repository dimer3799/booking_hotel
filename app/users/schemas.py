"""описание схемы регистрации пользователя"""

from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    """Схема регистрации пользователя"""

    email: EmailStr
    password: str

from secrets import token_bytes
from base64 import b64encode

print(b64encode(token_bytes(32)).decode())