# CLITool

Uma ferramenta de linha de comando (CLI) desenvolvida com Python. Crie projetos, configure ambientes, busque documentação,
teste APIs e visualize informações de perfis do GitHub - tudo pelo terminal.

**Compatível apenas com o Windows 11**

## Avisos
- Alguns comandos desta aplicação rodam direto no terminal com `os.system` e `subprocess`.
- Utilize com cautela em ambientes sensíveis.
- Este projeto foi criado apenas para **fins de estudos** e prática em desenvolvimento.

---
## Instalação

### 1. Baixe os arquivos
Faça o download do projeto clicando em **Code > Download ZIP**, depois extraia os arquivos em uma pasta.

### 2. Crie o ambiente virtual e ative-o
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Crie um arquivo .env
```bash
GITHUB_TOKEN=seu_token
```
É necessário para utilizar o GitStatus.
Certifique-se de ativar a permissão read:user ao gerar o token no GitHub.

## Como usar
Execute o CLI
```bash
python src/main.py
```
Navegue pelo menu de ferramentas com os números de 1 a 7 ou digite 99 para sair.

## Funcionalidades
| Código | Função         | Descrição                                                                                               |
| ------ | -------------- | ------------------------------------------------------------------------------------------------------- |
| 1      | Create Project | Cria projetos em Python, PHP ou C                                                                       |
| 2      | Search Project | Abre um projeto já criado no VS Code                                                                    |
| 3      | DevSetup       | Cria um ambiente virtual e instala pacotes Python (`requirements.txt`) ou executa um servidor PHP local |
| 4      | Select Path    | Define o caminho raiz para os projetos                                                                  |
| 5      | GitStatus      | Mostra dados públicos (e privados se autorizado) de um usuário do GitHub                                |
| 6      | DocSearch      | Abre a documentação da linguagem no navegador                                                           |
| 7      | APITester      | Testa endpoints de APIs usando arquivos `.txt`                                                          |
| 99     | Exit           | Encerra o programa                                                                                         |

## Teste de API - Exemplo de arquivo .txt
```bash
-h Accept: application/json
-h Authorization: <YOUR-TOKEN>
https://api.example.com/resource
```

## Busca por documentação - DocSearch
```bash
[linguagem] [termo]
python print
php echo
c printf
```

## Documentações
As documentações acessadas pela ferramenta podem ser encontradas nos seguintes sites:
- https://docs.python.org/3/
- https://www.php.net/
- https://devdocs.io/

## Estrutura de Pastas
```bash
CLITool/
├── docs/
│   └── todo.txt
├── src/
│   ├── main.py
│   ├── core.py
│   └── settings.py
├── .env             # Você cria esse arquivo com seu token GitHub
├── requirements.txt
└── README.md
```
## Autor
Desenvolvido por Everton Renan
