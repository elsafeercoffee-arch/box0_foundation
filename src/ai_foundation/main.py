from .config import Settings

def health_check():
    settings = Settings.load()
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.environment,
    }

if __name__ == "__main__":
    print(health_check())
