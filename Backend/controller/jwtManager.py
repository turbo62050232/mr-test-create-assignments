import os
import json
import jwt
class jwtManagerClass:
    def decodeJWT(encoded_jwt,target):
        # saving the header claims into a variable
        # header_data = jwt.get_unverified_header(token)
        # using that variable in the decode method
        file_path_students = os.path.join('data/students.json')
        with open(file_path_students) as json_file:
            students = json.load(json_file)
        try:
            decode_jwt=jwt.decode(
                encoded_jwt,
                key='secret',
                algorithms=['HS256']
            )
            
            print(decode_jwt[target])
        except Exception as error:
            print(f"An error occurred:{error}")
            return {"error":error,"status":403}
        jwtNotFound=True
        for student in students:
            if decode_jwt["userId"]==student["userId"]:
                jwtNotFound=False
                break
        if  jwtNotFound:
            return {"error":error,"status":403}
        return {target:decode_jwt[target],"status":200}
if __name__ == '__main__':
    jwtManagerClass.decodeJWT("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50TmFtZSI6InR1cmJvIHRlbWUiLCJyb2xlIjoic3R1ZGVudCIsInVzZXJJZCI6IjEwNDg2MjQ5Mzk4MzY2NDIxMTUxNCIsInN0dWRlbnRJZCI6IjYyMDUwMjMyeGQifQ.Ixwoc3rvgvB1O9D3hw_JzegzM7P9Dvjb4odqyz06Gxo","userId")