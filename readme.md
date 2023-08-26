<h1 align="center">Projeto Inicial E-commerce</h1>

<p align="center">Um simples projeto backend inicial de E-commerce utilizando Django Rest Framework para demonstração da disciplina MATE85 - Tópicos em Sistemas de Informação e Web I.</p>

![Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Badge](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)


=================
<!--ts-->
   * [Comentários](#Comentarios)
        * Como é uma demonstração deixei no sqlite padrão que o próprio Django oferece de início. Porém indico o PostgreSQL. 
   * [Manual](#Manual)
        * Versão Python Instalada -> 3.10.2
        * Crie o ambiente virtual de desenvolvimento 
        * ```
            id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, verbose_name="Id")
            ```
   * [Exemplo](#Exemplo)
        * Cadastro de animais, dentro do models ficaria:
        * ```
            from utils.renomeando_anexo import *
            ...
            class Animal(models.Model):
            ...
                carteira_vacinacao_anexo = models.FileField(upload_to=RenomeandoAnexo('carteira_vacinacao','cadastro_animal','.pdf'), blank=True, null = True,verbose_name="Carteira de Vacinação")
            ...
            ```
        * Caminho final do arquivo: media/uploads/cadastro_animal/099d5f3f-3795-4cae-8b18-d40dfd98b1b7/carteira_vacinacao.pdf
   * [Documentação](#Documentacao)
        * https://docs.djangoproject.com/en/4.2/
        * https://www.django-rest-framework.org/
<!--te-->
