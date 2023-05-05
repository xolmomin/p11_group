# from datetime import datetime
# from typing import Optional
#
# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     id: int
#     name:str = 'John Doe'
#     signup_ts: Optional[datetime] = None
#     friends: list[int] = []
#
#
# external_data = {
#     'id': '123',
#     'signup_ts': '2019-06-01 12:22',
#     'friends': [1, 2, '3'],
# }
# user = User(**external_data)
#
#
#
# from pydantic import ValidationError
#
# try:
#     User(signup_ts='broken', friends=[1, 2, 'not number'])
# except ValidationError as e:
#     print(e.json())
#
# import json
#
# import httpx
# from pydantic import BaseModel, ValidationError, validator
#
#
# class CommentModel(BaseModel):
#     postId: int
#     id: int
#     name: str
#     email: str
#     body: str
#
#     @validator('postId', 'id')
#     def check_post_id_with_id(cls, v):
#         if not isinstance(v, int):
#             raise ValueError('must be an integer')
#         return v
#
#     @validator('name', 'body')
#     def check_body_with_name(cls, v, values, **kwargs):
#         if not isinstance(v, str):
#             raise ValueError('must be an string')
#         return v
#
#     @validator('email')
#     def check_email(cls, value):
#         if not ('@' in value and '.' in value[value.index('@') + 2:]):
#             raise ValueError('must be email')
#         return value
#
#
# response = httpx.get('https://jsonplaceholder.typicode.com/comments').json()
#
# invalid_comments = []
# valid_comments = []
#
# for comment in response:
#     try:
#         valid_comments.append(CommentModel(**comment).dict())
#     except ValidationError as e:
#         invalid_comments.append({**comment})
#
# with open('invalid_comments.json', 'w') as invalid_f, open('valid_comments.json', 'w') as valid_f:
#     json.dump(valid_comments, valid_f, indent=4, ensure_ascii=False)
#     json.dump(invalid_comments, invalid_f, indent=4, ensure_ascii=False)
#
#


import json
from typing import Optional

import httpx
from pydantic import BaseModel, validator, ValidationError


class ItemModel(BaseModel):
    id: int
    title: str
    description: str
    payment_type: str
    price: int
    is_negotiable: bool
    owner_type: str
    status: str
    phone: Optional[int]
    type: str

    @validator('title', 'description', 'payment_type')
    def title_description_payment_type_check(cls, value):
        if not isinstance(value, str):
            raise ValueError('must be an string')
        return value

    @validator('id', 'price')
    def id_with_price_check(cls, value):
        if not (isinstance(value, int) and value >= 0):
            raise ValueError('must be an int')
        return value

    @validator('is_negotiable')
    def is_negotiable_check(cls, value):
        if not isinstance(value, bool):
            raise ValueError('must be an bool')
        return value

    @validator('phone')
    def phone_check(cls, value):
        if not (value is None or isinstance(value, int)):
            raise ValueError('must be an int')
        return value


url = 'http://10.10.1.238:8000/api/v1/adverts/data/'

response = httpx.get(url)

if response.status_code == 200:
    results = response.json()['results']
    invalid = []
    valid = []

    for result in results:
        try:
            valid.append(ItemModel(**result).dict())
        except ValidationError as e:
            print(e)
            invalid.append({**result})

    with open('invalid.json', 'w') as invalid_f, open('valid.json', 'w') as valid_f:
        json.dump(valid, valid_f, indent=4, ensure_ascii=False)
        json.dump(invalid, invalid_f, indent=4, ensure_ascii=False)
