import os
from dotenv import load_dotenv

BASE_ENV = os.path.join("configs", "base.env")

# Carrega config base
load_dotenv(BASE_ENV)

# Carrega .env principal (dev/prod)
ENV_FILE = os.getenv("ENV_FILE", ".env")
load_dotenv(ENV_FILE, override=True)


class Settings:
    def __init__(self):
        self.MIKROTIK_USERNAME_CPE = os.getenv("MIKROTIK_USERNAME_CPE", None)
        self.MIKROTIK_PASSWORD_CPE = os.getenv("MIKROTIK_PASSWORD_CPE", None)
        self.MIKROTIK_USERNAME_POP = os.getenv("MIKROTIK_USERNAME_POP", None)
        self.MIKROTIK_PASSWORD_POP = os.getenv("MIKROTIK_PASSWORD_POP", None)
        self.USERNAME_LDAP = os.getenv("USERNAME_LDAP", None)
        self.PASSWORD_LDAP = os.getenv("PASSWORD_LDAP", None)
        self.DEFAULT_PORT = os.getenv("DEFAULT_PORT", None)
settings = Settings()
