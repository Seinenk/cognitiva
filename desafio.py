import os
import requests
import json
from dotenv import load_dotenv
import textstat

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração das APIs
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Configurações dos modelos usados no OpenRouter
MODELS = {
    "Mistral": "cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    "Google Gemini": "google/gemini-2.0-flash-lite-preview-02-05:free"
}

# Pergunta a ser enviada para os modelos
QUESTION = "Qual é a importância da inteligência artificial na medicina moderna?"


# Função para chamar os modelos via OpenRouter
def get_response(model, question):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://seusite.com",  # Altere para o seu site se necessário
        "X-Title": "Desafio Cognitiva"
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response")
    else:
        return f"Erro na API {model}: {response.status_code} - {response.text}"


# Coletar respostas dos modelos
def get_all_responses():
    responses = {}
    for name, model in MODELS.items():
        responses[name] = get_response(model, QUESTION)
    return responses


# Função para avaliar a clareza e coerência das respostas
def evaluate_responses(responses):
    scores = {}
    for model, response in responses.items():
        readability = textstat.flesch_reading_ease(response)
        scores[model] = readability
    return scores


# Função para autoavaliação assistida por IA (usando Google Gemini para avaliar respostas)
def autoevaluate_responses(responses):
    evaluation_prompt = "Aqui estão respostas de diferentes modelos de IA para a mesma pergunta. Avalie e classifique as respostas com base nos critérios: clareza, precisão, criatividade e gramática. Justifique sua escolha.\n"
    for model, response in responses.items():
        evaluation_prompt += f"\n[{model}]:\n{response}\n"

    return get_response(MODELS["Google Gemini"], evaluation_prompt)


# Exibir respostas e avaliações
def print_responses(responses):
    for model, response in responses.items():
        print(f"\n[{model}]:\n{response}\n")

    scores = evaluate_responses(responses)
    print("\n📊 Avaliação da Clareza e Coerência (Flesch Reading Ease Score):")
    for model, score in scores.items():
        print(f"{model}: {score:.2f}")

    print("\n🤖 Autoavaliação das respostas pela IA:")
    print(autoevaluate_responses(responses))


# Executar o código
if __name__ == "__main__":
    print("\n🚀 Coletando respostas dos modelos de IA...")
    responses = get_all_responses()
    print_responses(responses)
