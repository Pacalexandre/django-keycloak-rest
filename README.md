# django-keycloak-rest
Implementação de middlewear utilizando keycloack aplicação rest  
Desenvolvimento de um middleware de authenticação Oauth2  
Capaz validar uma requisição rest atravez do django

## Pré requisitos para utilização desse projeto

para o uso é necessário:  
- [x] pré requisitos
    - [x] docker - Docker version 20.10.8, build 3967b7d
    - [x] docker-compose - Docker Compose version v2.2.2
    - [x] visual studio
    - [x] extensions: Remote - Containers
    - [x] [documentação](https://code.visualstudio.com/docs/remote/containers)

 - django 
 - djangorestframework
 - keycloack
 
## Servidor de Authenticação Keycloak
Serviço de authenticação para aplicaçõe em ambiente de teste temos um servidor  
instalado com o devcontainer e um postgres para gerenciar o serviço

## Configurações a parte.
algumas dicas de configurações interresantes para facilitar o uso

- Criando super user no django sem shell interativo via cli.
```bash
# Execute esses comandos em projeto django criado!
# Verifica se há altereções nas models do projeto
python manage.py makemigrations
# Aplica as migrações 
python manage.py migrate
# Cria super usuario django 
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python ./manage.py shell
```
