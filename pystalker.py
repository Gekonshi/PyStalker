import os, random

class world():
    def __init__(self):
        self.map=[[0 for j in range(12)] for i in range(12)]
        self.list_anomaliya=[]
        self.time=0
        for i in range(12):
            self.map[i][0]=1
            self.map[11][i]=1
            self.map[0][i]=1
            self.map[i][11]=1
        
        i=0
        while i<25:
            x=random.randint(1,10)
            y=random.randint(1,10)
            if self.map[y][x]==0:
                self.map[y][x]=2
                self.list_anomaliya.append([y,x])
                i+=1
                
        i=0
        while i<10:
            x=random.randint(1,10)
            y=random.randint(1,10)
            if self.map[y][x]==0:
                self.map[y][x]=3
                i+=1
        
        i=0
        while i<10:
            x=random.randint(1,10)
            y=random.randint(1,10)
            if self.map[y][x]==0:
                self.map[y][x]=4
                i+=1
                
        for i in range(1,10):
            self.map[1][i]=0
                
    def update(self):
        self.list_anomaliya=[]
               
        for y in range(12):
            for x in range(12):
                if self.map[y][x]==2:
                    if self.map[y-1][x]==0 or self.map[y][x+1]==0 or self.map[y+1][x]==0 or self.map[y][x-1]==0:
                        self.list_anomaliya.append([y,x])
        
        #print(self.list_anomaliya)
        
        r=random.random()
        if r<0.5:
            anomaliya=random.choice(self.list_anomaliya)
            x=anomaliya[1]
            y=anomaliya[0]
            n=[]
            if self.map[y-1][x]==0:
                n.append([y-1,x])
            elif self.map[y][x+1]==0:
                n.append([y,x+1])
            elif self.map[y+1][x]==0:
                n.append([y+1,x])
            elif self.map[y][x-1]==0:
                n.append([y,x-1])
            
            n1=random.choice(n)
            self.map[n1[0]][n1[1]]=2
                
            
    def print_map(self):
        chars={0:'.',
               1:'#',
               2:'%',
               3:'*',
               4:'&',
               5:'@'}
        s=''
        for i in self.map:
            for j in i:
                s+=chars[j]
            print(s)
            s=''
                
class player():
    def __init__(self):
        self.life=3
        self.nut=5
        self.med=1
        self.x=0
        self.y=0
        self.inventory={}
    
    def go(self,map,direction): # [y,x]
        v={'w':[-1,0],
            'a':[0,-1],
            's':[1,0],
            'd':[0,1]}
        message={0:'Всё чисто.',
                 1:'Эй, здесь граница карты!',
                 2:'Вот дерьмо! Аномалия! Вы потеряли 1 жизнь!',
                 3:'Вы нашли гайку.',
                 4:'Отлично! Вы нашли аптечку!',
                 5:'Вы здесь уже были.'}
        dir=v[direction]
        loc=map[self.y+dir[0]][self.x+dir[1]]
        print(message[loc])
        if loc!=1:
            self.x+=dir[1]
            self.y+=dir[0]
            if loc==2:
                self.life-=1
            elif loc==3:
                self.nut+=1
            elif loc==4:
                self.med+=1
        
        print('Нажмите ENTER')
        input()
        
        return [self.y,self.x]
    
    def throw(self,map,direction):
        self.nut-=1
        v={'w':[-1,0],
            'a':[0,-1],
            's':[1,0],
            'd':[0,1]}
        
        dir=v[direction]
        nut_path=[]
        nutx=self.x
        nuty=self.y
        for i in range(1,4):
            if 0<nuty+dir[0]*i<12 and 0<nutx+dir[1]*i<11:
                nut_path.append(map[nuty+dir[0]*i][nutx+dir[1]*i])
            else:
                break
        
        if 2 in nut_path:
            message='ВНИМАНИЕ! Впереди аномалия!'
            rez=False
        else:
            message='Всё чисто! Можно идти.'
            rez=True
        
        return rez, message, [nuty+dir[0]*3,nutx+dir[1]*3]
    
def game_help():
    os.system('cls')
    print('***HELP***')
    print('')
    print('Команда gn - идти в направлении n.')
    print('Команда tn - кинуть гайку в напрвлении n. Гайка летит на 3 клетки.')
    print('Команда m - применить аптечку. Восстанавливает 3 жизни.')
    print('n может принисать следующие значения:')
    print('    w - север;')
    print('    a - запад;')
    print('    s - юг;')
    print('    d - восток.')
    print('')
    print('***Легенда карты***')
    print('@ - игрок')
    print('. - пусто')
    print('# - граница карты')
    print('% - аномалия')
    print('& - аптечка')
    print('* - гайка')
    print('')
    print('Для возврата в игру нажмите ENTER.')
    input()
        
w=world()
p=player()
p.x=random.randrange(1,10)
p.y=1
w.map[p.y][p.x]=5

print('-=S.T.A.L.K.E.R=-')
print('')
print('Добро пожаловать в ЗОНУ!')
print('------------------------')
print('')
print('Для начала игры нажмите ENTER')
input()
game_loop=True
while game_loop==True:
    os.system('cls')
    #w.print_map()
    print('  Жизни: '+str(p.life))
    print('  Гайки: '+str(p.nut))
    print('Аптечки: '+str(p.med))
    print('    Ход: '+str(w.time))
    print('')
    print('Введите команду (h-помощь):')
    kom=input()
    if kom!='':
        if len(kom)>1:
            if kom[0]=='g' and kom[1] in ['w','a','s','d']:
                new_xy=p.go(w.map,kom[1])
                w.map[new_xy[0]][new_xy[1]]=5
                if new_xy[0]==10:
                    game_loop=False
                    w.print_map()
                    print('Вы вышли из ЗОНЫ!')
                    input()
                w.time+=1
            elif kom[0]=='t' and kom[1] in ['w','a','s','d']:
                if p.nut>0:
                    rez,mes,nutxy=p.throw(w.map,kom[1])
                    if rez==True:
                        w.map[nutxy[0]][nutxy[1]]=3
                    w.time+=1
                    print(mes)
                    print('Нажмите ENTER')
                    input()
                else:
                    print('Капец! Не осталось гаек!')
                    input()
        elif kom[0]=='m':
            if p.life<3:
                if p.med>0:
                    p.life+=1
                    p.med-=1
                    print('Вы чувствуете себя лучше.')
                    print('Нажмите ENTER')
                    input()
                else:
                    print('Дело плохо... Нет аптечки...')
                    print('Нажмите ENTER')
                    input()
            else:
                print('Вы чувствуете себя прекрасно! Аптечка не нужна.')
                print('Нажмите ENTER')
                input()
        elif kom[0]=='e':
            w.print_map()
            print('-=Выход=-')
            input()
            game_loop=False
        elif kom[0]=='h':
            game_help()
        else:
            print('Неправильная команда!')
            print('Нажмите ENTER')
            input()
    if p.life<=0:
        w.print_map()
        print('Вы погибли...')
        print('')
        print('Нажмите ENTER')
        input()
        game_loop=False
        
    w.update()
