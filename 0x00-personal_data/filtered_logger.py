#!/usr/bin/env python3
""" function called filter_datum that returns
    the log message obfuscated
"""
import re

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ uses regular expression with re.sub to replace occurences of
        certain field values with the specified redaction
    """
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message
