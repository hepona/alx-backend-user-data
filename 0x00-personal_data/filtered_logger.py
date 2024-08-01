#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for f in fields:
        message = re.sub(rf"{f}=.*?{separator}", f"{f}={redaction}{separator}", message)

    return message
