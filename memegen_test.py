# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('Meme.jpg')

    # add text to the top and bottom of the meme
    meme_gen.add_text("C", 350, 670, 90, 'black')
    meme_gen.add_text("Python", 1000, 670, 90, 'black')

    # generate the meme!
    meme_gen.render()

if __name__ == '__main__':
    main()
