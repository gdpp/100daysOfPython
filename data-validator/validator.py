import re

ALLOWED_COUNTRIES = ["USA", "Canada", "Mexico"]


def _validate_name(name):
    if len(name.strip()) == 0:
        return {"valid": False, "error": "Name can't be empty"}

    return {"valid": True}


def _validate_age(age):
    if age <= 0 or age < 18:
        return {"valid": False, "error": "Age must be greater than 0 or 17"}

    return {"valid": True}


def _validate_email(email):
    # Pattern explanation:
    # ^[a-zA-Z0-9._%+-]+ matches the local part (username)
    # @ ensures the @ symbol is present
    # [a-zA-Z0-9.-]+ matches the domain name
    # \.[a-zA-Z]{2,}$ ensures a dot followed by a 2+ character TLD (e.g., .com, .org)
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(regex, email.strip()):
        return {"valid": True}

    return {"valid": False, "error": "Email format is wrong"}


def _validate_country(country):
    if country.strip() in ALLOWED_COUNTRIES:
        return {"valid": True}

    return {
        "valid": False,
        "error": f"Country must be one of the following options: {[item for item in ALLOWED_COUNTRIES]}",
    }


def validate_user(user):
    response = {"valid": True, "errors": []}

    result_name = _validate_name(user.get("name"))

    if not result_name["valid"]:
        response["valid"] = False
        response["errors"].append(result_name["error"])

    result_age = _validate_age(user.get("age"))

    if not result_age["valid"]:
        response["valid"] = False
        response["errors"].append(result_age["error"])

    result_email = _validate_email(user.get("email"))

    if not result_email["valid"]:
        response["valid"] = False
        response["errors"].append(result_email["error"])

    result_country = _validate_country(user.get("country"))

    if not result_country["valid"]:
        response["valid"] = False
        response["errors"].append(result_country.get("errors"))

    return response
