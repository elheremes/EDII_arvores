
# Tópicos

1.  [Observações Iniciais](#org0210053)
    1.  [Parâmetros de Entrada](#org0e2ce21)
        1.  [Documentos](#orgfb5691f)
        2.  [Quantidade de caracteres retidos](#org8ea0880)
    2.  [Observações](#org54e9a8f)
2.  [Progresso](#org185b33e)
    1.  [Implementações <code>[2/5]</code>](#org536e560)
        1.  [Observações](#org6150ed8)
3.  [Estruturação](#org302e4b4)
    1.  [Objeto Word](#org6703bb7)
    2.  [Idéia básica](#org2854a10)
    3.  [Ferrame Análise](#org32ef31d)
4.  [Resultados](#orgbb436a1)



<a id="org0210053"></a>

# Observações Iniciais


<a id="org0e2ce21"></a>

## Parâmetros de Entrada


<a id="orgfb5691f"></a>

### Documentos

-   Quantidade N de caminhos de documentos na linha de comando


<a id="org8ea0880"></a>

### Quantidade de caracteres retidos

-   Parâmetro C que irá dizer a quantidade de caracteres comparados nas palavras


<a id="org54e9a8f"></a>

## Observações

-   Ignorar sinais de pontuação (TODOS)
-   Todas as palavras devem ser colocadas em LOWERCASE
-   Duas palavras que não diferem nos primeiros caracteres C são identicas
-   Palavras que possuem menos de C caracteres são desconsideradas
-   Criar própria coleção de testes


<a id="org185b33e"></a>

# Progresso


<a id="org536e560"></a>

## Implementações <code>[2/5]</code>

-   [ ] Hashing Aberto
-   [X] Árvore Binária
-   [X] Árvore AVL
-   [ ] Árvore Rubro Negra
-   [ ] Árvore B


<a id="org6150ed8"></a>

### Observações

-   Rever as já implementadas para lidar com possíveis falhas na estruturação


<a id="org302e4b4"></a>

# Estruturação


<a id="org6703bb7"></a>

## Objeto Word

-   Estruturação padrão em todo o programa
-   Objeto Word será guardardo na estrutura de dado escolhida e dentro dele uma mesma estrutura de dados irá guardas o objeto FilesOccur

![img](objeto.png)


<a id="org2854a10"></a>

## Idéia básica

![img](ideia_basica.png)

![img](ideia.png)


<a id="org32ef31d"></a>

## Ferrame Análise

-   Ainda pesquisar formas em python


<a id="orgbb436a1"></a>

# Resultados

