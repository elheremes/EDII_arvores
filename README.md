
# Tópicos

1.  [Observações Iniciais](#org13a13f3)
    1.  [Parâmetros de Entrada](#org4c53048)
        1.  [Documentos](#org3366c03)
        2.  [Quantidade de caracteres retidos](#orgd9a95a7)
    2.  [Observações](#org5a01f82)
2.  [Progresso](#org526ffdb)
    1.  [Implementações <code>[5/5]</code>](#orgd558474)
3.  [Estruturação](#org5100ebf)
    1.  [Objeto Word](#orgc4e91d9)
    2.  [Idéia básica](#orge0fee76)
4.  [Resultados](#orge467e4f)
    1.  [2º cenário](#orgc081da3)
    2.  [3º cenário](#org5e133d4)
        1.  [Entrada 67MB + 262MB](#org9a24004)



<a id="org13a13f3"></a>

# Observações Iniciais


<a id="org4c53048"></a>

## Parâmetros de Entrada


<a id="org3366c03"></a>

### Documentos

-   Quantidade N de caminhos de documentos na linha de comando


<a id="orgd9a95a7"></a>

### Quantidade de caracteres retidos

-   Parâmetro C que irá dizer a quantidade de caracteres comparados nas palavras


<a id="org5a01f82"></a>

## Observações

-   Ignorar sinais de pontuação (TODOS)
-   Todas as palavras devem ser colocadas em LOWERCASE
-   Duas palavras que não diferem nos primeiros caracteres C são identicas
-   Palavras que possuem menos de C caracteres são desconsideradas
-   Criar própria coleção de testes


<a id="org526ffdb"></a>

# Progresso


<a id="orgd558474"></a>

## Implementações <code>[5/5]</code>

-   [X] Hashing Aberto
-   [X] Árvore Binária
-   [X] Árvore AVL
-   [X] Árvore Rubro Negra
-   [X] Árvore B


<a id="org5100ebf"></a>

# Estruturação


<a id="orgc4e91d9"></a>

## Objeto Word

-   Estruturação padrão em todo o programa
-   Objeto Word será guardardo na estrutura de dado escolhida e dentro dele uma mesma estrutura de dados irá guardas o objeto FilesOccur

![img](objeto.png)


<a id="orge0fee76"></a>

## Idéia básica

![img](ideia_basica.png)

![img](ideia.png)


<a id="orge467e4f"></a>

# Resultados


<a id="orgc081da3"></a>

## 2º cenário

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Hash</th>
<th scope="col" class="org-right">C=3</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">Tamanho do Hash</th>
<th scope="col" class="org-right">CeC do IV</th>
<th scope="col" class="org-right">Memoria</th>
<th scope="col" class="org-right">IDF1</th>
<th scope="col" class="org-right">IDF2</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">20</th>
<th scope="col" class="org-right">2.629169</th>
<th scope="col" class="org-right">26800</th>
<th scope="col" class="org-right">0.000512000000000068</th>
<th scope="col" class="org-right">0.00047999999999959186</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">60</th>
<th scope="col" class="org-right">2.724151</th>
<th scope="col" class="org-right">26736</th>
<th scope="col" class="org-right">0.0005869999999998932</th>
<th scope="col" class="org-right">0.0006500000000002615</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">120</th>
<th scope="col" class="org-right">2.669139</th>
<th scope="col" class="org-right">26788</th>
<th scope="col" class="org-right">0.0005990000000002382</th>
<th scope="col" class="org-right">0.000412000000000301</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">C = 3</td>
<td class="org-right">BST</td>
<td class="org-right">AVL</td>
<td class="org-right">ARB</td>
<td class="org-right">BTree G=10</td>
<td class="org-right">BTree G=100</td>
</tr>


<tr>
<td class="org-left">CeC do IV</td>
<td class="org-right">2.788035</td>
<td class="org-right">2.697705</td>
<td class="org-right">3.2378199999999997</td>
<td class="org-right">2.736724</td>
<td class="org-right">2.699848</td>
</tr>


<tr>
<td class="org-left">Memoria</td>
<td class="org-right">26728</td>
<td class="org-right">26764</td>
<td class="org-right">26668</td>
<td class="org-right">26728</td>
<td class="org-right">26772</td>
</tr>


<tr>
<td class="org-left">IDF1</td>
<td class="org-right">0.0008880000000002219</td>
<td class="org-right">0.0012080000000000979</td>
<td class="org-right">0.0006839999999996849</td>
<td class="org-right">0.0007709999999998551</td>
<td class="org-right">0.0005899999999998684</td>
</tr>


<tr>
<td class="org-left">IDF2</td>
<td class="org-right">0.0008659999999998114</td>
<td class="org-right">0.0007129999999997416</td>
<td class="org-right">0.0008110000000001172</td>
<td class="org-right">0.0008919999999998929</td>
<td class="org-right">0.0013150000000003992</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Hash</td>
<td class="org-right">C=5</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">Tamanho do Hash</td>
<td class="org-right">CeC do IV</td>
<td class="org-right">Memoria</td>
<td class="org-right">IDF1</td>
<td class="org-right">IDF2</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">20</td>
<td class="org-right">1.9840140000000002</td>
<td class="org-right">26804</td>
<td class="org-right">0.0005489999999999107</td>
<td class="org-right">0.0007359999999998479</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">60</td>
<td class="org-right">2.070367</td>
<td class="org-right">26804</td>
<td class="org-right">0.0006969999999997256</td>
<td class="org-right">0.0005329999999998947</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">120</td>
<td class="org-right">1.9946290000000002</td>
<td class="org-right">26368</td>
<td class="org-right">0.0006309999999998261</td>
<td class="org-right">0.0006259999999995713</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">C = 5</td>
<td class="org-right">BST</td>
<td class="org-right">AVL</td>
<td class="org-right">ARB</td>
<td class="org-right">BTree G=10</td>
<td class="org-right">BTree G=100</td>
</tr>


<tr>
<td class="org-left">CeC do IV</td>
<td class="org-right">2.1238409999999996</td>
<td class="org-right">2.024773</td>
<td class="org-right">1.9617159999999998</td>
<td class="org-right">2.015054</td>
<td class="org-right">2.056037</td>
</tr>


<tr>
<td class="org-left">Memoria</td>
<td class="org-right">30904</td>
<td class="org-right">26704</td>
<td class="org-right">26608</td>
<td class="org-right">26604</td>
<td class="org-right">26700</td>
</tr>


<tr>
<td class="org-left">IDF1</td>
<td class="org-right">0.0006810000000001537</td>
<td class="org-right">0.0005260000000002485</td>
<td class="org-right">0.0008019999999997474</td>
<td class="org-right">0.0006439999999998669</td>
<td class="org-right">0.0005550000000003052</td>
</tr>


<tr>
<td class="org-left">IDF2</td>
<td class="org-right">0.0006710000000000882</td>
<td class="org-right">0.0007519999999998639</td>
<td class="org-right">0.0007049999999999557</td>
<td class="org-right">0.0005639999999997869</td>
<td class="org-right">0.0011540000000000994</td>
</tr>
</tbody>
</table>


<a id="org5e133d4"></a>

## 3º cenário


<a id="org9a24004"></a>

### Entrada 67MB + 262MB

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Hash</th>
<th scope="col" class="org-right">C=1</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">Tamanho do Hash</th>
<th scope="col" class="org-right">CeC do IV</th>
<th scope="col" class="org-right">Memoria</th>
<th scope="col" class="org-right">IDF1</th>
<th scope="col" class="org-right">IDF2</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">20</th>
<th scope="col" class="org-right">137.743045</th>
<th scope="col" class="org-right">27076</th>
<th scope="col" class="org-right">0.00028800000001183435</th>
<th scope="col" class="org-right">0.00038500000002272827</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">60</th>
<th scope="col" class="org-right">140.79580199999998</th>
<th scope="col" class="org-right">26804</th>
<th scope="col" class="org-right">0.00034499999998161</th>
<th scope="col" class="org-right">0.00041899999999372994</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">120</th>
<th scope="col" class="org-right">131.657103</th>
<th scope="col" class="org-right">27004</th>
<th scope="col" class="org-right">0.0005660000000204946</th>
<th scope="col" class="org-right">0.0002689999999745396</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>


<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
<th scope="col" class="org-right">&#xa0;</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">C = 1</td>
<td class="org-right">BST</td>
<td class="org-right">AVL</td>
<td class="org-right">ARB</td>
<td class="org-right">BTree G=10</td>
<td class="org-right">BTree G=100</td>
</tr>


<tr>
<td class="org-left">CeC do IV</td>
<td class="org-right">137.885787</td>
<td class="org-right">194.28471100000002</td>
<td class="org-right">207.075305</td>
<td class="org-right">168.479665</td>
<td class="org-right">166.195416</td>
</tr>


<tr>
<td class="org-left">Memoria</td>
<td class="org-right">26644</td>
<td class="org-right">26576</td>
<td class="org-right">26800</td>
<td class="org-right">26804</td>
<td class="org-right">26832</td>
</tr>


<tr>
<td class="org-left">IDF1</td>
<td class="org-right">0.00042099999998868043</td>
<td class="org-right">0.00021399999999971442</td>
<td class="org-right">0.00045399999999062857</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">0.0006629999999745451</td>
</tr>


<tr>
<td class="org-left">IDF2</td>
<td class="org-right">0.00048300000000267573</td>
<td class="org-right">0.0008780000000001564</td>
<td class="org-right">0.0008270000000152322</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">0.0008799999999951069</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Hash</td>
<td class="org-right">C=3</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">Tamanho do Hash</td>
<td class="org-right">CeC do IV</td>
<td class="org-right">Memoria</td>
<td class="org-right">IDF1</td>
<td class="org-right">IDF2</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">20</td>
<td class="org-right">173.040934</td>
<td class="org-right">26836</td>
<td class="org-right">0.0005079999999964002</td>
<td class="org-right">0.0004500000000007276</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">60</td>
<td class="org-right">181.379853</td>
<td class="org-right">27084</td>
<td class="org-right">0.0005869999999958964</td>
<td class="org-right">0.0006109999999921456</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">120</td>
<td class="org-right">160.836913</td>
<td class="org-right">26720</td>
<td class="org-right">0.0005000000000165983</td>
<td class="org-right">0.0005089999999938755</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">C = 3</td>
<td class="org-right">BST</td>
<td class="org-right">AVL</td>
<td class="org-right">ARB</td>
<td class="org-right">BTree G=10</td>
<td class="org-right">BTree G=100</td>
</tr>


<tr>
<td class="org-left">CeC do IV</td>
<td class="org-right">195.054941</td>
<td class="org-right">157.097983</td>
<td class="org-right">191.092486</td>
<td class="org-right">127.254069</td>
<td class="org-right">128.95186</td>
</tr>


<tr>
<td class="org-left">Memoria</td>
<td class="org-right">26824</td>
<td class="org-right">26824</td>
<td class="org-right">26824</td>
<td class="org-right">26604</td>
<td class="org-right">26776</td>
</tr>


<tr>
<td class="org-left">IDF1</td>
<td class="org-right">0.0003059999999948104</td>
<td class="org-right">0.0007350000000201362</td>
<td class="org-right">0.00036500000001638</td>
<td class="org-right">0.00029299999999921056</td>
<td class="org-right">0.00026799999997706436</td>
</tr>


<tr>
<td class="org-left">IDF2</td>
<td class="org-right">0.00083399999999755893</td>
<td class="org-right">0.0005390000000033979</td>
<td class="org-right">0.00040799999999308056</td>
<td class="org-right">0.0005469999999974107</td>
<td class="org-right">0.0005889999999908468</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">Hash</td>
<td class="org-right">C=5</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">Tamanho do Hash</td>
<td class="org-right">CeC do IV</td>
<td class="org-right">Memoria</td>
<td class="org-right">IDF1</td>
<td class="org-right">IDF2</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">20</td>
<td class="org-right">173.040934</td>
<td class="org-right">26836</td>
<td class="org-right">0.0005079999999964002</td>
<td class="org-right">0.0004500000000007276</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">60</td>
<td class="org-right">181.379853</td>
<td class="org-right">27084</td>
<td class="org-right">0.0005869999999958964</td>
<td class="org-right">0.0006109999999921456</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">120</td>
<td class="org-right">160.836913</td>
<td class="org-right">26720</td>
<td class="org-right">0.0005000000000165983</td>
<td class="org-right">0.0005089999999938755</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">C = 5</td>
<td class="org-right">BST</td>
<td class="org-right">AVL</td>
<td class="org-right">ARB</td>
<td class="org-right">BTree G=10</td>
<td class="org-right">BTree G=100</td>
</tr>


<tr>
<td class="org-left">CeC do IV</td>
<td class="org-right">153.19824699999998</td>
<td class="org-right">148.77687600000002</td>
<td class="org-right">147.75920200000002</td>
<td class="org-right">114.60230700000001</td>
<td class="org-right">121.563428</td>
</tr>


<tr>
<td class="org-left">Memoria</td>
<td class="org-right">26780</td>
<td class="org-right">26644</td>
<td class="org-right">26620</td>
<td class="org-right">26796</td>
<td class="org-right">26768</td>
</tr>


<tr>
<td class="org-left">IDF1</td>
<td class="org-right">0.0007249999999885404</td>
<td class="org-right">0.0006160000000079435</td>
<td class="org-right">0.0007759999999734646</td>
<td class="org-right">0.0006610000000080163</td>
<td class="org-right">0.0007409999999907768</td>
</tr>


<tr>
<td class="org-left">IDF2</td>
<td class="org-right">0.0006040000000098189</td>
<td class="org-right">0.0007350000000201362</td>
<td class="org-right">0.0009050000000172531</td>
<td class="org-right">0.0007869999999883248</td>
<td class="org-right">0.0006960000000049149</td>
</tr>
</tbody>
</table>

