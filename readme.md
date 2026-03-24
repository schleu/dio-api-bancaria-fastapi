# Desafio: API Bancária Assíncrona com FastAPI

Neste desafio, você irá projetar e implementar uma API RESTful assíncrona usando **FastAPI** para gerenciar operações bancárias de depósitos e saques, vinculadas a contas correntes. Este desafio irá lhe proporcionar a experiência de construir uma aplicação backend moderna e eficiente que utiliza autenticação **JWT** e práticas recomendadas de design de APIs.

---

# Objetivos e Funcionalidades

O objetivo deste desafio é desenvolver uma API com as seguintes funcionalidades:

### Cadastro de Transações
Permita o cadastro de transações bancárias, como **depósitos** e **saques**.

### Exibição de Extrato
Implemente um endpoint para **exibir o extrato de uma conta**, mostrando todas as transações realizadas.

### Autenticação com JWT
Utilize **JWT (JSON Web Tokens)** para garantir que apenas usuários autenticados possam acessar os endpoints que exigem autenticação.

---

# Requisitos Técnicos

Para a realização deste desafio, você deve atender aos seguintes requisitos técnicos:

### FastAPI
Utilize **FastAPI** como framework para criar sua API. Aproveite os recursos assíncronos do framework para lidar com operações de **I/O de forma eficiente**.

### Modelagem de Dados
Crie **modelos de dados adequados** para representar contas correntes e transações. Garanta que as transações estejam relacionadas a uma conta corrente, e que contas possam ter **múltiplas transações**.

### Validação das Operações
- Não permita **depósitos ou saques com valores negativos**.
- Valide se o usuário possui **saldo suficiente para realizar um saque**.

### Segurança
Implemente **autenticação usando JWT** para proteger os endpoints que necessitam de acesso autenticado.

### Documentação com OpenAPI
Certifique-se de que sua API esteja **bem documentada**, incluindo descrições adequadas para cada endpoint, parâmetros e modelos de dados.


---

# Rodando o projeto

Copie e cole no terminal
```CMD
rmdir /s /q  .venv
py -m venv .venv
.\\venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Explicando os comandos

Apagando pasta `.venv`, caso já exista
``` 
rmdir /s /q  .venv 
```

Criando pasta ambiente virtual `.venv`
```
py -m venv .venv
```

Informando para que o terminal utilize o ambiente virtual
```
.\\venv\\Scripts\\activate
```

Instalando as libs necessárias
```
pip install -r requirements.txt
```

Rodando o projeto, 
<small>por padrão utiliza a porta 8000</small>
```CMD
uvicorn main:app --reload
```

Para acessar o projeto acesse a rota
http://127.0.0.1:8000


Caso adicione uma lib que não está no requirements.txt