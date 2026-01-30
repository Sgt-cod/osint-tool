# 🚀 GUIA DE INSTALAÇÃO RÁPIDA

## Passo a Passo Completo (10 minutos)

### 📋 Pré-requisitos
- Conta no GitHub (gratuita)
- Navegador web

---

## 1️⃣ CRIAR REPOSITÓRIO NO GITHUB

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name**: `osint-tool` (ou outro nome)
   - **Description**: `Ferramenta OSINT gratuita`
   - ✅ **Public** (marque esta opção)
   - ✅ **Add a README file** (opcional)
3. Clique em **Create repository**

---

## 2️⃣ FAZER UPLOAD DOS ARQUIVOS

### Opção A: Upload Manual (Mais Fácil)

1. No seu repositório, clique em **Add file** → **Upload files**
2. Arraste todos os arquivos desta pasta:
   ```
   .github/
   docs/
   osint_search.py
   README.md
   .gitignore
   ```
3. Clique em **Commit changes**

### Opção B: Git CLI (Avançado)

```bash
git clone https://github.com/SEU-USUARIO/osint-tool.git
cd osint-tool
# Copie todos os arquivos para esta pasta
git add .
git commit -m "Initial commit"
git push
```

---

## 3️⃣ HABILITAR GITHUB PAGES

1. No seu repositório, clique em **⚙️ Settings**
2. No menu lateral, clique em **Pages**
3. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/docs`
4. Clique em **Save**
5. ⏱️ Aguarde 1-2 minutos
6. Aparecerá: "Your site is live at https://SEU-USUARIO.github.io/osint-tool/"

---

## 4️⃣ HABILITAR ISSUES

1. Ainda em **⚙️ Settings**
2. Role até **Features**
3. Marque ✅ **Issues**

---

## 5️⃣ CONFIGURAR PERMISSÕES

1. Em **⚙️ Settings**
2. No menu lateral, clique em **Actions** → **General**
3. Role até **Workflow permissions**
4. Selecione: `Read and write permissions`
5. Marque ✅ **Allow GitHub Actions to create and approve pull requests**
6. Clique em **Save**

---

## 6️⃣ CONFIGURAR A INTERFACE

1. No seu repositório, abra o arquivo: `docs/index.html`
2. Clique no ícone de lápis (✏️ Edit)
3. Encontre as linhas (por volta da linha 350):

```javascript
const GITHUB_CONFIG = {
    owner: 'SEU-USUARIO',      // ← ALTERE AQUI
    repo: 'SEU-REPOSITORIO',   // ← ALTERE AQUI
    token: ''
};
```

4. Altere para:
```javascript
const GITHUB_CONFIG = {
    owner: 'seu-usuario-github',  // seu username do GitHub
    repo: 'osint-tool',           // nome do repositório que criou
    token: ''
};
```

5. Clique em **Commit changes**
6. Clique em **Commit changes** novamente

---

## 7️⃣ TESTAR!

### Teste 1: Acessar Interface

1. Acesse: `https://SEU-USUARIO.github.io/osint-tool/`
2. Você deve ver a interface roxa bonita

### Teste 2: Criar Busca

1. Digite um username (ex: `github`)
2. Clique em **Iniciar Investigação**
3. Deve aparecer mensagem de sucesso

### Teste 3: Ver Resultado

1. Clique na aba **Actions** no seu repositório
2. Você verá o workflow rodando (amarelo 🟡)
3. Aguarde 2-5 minutos até ficar verde (✅)
4. Volte na interface e clique em **Ver Todos os Relatórios**
5. Clique no relatório gerado

---

## ✅ PRONTO!

Sua ferramenta OSINT está funcionando!

### 📱 Adicionar no Celular

**Android:**
1. Abra o site no Chrome
2. Menu (⋮) → "Adicionar à tela inicial"

**iPhone:**
1. Abra o site no Safari
2. Ícone compartilhar (□↑) → "Adicionar à Tela de Início"

---

## 🎯 URLs IMPORTANTES

Substitua `SEU-USUARIO` e `osint-tool`:

- 🌐 **Interface**: `https://SEU-USUARIO.github.io/osint-tool/`
- 📊 **Relatórios**: `https://SEU-USUARIO.github.io/osint-tool/reports/reports_index.html`
- 🔧 **Repositório**: `https://github.com/SEU-USUARIO/osint-tool`
- ⚙️ **Actions**: `https://github.com/SEU-USUARIO/osint-tool/actions`

---

## ❓ PROBLEMAS COMUNS

### "404 - Page Not Found"
- ✅ Aguarde 2-3 minutos após habilitar Pages
- ✅ Verifique se selecionou a pasta `/docs`
- ✅ Limpe cache do navegador (Ctrl+F5)

### Workflow não executa
- ✅ Verifique se Issues estão habilitadas
- ✅ Verifique permissões em Actions
- ✅ Veja logs na aba Actions

### "Erro ao criar issue"
- ✅ Verifique se alterou GITHUB_CONFIG corretamente
- ✅ Confirme que Issues estão habilitadas
- ✅ Pressione F12 e veja console

### Relatório não aparece
- ✅ Aguarde 3-5 minutos após criar issue
- ✅ Verifique aba Actions se workflow terminou
- ✅ Limpe cache e recarregue página

---

## 💡 DICAS

1. **Use usernames conhecidos** para teste (ex: `github`, `google`)
2. **Não abuse**: Você tem 2000 minutos/mês grátis
3. **Relatórios são públicos**: Use repositório privado se precisar privacidade
4. **Personalize**: Altere cores, textos, logos à vontade!

---

## 🆘 PRECISA DE AJUDA?

1. Veja os logs na aba **Actions**
2. Abra uma Issue no repositório original
3. Consulte o README.md completo

---

**🎉 Divirta-se investigando! 🔍**
