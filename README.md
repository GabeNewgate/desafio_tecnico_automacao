# Desafio Técnico: Automação de Consulta e Extração de Dados

Este projeto contém uma solução para o desafio técnico proposto, focado na automação de login, extração e processamento de dados de um site de e-commerce de teste, e aplicação de uma regra de negócio para seleção de produtos.

## Sumário

- [Visão Geral](#visão-geral)
- [Requisitos do Ambiente](#requisitos-do-ambiente)
- [Instalação](#instalação)
- [Execução](#execução)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Arquivos de Saída](#arquivos-de-saída)
- [Considerações Finais](#considerações-finais)

## Visão Geral

A automação realiza as seguintes etapas:

1.  **Login**: Autentica no site `https://www.saucedemo.com/` com credenciais pré-definidas.
2.  **Extração de Dados**: Navega até a página de produtos e extrai o nome e o preço de cada item.
3.  **Processamento de Dados**: Converte os preços extraídos para um formato numérico (float).
4.  **Regra de Negócio**: Adiciona ao carrinho apenas os produtos cujo preço é inferior a $20.00.
5.  **Geração de Saída**: Gera dois arquivos de saída: um CSV com todos os produtos e seus preços numéricos, e um TXT com os nomes dos produtos selecionados.

## Requisitos do Ambiente

Para executar este projeto, você precisará ter instalado:

-   Python 3.x
-   pip (gerenciador de pacotes do Python)

## Instalação

1.  **Clone o repositório** (se aplicável, ou crie um diretório para o projeto):

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <DIRETORIO_DO_PROJETO>
    ```

2.  **Crie e ative um ambiente virtual** (recomendado):

    ```bash
    python3 -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/macOS:
    source venv/bin/activate
    ```

3.  **Instale as dependências**:

    ```bash
    pip install selenium pandas
    ```

## Execução

Para executar a automação, navegue até o diretório raiz do projeto e execute o seguinte comando:

```bash
python main.py
```

## Estrutura do Projeto

```
.
├── main.py
└── README.md
```

-   `main.py`: Contém o código principal da automação, incluindo a lógica de login, extração, processamento e geração de arquivos.
-   `README.md`: Este arquivo de documentação.

## Arquivos de Saída

Após a execução, dois arquivos serão gerados no mesmo diretório do script `main.py`:

-   `todos_os_produtos.csv`: Um arquivo CSV contendo duas colunas: `Nome` e `Preco_Numerico`. Lista todos os produtos encontrados no site com seus preços convertidos.
-   `produtos_selecionados.txt`: Um arquivo de texto simples, onde cada linha contém o nome de um produto que foi adicionado ao carrinho (ou seja, com preço inferior a $20.00).

## Considerações Finais

O protótipo foi desenvolvido utilizando o Selenium WebDriver para interação com o navegador e o Pandas para manipulação de dados. A abordagem de seleção de elementos foi baseada em IDs e nomes de classes para garantir robustez. O modo headless do Chrome foi utilizado para execução em segundo plano.


