#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re
import logging


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    message = re.sub(r"\d{2}/\d{2}/\d{4}", redaction, message)

    return message
