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
        message = re.sub(rf"{f}=.*?{separator}", f"{f}={redaction}{separator}", message)

    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records"""
        logging.basicConfig(level=logging.DEBUG, format=record)
        logger = logging.getLogger()
        logger.info(record)
        # filter_datum(self.field)
