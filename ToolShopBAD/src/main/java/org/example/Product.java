package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Observer Pattern: Concrete Subject
class Product implements Subject {
private String name;
private int stock;
private double price;
private List<Observer> observers = new ArrayList<>();

public Product(String name, int stock, double price) {
        this.name = name;
        this.stock = stock;
        this.price = price;
        }

public String getName() {
        return name;
        }

public int getStock() {
        return stock;
        }

public double getPrice() {
        return price;
        }

public void setStock(int stock) {
        this.stock = stock;
        notifyObservers("Stock updated");
        }

@Override
public void addObserver(Observer observer) {
        observers.add(observer);
        }

@Override
public void removeObserver(Observer observer) {
        observers.remove(observer);
        }

@Override
public void notifyObservers(String message) {
        for (Observer observer : observers) {
        observer.update(message);
        }
        }
        }