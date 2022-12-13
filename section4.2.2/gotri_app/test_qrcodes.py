import qrcodes

# Given the GoTri app has a valid commuter ID
commuter_id = 'a5952d78-572b-4807-9239-d67bbb6136a9'

# And the GoTri app has a temporary security token for the commuter
security_token = 'HKhLwmGWR975EAqqVx0sJ5HgLW87Q1uvTt5CrPI4'

# And the GoTri app has a valid file path for saving a QR code
filepath = 'payment_code.png'

# When the GoTri app generates the QR payment code
qrcodes.generate_payment_code(commuter_id, security_token, filepath)

# Then the QR code is saved as a PNG image file to the file path
data = qrcodes.scan_payment_code(filepath)

# And the QR code’s data is a concatenation of the commuter ID and security token
print('Scanned QR code data: ' + data)
