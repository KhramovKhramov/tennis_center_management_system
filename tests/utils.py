from rest_framework.reverse import reverse


def get_api_url(basename: str, url_path: str, pk: int | None = None) -> str:
    """Получение url для запроса через APIClient."""

    return (
        reverse(f'{basename}-{url_path}')
        if not pk
        else reverse(f'{basename}-{url_path}', kwargs={'pk': pk})
    )
