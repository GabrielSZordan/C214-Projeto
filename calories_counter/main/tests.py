import unittest
from unittest.mock import patch
import requests
import unittest
from unittest import mock
import sys
import os

# Main
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calories_counter.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
# Para testar se a função execute_from_command_line(sys.argv) foi chamada corretamente
class TestMain(unittest.TestCase):
    @patch('sys.argv', ['manage.py', 'runserver'])
    @patch('django.core.management.execute_from_command_line')
    def test_main_executa_command_line(self, mock_execute_from_command_line):
        main()
        mock_execute_from_command_line.assert_called_once_with(['manage.py', 'runserver'])

# Verifica se a resposta da API tem um status de código 200 (OK) e se o texto da resposta não é nulo
class TestIndex(unittest.TestCase):
    def test_index(self):
        query = '100gr fries'
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        headers = {'X-Api-Key': 'mXQkKui50jO0+SOKXc8MRA==SBvHrJvnNrAIvTCk'}

        response = requests.get(api_url, headers=headers)

        self.assertEqual(response.status_code, requests.codes.ok)
        self.assertIsNotNone(response.text)

# Teste de verificação para entrada vazia
class TestNullQuery(unittest.TestCase):
    def test_index(self):
        query = ' '
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        headers = {'X-Api-Key': 'mXQkKui50jO0+SOKXc8MRA==SBvHrJvnNrAIvTCk'}

        response = requests.get(api_url, headers=headers)

        self.assertIsNotNone(response.text)

        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:", response.status_code, response.text)

# Verifica o teste de falha para entrada de caracteres fora do padrão ou especiais 
class TestWrongQuery(unittest.TestCase):
    def test_index(self):
        query = '*#kg gabriel'
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        headers = {'X-Api-Key': 'mXQkKui50jO0+SOKXc8MRA==SBvHrJvnNrAIvTCk'}

        response = requests.get(api_url, headers=headers)

        self.assertIsNotNone(response.text)

        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    unittest.main()
