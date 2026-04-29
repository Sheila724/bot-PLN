# TechBot 🤖 — Suporte de TI Universitário

Chatbot de suporte técnico universitário desenvolvido com **Rasa Open Source**.

## 📁 Estrutura do Projeto

```
rasa_chatbot/
├── actions/
│   ├── __init__.py
│   └── actions.py          # Ações customizadas
├── data/
│   ├── nlu.yml             # Exemplos de treinamento (intents)
│   ├── stories.yml         # Fluxos de conversa
│   └── rules.yml           # Regras de resposta
├── config.yml              # Pipeline de NLP e políticas
├── credentials.yml         # Canais de comunicação (REST)
├── domain.yml              # Intents, respostas e configurações
└── endpoints.yml           # Endpoint do servidor de ações
```

## 🤖 Tópicos Suportados

| Intenção | Descrição |
|----------|-----------|
| Wi-Fi | Problemas de conexão à rede sem fio |
| E-mail | Configuração e acesso ao e-mail institucional |
| Senha | Redefinição e recuperação de senha |
| Software | Softwares e licenças disponíveis para alunos |
| Impressora | Instalação e problemas com impressoras |
| Moodle/AVA | Acesso e problemas no ambiente virtual |
| Matrícula | Sistema de matrícula online |
| Portal | Portal do aluno |
| PC Lento | Otimização de desempenho |
| VPN | Configuração de acesso remoto |
| Antivírus | Proteção e remoção de vírus |
| Contato/Horário | Informações do suporte de TI |

## ⚙️ Instalação

### 1. Instalar o Rasa

```bash
pip install rasa
```

> **Recomendado:** Python 3.8 ou 3.9 (Rasa pode ter incompatibilidades com versões mais recentes)

### 2. Entrar na pasta do projeto

```bash
cd rasa_chatbot
```

### 3. Treinar o modelo

```bash
rasa train
```

## 🚀 Executar o Chatbot

### Terminal 1 — Servidor principal do Rasa

```bash
rasa run --enable-api --cors "*"
```

### Terminal 2 — Servidor de ações customizadas

```bash
rasa run actions
```

### Interface Web

Abra o arquivo `chat.html` (na pasta raiz do projeto) em qualquer navegador.

> O arquivo se conecta automaticamente ao Rasa em `http://localhost:5005`

## 💬 Testar pelo terminal (sem interface)

```bash
rasa shell
```

## 🧪 Testar a NLU isoladamente

```bash
rasa shell nlu
```

## 📊 Avaliar o modelo

```bash
rasa test
```

## 🛠️ Adicionar novos tópicos

1. Adicione a nova `intent` no arquivo `data/nlu.yml` com pelo menos **10 exemplos**
2. Adicione a resposta `utter_nova_intent` no `domain.yml`
3. Adicione uma regra em `data/rules.yml`
4. Registre a intent na lista de `intents` do `domain.yml`
5. Execute `rasa train` novamente
