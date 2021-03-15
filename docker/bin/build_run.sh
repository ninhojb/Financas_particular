#!/usr/bin/env bash

PROJETO="Financas Pessoais"

HR="***********************************************************************************"
PRE="-----------------"

echo
echo "${HR}"
echo "* [BUILD_RUN.SH]"
echo "* Projeto: ${PROJETO}"
echo "* ** Constroi os containers do projeto e os inicializa."
echo "* ** IMPORTANTE"
echo "* ** NAO Utilize esse script para iniciar os container JA CRIADOS."
echo "* ** Execute atraves do diretorio pai: cd DOCKER/ & sh bin/build_run.sh"
echo "${HR}"
echo ''

echo "${PRE} BUILD docker images"

echo "${PRE} ... Postgres"
sudo docker build -f docker-compose.yml


echo "${PRE} UP docker compose"
sudo docker-compose up -d --remove-orphans



echo "${PRE} DONE"
echo "${HR}"
echo ''

echo "${HR}"
echo ''
echo "${PRE} LISTANDO LOGS (ctrl+c NAO matara os containers!)"
echo ''
echo "${HR}"
echo ''
sudo docker-compose logs -f