// calculadora de %

// alterando o tipo da variavel
let valorConta = 0
let gorjeta = 0
valorTotal = 0

valorConta = parseFloat(prompt('Digite o valor da conta: '))
gorjeta = parseFloat(prompt('Digite a gorjeta (decimal)%: '))

// gorjeta = (valorConta * gorjeta) / 100
// valorTotal = valorConta + gorjeta

// inicializando o valor total (vt + vc)
// valor total = 0 + 100 = 100
valorTotal = valorTotal + valorConta
// valor total = 100 + (100*10) -> cálculo matematico
valorTotal = valorTotal + (valorConta * gorjeta) /100


// alert é para o resultado aparecer na tela, não na console
alert('O valor total com gorjeta é de $' + valorTotal)

// no meio do caminho o usuário falou o valor da conta e gorjeta são diferentes de 0
