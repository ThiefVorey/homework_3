def catname(self):
    print("Позывной котенка:")
    cat=input()
def kitty(self, cat):
    print('Состояние котенка ',cat,':')
    health=input()
    return health
def location(self,cat, health):
    print('Местоположение котенка ',cat,' с состоянием ', health,':')
    place=input()
def volunteer(self):
    print("Ветеринар:")
    who=input()
    return who
def cure(self, who, cat, health, place ):
    print('Ветеринар ', who,' лечит котенка ',cat,' с состоянием здоровья ',health,' в месте ',place, '.')
    pass
def result(self):
    print('Котенок здоров!')
    pass

