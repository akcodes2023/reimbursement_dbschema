# delete_employee.py
import requests

# Specify the URL of the API endpoint with the EmployeeID you want to delete
url = 'http://127.0.0.1:8000/employees/12/'  # Replace with your actual API URL

# Send a DELETE request to delete the employee with EmployeeID 1
response = requests.delete(url)

# Check the response status code to ensure the deletion was successful
if response.status_code == 204:
    print("Employee deleted successfully.")
else:
    print("Failed to delete employee. Status code:", response.status_code)
