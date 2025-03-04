title="Gym Management API - DEOLANG"

summary = "This is the documentation of Gym Management API developed by Deolang. It is a JSON based RESTful API with custom endpoints to streamline gym management."

contact = {
    "name": "Email- Uday Subba",
    "email": "udaysubba2004@gmail.com"
}

tags_metadata = [
    {
        "name": "Authentication",
        "description":
        """Authentication is required before using the API.
        Every API method requires the same authentication process.<br>
        <br>
        Header: JWT Bearer Auth<br>
        Format in header: `Authorization: Bearer <JWT-Token>`<br>
        <br>
        Every JWT-Token will be valid for 10 hours from the time of generation.<br>
        Example JSON request with authentication headers: Let the say the `JWT-Token = eyJhbGciOiJSUzI1.....`
        
    {
        "url": "https://gym-deolang.com/v1/api/members",
        "method": "POST",
        "headers": {
            "Authorization": "Bearer eyJhbGciOiJSUzI1.....",
        },
        "data": request_data
    }  
To obtain the JWT-Token send a post request to `/api/v1/auth/token` with username and password in the following format <br>
                
    {"username": "abc","password": "xyz"}
After successfully verifying the username and password the server will respond with

    {"access_token": "JWT-token","token_type": "bearer"}  
""",
    }
]