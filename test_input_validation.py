import pytest
from input_validation import is_valid_email

@pytest.mark.parametrize("email", [
    ("test@email.com")
,   ("t.est@email.com")
,   ("test@em.ail.com")
,   ("test@email.co.uk")
,   ("te-st@email.com")
,   ("te_st@email.com")
,   ("test1@email.com")
])
def test_is_valid_email__gueltige_Adressen(email):
    assert is_valid_email(email) == True



@pytest.mark.parametrize("email", [
    ("testemail.com")   # Fehlendes @-Zeichen
,   ("test@email")      # Fehlende Top-Level-Domain
,   ("test@em@ail.com") # Mehrfaches @-Zeichen
])
def test_is_valid_email__ungueltige_Adressen(email):
    assert is_valid_email(email) == False
