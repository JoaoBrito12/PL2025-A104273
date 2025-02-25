import re

def substituir(match):
        nivel = len(match.group(1))  
        conteudo = match.group(2).strip()  
        return f"<h{nivel}>{conteudo}</h{nivel}>"

def conversor_markdown(markdown):
    markdown = re.sub(r'^(#{1,6})\s*(.+)$', substituir, markdown, flags=re.MULTILINE)
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)
    

    return markdown


def conversor_listas(markdown):
    linhas = markdown.split("\n")
    dentro_lista = False
    resultado = []

    for linha in linhas:
        match = re.match(r'^\d+\.\s+(.*)', linha)  
        if match:
            if not dentro_lista:
                resultado.append("<ol>")  
                dentro_lista = True
            resultado.append(f"<li>{match.group(1)}</li>")
        else:
            if dentro_lista:
                resultado.append("</ol>")  
                dentro_lista = False
            resultado.append(linha)

    if dentro_lista:
        resultado.append("</ol>")
    return "\n".join(resultado)


markdown = """# Título
Texto **negrito** e *itálico*.
Aqui está um [link para a página](http://link.com).
E uma imagem: ![Imagem de Exemplo](imagem.jpg)

## Subtítulo
1. Primeiro item
2. Segundo item
3. Terceiro item
"""

html = conversor_markdown(markdown)
html = conversor_listas(html)
with open("output/output.txt", 'w', encoding='utf-8') as file:
        file.write(html)
