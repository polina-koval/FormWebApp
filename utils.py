import re
from urllib.parse import parse_qs


def type_v(v):
    re_expressions = {
        "email": r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$",
        "date": r"^(\d\d\.\d\d\.\d{4}|^\d{4}-\d\d-\d\d)$",
        "phone": r"^7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}$",
    }
    for field_type, re_expression in re_expressions.items():
        if re.fullmatch(re_expression, v):
            return field_type
    return "text"


def type_form(d):
    res = {k: type_v(v) for k, v in d.items()}
    return res


def convert_qs_to_dict(qs: str):
    # Convert querystring to dict
    dct = {k: v for k, vs in parse_qs(qs).items() for v in vs}
    return dct


def is_correct_form(request_body, db_item):
    return request_body.items() <= db_item.items()
