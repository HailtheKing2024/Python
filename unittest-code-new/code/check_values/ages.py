# check_values/ages.py


def categorize(age):
    if 0 <= age <= 9:
        return "child"
    elif 10 <= age <= 18:
        return "teen"
    elif 19 <= age <= 150:
        return "adult"

    return f"invalid age {age}"
