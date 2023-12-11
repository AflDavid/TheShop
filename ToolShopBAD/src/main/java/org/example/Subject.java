package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Observer Pattern: Subject interface
interface Subject {
    void addObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers(String message);
}