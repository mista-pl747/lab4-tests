import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from src.utils.validators import validate_user_email, validate_age

# === EMAIL TESTS ===
@pytest.mark.parametrize(
    "email, expected",
    [
        ("test@example.com", True),
        ("user.name@domain.co.uk", True),
        ("admin+tag@sub.domain.org", True),
        ("", False),
        ("invalid-email", False),
        ("user@.com", False),
        (None, False),
        (123, False),
    ],
    ids=["valid_basic", "valid_complex", "valid_plus", "empty", "no_at", "no_domain", "none", "int"]
)
def test_validate_user_email(email, expected):
    assert validate_user_email(email) == expected

# === AGE TESTS ===
def test_validate_age_valid():
    assert validate_age(18) is True
    assert validate_age(1) is True
    assert validate_age(150) is True

@pytest.mark.parametrize(
    "age", [0, -5, 151],
    ids=["zero", "negative", "too_old"]
)
def test_validate_age_invalid_range(age):
    with pytest.raises(ValueError, match="1–150"):
        validate_age(age)

@pytest.mark.parametrize(
    "age", ["25", None],
    ids=["str", "none"]
)
def test_validate_age_invalid_type(age):
    with pytest.raises(ValueError, match="цілим числом"):
        validate_age(age)