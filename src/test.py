import json
import os
from typing import Any

def test_taking(file_detect: str) -> Any:
    if not os.path.exists(file_detect):
        return "No such file or directory"
    try:
        with open(file_detect, "r", encoding="utf-8") as content:
            return json.load(content)
    except Exception as e:
        return f"Error found {e}"


def list_of_chosen_keys(brute_info: list[dict[str, str]], key_taked: str) -> list[str]:
    prompt_list: list[Any] = []
    for item in brute_info:
        prompt_content = item.get(key_taked, "")
        prompt_list.append(prompt_content)
    return prompt_list


def main() -> None:
    file_directory_test = "data/input/function_calling_tests.json"
    file_content_function = "data/input/functions_definition.json"
    print("\ntrying to encoding")

    brute_result = test_taking(file_directory_test)
    all_function_load = test_taking(file_content_function)

    print(f"\nType of result: {type(brute_result)}")

    print(f"\nthe final result is: \n{brute_result}")

    print("\nlet's separate the part of the brute_result")

    list_clean = list_of_chosen_keys(brute_result, "prompt")
    for i in list_clean:
        print(i)

    print("\nSo let's take all_function_load")
    all_function = list_of_chosen_keys(all_function_load, "name")
    for i in all_function:
        print(i)
