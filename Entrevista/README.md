 # Entrevista de opinião #

Projeto criado em Python para coletar dados e realizar uma pesquisa de satisfação de clientes de uma empresa

##  Funcionamento

O programa utiliza uma estrutura de repetição FOR para realizar uma pesquisa com 50 entrevistados

Para verificar a opinião de cada entrevistado, são utilizadas estruturas de decisão if e elif.

Ao final da pesquisa, o programa apresenta:

Quantidade de respostas EXCELENTE
Quantidade de respostas RUIM

## Como utilizar

1. Abra o arquivo `Entrevista.py`
2. Execute o programa.
3. Digite o nome do entrevistado quando solicitado.
4. Digite a idade do entrevistado.
5. Digite a opinião sobre o atendimento:

   * `1` para EXCELENTE
   * `2` para BOM
   * `3` para RUIM
6. Repita o processo para os 50 entrevistados.
7. Ao final, o programa exibirá a quantidade de respostas **EXCELENTE** e **RUIM**.
   

   ## Fórmulas e estruturas utilizadas

* `range(50)` — define que o programa será repetido 50 vezes, uma vez para cada entrevistado.
* `+= 1` — utilizado para adicionar 1 aos contadores de respostas.
* `if` — verifica se a opinião escolhida é EXCELENTE.
* `elif` — verifica se a opinião escolhida é RUIM.
* `input()` — utilizado para receber os dados digitados pelo entrevistado.
* `int()` — converte os valores de idade e opinião para números inteiros.
* `==` — utilizado para comparar a opinião digitada com as opções disponíveis.

### Contagem das respostas

A quantidade de respostas EXCELENTE é armazenada na variável `excelente`:

```python
excelente += 1
```

A quantidade de respostas RUIM é armazenada na variável `ruim`:

```python
ruim += 1
```

Os contadores começam em zero:

```python
excelente = 0
ruim = 0
```

A cada resposta correspondente, o contador é incrementado em 1.


![Python](https://img.shields.io/badge/Python-blue)
![Entrevistas](https://img.shields.io/badge/Entrevistas-50-orange)
![Excelente](https://img.shields.io/badge/Excelente-green)
![Bom](https://img.shields.io/badge/Bom-yellow)
![Ruim](https://img.shields.io/badge/Ruim-red)
