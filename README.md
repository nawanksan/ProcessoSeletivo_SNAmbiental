# 🚛 API de Gestão de Frota

Este projeto é uma API desenvolvida em **Django REST Framework** para gerenciamento de empresas e veículos, com autenticação, paginação e integração com banco de dados MySQL rodando em container Docker.

---

## 📋 Pré-requisitos

1. Utilize **Django REST Framework** na implementação da API.
2. Execute em **container (Docker)** um servidor de banco de dados MySQL/PostgreSQL na sua última versão.  
  - Caso **não utilize container**, documente no README a estrutura do banco de dados (DDL).
3. Implemente autenticação e autorização.
4. Implemente os verbos `POST`, `PUT`, `GET` e `DELETE` para as 3 entidades.
5. Adicione **paginação** em todas as consultas.
6. Armazene os dados no banco criado (em container ou local).
7. Utilizar um mecanismo para popular tabelas

---

## 🎯 Requisitos Específicos

1. Criar um CRUD para cada entidade preservando as relações.
2. Criar **endpoint** para consultar uma empresa por **CNPJ**.
3. Criar **endpoint** para consultar uma empresa por **ID**, retornando também seus veículos.
4. Criar **endpoint** para consultar uma empresa por **ID ou CNPJ**, retornando dados completos junto do endereço.
5. Criar **endpoint** para consultar uma empresa a partir de **parte do nome fantasia**.

---

## 🛠️ Tecnologias utilizadas

- Python 3.12+
- Django 5+
- Django REST Framework
- MySQL 8 (em container Docker)
- Docker e Docker Compose

---

## 🚀 Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/nawanksan/ProcessoSeletivo_SNAmbiental.git
cd ProcessoSeletivo_SNAmbiental
```
  
### 2️⃣ Criar e ativar o ambiente virtual
- Windows
```bash
python -m venv venv
venv\Scripts\activate
```
- Linux e MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Subir o banco de dados com Docker
```bash
docker-compose up -d
```
> Atenção: Certifique-se de que as configurações de `DATABASES` no `settings.py` estão iguais às do `docker-compose.yml`
### 5️⃣ Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6️⃣ Povoe o banco de dados
1.  Tabela Endereço
```bash
python manage.py loaddata endereco/fixtures/endereco.json
```
2.  Tabela Empresa
```bash
python manage.py loaddata empresa/fixtures/empresa.json
```
3.  Tabela Veiculo
```bash
python manage.py loaddata veiculo/fixtures/veiculo.json
```
### 7️⃣ Criar um usuário
```bash
python manage.py createsuperuser
```
- Crie seu usuario para obter o token no Postman
> Use as credenciais criadas para autenticar e obter o token no Postman.
Exemplo de payload:
``` bash
{
    "username": "admin",
    "password": "1234"
}
```
### 8️⃣ Rodar o servidor Django
```bash
python manage.py runserver
```

### 9️⃣ Autenticação
- O projeto utiliza autenticação via token. Para gerar um token, faça login e utilize o endpoint no Postman para pegar o token:
```bash
/token/
```
<img width="1277" height="763" alt="image" src="https://github.com/user-attachments/assets/c2502f74-a565-4492-8337-4d66e4b6a707" />

- copie **access** que é o token
  
<img width="1019" height="343" alt="image" src="https://github.com/user-attachments/assets/4ddcabf4-8aa6-4483-b922-45ffa330f7b0" />

- No Authorization, na esquerda coloque a opção **Bearer Token** e cole no campo **Token** o Token
  
- **Agora é só testar**
- O token tem um tempo, então caso der erro, faça login novamente e copie o token novamente

## 📌 Rotas Disponíveis

### **Entidades CRUD**
- **Empresa:** `/empresa/`
- **Endereço:** `/endereco/`
- **Veículo:** `/veiculo/`

---

### **Consultas Específicas**
- **OBS: onde tiver {}, remova e adicione somente o atributo:**
  Exemplo: `/empresa/{id}/com-veiculos/` depois `/empresa/1/com-veiculos/`
  
- **Consultar por CNPJ:**  
  `GET /empresa/cnpj/{cnpj}/`  
  Exemplo: `/empresa/cnpj/12345678000199/`

- **Consultar por ID com veículos:**  
  `GET /empresa/{id}/com-veiculos/`  
  Exemplo: `/empresa/1/com-veiculos/`

- **Consultar por ID ou CNPJ com endereço completo:**  
  `GET /empresa/buscar/?id={id}`  
  ou  
  `GET /empresa/buscar/?cnpj={cnpj}`  
  Exemplo: `/empresa/buscar/?id=1`

- **Consultar por parte do nome fantasia:**  
  `GET /empresa/buscar-por-nome/?nome={termo}`  
  Exemplo: `/empresa/buscar-por-nome/?nome=Transporte`

### 📄 Endpoints principais

| Ação                  | Verbo HTTP | URL de Acesso       | Descrição |
|-----------------------|------------|---------------------|-----------|
| Listar Empresas       | GET        | `/empresa/`        | Retorna a lista de todas as empresas. |
| Criar Empresa         | POST       | `/empresa/`        | Cria uma nova empresa com os dados enviados no corpo da requisição. |
| Recuperar Detalhe     | GET        | `/empresa/{id}/`   | Retorna os detalhes de uma empresa específica. |
| Atualizar (completo)  | PUT        | `/empresa/{id}/`   | Atualiza todos os dados de uma empresa. |
| Deletar Empresa       | DELETE     | `/empresa/{id}/`   | Remove uma empresa específica. |

---

### Agradecimentos
Agradeço sinceramente pela oportunidade de participar do processo seletivo e de poder desenvolver este projeto como teste.
Foi uma experiência bastante enriquecedora. Pude aplicar meus conhecimentos e, ao mesmo tempo, enfrentar desafios práticos que me permitiram aprender e crescer profissionalmente.
Espero que o projeto atenda às expectativas. Obrigado!
               
