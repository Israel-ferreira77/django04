Projeto Django com Django Rest Framework
Este projeto é um exemplo de aplicação Django utilizando o Django Rest Framework (DRF) para criar uma API que gerencia dois modelos relacionados. O banco de dados usado é o SQLite3.

Descrição do Projeto
Este projeto demonstra como configurar um projeto Django básico e usar o Django Rest Framework para criar endpoints de API para dois modelos relacionados. Os modelos e suas relações são definidos no arquivo models.py e a API é configurada no views.py e serializers.py.

Pré-requisitos
Antes de começar, certifique-se de ter o Python e o pip instalados em seu ambiente. Você pode verificar isso usando os seguintes comandos:

python --version
pip --version

Instalação
Clone o repositório:


git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie um ambiente virtual:


python -m venv venv
Ative o ambiente virtual:

No Windows:

venv\Scripts\activate
No macOS/Linux:

source venv/bin/activate
Instale as dependências:

pip install -r requirements.txt
Certifique-se de que o arquivo requirements.txt inclui o Django e o Django Rest Framework:

Django>=4.0,<5.0
djangorestframework>=3.14.0,<4.0
Configuração
Configure as variáveis de ambiente:

Verifique se o arquivo settings.py está configurado para usar o banco de dados SQLite3, que deve ser o padrão. Não é necessário modificar nada para o SQLite3, mas você deve configurar as permissões e as chaves secretas necessárias.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
Realize as migrações:

python manage.py makemigrations
python manage.py migrate
Crie um superusuário para acessar o admin:

python manage.py createsuperuser
Execução do Projeto
Inicie o servidor de desenvolvimento:

python manage.py runserver
O servidor estará disponível em http://127.0.0.1:8000/.

Acesse a API:

Endpoints: /api/modelo1/ e /api/modelo2/ (ou conforme definidos em urls.py).
Admin: Acesse a interface administrativa em http://127.0.0.1:8000/admin/.
Estrutura do Projeto
project_name/
manage.py
project_name/
settings.py
urls.py
wsgi.py
app_name/
migrations/
models.py
serializers.py
views.py
urls.py
Exemplos de Uso
Criar e listar Modelos
Criar um novo objeto:

Envie uma solicitação POST para /api/modelo1/ com os dados necessários.

Listar objetos existentes:

Envie uma solicitação GET para /api/modelo1/.
