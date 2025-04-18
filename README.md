# XML CLI Processor

Scripts para tratamento, extração e formatação de arquivos XML contendo múltiplos blocos `<Cli>`. Ideal para processar grandes volumes de dados em linha única e organizar os arquivos para análise ou importação em sistemas.

## 🚀 Funcionalidades

- 🧩 Extração de blocos `<Cli>` com tags aninhadas (ajustável)
- 📦 Limitação de até 20 blocos por arquivo (ajustável)
- 🧼 Formatação XML com indentação e limpeza 
- ⚡ Processamento rápido mesmo com arquivos grandes

## 📂 Estrutura

- `extrair_cli.py` – Extrai e salva blocos `<Cli>` com limite por arquivo
- `formatar_cli.py` – Formata os blocos extraídos em XML indentado
- `extrairEFormatar_cli.py` – Extrai e salva blocos `<Cli>` com limite por arquivo e formata os blocos extraídos em XML indentado
- `entrada.xml` – XML bruto em linha única (exemplo)
- `saida.xml` – XML processado com os blocos organizados

## 🛠 Requisitos

- Python 3.7+
- BeautifulSoup4
- lxml

Instale com:

```bash
pip install beautifulsoup4 lxml