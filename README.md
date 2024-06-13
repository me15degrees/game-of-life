## Jogo da vida
### O que é?
É uma simulação que segue regras bem definidas de como um grupo de seres vivos deve se orientar. O jogo foi criado de modo a reproduzir, através de regras simples, as alterações e mudanças em grupos de seres vivos, tendo aplicações em diversas áreas da ciência. É definido um tabuleiro bidimensional (nesse código será considerada uma matriz quadrada para facilitar a representação computacional) com valores binários para definir se o elemento da matriz - que representa uma célula, por exemplo - está viva, ou morta.

É o exemplo de autômato celular mais conhecido e foi criado por John Conway, em 1970.

> Nesse código será adotado 0 para morto e 1 para vivo.

### Regras
- Toda célula morta com exatamente três vizinhos vivos torna-se viva (nascimento);
- Toda célula viva com menos de dois vizinhos vivos morre por isolamento;
- Toda célula viva com mais de três vizinhos vivos morre por superpopulação;
- Toda célula viva com dois ou três vizinhos vivos permanece viva.

### Desenvolvimento
O jogo não precisa de interações com o usuário após a declaração do estado inicial. Ele é interessante para analisar como um estado pode evoluir para um mais complexo, dado regras simples. Para conhecer mais sobre a criação desse tipo de algoritmo, recomendo ler a página do Wikipedia (https://pt.wikipedia.org/wiki/Jogo_da_vida). Lá consta diversas curiosidades sobre a criação e como você pode encontrar aplicações diferentes (até na música!) do jogo da vida. 

### Sobre o código
Um menu é exibido no terminal para escolher a quantidade de gerações pode ser definida no início do programa e o tamanho da matriz (nxn).


## Game of Life
### What is it?
It is a simulation that follows well-defined rules on how a group of living beings should orient themselves. The game was created to reproduce, through simple rules, the alterations and changes in groups of living beings, having applications in various areas of science. A two-dimensional board is defined (in this code, a square matrix will be considered to facilitate computational representation) with binary values to define whether the element of the matrix - which represents a cell, for example - is alive or dead.

It is the most well-known example of a cellular automaton and was created by John Conway in 1970.

> In this code, 0 will be used for dead and 1 for alive.

### Rules
- Any dead cell with exactly three live neighbors becomes alive (birth);
- Any live cell with fewer than two live neighbors dies by isolation;
- Any live cell with more than three live neighbors dies by overpopulation;
- Any live cell with two or three live neighbors remains alive.

### Development
The game does not need interactions with the user after declaring the initial state. It is interesting for analyzing how a state can evolve into a more complex one, given simple rules. To learn more about the creation of this type of algorithm, I recommend reading the Wikipedia page (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). There you will find various curiosities about its creation and how you can find different applications (even in music!) of the game of life.

### About the code
A menu is displayed in the terminal to choose the number of generations that can be defined at the beginning of the program and the size of the matrix (nxn).