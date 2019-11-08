// ===================JEITO 1

// function mudarTexto(){
//     document.querySelector('#humilde').innerHTML = "Enviado!";
// }

//  ===================JEITO 2

// let botao = document.querySelector('button');

// function mudarBotao(){
//     botao.style.backgroundColor = 'purple';
// }

// botao.onclick = mudarBotao;

// 

let botao = document.querySelector("button");

function tirarClass(){
//     if(botao.classList.contains("humilde")){
//         botao.classList.remove("humilde");
//     }
//     else{
//         botao.classList.add("humilde");
//     }

    botao.classList.toggle('humilde');
    
}

botao.onclick = tirarClass;