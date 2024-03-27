import streamlit as st
from openai import OpenAI

class WhatIfMethod:
    @staticmethod
    def whatif_ai(msg, client):
        whatif_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a what if generator. You tell users what if scenarios based on their input."
                },
                {
                    "role": "user",
                    "content": f"{msg}" 
                }
            ],
            max_tokens=200,  
            temperature=0.9
        )

        whatif = whatif_response.choices[0].message.content

        return whatif

   # @staticmethod
    #def pic_ai(msg, client):
        pic_response = client.images.generate(
            model="dall-e-3",
            prompt=f"{msg}",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = pic_response.data[0].url

        return image_url
