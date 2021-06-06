# "User Server A"
A Wiremock mock API - returning users whose UUID start with an number

## API Endpoints
Request: 

```
GET /api/v3/search?user_uuid={uuid}
```

Response Schema: 
```
{
    "user" : { 
        "id": "XXX",
        "uuid": "XXX", 
        "name": { 
            "first": "XXX", 
            "last": "XXX"
        }, 
        "company": { 
            "uuid": "XXX" 
        } 
    }
}
```
Responds log normal distributed around ~100 - 150ms