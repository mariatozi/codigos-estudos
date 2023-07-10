
// A: 90-10 if
// B: 80-89 else if 
// C: 70-79 else if
// D: 60-69 else if
// F: below 60 else

let grade = prompt('Digite a nota do aluno: ')

// digitou errado (a mais que 100)
if (grade > 100) {
    alert('Nota inválida')
}

// as demais condições das notas
else if (grade >= 90) {
    alert('Aluno nota A')
}

else if (grade >=80) {
    alert('Aluno nota B')
}

else if (grade >=70) {
    alert('Aluno nota C')
}

else if (grade >=60) {
    alert('Aluno nota D')
}

// qualquer outra coisa abaixo de 60
else {
    alert('Aluno nota F')
}
