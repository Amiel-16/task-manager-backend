from dataclasses import dataclass
import os


@dataclass
class Settings:
    database_url: str = os.getenv(
        "DATABASE_URL", "postgresql://user:password@db:5432/app"
    )
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "change-this-secret")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
    )


settings = Settings()
