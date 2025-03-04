# Member API Documentation

This API allows to list members.

## GET /api/v1/members

Lists members.

### Authorization required [Staff, Admin]

### Response

- `data[]`: List of member JSON objects with the following properties:

  - `member_id`
  
  - `member_name`
  
  - `member_gender`
  
  - `member_phone`
    
### Example



```http
Request:

GET /api/v1/members HTTP/1.1
Content-Type: application/json

Response:

HTTP/1.1 200 OK
Content-Type: application/json

{
  "data": [
    {
      "member_id": 1,
      "member_name": "Raju Singh",
      "member_gender": "Male",
      "member_phone": "6001234567"
    },
    {
      "member_id": 2,
      "member_name": "Arjun Sharma",
      "member_gender": "Male",
      "member_phone": "6009876543"
    }
  ]
}
```