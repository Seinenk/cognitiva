# 🧠 Desafio Cognitiva Brasil - Comparação de Modelos de IA

Este projeto implementa uma solução que compara respostas geradas por diferentes Modelos de Linguagem de Grande Escala (LLMs) utilizando a API do OpenRouter. Ele envia uma mesma pergunta para modelos como **ChatGPT (GPT-4)** e **Google Gemini**, avalia a clareza e coerência das respostas e realiza uma **autoavaliação assistida por IA**.

---

## 📌 Funcionalidades

- **Envio de uma mesma pergunta para diferentes modelos de IA**
- **Avaliação da clareza e coerência das respostas** utilizando o índice de Flesch
- **Comparação automática das respostas** com base na legibilidade
- **Autoavaliação assistida por IA**, onde um dos modelos avalia e ranqueia as respostas
- **Uso da API OpenRouter**, permitindo acesso a múltiplos modelos de IA em uma única integração

---

## 🚀 Como Executar

### **1️⃣ Pré-requisitos**
Antes de rodar o código, instale as dependências necessárias:
```bash
pip install requests python-dotenv textstat
```
### **2️⃣ Obtenha a API Key do OpenRouter**

- Acesse OpenRouter
- Crie uma conta (se ainda não tiver)
- Gere uma API Key
- Copie essa chave e crie um arquivo chamado .env na raiz do projeto com o seguinte conteúdo: ```OPENROUTER_API_KEY=sua-chave-aqui```

### **3️⃣ Execute o código**

Para rodar o script e obter as comparações entre os modelos, utilize:
```bash
python desafio.py
```
O código exibirá as respostas dos modelos, a avaliação de clareza e a autoavaliação assistida por IA.

---

## 📊 Conclusões

Este projeto permitiu a comparação entre diferentes Modelos de Linguagem, destacando diferenças em clareza, coerência e detalhamento das respostas. O uso do OpenRouter facilitou a integração com múltiplos modelos sem precisar de múltiplas chaves de API. Além disso, a avaliação automática demonstrou que cada modelo pode ter um desempenho diferente dependendo do tipo de pergunta feita.

O desafio reforça a importância de avaliar criticamente as respostas geradas por IA, pois cada modelo pode apresentar viéses e variações na qualidade das informações. 🚀

---

## 📄 Licença

Este projeto foi desenvolvido para o Desafio Cognitiva Brasil e está disponível sob a licença MIT.
