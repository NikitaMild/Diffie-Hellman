from random import randint
import hashlib


class Diffie_Hellman():
    def __init__(self):
        self.p = 0
        self.g = 0
        self.a = 0
        self.public_key = 0
        self.session_key = 0

    @staticmethod
    def number_system_choice(simple_number, x):
        try:
            number = int(str(simple_number), x)
            return number
        except:
            return None

    @staticmethod
    def many_to_one(number):
        _ = ""
        for str in [line.replace(' ', '') for line in number.splitlines()]:
            _ += str
        return _

    def convert(self, simple_number):
        simple_number = Diffie_Hellman.many_to_one(simple_number)
        int_number = 0
        for x in range(0, 18, 2):
            int_number = Diffie_Hellman.number_system_choice(simple_number, x)
            if int_number is None:
                continue
            else:
                return int_number
        assert("Your number system is bad, please fix it")

    def random(self):
        self.a = randint(0, self.p - 1)

    def generate_value(self, base, power):
        return pow(base, power, self.p)

    def generate_public_keys(self):
        self.public_key = self.generate_value(self.g, self.a)

    def generate_session_key(self, base, power):
        session_key = self.generate_value(base, power)
        ripemd = hashlib.new('ripemd160')
        ripemd.update(str(session_key).encode('utf-8'))
        return ripemd.hexdigest()

    def run(self, p, g):
        self.p = self.convert(p)
        self.g = self.convert(g)
        self.random()
        self.generate_public_keys()
        self.session_key = self.generate_session_key(self.public_key, self.a)
        print(self.session_key)


def main():
    dh = Diffie_Hellman()
    p = """ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024
           e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd
           3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec
           6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f
           24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361
           c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552
           bb9ed529077096966d670c354e4abc9804f1746c08ca237327fff
           fffffffffffff"""
    q = "2"
    dh.run(p, q)


if __name__ == '__main__':
    main()
