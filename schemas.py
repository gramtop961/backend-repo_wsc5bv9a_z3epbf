from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Contact(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Work email")
    company: str = Field(..., description="Company name")
    message: str = Field(..., min_length=10, max_length=2000, description="Project goals and context")
