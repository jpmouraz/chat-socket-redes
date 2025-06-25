# chat-socket-redes

 
 
 
 
📡 ChatSimples TCP – Comunicação via Sockets em Python 
Projeto de Redes de Computadores – Engenharia de Software Comunicação em tempo real entre múltiplos clientes usando sockets TCP e multithreading. 
  
📝 Descrição Geral 
ChatSimples TCP é uma aplicação de chat desenvolvida em Python 3.11, utilizando sockets TCP e threads para permitir que vários clientes se comuniquem simultaneamente por meio de um servidor central. 
Este projeto visa demonstrar de forma prática o funcionamento da comunicação entre processos via rede, sendo ideal para estudos e experimentos na disciplina de Redes de Computadores. 
  
🎯 Objetivos 
•	Demonstrar uma aplicação prática da comunicação TCP/IP. 
•	Permitir múltiplas conexões e troca de mensagens em tempo real. 
•	Reforçar o entendimento sobre threads, sockets e conexões cliente-servidor. 
  
🛠 Tecnologias e Ferramentas 
•	Linguagem: Python 3.11 
•	Bibliotecas: socket, threading, sys 
•	Protocolo: TCP/IP 
•	Modelo de Comunicação: Cliente-Servidor 
  
🧱 Estrutura do Projeto 
ChatSimples/ 
├── servidor.py     # Gerencia conexões e repassa mensagens 
└── cliente.py      # Interface cliente para envio e recebimento de mensagens 
 
⚙️ Funcionamento dos Códigos 
🔁 servidor.py – O coração da comunicação 
•	Cria um socket TCP e o associa a um IP e porta (127.0.0.1:5000). • 	Escuta novas conexões com listen() e aceita clientes com accept(). 
•	Cada cliente conectado é adicionado a uma lista e tratado em uma thread separada. 
•	O servidor recebe mensagens de cada cliente e retransmite para todos os outros usando a função broadcast(). 
•	Se o cliente for desconectado ou ocorrer erro, ele é removido da lista de clientes. 
👥 cliente.py – Interface do usuário 
•	O cliente escolhe um apelido ao iniciar. 
•	Conecta ao servidor por meio de um socket TCP. 
•	Duas threads são iniciadas: 
o 	enviar_mensagens(): captura e envia mensagens digitadas no terminal. o 	receber_mensagens(): recebe mensagens dos outros clientes e as imprime no terminal. 
•	O comando /sair encerra a conexão do cliente com o servidor. 
  
▶️ Como Executar Passo a passo: 
1.	Abra um terminal e execute o servidor: 
python servidor.py 
2.	Em novos terminais separados, execute pelo menos dois clientes: 
python cliente.py 
3.	Digite mensagens no terminal de cada cliente. As mensagens serão transmitidas para todos os conectados em tempo real. 
4.	Para sair do chat: 
•	Digite /sair no cliente. 
•	Digite “/sair” no terminal do servidor para encerrar. 
 
 
👤 Manual do Usuário 
•	Inicie o servidor antes de qualquer cliente. 
•	Execute um ou mais clientes em terminais separados. 
•	Digite mensagens e veja as respostas em tempo real. 
•	Use /sair para sair de forma segura do chat. 
•	A troca de dados é feita em tempo real via TCP/IP. 
  
📁 Repositório e Vídeo 
•	Repositório GitHub: https://github.com/jpmouraz/chat-socket-redes#
•	Demonstração no YouTube: 
  
📌 Observações Finais 
Este projeto reforça conceitos importantes de redes, como: 
•	Comunicação orientada à conexão. 
•	Manipulação de múltiplos clientes com threads. 
•	Tratamento de erros e desconexões. 
É uma base sólida para projetos mais avançados de comunicação, como sistemas de mensagens, jogos em rede ou servidores dedicados. 
 
 
 
