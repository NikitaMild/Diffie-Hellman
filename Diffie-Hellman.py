from random import randint
import hashlib


class Diffie_Hellman():
    def __init__(self):
        self.p = 0
        self.g = 0
        self.a = 0
        self.b = 0
        self.public_key_A = 0
        self.public_key_B = 0
        self.session_key_A_b = 0
        self.session_key_B_a = 0

    @staticmethod
    def number_system_choice(simple_number, x):
        try:
            number = int(str(simple_number), x)
            return number
        except:
            return None

    def convert(self, simple_number):
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
        self.b = randint(0, self.p - 1)

    def generate_value(self, base, power):
        return (base**power) % self.p

    def generate_public_keys(self):
        self.public_key_A = self.generate_value(self.g, self.a)
        self.public_key_B = self.generate_value(self.g, self.b)

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
        self.session_key_B_a = self.generate_session_key(self.public_key_B, self.a)
        self.session_key_A_b = self.generate_session_key(self.public_key_A, self.b)
        if self.session_key_B_a == self.session_key_A_b:
            print("nice work")
        else:
            print("value1: ", value1)
            print("value2", value2)


def main():
    dh = Diffie_Hellman()
    dh.run(37, 5)


if __name__ == '__main__':
    main()
