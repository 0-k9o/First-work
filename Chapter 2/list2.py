invite_list = ['Nikita', 'Maksim', 'artem']
i_f_nik = f"Привет {invite_list[0]}, хотел бы приглосить тебя на обед"
i_f_mak = f"Привет {invite_list[1]}, давно не виделись, как на щет обеда?"
i_f_art = f"Привет {invite_list[2].title()}, скучно что-то пошли поедим"
print(i_f_mak)
print(i_f_art)
print(i_f_nik)
Cant = invite_list.pop(1)
print(f"\n{Cant} к сожелению не может прийти(")
invite_list.append('Egor')
print(f"\nПривет {invite_list[2]}, у меня появилось место и я бы хотел тебя приглосить на обед, еще будут {invite_list[0]} и {invite_list[1]}")
invite_list.insert(0, 'Mark')
invite_list.insert(2, 'oleg')
print("К нашему обеду присоедится еще несколько человек")
i_f_mar = f"Привет {invite_list[0]}, хотел бы приглосить тебя на обед"
i_f_ole = f"Привет {invite_list[2]}, давно не виделись, как на щет обеда?"
print(i_f_mar)
print(i_f_ole)  