from pet_display_mechanics import PetOutcome

class PetInfoOrganizer:

    input_pet = PetOutcome()

    print('=' * 80)
    print('                         PET INFORMATION REGISTRATION')
    print('=' * 80)

    input_name = input('Enter you pet name: ')
    input_animal_type = input('What type of animal is your pet?: ')
    input_age = int(input('How old is your pet?: '))

    input_pet.set_name(input_name)
    input_pet.set_animal_type(input_animal_type)
    input_pet.set_age(input_age)

    input_pet.pet_display_output()

if __name__ == '__main__':
    PetInfoOrganizer()