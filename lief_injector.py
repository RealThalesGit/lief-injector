import lief

lib = lief.parse("libminecraftpe.so")
lib.add_library("libpayload.so")  # adiciona libpayload.so na lista de dependências
lib.write("minecraftpe_patched.so")
