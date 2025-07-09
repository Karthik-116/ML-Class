
def count_vowels_consonants():

    string=input('Enter your string: ')
    vowels=0
    consonants=0

    for i in string:
        if(i=='a' or i=='e'or i=='i'or i=='o'or i=='u' or i=='A' or i=='E'or i=='I'or i=='O'or i=='U'):
            vowels=vowels+1
        else:
            consonants=consonants+1

    print(f"no of vowels are= {vowels} and consonants are {consonants}")


def main():
    count_vowels_consonants()

if __name__ == "__main__":
    main()