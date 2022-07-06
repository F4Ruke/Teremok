import os
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError


def my_awesome_upload_function(instance, filename):
    """Возвращает путь к файлу"""

    try:
        filename = translit(filename, reversed=True)
    except LanguageDetectionError:
        filename = filename

    return os.path.join(f"images/{instance.get_directory()}", filename)
