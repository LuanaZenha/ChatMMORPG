# 🧙‍♂️ Chat MMORPG com FastAPI e MongoDB Atlas

Um **chat em tempo real com temática de RPG**, construído com uma arquitetura moderna usando **FastAPI (Python)**.  
O histórico de mensagens é persistido no **MongoDB Atlas**, garantindo que as conversas nunca se percam.

O **front-end** é feito em **HTML, CSS e JavaScript puros**, trazendo a experiência de um chat de MMORPG

---

## ✨ Funcionalidades

- 📜 **Persistência de Mensagens**: histórico salvo em um banco NoSQL na nuvem (MongoDB Atlas).  
- ⚡ **Chat em Tempo Real**: comunicação instantânea via WebSockets.  
- 🗂️ **Estrutura Escalável**: código modularizado seguindo boas práticas de FastAPI.  
- 💬 **Múltiplas Salas**: canais como **Geral, Leilão, Guilda e Sussurro**.  
- 👥 **Contador de Usuários**: mostra quantos estão conectados em cada sala.  
- 🔔 **Mensagens de Sistema**: notificações ao entrar/sair de canais.  
- 🗄️ **Cache de Histórico**: troca de abas sem perder mensagens da sessão.  
- 🧹 **Limpar Chat**: botão para limpar o canal atual.  

---

## 🛠️ Tecnologias Utilizadas

### Back-end
- Python 3.9+  
- [FastAPI]
- [Uvicorn]  
- [Motor]
- [Pydantic]
- [python-dotenv]  

### Banco de Dados
- [MongoDB Atlas](https://www.mongodb.com/atlas)  

### Front-end
- HTML5, CSS3, JavaScript (Vanilla)  
- [Google Fonts](https://fonts.google.com/)  
- [Font Awesome](https://fontawesome.com/)  

---

## 🚀 Como Rodar o Projeto

### 📋 Pré-requisitos
- Python **3.8+** instalado  
- Conta gratuita no **MongoDB Atlas**  
- Connection String do seu cluster  

---

### ⚙️ Instalação

#### 1. Estrutura de Pastas
Monte os diretórios do projeto conforme a organização definida em aula.  

#### 2. Variáveis de Ambiente
Na raiz do projeto (`CHAT/`), crie um arquivo `.env` com o seguinte conteúdo:

```env
MONGODB_URL="mongodb+srv://<user>:<password>@<cluster-url>/<database-name>?retryWrites=true&w=majority"
Substitua os valores <...> pela sua connection string real do MongoDB Atlas.

3. Dependências
Crie um arquivo requirements.txt com:

txt
Copiar código
fastapi>=0.115
uvicorn[standard]>=0.30
motor>=3.4
python-dotenv>=1.0

4. Ambiente Virtual e Instalação
bash
Copiar código
# Criar e ativar ambiente virtual
python -m venv venv
.\venv\Scripts\activate   # Windows
# source venv/bin/activate   # macOS/Linux

# Instalar dependências
pip install -r requirements.txt
▶️ Execução
Inicie o servidor com:

bash
Copiar código
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Depois, abra o navegador em:

👉 http://localhost:8000

🎮 Experiência de Uso
O chat simula um MMORPG clássico:

Abra diferentes abas de canais (Geral, Guilda, etc.).

Converse em tempo real com outros usuários.

Receba notificações de entrada/saída.

Experimente o estilo pergaminho medieval na interface.

📌 Próximos Passos
Melhorar design do front-end (animações e sons de RPG).

Adicionar suporte a emojis e markdown.

Criar sistema de login com personagens.

👤 Autor: Seu Nome Aqui
📧 Contato: seu-email@exemplo.com

