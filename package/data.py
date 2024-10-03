import requests
import base64
from dataclasses import dataclass

@dataclass
class TriviaData:
    difficulty : str

    def get_api_url(self):
        return f"https://opentdb.com/api.php?amount=10&difficulty={self.difficulty}&type=boolean&encode=base64"

    def fetch_questions(self):
        api_url = self.get_api_url()
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if data["response_code"] == 0:
                return data["results"]
            else:
                print("Error: No results found.")
                return []
        
        else:
            print("Error: Unable to fetch data.")
            return []
        
    @classmethod
    def ask_difficulty(cls):
        difficulty = input("Enter difficulty (easy, medium, hard): \n").strip().lower()
        if difficulty in ["easy","medium","hard"]:
            return cls(difficulty)
        else:
            print("Invalid difficulty. Please enter 'easy', 'medium', or 'hard'.")
            return cls.ask_difficulty()