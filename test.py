from character import Character
from member import Member
from weapon import Weapon
from magazine import Magazine


bras = Member('tête', 8, True)
huit_balles = Magazine(5, 8, 'pistol_bullet')
huit_balles_2 = Magazine(8, 8, 'pistol_bullet')
huit_coups = Weapon("Huit-coups", False, huit_balles, 100, 'pistol', 10)
char_1 = Character("Michel", [bras], [huit_coups], [huit_balles_2])
print(char_1)