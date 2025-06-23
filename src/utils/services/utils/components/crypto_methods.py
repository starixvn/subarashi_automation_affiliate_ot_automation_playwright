import base64
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    ExtractTestCaseFailed
)

logger = get_logger(__name__)

KDF_ALGORITHM = hashes.SHA256()
KDF_LENGTH = 32
KDF_ITERATIONS = 120000

class CryptoMethods(ExtractTestCaseFailed):
    @staticmethod
    @log_exceptions(log_level="DEBUG")
    def decrypt(ciphertext, password, salt):
        try:
            validate_not_none(ciphertext, "ciphertext")
            validate_not_none(password, "password")
            validate_not_none(salt, "salt")
            
            logger.debug("Decrypting data with PBKDF2HMAC and Fernet")
            
            if isinstance(ciphertext, str):
                if ciphertext.startswith("b'") and ciphertext.endswith("'"):
                    ciphertext = eval(ciphertext)
                elif ciphertext.startswith("gAAAAAB"):
                    ciphertext = ciphertext.encode('utf-8')
                else:
                    ciphertext = ciphertext.encode('utf-8')
            
            if isinstance(salt, str):
                if salt.startswith("b'") and salt.endswith("'"):
                    salt = eval(salt)
                else:
                    salt = salt.encode('utf-8')
            
            if not isinstance(salt, bytes):
                raise TypeError(f"salt must be bytes, but is {type(salt)}")
                
            if not isinstance(ciphertext, bytes):
                raise TypeError(f"ciphertext must be bytes, but is {type(ciphertext)}")
                
            kdf = PBKDF2HMAC(
                algorithm=KDF_ALGORITHM, 
                length=KDF_LENGTH, 
                salt=salt,
                iterations=KDF_ITERATIONS
            )
            key = kdf.derive(password.encode("utf-8"))

            f = Fernet(base64.urlsafe_b64encode(key))
            plaintext = f.decrypt(ciphertext)
            
            logger.debug("Data decrypted successfully")
            return plaintext.decode("utf-8")
        except Exception as e:
            logger.error(f"Decryption failed: {str(e)}")
            raise
