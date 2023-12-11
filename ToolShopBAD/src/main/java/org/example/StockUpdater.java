package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Observer Pattern: Concrete Observer
class StockUpdater implements Observer {
    @Override
    public void update(String message) {
        System.out.println("StockUpdater received update: " + message);
    }
}