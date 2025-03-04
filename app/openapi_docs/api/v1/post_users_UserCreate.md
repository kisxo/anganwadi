# User API Documentation

This API allows to create users.

## POST /api/v1/users

Creates a user.

### Authorization required [ Admin ]

### Parameters

- `user` (body, required): The user to create. Must be a JSON object with the following properties:

  - `user_username` (string [4, 20], unique, required) Format `alpha-numeric`:
    - Unique username used for login. 
    
  - `password` (string >= 6, required):
    - Password of the user.
  
  - `user_role` (choice, required) `["Staff", "Admin"]` default="Staff":
    - User role staff has limited access where admin has full access.

### Example



```http
Request:

POST /api/v1/users HTTP/1.1
Content-Type: application/json

{
  "user_username": "adminRaju",
  "password": "admin@raju",
  "user_role": "Admin"
}

Response:

HTTP/1.1 201 OK
Content-Type: application/json

{
    "user_username": "adminRaju",
    "user_role": "Admin"
}
```