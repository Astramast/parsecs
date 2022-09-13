from character import Character
from member import Member
from weapon import Weapon
from magazine import Magazine


head = Member('tête', 8, True)
bras = Member('bras', 12, False)
huit_balles = Magazine(5, 8, 'pistol_bullet')
huit_balles_2 = Magazine(8, 8, 'pistol_bullet')
huit_coups = Weapon("Huit-coups", False, huit_balles, 100, 'pistol', 10)
char_1 = Character("Michel", [head, bras], [huit_coups], [huit_balles_2])
print(char_1)
