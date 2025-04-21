from pydantic import BaseModel, Field, EmailStr, field_validator
from pydantic_extra_types.country import CountryAlpha3


class UserData(BaseModel):
    full_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        regex=r"^[A-Za-z'-]+(?: [A-Za-z'-]+)?$",
        title="Full name",
        description="Customer full name",
        example="John Doe"
    )
    email: EmailStr = Field(
        ...,
        min_length=5,
        max_length=50,
        title="Customer email address",
        description="User’s e‑mail (normalized to lowercase)",
        example="example@example.com"
    )


class UserAddress(BaseModel):
    country: CountryAlpha3 = Field(
        ...,
        title="Country code",
        description="ISO 3166-1 code",
        example="USA"
    )
    city: str = Field(
        ...,
        min_length=1,
        max_length=20,
        regex=r"^[A-Za-z'-]+(?: [A-Za-z'-]+)?$",
        title="City",
        description="Only latin letters, spaces or hyphens",
        example="San Francisco"
    )
    postal_code: str = Field(
        ...,
        min_length=1,
        max_length=20,
        regex=r"^[A-Za-z0-9'-]+(?: [A-Za-z0-9'-]+)?$",
        title="Postal code",
        description="Latin letters, digits, hyphens or spaces",
        example="94016-ABC"
    )

    @field_validator('postal_code')
    def uppercase_postal_code(cls, postal_code: str) -> str:
        return postal_code.upper()


class UserInfo(BaseModel):
    customer: UserData = Field(..., title="Customer data")
    address: UserAddress = Field(..., title="Customer address")

    class Config:
        validate_all = True
        validate_assignment = True
        schema_extra = {
            "example": {
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


class CreatedUser(BaseModel):
    customer_id: str
