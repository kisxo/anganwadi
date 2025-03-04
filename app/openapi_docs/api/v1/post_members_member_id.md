# Member API Documentation

This API allows to get a member detail.

## POST /api/v1/members/{member_id}

Get a member detail.

### Authorization required [ Staff, Admin ]

### Response

- `member` (body, required): The member to create. Must be a JSON object with the following properties:

  - `member_name`
    - The full name of the member.
    
  - `member_image_url`
    - The profile image url of the member.

  - `member_phone`
    - The contact number of the member [Whatsapp preferred].

  - `member_status`
    - The status of member.

  - `member_gender`
    - The Gender of the member.
  
  - `member_measurements`
    - The measurements of the member.
    - `{"height": "string","weight": "string","chest": "string","waist": "string"}`
  
  - `member_dob` Format `YYYY-MM-DD`
    - The date of birth of member. 
    
  - `member_address`
    - The address of the member.

  - `member_training`
    - The training type whether regular trainer or personal trainer.
  
  - `member_plan`
    - The current training package whether regular or advance.
  
  - `member_batch`
    - The batch-timing of the member.
  
  - `member_starting_date` Format `YYYY-MM-DD`:
    - The training plan staring date of a member. 
    
  - `member_ending_date` Format `YYYY-MM-DD`:
    - The training plan ending date of a member.
  
  - `member_info`
    - Additional note about the member.
  
  - `member_due_date` Format `YYYY-MM-DD`:
    - The next due date.
    
  - `member_due_amount`
    - The due amount to be paid before the due date.

### Example



```http
Request:

POST /api/v1/members/1 HTTP/1.1
Content-Type: application/json

Response:

HTTP/1.1 200 OK
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
```