<!-- PROJECT LOGO -->
<br />

<p align="center">
  <img src="static/kashtable_dev_logo.png" width="50%" height="50%">
</p>

<h2 align="center">KashTable Flask App</h2>

# Table of Contents
<br>

* [About the Project](#about-the-project)
* [General](#general)
  * [Run locally](#run-locally)
  * [Built With](#built-with)
    * [Python](#python)
    * [Other Dependencies](#other-dependencies)
  * [Model](#model)
* [Excel Mandatory Format](#excel-mandatory-format)
  * [Column Name](#column-name)
  * [Formatter](#formatter)
* [Client Side](#client-side)
  * [Access](#access)
    * [Register](#register)
    * [Login](#login)
    * [Reset Password](#reset-password)
    * [Aside](#aside)
      * [Not Authenticated](#not-authenticated)
      * [Authenticated](#authenticated)
  * [Profile](#profile)  
  * [Upload](#upload)
  * [Posts](#posts)
    * [Home](#home)
    * [Table](#table)
  * [Graph](#graph)
* [CRUD Admin](#crud-admin)
  * [Home](#home)
  * [User](#user)
    * [List](#list)
    * [Create](#create)
    * [Details](#details)
    * [Edit](#edit)
  * [File](#file)
    * [List](#list)
    * [Create](#create)
    * [Details](#details)
* [Author](#author)
* [License](#license)

# About the Project

### Le constat

Dans le contexte économique actuel, les startup, PME et TPE sont plus exposées que jamais à des problèmes de liquidités. La maîtrise du BFR et de la rentabilité sont des facteurs clés de succès. 

### Notre solution 

Sur la base d’un premier diagnostic réalisé par nos experts, nous pourrons vous proposer les outils de reporting financiers adaptés qui vous permettront un pilotage plus efficient de votre business. Nos experts s’appuient sur des années d’expérience dans l’univers de l’analyse financière au cours desquelles ils ont été exposés à de nombreuses problématiques autour des enjeux que sont la rentabilité, le BFR et le cash. Notre solution vous garantit un reporting financier complet (compte de résultat, BFR, cash-flow) en ligne, revu et fiabilisé  par nos experts. Vous serez désormais en mesure d’avoir de la visibilité sur votre performance historique comme sur votre prévisionnel de trésorerie, afin de mieux l’anticiper. Vous ne vous souciez de rien, nous nous connectons directement à votre logiciel de comptabilité ou de facturation afin de récupérer l’intégralité de vos données financières. Votre unique mission, consulter chaque mois votre Kashtable sur notre plateforme SAAS dans votre espace dédié et sécurisé.
#### More info on https://kashtable.kavalry.fr/

# General

## Run locally

```
from KashTable import create_app
app = create_app()
app.run(debug=True) 
```

## Built With

### Python 

- flask
- flask_sqlalchemy
- flask_bcrypt
- flask_login
- flask_mail
- flask_admin
- flask_basicauth
- flask_wtf
- flask_excel
- os
- pandas
- itsdangerous
- sqlalchemy_utils
- datetime
- json
- jinja2
- uuid
- wtforms
- secrets
- PIL
- dateutil

### Other dependencies

- Bootstrap
- HighCharts
- DataTables
- KeenThemes JS bundles

## Model

<p align="center">
  <img src="static/db_model.png" width="50%" height="50%">
</p>

# Excel Mandatory Format

## Column Name

<p align="center">
  <img src="static/excel_columns.png" width="80%" height="80%">
</p>

## Formatter

<p align="center">
  <img src="static/excel_formatter.png" width="50%" height="50%">
</p>

# Client Side

## Access

### Register

<p align="center">
  <img src="static/register.png" width="80%" height="80%">
</p>

### Login

<p align="center">
  <img src="static/login.png" width="50%" height="50%">
</p>

<p align="center">
  <img src="static/login_field_required.png" width="50%" height="50%">
</p>

<p align="center">
  <img src="static/login_error.png" width="50%" height="50%">
</p>

### Reset Password

<p align="center">
  <img src="static/reset_password.png" width="50%" height="50%">
</p>

<p align="center">
  <img src="static/reset_password_field_required.png" width="50%" height="50%">
</p>

### Aside

#### Not Authenticated

<p align="center">
  <img src="static/aside_not_oauth.png" width="10%" height="10%">
</p>

#### Authenticated

<p align="center">
  <img src="static/aside_oauth.png" width="80%" height="80%">
</p>

## Profile

<p align="center">
  <img src="static/profile.png" width="80%" height="80%">
</p>

<p align="center">
  <img src="static/profile_field_required.png" width="80%" height="80%">
</p>

<p align="center">
  <img src="static/profile_picture.png" width="80%" height="80%">
</p>

## Upload

<p align="center">
  <img src="static/upload_forms.png" width="80%" height="80%">
</p>

<p align="center">
  <img src="static/upload_forms_validation.png" width="80%" height="80%">
</p>

## Posts

### Home

<p align="center">
  <img src="static/home.png" width="80%" height="80%">
</p>

### Table

<p align="center">
  <img src="static/table.png" width="50%" height="50%">
</p>

<p align="center">
  <img src="static/table_updated.png" width="50%" height="50%">
</p>

<p align="center">
  <img src="static/table_no_data.png" width="50%" height="50%">
</p>

<p align="center">
  <img src="static/table_no_materials.png" width="80%" height="80%">
</p>

## Graph

<p align="center">
  <img src="static/graph.png" width="50%" height="50%">
</p>

<p align="center">
  <img src="static/graph_multicharts.png" width="50%" height="50%">
</p>

<p align="center">
  <img src="static/graph_filters.png" width="50%" height="50%">
</p>

# CRUD Admin

## Home

<p align="center">
  <img src="static/admin_home.png" width="50%" height="50%">
</p>

## User

### List

<p align="center">
  <img src="static/admin_user_list.png" width="50%" height="50%">
</p>

### Create

<p align="center">
  <img src="static/admin_user_create.png" width="50%" height="50%">
</p>

### Details

<p align="center">
  <img src="static/admin_user_details.png" width="50%" height="50%">
</p>

### Edit

<p align="center">
  <img src="static/admin_user_edit.png" width="50%" height="50%">
</p>

## File

### List

<p align="center">
  <img src="static/admin_file_list.png" width="50%" height="50%">
</p>

### Create

<p align="center">
  <img src="static/admin_file_create.png" width="50%" height="50%">
</p>

### Details

<p align="center">
  <img src="static/admin_file_details.png" width="50%" height="50%">
</p>

# Author

**Jean Meilhoc Ricaume** - [LinkedIn](www.linkedin.com/in/j-mr)

# License

This project is licensed under the MIT License
