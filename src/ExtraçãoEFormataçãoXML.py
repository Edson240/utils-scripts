from bs4 import BeautifulSoup
import re
import os

# Caminhos dos arquivos
arquivo_entrada = r"../data/exemplo_entrada.xml"
arquivo_saida = r"../data/cli_limitado.xml"

# Verifica se o arquivo de entrada existe
if not os.path.exists(arquivo_entrada):
    print(f"❌ Arquivo de entrada não encontrado: {arquivo_entrada}")
else:
    with open(arquivo_entrada, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Regex para pegar tudo entre <Cli ...> e </Cli>, mesmo com várias linhas
    blocos_cli = re.findall(r"<Cli\b[^>]*>.*?</Cli>", conteudo, re.DOTALL | re.IGNORECASE)

    if not blocos_cli:
        print("❌ Nenhuma tag <Cli> encontrada no arquivo.")
    else:
        # Pega os primeiros 20, para pegar mais so trocar o número para pegar blocos maiores
        blocos_limitados = blocos_cli[:20]

        # Remove quebras de linha e junta tudo em linha unica
        linha_unica = "".join(bloco.replace("\n", "").replace("\r", "") for bloco in blocos_limitados)

        # Escreve no arquivo de saída para não alterar o arquivo original 
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write(linha_unica)

        print(f"✅ Sucesso! {len(blocos_limitados)} blocos <Cli> salvos em linha única no arquivo: {arquivo_saida}")

# Caminhos dos arquivos
arquivo_entrada = r"../data/cli_limitado.xml"
arquivo_saida = r"../data/cli_formatado.xml"

# Lê o conteúdo dos <Cli>
with open(arquivo_entrada, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Adiciona tag raiz temporária só para parsing
conteudo_completo = f"<Clientes>{conteudo}</Clientes>"

# Formata com BeautifulSoup
soup = BeautifulSoup(conteudo_completo, "xml")

# Extrai as tag <Cli>
blocos_cli = soup.Clientes.find_all("Cli")

# Gera a saída formatada apenas com os blocos <Cli>
xml_formatado = "".join(bloco.prettify() for bloco in blocos_cli)

# Salva no novo arquivo
with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write(xml_formatado)

print(f"✅ XML formatado sem tag raiz salvo em: {arquivo_saida}")

