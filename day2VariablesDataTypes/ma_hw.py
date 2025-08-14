import json


def test_case_id_storage():
    test_case_id = "TC_LOGIN_001"
    print(test_case_id, type(test_case_id).__name__, sep=" data type:")


test_case_id_storage()


def response_time_check():
    api_response_time = 0.356
    converted_api_response_time = round(api_response_time*1000)
    print(f"Response time: {converted_api_response_time} ms")


response_time_check()


def boolean_test_result():
    test_passed = True
    print("Test Passed" if test_passed else "Test Failed")


boolean_test_result()


def mixed_test_data_dictionary():
    test_data = {
        "id": 101,
        "name": "Login Test",
        "status": True,
        "duration": 1.23
    }
    for key, value in test_data.items():
        print(key, value, type(value).__name__)


mixed_test_data_dictionary()


def data_conversion():
    variable = "200"
    converted = int(variable)*3
    return converted


print(data_conversion())


def string_concatenation_for_test_names():
    feature = "Checkout"
    scenario = "Successful Payment"
    print(f"{feature} - {scenario}")


string_concatenation_for_test_names()


def data_type_validation(status):
    if isinstance(status, bool):
        return status
    if isinstance(status, str):
        s = status.strip().lower()
        if s in {"true", "false"}:
            return s == "true"
        return bool(s)
    return bool(status)


print(type(data_type_validation(status="True")))


def test_status_list():
    statuses = ["PASS", "FAIL", "PASS"]
    passed = statuses.count("PASS")
    print(passed)


test_status_list()


def api_json_simulation():
    api_status_code = 200
    api_response = '{"result": "success"}'
    print(type(api_status_code).__name__, type(api_response).__name__)
    data = json.loads(api_response)
    print(data["result"])


api_json_simulation()

