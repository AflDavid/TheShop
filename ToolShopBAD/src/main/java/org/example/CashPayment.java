package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

class CashPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("Paid with cash: $" + amount);
    }
}