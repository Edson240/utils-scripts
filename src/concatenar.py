import xml.etree.ElementTree as ET

# Caminhos dos arquivos
caminho_base = r'C:\Users\pedro\xml-utils\data\base.xml'
caminho_complementar = r'C:\Users\pedro\xml-utils\data\complementar.xml'
caminho_saida = r'C:\Users\pedro\xml-utils\data\saida.xml'

# Função para ler XMLs sem tag raiz e adicionar uma artificialmente
def ler_xml_sem_raiz(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        conteudo_com_raiz = f"<Root>{conteudo}</Root>"
        return ET.ElementTree(ET.fromstring(conteudo_com_raiz))

# Função para salvar XML em formato compacto (sem indentação)
def salvar_xml_compacto(tree, caminho):
    with open(caminho, 'wb') as f:
        # Converte a árvore para string e salva diretamente
        f.write(ET.tostring(tree.getroot(), encoding='utf-8', xml_declaration=True))

# Carrega os arquivos
base_tree = ler_xml_sem_raiz(caminho_base)
complementar_tree = ler_xml_sem_raiz(caminho_complementar)

# Elemento raiz de cada árvore
base_root = base_tree.getroot()
complementar_root = complementar_tree.getroot()

# Indexa os elementos <Cli> da base por 'Contrt'
contratos_cli_map = {}
for cli in base_root.findall('Cli'):
    for op in cli.findall('Op'):
        contratos_cli_map[op.attrib.get('Contrt')] = cli

# Para cada <Op> do complementar, verifica se o Contrt existe na base e adiciona
for op in complementar_root.findall('Op'):
    contrt = op.attrib.get('Contrt')
    if contrt in contratos_cli_map:
        nova_op = ET.fromstring(ET.tostring(op))
        contratos_cli_map[contrt].append(nova_op)

# Salva o resultado em um novo arquivo em formato compacto
salvar_xml_compacto(base_tree, caminho_saida)
print(f"✅ Arquivo final salvo em: {caminho_saida}")

