import os
import json
from pathlib import Path
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "projectManager.json.log"


# === Custom JSON Formatter ===
class JsonFormatter(Formatter):
    """Convierte los registros de log a JSON estructurado."""
    def format(self, record):
        log_object = {
            "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "filename": record.filename,
            "line": record.lineno,
        }
        if record.exc_info:
            log_object["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_object, ensure_ascii=False)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "json": {
            "()": JsonFormatter,  # Usa la clase personalizada
        },
        "console_simple": {
            "format": "{levelname}: {message}",
            "style": "{",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console_simple",
        },
        # Guarda logs en un archivo JSON rotativo semanal
        "file_json": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "json",
            "filename": LOG_FILE,
            "when": "W0",         # Rota cada semana (lunes)
            "backupCount": 8,     # Mantiene 8 semanas de logs
            "encoding": "utf8",
        },
    },

    "root": {
        "handlers": ["console", "file_json"],
        "level": "INFO",
    },

    "loggers": {
        "django": {
            "handlers": ["console", "file_json"],
            "level": "INFO",
            "propagate": True,
        },
        "projectManager": {
            "handlers": ["console", "file_json"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
