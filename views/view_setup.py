from flask import jsonify, request


def format_api_response(payload, status: str) -> str:
    return jsonify({"status": status, "payload": payload})


# TODO: validate fields using e.g. WTForms or something for security / input validation countermeasure
def validate_field(field: str):
    if field not in list(request.json.keys()):
        raise Exception("Missing required field " + field + " in request JSON")
    else:
        return "valid"