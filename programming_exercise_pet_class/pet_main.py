from pet_class import Pet

class PetInfoOrganizer:

    input_pet = Pet()

    print('PET INFORMATION REGISTRATION')

    input_name = input('Enter you pet name: ')
    input_animal_type = input('What type of animal is your pet?: ')
    input_age = int(input('How old is your pet?: '))

    input_pet.set_name(input_name)
    input_pet.set_animal_type(input_animal_type)
    input_pet.set_age(input_age)

    print('COLLECTED PET DATA')
    print(f'Pet name: {input_pet.get_name()}.')
    print(f'Animal Type: {input_pet.get_animal_type()}.')
    print(f'Pet Age: {input_pet.get_age()}.')

if __name__ == '__main__':
    PetInfoOrganizer()