let chat = document.querySelector('#chat');
let input = document.querySelector('#input');
let botaoEnviar = document.querySelector('#botao-enviar');

//Permitindo anexar imagens
let imagemSelecionada; 
let botaoAnexo = document.querySelector('#mais_arquivo');
let miniaturaImagem;

//Função assíncrona que vai buscar a imagem 
async function pegarImagem(){
    //buscando a imagem da aplicação python
    let fileInput = document.createElement('input');
    fileInput.type = 'file'; //do tipo 'file'
    fileInput.accept = 'image/*'; //aceita imagens

    fileInput.onchange = async e => { //quando o fileInput mudar de estado executa:
        if (miniaturaImagem){
            miniaturaImagem.remove(); //remove a miniatura de imagem caso já exista
        }

        imagemSelecionada = e.target.files[0]; //pega o arquivo identificado e armazena em 'imagemSelecionada'
        
        miniaturaImagem = document.createElement('img'); //novo elemento do tipo imagem
        miniaturaImagem.src = URL.createObjectURL(imagemSelecionada); //cria a url para acessar a imagem
        miniaturaImagem.style.maxWidth = '3rem';
        miniaturaImagem.style.maxHeight = '3rem';
        miniaturaImagem.style.margin = '0.5rem';

        document.querySelector('.entrada__container').insertBefore(miniaturaImagem, input); //insere a miniatura de imagem antes da entrada de texto

        let formData = new FormData(); //variável do tipo formdata
        formData.append('imagem', imagemSelecionada); //adiciona a imagem associada à chave 'imagem'
        
        const response = await fetch("http://127.0.0.1:5000/upload_imagem",{
            method: 'POST',
            body: formData
        }); //gera uma requisição toda vez que a rota for chamada

        const resposta = await response.text(); //espera a resposta
        console.log(resposta);
        console.log(imagemSelecionada);
    }
    fileInput.click(); //autoclique para avançar o fluxo
}

async function enviarMensagem() {
    if(input.value == "" || input.value == null) return;
    let mensagem = input.value;
    input.value = "";

    let novaBolha = criaBolhaUsuario();
    novaBolha.innerHTML = mensagem;
    chat.appendChild(novaBolha);

    let novaBolhaBot = criaBolhaBot();
    chat.appendChild(novaBolhaBot);
    vaiParaFinalDoChat();
    novaBolhaBot.innerHTML = "Analisando ..."
    
    // Envia requisição com a mensagem para a API do ChatBot
    const resposta = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify({'msg':mensagem}),
    });
    const textoDaResposta = await resposta.text();
    console.log(textoDaResposta);
    novaBolhaBot.innerHTML = textoDaResposta.replace(/\n/g, '<br>');
    vaiParaFinalDoChat();
}

function criaBolhaUsuario() {
    let bolha = document.createElement('p');
    bolha.classList = 'chat__bolha chat__bolha--usuario';
    return bolha;
}

function criaBolhaBot() {
    let bolha = document.createElement('p');
    bolha.classList = 'chat__bolha chat__bolha--bot';
    return bolha;
}

function vaiParaFinalDoChat() {
    chat.scrollTop = chat.scrollHeight;
}

botaoEnviar.addEventListener('click', enviarMensagem);
input.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        botaoEnviar.click();
    }
});

botaoAnexo.addEventListener('click', pegarImagem);