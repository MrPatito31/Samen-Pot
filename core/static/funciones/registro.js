const $formulario = document.getElementById('formulario');
const $usuario = document.getElementById('username');

(function (){
    $formulario.addEventListener('submit', function(e){
    let usuario=String($usuario.value).trim();
    if (usuario.length===0){
        e.preventDefault();
    }
    
});
})()
