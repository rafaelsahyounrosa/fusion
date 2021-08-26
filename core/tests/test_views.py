from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@mail.com',
            'assunto': 'Um assunto qualquer',
            'mensagem': 'Uma mensagem qualquer'
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302) #O 302 representa o redirect. Como caso o nosso formulário seja válido ele redireciona para a página principal, usamos o 302
    
    def test_form_invalid(self):
        dados = {
            'nome': 'Felicity Jones',
            'assunto': 'Um assunto qualquer'
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
