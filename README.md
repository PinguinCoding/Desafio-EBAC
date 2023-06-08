# Desafio-EBAC
Resolução do Desafio EBAC | Máquina do Tempo
Contexto
Maria criou uma máquina do tempo, e, para testa-la, quer visitar a Rússia no dia do programador entre os anos 1700 e 2700 ( inclusivo ). O dia do programador é o 256º de cada ano.

De 1700 a 1917 a Rússia utilizava o [calendário juliano](https://pt.wikipedia.org/wiki/Calend%C3%A1rio_juliano) e a partir de 1919 adotou plenamente o [calendário gregoriano](https://pt.wikipedia.org/wiki/Calend%C3%A1rio_gregoriano). O ano de 1918 foi de transição e, para adaptar o calendário, convencionou-se que o dia seguinte a 31 de janeiro seria 14 de fevereiro. Isso significa que o dia 14 de fevereiro foi 32º dia do ano de 1918 na Rússia.

Em ambos os calendários, fevereiro é o único mês que possui uma quantidade de dias variável, podendo ter 29 dias em anos bissextos ou 28 dias nos anos normais.

Anos Bissextos
Calendário Juliano:
Qualquer ano divisível por 4;

Calendário Gregoriano:
Anos divisíveis por 400;
Anos divisíveis por 4 e não divisíveis por 100;

Desafio
Dado um ano qualquer y ache a data do do dia do programador de acordo com o calendário oficial Russo daquele ano. A saída da função deve ser no formato dd/MM/yyyy, de preferência na saída padrão da linguagem de programação de sua escolha.

Condições
Entrada: A função deverá receber um inteiro 1700<=y<=2700
Saída: data do dia do programador em formato de texto dd/MM/yyyy printado na saída padrão.

Exemplos
Entrada: 2017
Saída: 13/09/2017

Entrada: 1800
Saída: 12/09/1800
