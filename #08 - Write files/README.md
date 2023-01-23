# Write files

Write files, combinado ao uso do open files o write files pode ser utilizado para quando você necessita de registrar alguma informação em um arquivo, seja JSON, CSV ou um simples TXT. Esse método é muito importante, pois com ele conseguimos escrever no arquivo e reutilizar depois.

Para abrir um arquivo em python é necessário utilizar a palavra reservada `open`, exemplo:

```python
open('file.txt','rw')
```

Neste caso acima, ele esta passando o primeiro parâmetro para dizer o caminho do arquivo e o seguindo parâmetro para dizer a ação que esta fazendo 'read and write'.