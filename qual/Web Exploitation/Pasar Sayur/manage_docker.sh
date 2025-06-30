#!/bin/bash

# Build Docker image
function build_image() {
    echo "Building Docker image..."
    docker-compose build
}

# Start Docker container
function start_container() {
    echo "Starting Docker container..."
    docker-compose up -d
}

# Stop Docker container
function stop_container() {
    echo "Stopping Docker container..."
    docker-compose down
}

# Main menu
function main_menu() {
    echo "Select an option:"
    echo "1) Build Docker image"
    echo "2) Start Docker container"
    echo "3) Stop Docker container"
    echo "4) Exit"

    read -p "Enter your choice: " choice

    case $choice in
        1)
            build_image
            ;;
        2)
            start_container
            ;;
        3)
            stop_container
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            main_menu
            ;;
    esac
}

# Run the menu
main_menu
