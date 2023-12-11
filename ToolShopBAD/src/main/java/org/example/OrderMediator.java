package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Mediator Pattern: Concrete Mediator
class OrderMediator implements Mediator {
    private List<Observer> observers = new ArrayList<>();

    public void registerObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void mediate(String message, Object source) {
        for (Observer observer : observers) {
            if (observer != source) {
                observer.update(message);
            }
        }
    }
}