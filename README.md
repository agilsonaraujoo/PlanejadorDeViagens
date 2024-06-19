# Sistema de Gerenciamento de Viagens

Este é um sistema simples de gerenciamento de viagens desenvolvido em Python. Permite aos usuários se cadastrarem, fazerem login, adicionar, listar e excluir viagens. As informações dos usuários e das viagens são armazenadas em arquivos de texto.

---

## Funcionalidades

### Cadastro de Usuário

- **Função:** `cadastrar_usuario(usuarios)`
- **Descrição:** Permite que novos usuários se cadastrem no sistema fornecendo um nome de usuário e uma senha.

### Autenticação de Usuário

- **Função:** `autenticar_usuario(usuarios)`
- **Descrição:** Verifica se um usuário existe e se a senha fornecida está correta para permitir o login no sistema.

### Adicionar Viagem

- **Função:** `adicionar_viagem(viagens, usuario)`
- **Descrição:** Permite que um usuário autenticado adicione uma nova viagem especificando destino, datas de início e término, e atividades planejadas durante a viagem.

### Listar Viagens

- **Função:** `listar_viagens(viagens, usuario)`
- **Descrição:** Lista todas as viagens de um usuário autenticado.

### Excluir Viagem

- **Função:** `excluir_viagem(viagens, usuario)`
- **Descrição:** Permite que um usuário autenticado exclua uma viagem específica com base em um índice fornecido.

---

## Arquivos de Armazenamento

### Arquivo `usuarios.txt`

Armazena os dados dos usuários no formato `usuario:senha`. Cada linha representa um usuário cadastrado.

### Arquivo `viagens.txt`

Armazena os dados das viagens no seguinte formato:


