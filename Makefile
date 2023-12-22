include .env
export

.RECIPEPREFIX := $() $()

# ------------------------------------- PRD -------------------------------------------

COMPOSE_PRD :=                  \
    -f docker-compose.yaml      \
    -f ${COMPOSE_PRD_KAFKA}     \
    -f ${COMPOSE_PRD_MONGO}     \
    -f ${COMPOSE_PRD_REDIS}     \
    -f ${COMPOSE_PRD_WEB}       \

COMPOSE_PRD_ENV :=                                       \
    --env-file=.env                                      \
    --env-file=tlparser/env/production/.env.prd.compose  \

prdstart: docker-compose.yaml
    sudo docker compose -p prd ${COMPOSE_PRD_ENV} ${COMPOSE_PRD} up --build --force-recreate

prdstop: docker-compose.yaml
    sudo docker compose -p prd ${COMPOSE_PRD_ENV} ${COMPOSE_PRD} down

# ------------------------------------- DEV -------------------------------------------

COMPOSE_DEV :=                  \
    -f docker-compose.yaml      \
    -f ${COMPOSE_DEV_KAFKA}     \
    -f ${COMPOSE_DEV_MONGO}     \
    -f ${COMPOSE_DEV_REDIS}     \
    -f ${COMPOSE_DEV_WEB}       \

COMPOSE_DEV_ENV :=                                       \
    --env-file=.env                                      \
    --env-file=tlparser/env/development/.env.dev.compose \

devstart: docker-compose.yaml
    sudo docker compose -p dev ${COMPOSE_DEV_ENV} ${COMPOSE_DEV} up --build --force-recreate

devstop: docker-compose.yaml
    sudo docker compose -p dev ${COMPOSE_DEV_ENV} ${COMPOSE_DEV} down

# ------------------------------------- TESTS -------------------------------------------

COMPOSE_TESTS :=                \
    -f docker-compose.yaml      \
    -f ${COMPOSE_TESTS_KAFKA}   \
    -f ${COMPOSE_TESTS_MONGO}   \
    -f ${COMPOSE_TESTS_REDIS}   \
    -f ${COMPOSE_TESTS_WEB}     \

COMPOSE_TESTS_ENV :=                                    \
    --env-file=.env                                     \
    --env-file=tlparser/env/tests/.env.tests.compose    \

GREEN := \033[0;32m
RED := \033[0;31m
NC := \033[0m

e2e: docker-compose.yaml
    sudo docker compose -p tests ${COMPOSE_TESTS_ENV} ${COMPOSE_TESTS} up -d --build
    @if [ `sudo docker wait tests` -ne 0 ] ; then                                           \
        sudo docker logs tests;                                                             \
        printf "${RED}Tests Failed${NC}\n";                                                 \
        sudo docker compose -p tests ${COMPOSE_TESTS_ENV} ${COMPOSE_TESTS} down;            \
    else                                                                                    \
        sudo docker logs tests;                                                             \
        printf "${GREEN}Tests Passed${NC}\n";                                               \
        sudo docker compose -p tests ${COMPOSE_TESTS_ENV} ${COMPOSE_TESTS} down;            \
    fi                                                                                      \