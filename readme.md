<h1 align="center">Projeto Inicial E-commerce</h1>

<p align="center">Um simples projeto backend inicial de E-commerce utilizando Django Rest Framework para demonstração da disciplina MATE85 - Tópicos em Sistemas de Informação e Web I.</p>

![Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Badge](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)


=================
<!--ts-->
   * [Comentários](#Comentarios)
        * Como é uma demonstração deixei no sqlite padrão que o próprio Django oferece de início. Porém indico o PostgreSQL. 
        * Estou utilizando a própria documentação do Django Rest Framework mas é possivel utilizar o Swagger 
   * [Manual](#Manual)
        * Versão Python Instalada -> 3.10.2
        * Crie o ambiente virtual de desenvolvimento
            * ```python
                python -m venv venv     
              ```
            * ```python
                source venv/Scripts/activate    
              ```
        * Instale as dependências
            * ```python
                pip install -r requirements.txt     
              ```
        * Faça as migrações e rode localmente
            * ```python
                python manage.py migrate    
              ```
            * ```python
                python manage.py runserver    
              ```
   * [Documentação](#Documentacao)
        * https://docs.djangoproject.com/en/4.2/
        * https://www.django-rest-framework.org/
<!--te-->
