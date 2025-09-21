from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class TestSettings(BaseSettings):
    """
    Настройки для тестовой среды.

    Вынесены отдельно, чтобы не мешать настройки
    тестовой БД с настройками основной.
    """

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='allow',
        case_sensitive=True,
    )

    TEST_DB_USER: str | None = None
    TEST_DB_PASSWORD: str | None = None
    TEST_DB_HOST: str | None = None
    TEST_DB_PORT: str | None = None
    TEST_DB_NAME: str | None = None

    @property
    def test_database_url(self) -> str:
        """Формирование урла для подключения к тестовой БД."""

        # Если нет, то формируем или выдаем ошибку, если нет необходимых данных
        if not all(
            (
                self.TEST_DB_USER,
                self.TEST_DB_PASSWORD,
                self.TEST_DB_HOST,
                self.TEST_DB_PORT,
                self.TEST_DB_NAME,
            ),
        ):
            raise ValueError(
                'Отсутствуют необходимые данные для подключения к тестовой БД',
            )

        return (
            f'postgresql+asyncpg://'
            f'{self.TEST_DB_USER}:{self.TEST_DB_PASSWORD}@'
            f'{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}'
        )


@lru_cache
def get_test_settings() -> TestSettings:
    """Получение экземпляра тестовых настроек."""

    return TestSettings()


test_settings = get_test_settings()
