import pytest

from .triangulo import Bhaskara

#criando Fixtures


class TestBhaskara:
    @pytest.fixture
    def b(self):
        return Bhaskara()
    
    def test_uma_raiz(self, b):
        assert (1,0) == b.calcular_raizes(1, 0, 0)
    
    def test_duas_raizes(self, b:Bhaskara):
        assert (2, 3, 2) == b.calcular_raizes(1, -5, 6)
    
    def test_zero_raizes(self, b:Bhaskara):
        assert  0 == b.calcular_raizes(10, 10, 10)
    
    def test_raiz_negativa(self, b:Bhaskara):
        assert (1, -1) == b.calcular_raizes(10, 20, 10)