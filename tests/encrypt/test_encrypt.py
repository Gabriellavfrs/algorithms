import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    'Raises an error with invalid key'
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('abcde', '2')
    
    'Raises an error with invalid message'
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 2)
    
    'Should returns a reversed message if the key is invalid'
    assert encrypt_message('ab cde_', 8) == '_edc ba'

    'Returns encrypted message if the key is valid and even'
    assert encrypt_message('a bcd_e', 2) == 'e_dcb_ a'

    'Returns encrypted message if the key is valid and odd'
    assert encrypt_message('abc_de', 3) == 'cba_ed_'
