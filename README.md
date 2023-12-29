
# Задача: Написать парсер для игр, стримеров и стримов Twich-a, а также для продуктов Lamod-ы по категориям.

**Предварительные действия для запуска проекта**
- Выполнить команду chmod -R 777 twich_lamoda_parser/tlparser/data/dev/elastic для develop среды
- Выполнить команду chmod -R 777 twich_lamoda_parser/tlparser/data/prd/elastic для production среды.
- Установить gnu make и docker + docker-compose

**Запуск проекта**
1. make devstart - запуск проекта в develop среде
2. make prdstart - запуск проекта в production среде
3. make parser_it - запуск интеграционных тестов для сервиса parser
4. make caller_it - запуск интеграционных тестов для сервиса caller
5. make parser_component - запуск компонентных тестов для сервиса parer.

**Закрытие проекта**
1. make devstop - закрытие проекта в develop среде.
2. make prdstop - закрытие проекта в production среде.
3. Тесты закрываются автоматически после того как будут выполнены.


**Архитектура на примере twich game**

1. **Сервис parser**
![Image alt](https://github.com/Twelvews/twich_lamoda_parser/raw/feature/initproject/images/parser_architecture.png)

2. **Сервис caller**
![Image alt](https://github.com/Twelvews/twich_lamoda_parser/raw/feature/initproject/images/caller_architecture.png)

**Описание потока выполнения при удалении сущности и при ее парсинге через caller (на примере twich game)**
1. **Create, Delete operations**
![Image alt](https://github.com/Twelvews/twich_lamoda_parser/raw/feature/initproject/images/parser_create_flow.png)
2. **Read operations**
![Image alt](https://github.com/Twelvews/twich_lamoda_parser/raw/feature/initproject/images/parser_read_flow.png)

**Описание межсервисного взаимодействия**
![Image alt](https://github.com/Twelvews/twich_lamoda_parser/raw/feature/initproject/images/ipc.png)

**Описание паттерна cqrs**
![Image alt](https://github.com/Twelvews/twich_lamoda_parser/raw/feature/initproject/images/cqrs.png)

**Развертывания на примере среды production**
![Image alt](https://github.com/Twelvews/twich_lamoda_parser/raw/feature/initproject/images/deployment.png)
