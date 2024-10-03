# Pousada_Sunset

# Pousada-Sunset

● Título do projeto: Pousada Sunset;

● Autores: Leidiana Nascimento Patrício - leidiana.patricio@academico.ifpb.edu.br,<br>
           Domilson Gomes de Sena Filho - domilson.gomes@academico.ifpb.edu.br,<br>
           Lucas Emanuel Araújo Toscano - lucas.toscano@academico.ifpb.edu.br;
           
● Disciplinas: Protocolos e Interconexão de Redes de Computadores - Leonidas Francisco de Lima Junior;

● Descrição do problema: O programa consiste em um sistema de hospedagem de pousada, onde através de uma interface gráfica o usuario consegue escolher e e ver informações do quarto, verificar a disponibilidade, reservar acomodação e escolher a forma de pagamento;

● Arquivos do Projeto: cliente.py: Esse arquivo representa o código do cliente, nele será feita algumas configurações básicas, além de se conectar ao servidor, escolher quarto, nome, email e forma de pagamento, juntamente com o valor total da reserva.
servidor.py: Está contido nesse arquivo o código para o funcionamento do servidor, sendo possivel aceitar conexões de clientes, também será verificado se os quartos estão disponíveis, confirma a reserva caso seja possivel, e sinaliza para o cliente caso a reserva tenha sido bem sucedida ou não;

● Pré-requisitos para execução: Python3, linguagem de programação utilizada para desenvolver o projeto. O projeto faz uso de algumas bibliotecas padrões do python (que não precisam de instalação) e bibliotecas que necessitam de instalação. Primeiramente segue as bibliotecas padrões do python: Biblioteca OS: Biblioteca para interação com o sistema operacional. Módulo json: Módulo para manipulação de dados em formato JSON. Biblioteca socket: Biblioteca para comunicação de rede. Biblioteca datetime: Biblioteca para trabalhar com datas e horas. Biblioteca threading: Biblioteca para manipulação de threads. Biblioteca pathlib.Path: Biblioteca para manipulação de caminhos de arquivos e diretórios. <br>

Além disso, é necessário a instalar duas bibliotecas, TKINTER (Uma biblioteca do Python para criar interfaces gráficas de usuárioe) e TKCALENDAR (Extensão do Tkinter que fornece widgets de calendário e data).<br>
Em alguns casos o TKINTER é instalado junto do python, portanto deve se verificar se o modulo já esta instalado.

Verificando a instalação do TKINTER no Linux:<br>
           1 - Para a verificação abra um terminal e digite os seguintes comandos<br>
           2 - python3<br>
           3 - import tkinter<br>
           Se o módulo estiver instalado, ele não retornará erro, mas ainda será preciso instalar o TKCALENDAR.<br>

Instalar TKINTER NO LINUX:<br>
           1 - Abra um terminal<br>
           2 - Utilize o comando "sudo apt install python3-tk"<br>
           
Instalar TKCALENDAR no LINUX: <br>
 1 - Abra um terminal e use os seguintes comandos<br>
 2 - sudo apt install python3-pip<br>
 3 - pip install tkcalendar;

● Protocolo da Aplicação: O projeto faz uso de uma interface front-end para a interação do cliente com o servidor, portanto os comandos não são aplicados pelo cliente no terminal.<br>
verificar_disponibilidade: Verifica se o quarto está disponível nas datas solicitadas, através do quarto escolhido, da data de inicio e da data final de estadia.<br>
adicionar_reserva: Adiciona uma nova reserva passando o quarto escolhido, data de inicio e data final de estadia.;

● Instruções para execução: No cliente.py deve se trocar o caminho do arquivo nas linhas 59, 64, 75, 94, o caminho deve ser a pasta onde se localiza todos os arquivos do projeto. Após isso, inicialize o terminal e execute "python3 servidor.py" para iniciar o servidor. Em outro terminal execute "python3 cliente.py", dessa maneira será aberta uma interface de front-end para o cliente interagir com o servidor.  
