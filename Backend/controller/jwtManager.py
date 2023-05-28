import os
import json
import jwt
class jwtManagerClass:
    def decodeJWT(encoded_jwt):
        # saving the header claims into a variable
        # header_data = jwt.get_unverified_header(token)
        # using that variable in the decode method
        try:
            decode_jwt=jwt.decode(
                encoded_jwt,
                key='secret',
                algorithms=['HS256']
            )
            print(decode_jwt["userId"])
        except Exception as error:
            print(f"An error occurred:{error}")
            return error,403
        
        return decode_jwt
if __name__ == '__main__':
    jwtManagerClass.decodeJWT("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50TmFtZSI6InR1cmJvIHRlbWUiLCJyb2xlIjoic3R1ZGVudCIsInVzZXJJZCI6IjEwNDg2MjQ5Mzk4MzY2NDIxMTUxNCIsInN0dWRlbnRJZCI6IjYyMDUwMjMyeGQifQ.Ixwoc3rvgvB1O9D3hw_JzegzM7P9Dvjb4odqyz06Gxo")