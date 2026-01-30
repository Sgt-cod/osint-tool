# 🔍 OSINT Username Search Tool

Ferramenta de investigação OSINT totalmente gratuita usando **GitHub Pages** + **GitHub Actions** + **Maigret** + **Sherlock**.

## ✨ Características

- 🆓 **100% Gratuito** - Sem custos de hospedagem ou domínio
- 📱 **PWA** - Funciona como app no celular
- 🤖 **Automatizado** - GitHub Actions processa tudo
- 🔍 **Dupla Investigação** - Maigret + Sherlock
- 📊 **Relatórios HTML** - Interface moderna e responsiva
- 🔒 **Privado** - Seus dados ficam no seu repositório

## 🚀 Instalação Rápida

### 1️⃣ Criar Repositório

```bash
# No seu GitHub, crie um novo repositório público
# Nome sugerido: osint-tool
```

### 2️⃣ Fazer Upload dos Arquivos

Faça upload de todos os arquivos deste projeto para seu repositório:

```
osint-tool/
├── .github/
│   └── workflows/
│       └── osint-search.yml
├── docs/
│   ├── index.html
│   ├── manifest.json
│   └── sw.js
├── osint_search.py
└── README.md
```

### 3️⃣ Configurar GitHub Pages

1. Vá em **Settings** → **Pages**
2. Em **Source**, selecione: `Deploy from a branch`
3. Em **Branch**, selecione: `main` e pasta `/docs`
4. Clique em **Save**

### 4️⃣ Habilitar Issues

1. Vá em **Settings** → **General**
2. Em **Features**, marque ✅ **Issues**

### 5️⃣ Configurar Permissões do Workflow

1. Vá em **Settings** → **Actions** → **General**
2. Em **Workflow permissions**, selecione: `Read and write permissions`
3. Marque ✅ **Allow GitHub Actions to create and approve pull requests**
4. Clique em **Save**

### 6️⃣ Atualizar a Interface

Edite o arquivo `docs/index.html` e altere as linhas:

```javascript
const GITHUB_CONFIG = {
    owner: 'SEU-USUARIO',      // ← Seu username do GitHub
    repo: 'SEU-REPOSITORIO',   // ← Nome do repositório (ex: osint-tool)
    token: ''
};
```

Exemplo:
```javascript
const GITHUB_CONFIG = {
    owner: 'joaosilva',
    repo: 'osint-tool',
    token: ''
};
```

## 📱 Como Usar

### Opção 1: Interface Web (Recomendado)

1. Acesse: `https://SEU-USUARIO.github.io/SEU-REPOSITORIO/`
2. Digite o username que deseja investigar
3. Clique em "Iniciar Investigação"
4. Aguarde 2-5 minutos
5. Acesse o relatório gerado

### Opção 2: Criar Issue Manualmente

1. Vá na aba **Issues** do repositório
2. Clique em **New Issue**
3. No título, digite: `@username` (substitua username)
4. Clique em **Submit new issue**
5. O workflow será acionado automaticamente

### Opção 3: Manual Dispatch (Avançado)

1. Vá na aba **Actions**
2. Selecione **OSINT Username Search**
3. Clique em **Run workflow**
4. Digite o username
5. Clique em **Run workflow**

## 📊 Acessar Relatórios

Os relatórios são salvos em:

- **Relatório individual**: `https://SEU-USUARIO.github.io/SEU-REPOSITORIO/reports/USERNAME_report.html`
- **Índice de relatórios**: `https://SEU-USUARIO.github.io/SEU-REPOSITORIO/reports/reports_index.html`

## 📱 Instalar como App no Celular

### Android (Chrome)

1. Acesse o site pelo Chrome
2. Toque no menu (⋮)
3. Selecione "Adicionar à tela inicial"
4. Confirme

### iOS (Safari)

1. Acesse o site pelo Safari
2. Toque no ícone de compartilhar (□↑)
3. Selecione "Adicionar à Tela de Início"
4. Confirme

## 🛠️ Ferramentas Utilizadas

- **[Maigret](https://github.com/soxoj/maigret)** - Busca usernames em +2500 sites
- **[Sherlock](https://github.com/sherlock-project/sherlock)** - Busca usernames em +300 sites
- **GitHub Actions** - Execução automatizada
- **GitHub Pages** - Hospedagem gratuita

## 🔧 Estrutura do Projeto

```
├── .github/workflows/
│   └── osint-search.yml        # Workflow do GitHub Actions
├── docs/
│   ├── index.html              # Interface PWA
│   ├── manifest.json           # Configuração PWA
│   ├── sw.js                   # Service Worker
│   └── reports/                # Relatórios gerados (auto-criado)
├── osint_search.py             # Script Python principal
└── README.md                   # Este arquivo
```

## 🎯 Fluxo de Trabalho

```
┌─────────────────┐
│  Usuário acessa │
│   interface web │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Cria Issue ou  │
│  usa Dispatch   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GitHub Actions  │
│   é acionado    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Instala Python │
│ Maigret+Sherlock│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Executa busca   │
│  no username    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Gera relatório │
│   HTML + JSON   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Commit no repo  │
│  Publica Pages  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Usuário acessa  │
│    relatório    │
└─────────────────┘
```

## ⚙️ Customização

### Timeout das Ferramentas

Edite `osint_search.py`:

```python
# Linha com --timeout
['maigret', username, '--json', 'simple', '--timeout', '10'],  # Altere 10 para outro valor
['sherlock', username, '--timeout', '10', '--print-found'],     # Altere 10 para outro valor
```

### Design do Relatório

Edite a função `generate_html_report()` em `osint_search.py` para personalizar cores, layout, etc.

### Interface Web

Edite `docs/index.html` para alterar cores, textos, e estilo.

## 🔒 Segurança e Privacidade

- ✅ Não requer API keys ou tokens
- ✅ Dados ficam no seu repositório
- ✅ Você controla tudo
- ⚠️ Repositório público = Relatórios públicos
- 💡 Para privacidade total, use repositório privado (GitHub Actions funciona igual)

## ❓ Troubleshooting

### Workflow não executa

1. Verifique se Issues estão habilitadas
2. Verifique permissões em Settings → Actions
3. Veja logs na aba Actions

### Relatório não aparece

1. Aguarde 3-5 minutos
2. Limpe cache do navegador
3. Verifique se o commit foi feito
4. Veja logs do workflow

### "404 Page Not Found"

1. Verifique se GitHub Pages está habilitado
2. Confirme que a pasta é `/docs`
3. Aguarde alguns minutos após habilitar

### Interface não cria Issue

1. Verifique se alterou `GITHUB_CONFIG` corretamente
2. Confirme que Issues estão habilitadas
3. Veja console do navegador (F12)

## 📝 Limitações

- ⏱️ GitHub Actions: 2000 minutos/mês (gratuito)
- 📦 Cada busca leva 2-5 minutos
- 🔄 ~400-600 buscas/mês possíveis
- 📊 Ideal para investigações pontuais, não para monitoramento contínuo

## 🤝 Contribuindo

Sinta-se livre para fazer fork e melhorar o projeto!

## 📄 Licença

MIT License - Use livremente!

## 🎓 Uso Ético

Esta ferramenta é para fins educacionais e investigação legítima. Use com responsabilidade e respeite a privacidade das pessoas.

---

**Desenvolvido com ❤️ para a comunidade OSINT**

🔗 GitHub: `https://github.com/SEU-USUARIO/SEU-REPOSITORIO`
🌐 Site: `https://SEU-USUARIO.github.io/SEU-REPOSITORIO`
