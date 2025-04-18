import re
import os

# Caminhos dos arquivos
arquivo_entrada = "../data/exemplo_entrada.xml"
arquivo_saida = "../data/cli_limitado.xml"

# Verifica se o arquivo de entrada existe
if not os.path.exists(arquivo_entrada):
    print(f"❌ Arquivo de entrada não encontrado: {arquivo_entrada}")
else:
    with open(arquivo_entrada, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Regex melhorada para pegar tudo entre <Cli ...> e </Cli>, mesmo com várias linhas
    blocos_cli = re.findall(r"<Cli\b[^>]*>.*?</Cli>", conteudo, re.DOTALL | re.IGNORECASE)

    if not blocos_cli:
        print("❌ Nenhuma tag <Cli> encontrada no arquivo.")
    else:
        # Pega os primeiros 20
        blocos_limitados = blocos_cli[:20]

        # Remove quebras de linha e junta tudo
        linha_unica = "".join(bloco.replace("\n", "").replace("\r", "") for bloco in blocos_limitados)

        # Escreve no arquivo de saída
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write(linha_unica)

        print(f"✅ Sucesso! {len(blocos_limitados)} blocos <Cli> salvos em linha única no arquivo: {arquivo_saida}")
