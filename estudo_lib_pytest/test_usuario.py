from .db import Conexao, Sessao
from .model import Usuario
import pytest



def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Bruno', email='meu_email@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Bruno', email='email1@hotmail.com'), Usuario(nome='Torres', email='email2@gmai.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
