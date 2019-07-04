import string
import country_controller

controller = country_controller.CountryController()


def invalid_chars():
    allowed_punctuation = ["_", "'", '"', "^", "-", "(", ")", ","]
    punctuation = string.punctuation
    for s in allowed_punctuation:
        punctuation = punctuation.replace(s, "")
    return set(punctuation)


def process(invalid_chars):
    print("*******************")
    print("Enter one country name or code to see the capital city")
    print("to exit type 'q', 'quit', or 'exit'")
    arg = input("enter country code or name --> ").strip()
    # reject empty input
    if not arg:
        print(f"The input is empty. Try again.")
        return {"continue": True, "value": "empty input"}
    # reject input that has characters we don't want
    if any(char in invalid_chars for char in arg):
        print(f"The input {arg} has improper character(s). Try again.")
        return {"continue": True, "value": "garbage input"}
    # let the user quit
    if arg.lower() in ["quit", "q", "exit"]:
        return {"continue": False, "value": "kill"}
    output = controller.resolve_country(arg)
    if output:
        print("The resolved country is:")
        print(output)
        return {"continue": True, "value": output}
    else:
        print(f"The input {arg} did not resolve a country. Try again.")
    return {"continue": True, "value": "not found"}


def run():
    invalid_chars_holder = invalid_chars()
    while process(invalid_chars_holder)["continue"]:
        pass


if __name__ == "__main__":
    run()
