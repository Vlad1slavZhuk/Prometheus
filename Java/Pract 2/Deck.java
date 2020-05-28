package com.tasks3.carddeck;

import java.util.ArrayList;
import java.util.Collections;

public class Deck {
    private ArrayList<Card> cardsList;
    
    public Deck() {
        cardsList = new ArrayList<>();

        for (int suit = 0; suit < Suit.values.length; suit++) {
            for (int rank = 0; rank < Rank.values.length; rank++) {
                cardsList.add(new Card(Rank.values[rank], Suit.values[suit]));
            }
        }
    }
    //Перемішує колоду у випадковому порядку 
    public void shuffle() {
        Collections.shuffle(cardsList);
    }
    /* * Впорядкування колоди за мастями та значеннями 
    * Порядок сотрування: 
    * Спочатку всі карти з мастю HEARTS, потім DIAMONDS, CLUBS, SPADES 
    * для кожної масті порядок наступний: Ace,King,Queen,Jack,10,9,8,7,6 
    * Наприклад 
    * HEARTS Ace 
    * HEARTS King 
    * HEARTS Queen 
    * HEARTS Jack 
    * HEARTS 10 
    * HEARTS 9 
    * HEARTS 8 
    * HEARTS 7 
    * HEARTS 6 
    * І так далі для DIAMONDS, CLUBS, SPADES */
    public void order() {
        for (int suit = 0; suit < Suit.values.length; suit++) {
            for (int rank = 0; rank < Rank.values.length; rank++) {
                cardsList.add(new Card(Rank.values[rank], Suit.values[suit]));
            }
        }
    }
    
    //Повертає true у випадку коли в колоді ще доступні карти
    public boolean hasNext() {
        return !cardsList.isEmpty();
    }
    
    //"Виймає" одну карту з колоди, коли буде видано всі 36 карт повертає null
    //Карти виймаються з "вершини" колоди. Наприклад перший виклик видасть SPADES 6 потім
    //SPADES 7, ..., CLUBS 6, ..., CLUBS Ace і так далі до HEARTS Ace
    public Card drawOne() {
        if (hasNext()) {
            return cardsList.remove(cardsList.size() - 1);
        }
        return null;
    } 
}