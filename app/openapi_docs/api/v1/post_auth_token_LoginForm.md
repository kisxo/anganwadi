# Auth API Documentation

This API allows to generate access JWT-Token.

## POST /api/v1/auth/token

Generates an access JWT-Token.<br>
JWT-Token will be valid for 10 hours from the time of generation.

### Parameters

- `user` (body, required): The user data to verify. Must be a JSON object with the following properties:

  - `user_username` (string, required) Format `alpha-numeric`:
    - Unique username used for login. 
    
  - `password` (string, required):
    - Password of the user.

### Response
Response data:
```
{
  "access_token": "JWT-token",
  "token_type": "bearer"
}
```

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