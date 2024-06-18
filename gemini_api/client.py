import google.generativeai as genai
from decouple import config


def get_car_ai_bio(model_car, brand, model_year):
    genai.configure(api_key=config('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f'Faça uma descrição de até 250 caracteres para o carro {brand} {model_car} {model_year}')
    return response.text


    






































