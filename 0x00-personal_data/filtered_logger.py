#!/usr/bin/env python3
""" function called filter_datum that returns the log message
    obfuscated
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ Replacing """
    return re.sub(
        rf"({'|'.join(map(re.escape, fields))})=[^{separator}]+{re.escape(separator)}",
        rf"\1={redaction}{separator}",
        message
    )
