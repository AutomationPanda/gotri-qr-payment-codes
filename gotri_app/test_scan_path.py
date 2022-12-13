# --------------------------------------------------------------------------------
# Listing 4.7
# --------------------------------------------------------------------------------

# import qrcodes

# # Given the GoTri app has an invalid filepath for a QR payment code
# filepath = 'does_not_exist.png'

# # When the GoTri app attempts to scan a QR code from the invalid filepath
# try:
#     qrcodes.scan_payment_code(filepath)
#     raised = False
# except ValueError:
#     raised = True
# except:
#     raised = False

# # Then the scanning attempt raises a ValueError exception
# if raised:
#     print('PASS: Scanning a nonexistent file raises a ValueError')
# else:
#     print('FAIL: Scanning a nonexistent file raises a ValueError')


# --------------------------------------------------------------------------------
# Listing 4.9
# --------------------------------------------------------------------------------

# import qrcodes

# class TestQRCodeScanPath:

#     def run(self):

#         # Given the GoTri app has an invalid filepath for a QR payment code
#         filepath = 'does_not_exist.png'

#         # When the GoTri app attempts to scan a QR code from the invalid filepath
#         try:
#             qrcodes.scan_payment_code(filepath)
#             raised = False
#         except ValueError:
#             raised = True
#         except:
#             raised = False

#         # Then the scanning attempt raises a ValueError exception
#         if raised:
#             print('PASS: Scanning a nonexistent file raises a ValueError')
#         else:
#             print('FAIL: Scanning a nonexistent file raises a ValueError')


# --------------------------------------------------------------------------------
# Listing 4.13
# --------------------------------------------------------------------------------

import qrcodes

class TestQRCodeScanPath:

    def __init__(self):
        self.name = 'Scanning a nonexistent file raises a ValueError'

    def run(self):

        # Given the GoTri app has an invalid filepath for a QR payment code
        filepath = 'does_not_exist.png'

        # When the GoTri app attempts to scan a QR code from the invalid filepath
        try:
            qrcodes.scan_payment_code(filepath)
            raised = False
        except ValueError:
            raised = True
        except:
            raised = False

        # Then the scanning attempt raises a ValueError exception
        assert raised
