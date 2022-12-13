# --------------------------------------------------------------------------------
# Listing 4.5
# --------------------------------------------------------------------------------

# import qrcodes

# # Given the GoTri app has a valid commuter ID
# commuter_id = 'a5952d78-572b-4807-9239-d67bbb6136a9'

# # And the GoTri app has a temporary security token for the commuter
# security_token = 'HKhLwmGWR975EAqqVx0sJ5HgLW87Q1uvTt5CrPI4'

# # And the GoTri app has a valid file path for saving a QR code
# filepath = 'payment_code.png'

# # When the GoTri app generates the QR payment code
# qrcodes.generate_payment_code(commuter_id, security_token, filepath)

# # Then the QR code is saved as a PNG image file to the file path
# data = qrcodes.scan_payment_code(filepath)

# # And the QR code’s data is a concatenation of the commuter ID and security token
# print('Scanned QR code data: ' + data)


# --------------------------------------------------------------------------------
# Listing 4.6
# --------------------------------------------------------------------------------

# import qrcodes

# # Given the GoTri app has a valid commuter ID
# commuter_id = 'a5952d78-572b-4807-9239-d67bbb6136a9'

# # And the GoTri app has a temporary security token for the commuter
# security_token = 'HKhLwmGWR975EAqqVx0sJ5HgLW87Q1uvTt5CrPI4'

# # And the GoTri app has a valid file path for saving a QR code
# filepath = 'payment_code.png'

# # When the GoTri app generates the QR payment code
# qrcodes.generate_payment_code(commuter_id, security_token, filepath)

# # Then the QR code is saved as a PNG image file to the file path
# data = qrcodes.scan_payment_code(filepath)
# print('Scanned QR code data: ' + data)

# # And the QR code’s data is a concatenation of the commuter ID and security token
# expected_data = commuter_id + ':' + security_token
# print('Expected QR code data: ' + expected_data)

# if data == expected_data:
#     print('PASS: Generate a QR payment code for a commuter')
# else:
#     print('FAIL: Generate a QR payment code for a commuter')


# --------------------------------------------------------------------------------
# Listing 4.8
# --------------------------------------------------------------------------------

# import qrcodes

# class TestQRCodeGeneration:

#     def run(self):

#         # Given the GoTri app has a valid commuter ID
#         commuter_id = 'a5952d78-572b-4807-9239-d67bbb6136a9'

#         # And the GoTri app has a temporary security token for the commuter
#         security_token = 'HKhLwmGWR975EAqqVx0sJ5HgLW87Q1uvTt5CrPI4'

#         # And the GoTri app has a valid file path for saving a QR code
#         filepath = 'payment_code.png'

#         # When the GoTri app generates the QR payment code
#         qrcodes.generate_payment_code(commuter_id, security_token, filepath)

#         # Then the QR code is saved as a PNG image file to the file path
#         data = qrcodes.scan_payment_code(filepath)
#         print('Scanned QR code data: ' + data)

#         # And the QR code’s data is a concatenation of the commuter ID and security token
#         expected_data = commuter_id + ':' + security_token
#         print('Expected QR code data: ' + expected_data)

#         if data == expected_data:
#             print('PASS: Generate a QR payment code for a commuter')
#         else:
#             print('FAIL: Generate a QR payment code for a commuter')


# --------------------------------------------------------------------------------
# Listing 4.12
# --------------------------------------------------------------------------------

# import qrcodes

# class TestQRCodeGeneration:

#     def __init__(self):
#         self.name = 'Generate a QR payment code for a commuter'

#     def run(self):

#         # Given the GoTri app has a valid commuter ID
#         commuter_id = 'a5952d78-572b-4807-9239-d67bbb6136a9'

#         # And the GoTri app has a temporary security token for the commuter
#         security_token = 'HKhLwmGWR975EAqqVx0sJ5HgLW87Q1uvTt5CrPI4'

#         # And the GoTri app has a valid file path for saving a QR code
#         filepath = 'payment_code.png'

#         # When the GoTri app generates the QR payment code
#         qrcodes.generate_payment_code(commuter_id, security_token, filepath)

#         # Then the QR code is saved as a PNG image file to the file path
#         data = qrcodes.scan_payment_code(filepath)
#         print('Scanned QR code data: ' + data)

#         # And the QR code’s data is a concatenation of the commuter ID and security token
#         expected_data = commuter_id + ':' + security_token
#         print('Expected QR code data: ' + expected_data)
#         assert data == expected_data


# --------------------------------------------------------------------------------
# Listing 4.15
# --------------------------------------------------------------------------------

import os
import qrcodes

class TestQRCodeGeneration:

    def __init__(self):
        self.name = 'Generate a QR payment code for a commuter'

    def delete_file(self, filepath):
        if os.path.isfile(filepath):
            os.remove(filepath)

    def setup(self):

        # Given the GoTri app has a valid commuter ID
        self.commuter_id = 'a5952d78-572b-4807-9239-d67bbb6136a9'

        # And the GoTri app has a temporary security token for the commuter
        self.security_token = 'HKhLwmGWR975EAqqVx0sJ5HgLW87Q1uvTt5CrPI4'

        # And the GoTri app has a valid file path for saving a QR code
        self.filepath = 'payment_code.png'
        self.delete_file(self.filepath)

    def run(self):

        # When the GoTri app generates the QR payment code
        qrcodes.generate_payment_code(
            self.commuter_id,
            self.security_token,
            self.filepath)

        # Then the QR code is saved as a PNG image file to the file path
        data = qrcodes.scan_payment_code(self.filepath)
        print('Scanned QR code data: ' + data)

        # And the QR code’s data is a concatenation of the commuter ID and security token 
        expected_data = self.commuter_id + ':' + self.security_token
        print('Expected QR code data: ' + expected_data)
        assert data == expected_data

    def cleanup(self):
        if hasattr(self, 'filepath'):
            self.delete_file(self.filepath)
