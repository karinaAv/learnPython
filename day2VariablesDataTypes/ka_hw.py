# 1. Test Case ID Storage
test_case_id = "TC_LOGIN_001"
print(test_case_id, type(test_case_id))

# 2. Response Time Check
response_time_sec = 0.356
response_time_ms = int(response_time_sec * 1000)
print(f"Response time: {response_time_ms} ms")


# 3. Boolean Test Result
test_passed = False
print("Test Passed" if test_passed else "Test Failed")

# 4. Mixed Test Data Dictionary
test_data = {
    "id": 101,
    "name": "Login Test",
    "status": True,
    "duration": 1.23
}
print(f"{test_data['id']}")
print(f"{test_data['name']}")
print(f"{test_data['status']}")
print(f"{test_data['duration']}")

# 5. Data Conversion (Type Casting)
num_str = "200"
num_int = int(num_str)
print(num_int * 3)

# 6. Test Step Counter
total_steps = 10
total_steps += 2
print(f"Total steps after adding: {total_steps}")

# 7. String Concatenation for Test Names
feature = "Checkout"
scenario = "Successful Payment"
full_test_name = f"{feature} - {scenario}"
print(full_test_name)

# 8. Data Type Validation
status = "True"
print(status, type(status))

# 9. Test Status List
statuses = ["PASS", "FAIL", "PASS"]
passed_count = statuses.count("PASS")
print(f"Passed tests: {passed_count}")

# 10. API JSON Simulation
api_status_code = 200
api_response = '{"result": "success"}'

print(type(api_status_code), type(api_response))
