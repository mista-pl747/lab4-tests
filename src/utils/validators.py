import re
from typing import Union

def validate_user_email(email: Union[str, None]) -> bool:
    if not email or not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email.strip()))

def validate_age(age: Union[int, None]) -> bool:
    if not isinstance(age, int):
        raise ValueError("Вік повинен бути цілим числом")
    if age <= 0 or age > 150:
        raise ValueError("Вік повинен бути в межах 1–150")
    return True