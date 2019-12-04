import dog
import pack

make_a_dog = dog.Dog("Randal")
make_a_dog.print_name()
make_a_dog.print_trick_list()

dog_2 = dog.Dog("Junno")

dog_3 = dog.Dog("Kinny")

dog_4 = dog.Dog("Betty")


make_a_pack_leader = pack.Pack(make_a_dog)
print(make_a_pack_leader.get_leader_name())
