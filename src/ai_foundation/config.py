import os
from dataclasses import dataclass

@dataclass
class Settings:
    app_name: str = "AI Engineering Foundation"
    environment: str = "development"
    gemini_api_key: str = ""

    @classmethod
    def load(cls):
        return cls(
            app_name=os.getenv(
                "APP_NAME", "AI Engineering Foundation"
            ),
            environment=os.getenv(
                "APP_ENV", "development"
            ),
            gemini_api_key=os.getenv(
                "GEMINI_API_KEY", ""
            ),
        )
