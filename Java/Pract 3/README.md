# Sort.java

Використовуючи наведені нижче класи змініть порядок сортування на зворотній.

Наведений нижче код виводить:

```
0 1 2 3 4 5 6 10 10
```

Потрібно щоб він вивів:

```
10 10 6 5 4 3 2 1 0
```
Дозволено змінювати лише код між рядками

```java
//Change your code here

//Change your code here
```

Порівняння відбувається за допомогою класу:

```java
public class Comparator {
	public int compare(int a, int b){
		if (a>b) {
			return 1;
		} else if (a == b){
			return 0;
		} else {
			return -1;
		}
	}
}
```