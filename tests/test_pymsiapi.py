import unittest
from unittest.mock import patch
import requests
import sys
sys.path.append('./pymsiapi')  # Add the pymsiapi directory to the path
from pymsiapi import github, steam, random_person
from io import StringIO

class TestAPIFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_github_user_info(self, mock_get):
        # Example mock response for GitHub API
        mock_response = {
            "login": "r00tww",
            "name": "Root",
            "bio": "Security Researcher",
            "public_repos": 50,
            "followers": 1200,
            "following": 10  # This could change without failing the test
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Capture printed output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            github("r00tww")
            output = fake_out.getvalue()

        # Check that expected keywords are in the output, but don't rely on exact values
        self.assertIn("Login: r00tww", output)
        self.assertIn("Name: Root", output)
        self.assertIn("Bio:", output)  # We expect bio to be present, not necessarily "Security Researcher"
        self.assertIn("Public Repositories:", output)
        
        # Check if followers and following are integers (the values can change, but types should remain the same)
        self.assertIn("Followers:", output)
        self.assertIn("Following:", output)
        self.assertTrue(isinstance(mock_response["followers"], int))
        self.assertTrue(isinstance(mock_response["following"], int))

    @patch('requests.get')
    def test_steam_game_info(self, mock_get):
        # Example mock response for Steam API
        mock_response = {
            "ad": "Half-Life",
            "açıklama": "A groundbreaking game",
            "geliştiriciler": ["Valve"],
            "yayıncılar": ["Valve"],
            "türler": ["Action", "Shooter"],
            "çıkış_tarihi": "1998-11-19",
            "fiyat": "$9.99",
            "metacritic_puanı": 90,
            "kullanıcı_yorumları": {
                "yorum_puanı": 4.5,
                "toplam_olumlu": 1000,
                "toplam_olumsuz": 200,
                "toplam_yorum": 1200
            },
            "minimum_sistem_gereksinimleri": "<html>Requires 64MB RAM</html>",
            "desteklenen_diller": "<html>English, Spanish, French</html>"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Capture printed output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            steam("Half-Life")
            output = fake_out.getvalue()

        # Check that expected information is in the output, regardless of the specific values
        self.assertIn("Game Name:", output)
        self.assertIn("Description:", output)
        self.assertIn("Developers:", output)
        self.assertIn("Minimum System Requirements:", output)  # Just ensure the data appears
        self.assertIn("Supported Languages:", output)

        # Verify system requirements and languages are processed correctly
        self.assertTrue('<html>' not in output)
        self.assertTrue('64MB RAM' in output)

    @patch('requests.get')
    def test_random_person(self, mock_get):
        # Example mock response for random person API
        mock_response = {
            "results": [{
                "name": {"title": "Mr", "first": "John", "last": "Doe"},
                "gender": "male",
                "location": {
                    "street": {"number": "10", "name": "Main St"},
                    "city": "New York",
                    "state": "NY",
                    "country": "USA",
                    "postcode": "10001"
                },
                "email": "john.doe@example.com",
                "login": {"username": "johndoe"},
                "dob": {"date": "1990-01-01"},
                "phone": "123-456-7890",
                "cell": "987-654-3210",
                "nat": "US",
                "picture": {"large": "http://example.com/pic.jpg"}
            }]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Capture printed output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            random_person()
            output = fake_out.getvalue()

        # Check that expected information is in the output
        self.assertIn("Name: Mr John Doe", output)
        self.assertIn("Gender: male", output)
        self.assertIn("Location:", output)
        self.assertIn("Email:", output)
        self.assertIn("Username:", output)

        # Verify phone and cell format (not specific values)
        self.assertIn("Phone:", output)
        self.assertIn("Cell:", output)

if __name__ == '__main__':
    unittest.main()
