from pet_display_mechanics import PetOutcome

class PetInfoOrganizer:

    input_pet = PetOutcome()

    print('=' * 80)
    print('                         PET INFORMATION REGISTRATION')
    print('=' * 80)

    input_name = input('Enter your pet name: ')
    input_animal_type = input('What type of animal is your pet?: ')

    while True:
        try:
            input_age = int(input('How old is your pet?: '))
            if input_age < 0:
                print('Error: A pet age cannot be negative. Please try again.')
                continue
            break
        except ValueError:
            print('Invalid Input. Please Enter a Number.')

    input_pet.set_name(input_name)
    input_pet.set_animal_type(input_animal_type)
    input_pet.set_age(input_age)

    input_pet.pet_display_output()

if __name__ == '__main__':
    PetInfoOrganizer()