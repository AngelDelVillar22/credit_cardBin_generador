#!/usr/bin/env python
#-*- coding: iso-8859-1 -*-
import getopt
import time
import os
import sys
import datetime
from random import randint

version = "1.0.0"
#Mensaje
os.system ("clear")
print("\033[1;32m+\033[1;36m GENERADOR")
time.sleep(1.2)
#Informacion de ayuda
def angeldelvillar ():
time.sleep(1.2)
print("")
print("\033[1;32m Informacion de Termux")
print("")
time.sleep(1.6)
print(" https://t.me/master_Angel_Delvillar")
print("")
time.sleep(2.2)
# Función para generar una fecha aleatoria entre 2023 y 2031
generate_random_date() {
    local year=$((2023 + RANDOM % 9))
    local month=$((1 + RANDOM % 12))
    local day=$((1 + RANDOM % 28))
    echo "$month/$day/$year"
}

# Función para generar un número de tarjeta de crédito
generate_card_number() {
    local prefix="4"
    local mid=$((1000 + RANDOM % 9000))
    local last=$((1000 + RANDOM % 9000))
    echo "$prefix$mid$last"
}

# Función principal
main() {
    echo "¿Quieres generar tarjetas con fechas aleatorias o manuales?"
    echo "1. Aleatorio"
    echo "2. Manual"
    read -p "Elige una opción (1/2): " option

    read -p "¿Cuántas tarjetas quieres generar? " num_cards

    for ((i=1; i<=num_cards; i++)); do
        if [ "$option" == "1" ]; then
            date=$(generate_random_date)
        elif [ "$option" == "2" ]; then
            read -p "Introduce la fecha (MM/DD/YYYY): " date
        else
            echo "Opción inválida"
            return
        fi

        card_number=$(generate_card_number)
        echo "Tarjeta $i:"
        echo "Número de tarjeta: $card_number"
        echo "Fecha de expiración: $date"
        echo
    done
}

if __name__ == '__main__':
    main(sys.argv[1:])
