# forms/utils.py
import re

class FieldValidator:
    @staticmethod
    def validate_email(value):
        return re.match(r"[^@]+@[^@]+\.[^@]+", value)

    @staticmethod
    def validate_phone(value):
        return re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value)

    @staticmethod
    def validate_date(value):
        return re.match(r"^\d{4}-\d{2}-\d{2}$", value) or re.match(r"^\d{2}\.\d{2}\.\d{4}$", value)

    @staticmethod
    def detect_field_type(value):
        if FieldValidator.validate_date(value):
            return "date"
        if FieldValidator.validate_phone(value):
            return "phone"
        if FieldValidator.validate_email(value):
            return "email"
        return "text"
