# Vamos-Joga-Minecraft-Bot
Bot feito para Erikcraft

## 🧠 Funcionalidades Principais

### 🔧 Moderação Avançada
- Comandos via `/modpainel` com botões interativos: `Banir`, `Expulsar`, `Mutar`
- Sistema de mute real (castigo nativo do Discord)
- Logs completos com embeds detalhados
- Mensagens diretas para o usuário punido, com link de apelação personalizado

### 🛠️ Painel Interativo
- Embed com informações do usuário:
  - Menção, apelido, ID, data de criação, entrada no servidor
- Interface com botões para ações rápidas de moderação
- Tudo efêmero (só visível para quem executa)

### ✏️ Criador de Embeds
- Comando `/embed` abre um painel onde o usuário pode:
  - Definir título, descrição, cor, imagem, thumbnail
  - Visualizar o embed em tempo real antes de enviar

### 🚀 Incentivo a Boost
- Sistema automático que envia mensagens criativas incentivando o boost a cada X mensagens
- Variações armazenadas em vetor (`booster = []`)
- Canal de boost mencionado diretamente

## 📁 Estrutura do Projeto

```bash
bot/
├── cogs/
│   ├── mod.py              # Comandos de moderação (painel, punições)
│   ├── embed_creator.py    # Criador de embeds interativos
│   ├── booster.py          # Mensagens automáticas de incentivo ao boost
│   └── ...                 # Outros Cogs futuros
├── config.py               # Variáveis de configuração (token, IDs, link de apelação)
├── main.py                 # Arquivo principal de inicialização do bot
├── requirements.txt        # Dependências do projeto
└── README.md               # Você está aqui
```

🧩 Requisitos
Python 3.10+


discord.py 2.3+


Permissões de administrador para testes


Instale com:
pip install -r requirements.txt

🧠 Como Usar
Clone o repositório e crie seu ambiente virtual


Preencha config.py com:

 TOKEN = "seu-token-aqui"
GUILD_ID = 1234567890
link_apelacao = "https://seulink.com"


Rode o bot:

 python main.py


📌 Observações
O sistema de mute usa timeout real do Discord, não apenas cargos

A maioria das respostas são efêmeras para manter a interface limpa

O bot possui uma personalidade sarcástica e filosófica, como configurado

