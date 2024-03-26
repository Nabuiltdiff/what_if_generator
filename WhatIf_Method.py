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

    @staticmethod
    def pic_ai(msg, client):
        cover_response = client.images.generate(
            model="dall-e-2",
            prompt=f"{msg}",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = cover_response.data[0].url

        return image_url

# Define a list of random scenarios
    random_scenarios = [
        "What if robots ruled the world?",
        "What if time travel was possible?",
        "What if dinosaurs still existed?",
        "What if humans could breathe underwater?",
        "What if teleportation became a reality?",
        # Add more scenarios here
    ]