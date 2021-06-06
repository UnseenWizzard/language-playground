# "User Server B"
A Wiremock mock API - returning users whose UUID start with an letter

## Running
Starting with `./run.sh` this will listen on port 8082.

## API Endpoints
Request: 

```
GET /users/{uuid}
```

Response Schema: 
```
{
    "user" : {
        "first": "XXX", 
        "last": "XXX", 
        "id": "XXX",
        "uuid": "XXX", 
        "company_id": "XXX"
    }
}
```
Responds within 50 - 90 ms