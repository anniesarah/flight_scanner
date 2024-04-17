# Flight Scanner Python Program

Welcome to the Flight Scanner Python program! This tool collects historical low prices of flights using APIs and sends email notifications to subscribed users.

## Features

- Retrieves historical low prices of flights using Sheety and Tequila APIs.
- Sends email notifications to users who have signed up for updates.

## APIs Used

### Sheety API

The Sheety API is utilized for storing and retrieving flight price data. It provides a convenient way to manage flight information in a spreadsheet format.

- **API Documentation**: [Sheety API Documentation](https://sheety.co/docs/)

### Tequila API (by Kiwi.com)

The Tequila API (formerly known as Kiwi.com's APIs) is used to fetch flight details, including historical price data.

- **API Documentation**: [Tequila API Documentation](https://tequila.kiwi.com/portal/docs/)

## Libraries Used

- **smtplib**: Used for sending emails programmatically.
- **requests**: Used for making HTTP requests to interact with APIs.

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please [open an issue](https://github.com/anniesarah/flight-scanner/issues) or submit a pull request.
