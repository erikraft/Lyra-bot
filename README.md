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
