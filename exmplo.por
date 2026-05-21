inteiro: limite;
inteiro: i;
inteiro: dobro;

escreva("Digite um valor positivo");
leia(limite);

se limite > 0 então
    para i <- 1 até limite passo 1
        dobro <- i * 2;
        escreva(dobro);
    fim_para;
senão
    escreva("Valor invalido");
fim_se;


