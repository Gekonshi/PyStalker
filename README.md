# Текстовая игра "СТАЛКЕР"

## Об игре

Вы играете за сталкера, который бродит по ЗОНЕ. Цель простая - выйти живым из опасной и враждебной зоны.

## Игровой мир

Мир игры представляет собой поле 10х10 клеток. В каждой клетке может находиться аномалия, аптечка или гайка. Гайки помогают обнаруживать аномалии. Если вы наступаете на аномалию, то теряете 1 жизнь. Аптечки восстанавливают одну жинь. Вы начинаете свой путь у верхнего края карты и должны дойти до нижнего края карты. Каждый ход количество анамалий увеличивается.

## Управление

Управление игрой происходит в текстовом режиме. Для вызова помощи нужно ввести команду 'h'.  
Игровые команды:  
gn - идти в направлении n;  
tn - бросить гайку в направлении n. Гайка летит на 3 клетки. Если хотя бы в одной из этих клеток есть аномалия, то игра выведет предупреждающее сообщение;  
m - использовать аптечку (Восстанавливает 1 жизнь).

Параметр 'n' может принимать следующие значения:  
w - вверх;  
a - влево;  
s - вниз;  
d - вправо.  

## TODO

В игру планируется добавить:  
- Еду;  
- Монстров;  
- Различные артефакты;  
- Новые предметы;  
- Время суток;  
- Боевую систему;  
- Более разнообразное описание локаций;  
- Текстовый интерфейс.
