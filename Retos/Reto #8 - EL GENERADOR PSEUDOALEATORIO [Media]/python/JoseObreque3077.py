"""
Reto 8:

Crea un generador de números pseudoaleatorios entre 0 y 100.

No puedes usar ninguna función "random" (o semejante) del lenguaje de
programación seleccionado.
"""
from math import gcd


class RandomIntegerGenerator:
    """
    Clase que contiene diversos métodos para generar números enteros aleatorios.
    """
    def LCG(self, seed:int, multiplier:int, increment:int, modulus:int) -> int:
        """
        A Linear Congruential Generator (LCG) algorithm implementation for
        integers generation in the range 0 to 100.

        Args:
            seed (int): Initial seed value for generating random integers. Must
            be a positive integer greater than zero.
            multiplier (int): Multiplicative constant of the algorithm. Must be
            a positive integer greater than zero and prime with respect to the
            modulus.
            increment (int): Additive constant of the algorithm. Must be an
            integer greater than or equal to zero.
            modulus (int): Normalization modulus of the algorithm. Must be an
            integer greater than zero, and greater than the seed and the
            additive constant.

        Yields:
            Iterator[int]: A pseudo-random integer value generated by the LCG
            algorithm in the range 0 to 100.
        """
        non_zero_parameters = {
            'seed': seed,
            'multiplier': multiplier,
            'modulus': modulus
        }
        
        for name, value in non_zero_parameters.items():
            if not isinstance(value, int) or value <= 0:
                message = f'The {name} must be a positive non-zero integer'
                raise ValueError(message)
        
        if not isinstance(increment, int) or increment < 0:
            raise ValueError('The increment must be a positive integer')
        
        if gcd(multiplier, modulus) != 1:
            message = 'The multiplier must be prime with respect to the modulus'
            raise ValueError(message)
             
        while True:
            generated_value = (multiplier * seed + increment) % modulus
            normalized_value = generated_value / modulus
            seed = generated_value
            yield round(normalized_value * 100)
        
    def QCG(self, seed:int, multiplier:int, increment:int, modulus:int) -> int:
        """
        A Quadratic Congruential Generator (QCG) algorithm implementation for
        integers generation between 0 and 100.

        Args:
            seed (int): Initial seed value for generating random integers. Must
            be a positive integer greater than zero.
            multiplier (int): A multiplier value for the generator. Must
            be a positive integer greater than zero.
            increment (int): An increment value for the generator. Must
            be a positive integer greater than or equal to zero.
            modulus (int): A modulus value for the generator. Must be a positive integer greater than zero. The modulus must be greater than the
            seed, have no common factors with the multiplier and must have a
            quadratic residue of 1 with respect to the multiplier.

        Returns:
            int: A pseudo-random integer value generated by the QCG
            algorithm in the range 0 to 100.
        """
        if not isinstance(seed, int) or seed <= 0:
            raise ValueError('The seed must be a positive non-zero integer')
        
        if not isinstance(multiplier, int) or multiplier <= 0:
            raise ValueError('The multiplier must be a positive integer')
        
        if not isinstance(increment, int) or increment < 0:
            message = 'The increment must be a positive integer or zero'
            raise ValueError(message)
        
        if not isinstance(modulus, int) or modulus <= 0:
            raise ValueError('The modulus must be a positive non-zero integer')
        
        if gcd(modulus, multiplier) != 1:
            message = 'The modulus cannot have common factors with the multiplier'
            raise ValueError(message)
        
        legendre_symbol = pow(
            base=multiplier,
            exp=(modulus - 1) // 2,
            mod=modulus
        )
        
        if legendre_symbol != 1:
            message = ('The modulus and multiplier must satisfy the quadratic '
                       'residue requirement')
            raise ValueError(message)
        
        while True:
            generated_value = (multiplier * (seed ** 2) + increment) % modulus
            normalized_value = generated_value / modulus
            seed = generated_value
            yield round(normalized_value * 100)

if __name__ == '__main__':
    generators = RandomIntegerGenerator()
    
    lcg_generator = generators.LCG(
        seed=1234,
        multiplier=1103515245,
        increment=12348,
        modulus=2**31 - 1
    )
    
    qcg_generator = generators.QCG(
        seed=123456789,
        multiplier=9301,
        increment= 49297,
        modulus=281474976710597
    )
    
    print('LCG:')
    for _ in range(10):
        print(next(lcg_generator))
    
    print('\nQCG:')
    for _ in range(10):
        print(next(qcg_generator))
