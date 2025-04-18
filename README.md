# XML CLI Processor

Scripts para tratamento, extração, formatação e concatenação de arquivos XML contendo múltiplos blocos `<Cli>`. Ideal para processar grandes volumes de dados em linha única e organizar os arquivos para análise ou importação em sistemas.

## 🚀 Funcionalidades

- 🧩 Extração de blocos `<Cli>` com tags aninhadas (ajustável)
- 📦 Limitação de até 20 blocos por arquivo (ajustável)
- 🧼 Formatação XML com indentação e limpeza
- ⚡ Processamento rápido mesmo com arquivos grandes
- 🔄 Concatenação de arquivos XML Adiciona dados de arquivos complementares ao arquivo base

## 📂 Estrutura

- **`src/`**: Contém todos os scripts responsáveis pelo processamento dos arquivos XML. 
    - `extrair_cli.py` - Extrai e salva os blocos `<Cli>` a partir de um XML grande.
    - `formatar_cli.py` - Formata os blocos extraídos, aplicando indentação e limpeza do XML.
    - `extrairEFormatar_cli.py` - Combina a extração e a formatação em um único processo.
    - `concatenar.py` - Concatena arquivos XML base e complementar, mesclando-os conforme a necessidade.
 
- **`data/`**: Contém os arquivos de entrada e saída do processo.
    - `exemplo_entrada.xml` - Exemplo de arquivo XML bruto em linha única.
    - `cli_limitado.xml` - Arquivo XML `base` que foi extraido de acordo com a quantidade definada e será formatado.
    - `cli_formatado.xml` - Arquivo XML `base` que foi formatado e será utilizado para a concatenação.
    - `complementar.xml` - Arquivo complementar que será adicionado ao arquivo `cli_formatado` que foi extraido do arquivo bruto e formatado mantendo o padrão.
    - `saida.xml` - Arquivo de saída após o processamento da concatenação.
    - `saida_formatado.xml` - Arquivo de saída após formatar.

## 🛠 Requisitos

- Python 3.7+
- BeautifulSoup4
- lxml

Instale com:

```bash
pip install beautifulsoup4 lxml
