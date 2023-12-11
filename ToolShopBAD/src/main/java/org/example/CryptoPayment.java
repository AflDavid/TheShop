package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

class CryptoPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("Paid with cryptocurrency: $" + amount);
    }
}