#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re
import logging


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """returns the log message obfuscated"""
    for f in fields:
        message = re.sub(
            rf"{f}=.*?{separator}", f"{f}={redaction}{separator}", message)

    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init func"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records"""
        filtred_msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        record.msg = filtred_msg
        return super(RedactingFormatter, self).format(record)


PII_FIELDS = [
    "snn",
    "email",
    "password",
    "ip",
    "phone",
]


def get_logger() -> logging.Logger:
    """returns a logging.Logger object."""
    logging.Logger("user_data")
    logging.setLevel(logging.INFO)
    logging.propagate = False
    h = logging.StreamHandler()
    h.setFormatter(RedactingFormatter(PII_FIELDS))
