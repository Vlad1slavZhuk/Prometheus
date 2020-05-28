# LinkedList.java

Створіть клас що описує зв'язний список. Клас повинен мати можливість додавання елементів та вилучення елементів. Додавання елементів відбувається в кінець списку, вилучення елементів відбувається за порядковим номером.Також створіть методи, що дозволяють отримати розмір списку та елемент за його порядковим номером.

Елементи списку повинні бути типу `Node`.

Просимо врахувати деякі особливості перевірки завдань:

1. Декларація package повинна залишатися незмінною (як у шаблоні), зверніть на це увагу вставляючи Ваш код у вікно перевірки.
2. Для перевірки використовуються (беруться до уваги) виключно методи з сигнатурою описаною в шаблоні.
3. Кількість та зміст полів та/або методів відмінних від наведених в шаблоні не обмежена.
4. В кожному класі повинен бути або конструктор за замовчанням або public безаргументний конструктор.
5. Не рекомендовано робити вивід на екран.

```java
class Node{
	private Node next;
	private Integer data;
	
	public Node() {
	}

	public Node getNext() {
		return next;
	}
	public void setNext(Node next) {
		this.next = next;
	}
	public Integer getData() {
		return data;
	}
	public void setData(Integer data) {
		this.data = data;
	}
}
```

Клас списку повинен мати наступну структуру:

```java
public class LinkedList {
/* Конструктор без аргументів */
    public LinkedList() {}
/* Додати елемент в кінець списку */
    public void add(Integer data) {}
/* Отримати елемент по індексу, повертає null якщо такий елемент недоступний */
    public Integer get(int index) {}
/* Вилучення елементу за індексом, повертає true у разі успіху або false в іншому випадку */
    public boolean delete(int index) {}
/*Поверта розмір списку: якщо елементів в списку нема то повертає 0 (нуль)*/
    public int size() {}
}
```
**ЗВЕРНІТЬ УВАГУ**: елементи списку повинні мати номери починаючи з нуля!

# Deck.java

Створіть класи для зберігання колоди з 36 карт (детальніше про колоду 36 карт [Побачити](https://en.wikipedia.org/wiki/Russian_playing_cards)). Використовуйте класи заготовки

Просимо врахувати деякі особливості перевірки завдань:

1. Декларація `package` повинна залишатися незмінною (як у шаблоні), зверніть на це увагу вставляючи Ваш код у вікно перевірки.
2. Для перевірки використовуються (беруться до уваги) виключно методи з сигнатурою описаною в шаблоні.
3. Кількість та зміст полів та/або методів відмінних від наведених в шаблоні не обмежена.
4. В кожному класі повинен бути або конструктор за замовчанням або `public` безаргументний конструктор.
5. Не рекомендовано робити вивід на екран.

`Card.java`

```java
package com.tasks3.carddeck;

public class Card {
	private Rank rank;
	private Suit suit;

	public Card(Rank rank, Suit suit) {
		this.rank = rank;
		this.suit = suit;
	}

	public Rank getRank() {
		return rank;
	}

	public void setRank(Rank rank) {
		this.rank = rank;
	}

	public Suit getSuit() {
		return suit;
	}

	public void setSuit(Suit suit) {
		this.suit = suit;
	}
}
```

`Rank.java`

```java
package com.tasks3.carddeck;

public class Rank {
	public static final Rank ACE = new Rank("Ace");
	public static final Rank KING = new Rank("King");
	public static final Rank QUEEN = new Rank("Queen");
	public static final Rank JACK = new Rank("Jack");
	public static final Rank TEN = new Rank("10");
	public static final Rank NINE = new Rank("9");
	public static final Rank EIGHT = new Rank("8");
	public static final Rank SEVEN = new Rank("7");
	public static final Rank SIX = new Rank("6");

	public static Rank[] values = { ACE, KING, QUEEN, JACK, TEN, NINE, EIGHT, SEVEN, SIX };

	private String name;

	Rank(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}
}
```

`Suit.java`

```java
package com.tasks3.carddeck;

public class Suit {
	public static final Suit HEARTS = new Suit("HEARTS");
	public static final Suit DIAMONDS = new Suit("DIAMONDS");
	public static final Suit CLUBS = new Suit("CLUBS");
	public static final Suit SPADES = new Suit("SPADES");
	
	public static Suit[] values = { HEARTS, DIAMONDS, CLUBS, SPADES};
	
	private String name;

	Suit(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}
}
```

# Fibonacci.java

Використовуючи рекурсію, виведіть на екран задане по порядковому номеру число Фібоначі. Для вирішення завдання використовуйте шаблон:

Просимо врахувати деякі особливості перевірки завдань:

1. Декларація `package` повинна залишатися незмінною (як у шаблоні), зверніть на це увагу вставляючи Ваш код у вікно перевірки.
2. Для перевірки використовуються (беруться до уваги) виключно методи з сигнатурою описаною в шаблоні.
3. Кількість та зміст полів та/або методів відмінних від наведених в шаблоні не обмежена.
4. В кожному класі повинен бути або конструктор за замовчанням або `public` безаргументний конструктор.

```java
package com.tasks3.fibonacci;

public class Fibonacci
{
    //Повертає число Фібоначчі за номером, нумерація почнеться з одиниці
    //якщо число не можливо вирахувати поверніть -1
    public long getNumber(int position){
    }
}
```