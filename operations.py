import tenseal as ts
import utils

context = ts.context_from(utils.read_data("keys/public.txt"))

salary_proto = utils.read_data("outputs/salary_encrypted.txt")
salary_encrypted = ts.lazy_ckks_vector_from(salary_proto)
salary_encrypted.link_context(context)
# wage * 1.2 +600
wage_increase_rate_plain = ts.plain_tensor([1.2])
bonus_increase_rate_plain = ts.plain_tensor([600])

salary_new_encrypted=(salary_encrypted * wage_increase_rate_plain) + bonus_increase_rate_plain
utils.write_data("outputs/salary_encrypted_new_with_plain_calculations.txt",salary_new_encrypted.serialize())
