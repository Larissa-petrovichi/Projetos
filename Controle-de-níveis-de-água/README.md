# Controle de Níveis de Água

## Sobre o projeto

Este projeto é uma simulação de um sistema de monitoramento do nível de água de um reservatório, desenvolvido em Python.

O programa exibe mensagens de alerta coloridas no terminal, de acordo com o nível de água informado na lista.


##  Níveis do reservatório

| Nível | Situação | Cor |
|---|---|---|
| Nível 1 | Muito baixo (crítico) | Vermelho |
| Nível 2 | Baixo | Amarelo |
| Nível 3 | Médio | Verde |
| Nível 4 | Alto | Ciano |
| Nível 5 | Muito alto (alerta) | Azul |

##  Funcionamento

O programa armazena os cinco níveis em uma lista e utiliza uma função chamada `verificar_nivel()` para identificar a situação correspondente e exibir a mensagem com sua respectiva cor.

Um laço de repetição `for` percorre a lista e chama a função para cada nível. Ao final de cada mensagem, o estilo padrão do terminal é restaurado.

##  Instalação

Para utilizar a biblioteca Colorama, execute o seguinte comando no terminal:

```bash
pip install colorama
```


##  Como executar

Abra o arquivo `Larissa_Ag11_DSI.py` no editor Python e execute o programa.

**Observação:** é necessário ter o Python e a biblioteca Colorama instalados.

##  Resultado

O terminal exibirá cinco mensagens, cada uma com a cor correspondente à situação do nível de água do reservatório.

