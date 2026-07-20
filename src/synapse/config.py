"""Application configuration, loaded from environment variables and .env."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Synapse gateway settings.

    Values are read from environment variables prefixed with SYNAPSE_,
    falling back to a local .env file. e.g. SYNAPSE_PORT=9000 sets `port`.
    """

    model_config = SettingsConfigDict(
        env_prefix="SYNAPSE_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "INFO"

    # Comma-separated API keys, parsed into a list.
    api_keys: str = "dev-key-replace-me"


def get_settings() -> Settings:
    """Return a Settings instance.

    Kept as a function so it can be overridden in tests and used as a
    FastAPI dependency later.
    """
    return Settings()
