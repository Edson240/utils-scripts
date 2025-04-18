from bs4 import BeautifulSoup

# Caminhos dos arquivos
arquivo_entrada = "../data/cli_limitado.xml"
arquivo_saida = "../data/cli_formatado.xml"

# Lê o conteúdo dos <Cli>
with open(arquivo_entrada, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Adiciona tag raiz temporária só para parsing
conteudo_completo = f"<Clientes>{conteudo}</Clientes>"

# Formata com BeautifulSoup
soup = BeautifulSoup(conteudo_completo, "xml")

# Extrai apenas os filhos da tag <Clientes>
blocos_cli = soup.Clientes.find_all("Cli")

# Gera a saída formatada apenas com os blocos <Cli> (sem <Clientes>)
xml_formatado = "\n\n".join(bloco.prettify() for bloco in blocos_cli)

# Salva no novo arquivo
with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write(xml_formatado)

print(f"✅ XML formatado sem tag raiz salvo em: {arquivo_saida}")
