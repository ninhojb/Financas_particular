#!/usr/bin/env bash

PROJETO="Fincanca Pessoais"

HR="***********************************************************************************"
PRE="-----------------"

echo
echo "${HR}"
echo "* [START.SH]"
echo "* Projeto: ${PROJETO}"
echo "* ** Utilitario APENAS para ligar containers"
echo "* ** IMPORTANTE"
echo "* ** Execute atraves do diretorio pai: cd DOCKER/ & sh bin/start.sh"
echo "${HR}"
echo ''

echo "${PRE} START docker containers"
sudo docker-compose start
echo "${PRE} DONE"
echo "${HR}"
echo ''

echo "${HR}"
echo ''
echo "${PRE} LISTANDO LOGS (ctrl+c NAO matarah os containers!)"
echo ''
echo "${HR}"
echo ''
sudo docker-compose logs -f
