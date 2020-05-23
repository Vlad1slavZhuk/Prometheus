# marioEasy.c

### World 1-1

В кінці рівня World 1-1 гри Super Mario Brothers компанії Nintendo, Маріо має піднятись на напівпіраміду з блоків перед тим, як стрибнути до флагштока (якщо він хоче максимізувати набрані очки). Знизу ви можете побачити скріншот з гри.

![mario](https://edx.prometheus.org.ua/assets/courseware/v1/672f3ada6590fcbbf9f9c0a86bb9089b/asset-v1:Prometheus+CS50+YCE+type@asset+block/mario.png)

Давайте відтворимо цю піраміду на С, у текстовому вигляді за допомогою хешів `#`, які будуть замість цеглин. Кожен хеш трохи вищий, ніж ширший, то ж і сама піраміда стає вищою та вужчою.

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

Наша програма буде називатись `mario`. Давайте дамо користувачеві можливість вирішити самостійно, наскільки високою має бути піраміда, спочатку запитавши в користувача ціле число від 1 до 8 включно.

Ось, як має працювати програма, якщо користувач ввів число `8`:

```c
$ ./mario
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

Ось, як має працювати програма, якщо користувач ввів число `4`:

```c
$ ./mario
Height: 4
   #
  ##
 ###
####
```

Ось, як має працювати програма, якщо користувач ввів число `2`:

```c
$ ./mario
Height: 2
 #
##
```

Ось, як має працювати програма, якщо користувач ввів число `1`:

```c
$ ./mario
Height: 1
#
```

Якщо користувач не ввів додатне ціле число від 1 до 8 включно, програма має продовжувати запитувати число, поки користувач його не введе:

```c
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #
  ##
 ###
#### 
```

# marioHard.c

### World 1-1
На початку рівня World 1-1 гри Super Mario Brothers компанії Nintendo Маріо повинен перестрибнути через дві напівпіраміди блоків на його шляху до флагштока. Знизу наведено скріншот.

![mario](https://edx.prometheus.org.ua/assets/courseware/v1/49eae914b8be8df2ad1b3518f59435a7/asset-v1:Prometheus+CS50+YCE+type@asset+block/mario-more.png)

Давайте відтворимо цю піраміду на С, подамо у тексті за допомогою хешів `#`, які будуть замість цеглин. Кожен хеш трохи вищий, ніж ширший, тож і сама піраміда стає вищою та вужчою.

```
   #  #
  ##  ##
 ###  ###
####  ####
```

Наша програма буде називатись `mario`. Давайте дамо користувачеві можливість вирішити самостійно, наскільки високою має бути піраміда, спочатку запитавши в нього чи в неї ціле число від 1 до 8 включно.

Ось, як має працювати програма, якщо користувач ввів число `8`:

```c
$ ./mario
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

А так вона буде працювати, якщо він ввів число `4`:

```c
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

Так програма працюватиме, якщо було введено число `2`:

```c
$ ./mario
Height: 2
 #  #
##  ##
```

І ось так буде працювати програма, якщо введено число `1`:

```c
$ ./mario
Height: 1
#  #
```

Якщо користувач не ввів додатне ціле число від 1 до 8 включно, програма має продовжувати запитувати число, поки користувач його не введе:

```c
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```
---