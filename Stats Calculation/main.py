import argparse
from character import Character
import util

def initialize_argument_parser():
    parser = argparse.ArgumentParser(description='Calculate combat statistics for Rise characters')
    parser.add_argument('-c', '--character', dest='character', 
            help='the character file to load', default='brb-heavy')
    parser.add_argument('-l', '--level', dest='level',
            help='the level of the character', default=None)
    return vars(parser.parse_args())

if __name__ == "__main__":
    args = initialize_argument_parser()
    print 'character:', args['character']
    character_filename = 'data/'+args['character']+'.txt'
    #If a specific level is given, show that level
    if args['level']:
        character = Character.from_filename(character_filename,
                int(args['level']))
        print character
    #Otherwise, show all levels
    else:
        for i in xrange(1,21):
            character = Character.from_filename(character_filename, i)
            print i, util.mstr(character.attack_bonus.total()), character.avg_hit_probability(20)
