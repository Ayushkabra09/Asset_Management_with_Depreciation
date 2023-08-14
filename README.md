# Asset Management System

Welcome to the Asset Management System project! This application is developed using Flask, providing efficient management of assets within an organization. It enables users to manage, track, and report on various assets while maintaining data privacy and security.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Asset Management System is a web-based application designed to simplify the management of assets within an organization. It offers a user-friendly interface to facilitate asset registration, tracking, and reporting, making it a valuable tool for effective asset management.

## Features

- **Organization-based Data Segregation**: Users are seamlessly divided into organizations, ensuring data isolation and enhanced privacy.
- **Role-based Authentication**: Implemented secure login and user roles to control data access based on user authorization levels.
- **Dynamic Depreciation Reporting**: Provides detailed depreciation reports, aiding in financial planning and asset lifecycle management.
- **Advanced Backend Tools**: Utilized Redis caching and PostgreSQL database for optimized performance and seamless user experience.

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory: `cd asset-management-system`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`
6. Set up your environment variables. Create a `.env` file based on `.env.example` and fill in the necessary information.
7. Initialize the database:
   - Run migrations: `flask db upgrade`
   - Create an initial user: `flask create_user`

## Usage

1. Activate the virtual environment as shown in the installation steps.
2. Start the Flask development server: `flask run`
3. Access the application in your web browser: `http://localhost:5000`

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please submit an issue or pull request. For major changes, please open an issue first to discuss the changes.

## License

This project is licensed under the [MIT License](LICENSE).
