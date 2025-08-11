#### **1. Test Case ID Storage**

* **Task:** Create a variable `test_case_id` storing `"TC_LOGIN_001"` (string).
* **Action:** Print it and its data type using `type()`.

---

#### **2. Response Time Check**

* **Task:** Store an API response time `0.356` (float).
* **Action:** Convert it to milliseconds and print: `"Response time: 356 ms"`.

---

#### **3. Boolean Test Result**

* **Task:** Store `True` in a variable `test_passed`.
* **Action:** Print `"Test Passed"` if `True`, else `"Test Failed"`.

---

#### **4. Mixed Test Data Dictionary**

* **Task:** Create a dictionary:

  ```python
  test_data = {
      "id": 101,
      "name": "Login Test",
      "status": True,
      "duration": 1.23
  }
  ```
* **Action:** Print each key and value with its type.

---

#### **5. Data Conversion (Type Casting)**

* **Task:** Store `"200"` as a string.
* **Action:** Convert it to an integer and multiply by 3.

---

#### **6. Test Step Counter**

* **Task:** Store an integer `total_steps = 10`.
* **Action:** Increment it by 2 and print: `"Total steps after adding: 12"`.

---

#### **7. String Concatenation for Test Names**

* **Task:** Create two variables:

  ```python
  feature = "Checkout"
  scenario = "Successful Payment"
  ```
* **Action:** Combine them into `"Checkout - Successful Payment"` and print.

---

#### **8. Data Type Validation**

* **Task:** Given a variable `status = "True"`,

  * Check if it's a boolean using `isinstance()`.
  * If not, convert it to boolean.

---

#### **9. Test Status List**

* **Task:** Create a list `statuses = ["PASS", "FAIL", "PASS"]`.
* **Action:** Print how many tests passed.

---

#### **10. API JSON Simulation**

* **Task:** Store the following as variables:

  ```python
  api_status_code = 200
  api_response = '{"result": "success"}'
  ```
* **Action:**

  * Print types of both variables.
  * Convert `api_response` to a dictionary using `json.loads()` and print the `"result"` value.
