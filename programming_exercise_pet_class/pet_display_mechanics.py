from pet_class import Pet

class PetOutcome(Pet):
    
    def __init__(self):
        super().__init__()

    def pet_display_output(self):
        print('=' * 80)
        print('                              COLLECTED PET DATA')
        print('=' * 80)

        print(f'Pet name: {input_pet.get_name()}.')
        print(f'Animal Type: {input_pet.get_animal_type()}.')
        print(f'Pet Age: {input_pet.get_age()}.')
        print('=' * 80)