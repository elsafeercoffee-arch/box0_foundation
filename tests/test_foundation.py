import os
import unittest
from unittest.mock import patch

from ai_foundation.config import Settings
from ai_foundation.security import redact_secret
from ai_foundation.main import health_check

class FoundationTests(unittest.TestCase):

    def test_default_settings(self):
        with patch.dict(os.environ, {}, clear=True):
            settings = Settings.load()
            self.assertEqual(
                settings.environment, "development"
            )
            self.assertEqual(
                settings.gemini_api_key, ""
            )

    def test_custom_settings(self):
        with patch.dict(os.environ, {
            "APP_NAME": "Test App",
            "APP_ENV": "testing",
            "GEMINI_API_KEY": "secret123",
        }):
            settings = Settings.load()
            self.assertEqual(settings.app_name, "Test App")
            self.assertEqual(settings.environment, "testing")
            self.assertEqual(settings.gemini_api_key, "secret123")

    def test_secret_redaction(self):
        self.assertEqual(
            redact_secret("secret123"), "[REDACTED]"
        )

    def test_health_check(self):
        result = health_check()
        self.assertEqual(result["status"], "ok")

if __name__ == "__main__":
    unittest.main()
