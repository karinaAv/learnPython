import json


# 1. Test Case ID Storage
def test_case_id_storage():
    test_case_id = "TC_LOGIN_001"
    print(test_case_id, type(test_case_id).__name__, sep=" data type:")


test_case_id_storage()


# 2. Response Time Check
def response_time_check():
    api_response_time = 0.356
    converted_api_response_time = round(api_response_time*1000)
    print(f"Response time: {converted_api_response_time} ms")


response_time_check()


# 3. Boolean Test Result
def boolean_test_result():
    test_passed = True
    print("Test Passed" if test_passed else "Test Failed")


boolean_test_result()


# 4. Mixed Test Data Dictionary
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


# 5. Data Conversion (Type Casting)
def data_conversion():
    variable = "200"
    converted = int(variable)*3
    return converted


print(data_conversion())


# 6. Test Step Counter
def test_step_counter():
    total_steps = 10
    total_steps += 2
    print(f"Total steps after adding: {total_steps}")


test_step_counter()


# 7. String Concatenation for Test Names
def string_concatenation_for_test_names():
    feature = "Checkout"
    scenario = "Successful Payment"
    print(f"{feature} - {scenario}")


string_concatenation_for_test_names()


# 8. Data Type Validation
def data_type_validation(status):
    if isinstance(status, bool):
        return status
    elif isinstance(status, str):
        s = status.strip().lower()
        if s in {"true", "false"}:
            return s == "true"
        return bool(s)
    return bool(status)


print(type(data_type_validation(status="True")))


# 9. Test Status List
def test_status_list():
    statuses = ["PASS", "FAIL", "PASS"]
    passed = statuses.count("PASS")
    print(passed)


test_status_list()


# 10. API JSON Simulation
def api_json_simulation():
    api_status_code = 200
    api_response = '{"result": "success"}'
    print(type(api_status_code).__name__, type(api_response).__name__)
    data = json.loads(api_response)
    print(data["result"])


api_json_simulation()
