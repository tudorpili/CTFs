import base64

encoded_string = "RUNTQ3tEQUM1NTM1MDBCNjBCRjcwMEY1NkU0NTY5MjIxMDRGQTA2QkMxNDQyMTNFRDJCNThCRUMyNDI5RjAxNTI0MkRCfQ=="
decoded_string = base64.b64decode(encoded_string).decode('utf-8')

print(decoded_string)