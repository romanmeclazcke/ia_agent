from langchain.tools import tool

from schemas.pais import PaisInformation


@tool
def send_pais_information_message(message:PaisInformation):
    """ Allow send message with pais information content """
    print(f"Hello, here you have information about  {message.spanish_name}, have   {message.number_of_inhabitants} inhabitants, and its economy {message.economy}")