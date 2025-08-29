## 🧪 Desafio Técnico — Automação de Consulta e Extração de Dados

Bem-vindo(a)! Este repositório contém as instruções do teste prático para candidatos(as) à vaga de desenvolvimento.

O objetivo é avaliar sua capacidade de automatizar login, navegar, extrair, processar dados e aplicar uma regra de negócio simples, gerando saídas organizadas.

### 📚 Contexto
Somos uma promotora de crédito e precisamos consultar informações em um portal parceiro para validar dados. Seu desafio é criar um robô que execute os passos abaixo usando um site público de testes.

### 🌐 Site de Teste
- Use o `https://www.saucedemo.com/` (e-commerce de testes com login).
- As credenciais ficam na própria página. Exemplos úteis:
  - 👤 Usuário: `standard_user`
  - 🔑 Senha: `secret_sauce`

### ✅ Requisitos do Desafio
1. 🔐 Login
   - Acesse a página de login e autentique com as credenciais fornecidas.
   - O robô deve identificar e validar se o login foi bem-sucedido.

2. 🧾 Extração de Dados
   - Após o login, navegue até a página de produtos.
   - Extraia para cada produto: `Nome` e `Preço`.

3. 🧮 Processamento de Dados
   - Remova o cifrão `$` do preço.
   - Converta o preço para um número (float/decimal).

4. ⚖️ Regra de Negócio (Ação Condicional)
   - 🛒 Adicione ao carrinho apenas os produtos com preço menor que `$20.00`.

5. 📄 Geração de Saída
   - Gere os arquivos ao final da execução:
     - `todos_os_produtos.csv`: colunas `Nome` e `Preco_Numerico`.
     - `produtos_selecionados.txt`: relação simples dos nomes dos produtos adicionados ao carrinho.

### 🧰 Linguagem e Ferramentas
- Use a linguagem na qual você é mais produtivo(a). Python é uma ótima opção.
- Ferramentas sugeridas (não obrigatório):
  - Python: Selenium, Playwright, Requests (quando aplicável), Pandas (para CSV).
  - Node.js/TS: Playwright, Puppeteer.
  - Outras stacks são bem-vindas se cumprirem os requisitos.

### 📦 O que esperamos no repositório
- Código-fonte completo da automação.
- Um `README.md` próprio explicando:
  - Pré-requisitos de ambiente.
  - Como instalar dependências.
  - Como executar o robô (comando único preferencial).
  - Como configurar variáveis de ambiente (se houver).
- Os arquivos de saída gerados (`todos_os_produtos.csv` e `produtos_selecionados.txt`) não precisam ser commitados, mas descreva onde serão criados.

### 🧭 Critérios de Avaliação
- Correção funcional (login, extração, processamento, regra de negócio, geração de arquivos).
- Clareza e organização do código (nomes, estruturas, modularização).
- Robustez (tratamento de erros, esperas explícitas/implícitas, seletor resiliente).
- Reprodutibilidade (facilidade de executar do zero seguindo seu README).
- Boas práticas (separação de camadas, logs mínimos, formatação/linters, `.gitignore`).
- Testes (bônus se incluir testes automatizados para partes críticas/parse e regras).

### ✨ Bônus (opcional)
- Containerização com Docker (execução em um único comando).
- Pipeline simples de CI (lint/test/build).
- Parametrização de ambiente (ex.: usuários diferentes por variável de ambiente).

### 🚧 Limites e Escopo
- Evite over-engineering. Mire em conclusão entre 2 a 4 horas.
- Documente rapidamente escolhas e trade-offs no seu README.

### 🚀 Como Entregar
1. Faça um fork deste repositório.
2. Implemente a solução no seu fork.
3. Atualize o seu `README.md` com instruções de execução claras.
4. Envie o link do seu repositório (GitHub/GitLab) para avaliação.

### 🗂️ Sugestão de Estrutura (opcional)
```
.
├─ src/                  # seu código-fonte
├─ tests/                # seus testes (opcional)
├─ README.md             # instruções de execução do candidato
├─ requirements.txt      # se usar Python (opcional)
└─ package.json          # se usar Node.js (opcional)
```

### ▶️ Diretrizes de Execução (exemplo em Python — opcional)
- Documente no seu README algo como:
  - Criação de ambiente: `python -m venv .venv && .venv\\Scripts\\activate` (Windows) ou `source .venv/bin/activate` (Unix)
  - Instalação: `pip install -r requirements.txt`
  - Execução: `python -m src.main`

Boa sorte! Estamos interessados em ver seu raciocínio, organização e qualidade de entrega tanto quanto o resultado final.


