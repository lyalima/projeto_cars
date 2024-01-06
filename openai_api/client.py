import openai
import os


def get_car_ai_bio(model_car, brand, model_year):
    try:
        openai.api_key = os.environ.get('OPENAI_API_KEY')

        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": '''Faça uma descrição de até 250 caracteres com especificações técnicas sobre o carro {} {} {}.
                                A descrição deve ser feita para ajudar o carro a ser vendido.'''.format(brand, model_car, model_year),
                },
            ],
        )
        return completion.choices[0].message.content
    
    except Exception as e:
        print(e)






































