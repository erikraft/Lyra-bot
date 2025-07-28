# Vamos-Joga-Minecraft-Bot
Bot feito para ErikrafT

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
│   ├── mod.py                     # Comandos de moderação (painel, punições)
│   ├── embed_creator.py           # Criador de embeds interativos
│   ├── main.py (booster = [)    # Mensagens automáticas de incentivo ao boost
│   └── ...                        # Outros Cogs futuros
├── config.py                      # Variáveis de configuração (token, IDs, link de apelação)
├── main.py                        # Arquivo principal de inicialização do bot
├── requirements.txt               # Dependências do projeto
└── README.md                      # Você está aqui
```

## 🧩 Requisitos

* Python 3.10+
* [discord.py 2.3+](https://pypi.org/project/discord.py/)
* Permissões de administrador para testes

Instale com:

```bash
pip install -r requirements.txt
```

## 🧠 Como Usar

1. Clone o repositório e crie seu ambiente virtual
2. Preencha `config.py`
3. Rode o bot:

   ```bash
   python main.py
   ```

## 📌 Observações

* O sistema de mute usa `timeout` real do Discord, não apenas cargos
* A maioria das respostas são efêmeras para manter a interface limpa




---

### 📄 Variáveis de Configuração do Bot

```python
ID_SERVIDOR = 1121464803941171270
```

**Identificador do servidor Discord principal** onde o bot será executado.

```python
ID_CANAL_PAINEL_TICKETS = 1309586413422907452
```

Canal onde o **painel de criação de tickets** será exibido aos usuários.

```python
ID_CARGO_ATENDENTE = 1138938495428214824
```

Cargo atribuído aos **atendentes**, responsáveis por responder e gerenciar tickets.

```python
BOT_TOKEN = "##"
```

**Token de autenticação do bot.** Nunca compartilhe este valor publicamente.

```python
ID_CANAL_LOGS_PUNICOES = 1161375392582619206
```

Canal onde os **logs de punições** (como banimentos e silenciamentos) serão registrados automaticamente.

```python
ID_CANAL_MODERACAO = 1398446601072283758
```

Canal privado da **equipe de moderação**, usado para discussões internas e controle.

```python
LINK_FORMULARIO_APELACAO = "https://form.jotform.com/242088340178054"
```

Link para o **formulário de apelação**, onde usuários punidos podem contestar suas punições.

