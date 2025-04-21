# simple 'in-memory' db

db: dict[str, dict] = {
    "12345": {
        "customer": {
            "full_name": "John Doe",
            "email": "example@example.com"
        },
        "address": {
            "country": "USA",
            "city": "San Francisco",
            "postal_code": "94016-ABC"
        }
    }
}
