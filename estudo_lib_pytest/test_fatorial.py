import pytest
from .fatorial import fatorial, FatorialInvalido


@pytest.mark.parametrize('entrada, esperado',[
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
    ])
def test_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado

@pytest.mark.parametrize('entrada',[
    'w',
    '8',
    5.9
    ])
def test_fatorial_invalido(entrada):
    with pytest.raises(FatorialInvalido):
        fatorial(entrada)
