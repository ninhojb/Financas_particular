#!/usr/bin/env bash

PROJETO="Financas Pessoais"

HR="***********************************************************************************"
PRE="-----------------"

echo
echo "${HR}"
echo "* [STOP.SH]"
echo "* Projeto: ${PROJETO}"
echo "* ** Utilitario APENAS para desligar containers"
echo "* ** IMPORTANTE"
echo "* ** Execute atraves do diretorio pai: cd DOCKER/ & sh bin/stop.sh"
echo "${HR}"
echo ''

echo "${PRE} STOP docker containers"
sudo docker-compose stop
echo "${PRE} DONE"
echo "${HR}"
echo ''
