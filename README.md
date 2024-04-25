# Projeto de Gerenciamento Bancário - Portfólio de Linguagem Orientada a Objetos

Este projeto foi desenvolvido como parte do portfólio da disciplina de Linguagem Orientada a Objetos do 3º semestre do curso de Análise e Desenvolvimento de Sistemas da Faculdade Anhanguera/Unopar.

## Descrição

O projeto consiste em uma aplicação de gerenciamento bancário básica desenvolvida em Python com interface gráfica utilizando a biblioteca flet. Permite aos usuários realizar operações bancárias como consulta de saldo, depósitos e saques.
<p align="center">
  <img src="https://github.com/lgluiz1/Portifolio-Linguagem-Orientada-a-Objetos-UNOPAR-ANHAGUERA/assets/125038498/f2f89815-c99b-41b3-a9aa-2fd2c96cb194" alt="SISTEMA_UNOPAR">
</p>


## Como Utilizar

### Instalação

Para executar este projeto, siga os passos abaixo:

1. **Pré-requisitos:**
   - Python instalado no computador (versão 3.x)
   - IDE de desenvolvimento (recomendado: Visual Studio Code)

2. **Instalação da Biblioteca flet:**

   Para utilizar a biblioteca flet no seu projeto, você precisa instalá-la via pip:

   ```bash
   pip install flet
   ```

3. **Executando o Projeto:**
  - Clone o repositório para o seu computador:
     
    ```bash
    git clone https://github.com/lgluiz1/Portifolio-Linguagem-Orientada-a-Objetos-UNOPAR-ANHAGUERA.git
    
  - Acesse o diretório do projeto:
    ```bash

    cd Portifolio-Linguagem-Orientada-a-Objetos-UNOPAR-ANHAGUERA
    ```
  - Execute o arquivo main.py para iniciar a aplicação:
    ```bash
      python main.py
    ```
    
### Funcionalidades

  - **Cadastro de Cliente:** Permite cadastrar um novo cliente informando nome, sobrenome e CPF.

  - **Consulta de Saldo:** Permite consultar o saldo atual da conta bancária do cliente.

  - **Realização de Depósitos:** Permite realizar depósitos na conta bancária do cliente.

  - **Realização de Saques:** Permite realizar saques respeitando o saldo disponível na conta.

### Estrutura do Projeto

  - O projeto está estruturado da seguinte forma:

    - **main.py:** Arquivo principal que contém a lógica da aplicação.

    - **flet.py:** Arquivo da biblioteca flet utilizada para criação da interface gráfica.

    - **README.md:** Arquivo de documentação do projeto.
      
## Uso da Orientação a Objetos no Projeto

Este projeto foi desenvolvido utilizando os principais conceitos da programação orientada a objetos (POO). A POO é um paradigma de programação que organiza o código em entidades chamadas de objetos, cada um representando uma instância de uma classe. Aqui estão alguns pontos-chave do uso da orientação a objetos neste projeto:

- **Classes:** O projeto utiliza classes para modelar entidades relevantes, como `Cliente` e `ContaBancaria`. As classes definem atributos (dados) e métodos (comportamentos) relacionados a essas entidades.

- **Encapsulamento:** Os princípios de encapsulamento foram aplicados para proteger os dados dentro das classes, permitindo acesso controlado por meio de métodos.

- **Abstração:** O projeto utiliza abstração para representar entidades do mundo real de forma simplificada e relevante para o contexto bancário.

- **Herança:** Embora não explicitamente mencionado, a herança pode ser utilizada para estender o comportamento de classes, como `Cliente` e `ContaBancaria`, para outras subclasses específicas.

- **Polimorfismo:** O polimorfismo permite que diferentes objetos respondam ao mesmo método de maneiras diferentes, facilitando operações comuns como depósitos e saques.

O uso da orientação a objetos neste projeto promove uma estrutura organizada e reutilizável, facilitando a manutenção e expansão do sistema bancário implementado.

---

### Trechos de Código Exemplificando Classes e Métodos

Aqui estão alguns trechos de código que exemplificam a definição de classes e métodos no projeto:

  ```python
  # Definição da classe Cliente
  class Cliente:
      def __init__(self, nome: str, sobrenome: str, cpf: int):
          self.nome = nome
          self.sobrenome = sobrenome
          self.cpf = cpf
  
  # Definição da classe ContaBancaria
  class ContaBancaria:
      def __init__(self, cliente: Cliente):
          self.cliente = cliente
          self.saldo = 0
  
      def deposito(self, valor: float):
          valor = float(valor)
          if valor > 0:
              self.saldo += valor
              print(f"Depósito de R${valor:.2f} realizado.")
          else:
              print("Valor de depósito inválido.")
  
      def saque(self, valor: float):
          valor = float(valor)
          if 0 < valor <= self.saldo:
              self.saldo -= valor
              print(f"Saque de R${valor:.2f} realizado.")
          else:
              print("Saldo insuficiente ou valor de saque inválido.")
  
  # Criação de instâncias das classes Cliente e ContaBancaria
  cliente = Cliente("João", "Silva", 12345678900)
  conta = ContaBancaria(cliente)
  
  # Exemplo de uso dos métodos das classes
  conta.deposito(100.0)
  conta.saque(50.0)
```

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir novas issues ou enviar pull requests para melhorar este projeto.

## Autor:
  - [Luiz Gustavo](https://github.com/lgluiz1)


