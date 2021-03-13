#!/usr/bin/env bash

PROJETO="Financas Pessoais"
POSTGRES="post"

HR="***********************************************************************************"
PRE="-----------------"

echo
echo "${HR}"
echo "* [CLEAN.SH]"
echo "* Projeto: ${PROJETO}"
echo "* ** Utilize esse script caso queira limpar os containers do projeto ja criados e atualizar o repositorio git."
echo "* ** Esse script NAO constroi, apenas LIMPA"
echo "* ** IMPORTANTE"
echo "* ** Execute atraves do diretorio pai: cd DOCKER/ & sh bin/clean.sh"
echo "${HR}"
echo ''

echo "${PRE} STOP docker containers"
sudo docker-compose stop

echo "${PRE} REMOVE docker containers"
sudo docker-compose rm -f

echo "${PRE} REMOVE docker images"
sudo docker image rm ${POSTGRES}


echo "${PRE} DONE"
echo "${HR}"
echo ''