#!/usr/bin/env python3
""" function called filter_datum that returns
    the log message obfuscated
"""
import re


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields, redaction, message, separator):
    return re.sub(fr'\b(?:{"|".join(fields)})\b', redaction, message)
