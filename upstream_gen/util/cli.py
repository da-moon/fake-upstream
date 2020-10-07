#!/usr/bin/env python3

def MakeCaseAgnostic(choices):
    def find_choice(choice):
        for key, item in enumerate(choice.lower() for choice in choices):
            if choice.lower() == item:
                return choices[key]
        else:
            return choice
    return find_choice