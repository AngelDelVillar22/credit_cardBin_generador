#!/bin/bash

echo -e "\e[33mGenerador de Bines Creado Por: 🔮Angel Del Villar🔮\e[0m"
echo -e "\e[33mBIENVENID@S AL GENERADOR DE BINES,USA ESTE SCRIPT SOLO CON FINES EDUCATIVOS\e[0m"
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

main
