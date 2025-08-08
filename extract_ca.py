from cryptography import x509
from cryptography.hazmat.backends import default_backend

def extract_root_ca(cert_data):
    # Load the X.509 certificate
    cert = x509.load_pem_x509_certificate(cert_data, default_backend())

    # Extract the root CA
    root_ca = cert.issuer

    return root_ca

def add_root_ca_to_chain(cert_chain, root_ca):
    # Add the root CA to the certificate chain
    new_chain = [root_ca] + cert_chain

    return new_chain

# Example usage:
# Assuming you have a PEM-formatted certificate in cert_data
cert_data = b"-----BEGIN CERTIFICATE-----\nMIIC...your certificate data...-----END CERTIFICATE-----"

# Extract the root CA
root_ca = extract_root_ca(cert_data)

# Example certificate chain (list of certificates)
cert_chain = [cert1, cert2, cert3]  # Replace with your actual certificate chain

# Add the root CA to the certificate chain
new_cert_chain = add_root_ca_to_chain(cert_chain, root_ca)

# Print the new certificate chain
for cert in new_cert_chain:
    print(cert.public_bytes(serialization.Encoding.PEM).decode())
