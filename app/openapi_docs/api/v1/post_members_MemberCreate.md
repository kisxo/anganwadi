# Member API Documentation

This API allows to create members.

## POST /api/v1/members

Creates a member.

### Authorization required [ Staff, Admin ]

### Parameters

- `member` (body, required): The member to create. Must be a JSON object with the following properties:

  - `member_name` (string <= 30, required):
    - The full name of the member.
    
  - `member_image_url` (url <= 250, optional):
    - The profile image url of the member.

  - `member_phone` (number, required):
    - The contact number of the member [Whatsapp preferred].

  - `member_status` (choice, required) `["Active", "Inactive"]` default="Active":
    - The status of member.

  - `member_gender` (choice, required) `["Male", "Female"]`:
    - The Gender of the member.
  
  - `member_measurements` (object, optional)
    - The measurements of the member.
    - `{"height": "string","weight": "string","chest": "string","waist": "string"}`
  
  - `member_dob` (date, optional) Format `YYYY-MM-DD` eg- For 2004 January 30 `2004-01-30`:
    - The date of birth of member. 
    
  - `member_address` (string <= 150, optional)
    - The address of the member.

  - `member_training` (choice, required) `["Trainer", "Personal"]`:
    - The training type whether regular trainer or personal trainer.
  
  - `member_plan` (choice, required) `["Regular" "Advance"]`:
    - The current training package whether regular or advance.
  
  - `member_batch` (choice, required) `["Morning" "Evening"]`:
    - The batch-timing of the member.
  
  - `member_starting_date` (date, optional) Format `YYYY-MM-DD`:
    - The training plan staring date of a member. 
    
  - `member_ending_date` (date, optional) Format `YYYY-MM-DD`:
    - The training plan ending date of a member.
  
  - `member_info` (string <= 50, optional):
    - Additional note about the member.
  
  - `member_due_date` (date, required) Format `YYYY-MM-DD`:
    - The next due date.
    
  - `member_due_amount` (float, required):
    - The due amount to be paid before the due date.

### Example



```http
Request:

POST /api/v1/members HTTP/1.1
Content-Type: application/json

{
  "member_name": "Raju Singh",
  "member_image_url": "https://gym-deolang.com/media/members/image/1.png",
  "member_phone": "6001234567",
  "member_status": "Active",
  "member_gender": "Male",
  "member_measurements": {
    "height": "170cm",
    "weight": "96kg",
    "chest": "100cm",
    "waist": "80cm"
  },
  "member_dob": "2004-01-30",
  "member_address": "Near Railwaystation, Guwahati",
  "member_training": "Personal",
  "member_plan": "Advance",
  "member_batch": "Morning",
  "member_starting_date": "2025-02-20",
  "member_ending_date": "2025-05-20",
  "member_info": "Very fat, in weight loss program",
  "member_due_date": "2025-03-20",
  "member_due_amount": 3000
}

Response:

HTTP/1.1 201 OK
Content-Type: application/json

{
    "member_id": 1,
    "member_name": "Raju Singh",
    "member_gender": "Male",
    "member_phone": "6001234567"
}
```