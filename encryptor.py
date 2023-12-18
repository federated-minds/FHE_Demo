import utils
import tenseal as ts

context = ts.context_from(utils.read_data("keys/public.txt"))
salary = [10000]
salary_encrypted = ts.ckks_vector(context, salary)
utils.write_data("outputs/salary_encrypted.txt", salary_encrypted.serialize())
