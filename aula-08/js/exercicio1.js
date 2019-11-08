let degrau = Number(prompt("Insira quantos degraus voce quer que a sua escada tenha"));
let material = prompt("Insira qual material voce quer usar para construir sua escada");
let escada = "";

for(let i = 0; i < degrau; i++){
   escada = escada + material;
   console.log(escada);
}
