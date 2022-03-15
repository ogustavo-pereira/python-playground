# Open files

Open files, ou melhor dizendo abrir arquivos é algo que pode ser amplamente utilizado quando se trata de scripts que possuem alguma interação com uma fonte externa, seja JSON, CSV ou um simples TXT. Esse método é muito importante, pois com ele conseguimos abrir o arquivo e visualizar os conteúdos internos.

Para criar abrir um arquivo em python é necessário utilizar a palavra reservada `open`, exemplo:

```python
open('file.txt','r')
```

Neste caso acima, ele esta passando o primeiro parâmetro para dizer o caminho do arquivo e o seguindo parâmetro para dizer a ação que esta fazendo 'read'.

Em alguns casos é necessário utilizar de uma biblioteca para interpretar os dados. Exemplo:

```python
import json

json.load(open('file.json'))
```