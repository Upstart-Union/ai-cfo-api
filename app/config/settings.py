from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI CFO API"
    VERSION: str = "1.0.0"

    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    FIREWORKS_API_KEY: str = ""

settings = Settings()
