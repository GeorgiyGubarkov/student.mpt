# student.mpt

- main page
  - / - Auth page. Page with all routes after auth. 
- certificates | characteristics
  - /certificate | /characteristics
    - GET - Get page with form for students. Get page with all tickets certificate for admin
    - POST - Send data for register ticket
  - /certificate/\<int:id> | /characteristics/\<int:id>
    - PUT - Certificate is ready for issuance
    - DELETE - Ticket was in error. Refusal
- Payments
  - /certificate
    - GET - Get page with form for students. Get page with all tickets certificate for admin
    - POST - Send data for register ticket