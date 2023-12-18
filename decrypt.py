import tenseal as ts 
import utils

# decryption
m_proto = utils.read_data(
    "outputs/salary_encrypted_new_with_plain_calculations.txt")
context = ts.context_from(utils.read_data("keys/secret.txt"))

m = ts.lazy_ckks_vector_from(m_proto)
m.link_context(context)
print(m.decrypt())