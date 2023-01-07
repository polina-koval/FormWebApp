import re


def type_v(v):
    re_expressions = {
        "email": r"^\S+@\w+.\w{2,4}$",
        "date": r"^(\d\d\.\d\d\.\d{4}|^\d{4}-\d\d-\d\d)$",
        "phone": r"^\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}$",
    }
    for field_type, re_expression in re_expressions.items():
        if re.fullmatch(re_expression, v):
            return field_type
    return "text"


def type_form(d):
    res = {k: type_v(v) for k, v in d.items()}
    return res


def predicate(obj, requirements):
    for k, v in requirements.items():
        if k not in obj.keys():
            return False
    return True
