# ECP
Python implementation of ECP* SOAP MADES API

**ENTSO-E Energy Communication Platform (ECP) Software - https://www.entsoe.eu/data/ECP/*

# Installation

    pip install ecp-api

or

    pip install --user ecp-api

or 

    python -m pip install --user ecp-api


# Usage

### Initialise
    import ECP

    client = ECP.Client("https://ecp.elering.sise")

### Send message
    with open("message.xml", "rb") as loaded_file:
        message_ID = client.send_message("10V000000000011Q", "RIMD", loaded_file.read())

### Check message status
    status = client.check_message_status(message_ID)

### Retrieve message
    message = client.receive_message()
    
### Confirm retrieval of message
    client.confirm_received_message(message.receivedMessage.messageID)
    
### Save message on drive
*in case of excel use .xlsx and in case of PDF use .pdf and etc*

    with open("report.xml", 'wb') as report_file:
        report_file.write(message.receivedMessage.content)
        
### Save message as file like object in memory

    file_like_object = io.BytesIO(message.receivedMessage.content)

    
    
