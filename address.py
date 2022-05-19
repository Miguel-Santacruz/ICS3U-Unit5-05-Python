#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program writes an address as a mailing address


def mailing_address(
    name, street_number, street_name, city, province, postal_code, apartment=None
):
    # return the mailing address

    address = name
    if apartment != None:
        address = (
            address
            + "\n"
            + apartment
            + " - "
            + street_number
            + " "
            + street_name
            + "\n"
            + city
            + " "
            + province
            + " "
            + postal_code
        )
    else:
        address = (
            address
            + "\n"
            + street_number
            + " "
            + street_name
            + "\n"
            + city
            + " "
            + province
            + " "
            + postal_code
        )
    address = address.upper()

    return address


def main():
    # gets user's info an prints the mailing address

    apartment = None

    name = input("Enter your full name: ")
    question = input("Do you live in apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name AND type: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal_code = input("Enter your postal code: ")

    if apartment == None:
        address = mailing_address(
            name, street_number, street_name, city, province, postal_code
        )
    else:
        address = mailing_address(
            name, street_number, street_name, city, province, postal_code, apartment
        )

    print("")
    print(address)


if __name__ == "__main__":
    main()
