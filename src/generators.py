# Asynchronous Example
import os
import asyncio

from typing import Optional, Union
from mistralai import Mistral

from config import AI_TOKEN


async def generate_response(content: str) -> Optional[str]:
    s = Mistral(api_key=AI_TOKEN,)
    
    res: Optional[str] = await s.chat.complete_async(
        model="mistral-large-latest",
        messages=[
            {
            "content": content,
            "role": "user",
            },
        ]
    )
    
    #if res is not None: # -> нет смысла, если res != None, то... он он ничего не делает, значит вернет None
    return res
