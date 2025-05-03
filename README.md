# Avto E'lon

## Users

POST api/auth/register/ - регистрация

POST api/auth/login/ - вход

POST api/token/refresh/ - обновить токен

GET api/users/id/ - профиль юзера

## Dealers

GET api/dealers/ - список дилеров

POST api/dealers/ - создать дилера

GET api/dealers/id/ - информация о дилере

PUT api/dealers/id/ - изменить дилера

PATCH api/dealers/id/ - частично изменить дилера

DELETE api/dealers/id - удалить дилера

## Makes

GET api/makes/ - список марок авто

POST api/makes/ - добавить марку авто

GET api/makes/id/models/ - модели марки

## Models

GET api/models/ - список моделей авто

POST api/models/ - добавить модель авто

## BodyType

GET api/body_types/ - список body_types

POST api/body_types/ - добавить body_type

## Features

GET api/features/ - список особенностей авто

POST api/features/ - добавить особенность

## Cars

GET api/cars/ - список авто

POST api/cars/ - добавить авто

GET api/cars/id/ - информация об авто

PUT api/cars/id/ - изменить информацию об авто

PATCH api/cars/id/ - частично изменить информацию об авто