import pandas
import random
from functools import reduce


class Anonymize:

    def __init__(self):
        pass

    def hashval(self, word, size):
        """ Returns an integer

        This function calculates the hash value 
        given the word and the max value of the
        possible hash
        """
        # The hash is calculated by adding the ascii values 
        # of the alphabets. The modulo of the number is done 
        # with respect to the max value.
        calc_hash = reduce(lambda x, y: x + ord(y), word, 0)
        return (calc_hash % size)
    
    def hash_anonymize(self, fname = "", lname = ""):
        """ Returns a tuple of randomized names

        This function takes in either two or one input names
        and calculates the hash value of whatever is passed
        then returns a randomized name based on the calculated 
        hash value.
        """
        # Reads the csv file containing the top 100 first and last names
        names = pandas.read_csv("./Names_List.csv", header=0)
        random_fname = random_lname = None
        if len(fname) != 0:
            # Calculates the hash value for the first name if passed
            f = self.hashval(fname.lower(), 200)
            # Assigns the name corresponding to the calculated hash value
            # from the csv file
            random_fname = names.at[f, "first_name"]
        if len(lname) != 0:
            # Calculates the hash value for the last name if passed
            l = self.hashval(lname.lower(), 100)
            # Assigns the name corresponding to the calculated hash value
            # from the csv file
            random_lname = names.at[l, "last_name"]
        if random_fname is None:
            return random_lname.lower()
        if random_lname is None:
            return random_fname.lower()
        return random_fname.lower(), random_lname.lower()


if __name__ == "__main__":
    # Executes the code on a few random names
    a = Anonymize()
    print(a.hash_anonymize(fname="Oliver"))
    print(a.hash_anonymize(lname="Carter"))
    print(a.hash_anonymize("Oliver", "Carter"))
    print(a.hash_anonymize("Elijah", "Perez"))
    print(a.hash_anonymize("Michael", "kenway"))
    print(a.hash_anonymize("Katie", "murphy"))
    print(a.hash_anonymize("joe", "Hayden"))
