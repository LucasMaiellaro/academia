let login = "lucas";
let senha = 123;
let loginDigitado = prompt("Digite o login");
let senhaDigitada = prompt("Digite a senha");
let tentativas = 0;

while(tentativas == 3){
        if(login == loginDigitado && senha == senhaDigitada ){
            alert("Voce está logado");
            }
         else{
            alert("Voce não está logado");
    }
}
alert("você atingiu o limite de tentativas");

