package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

class LoanPayment implements PaymentStrategy {
    private int months;

    public LoanPayment(int months) {
        this.months = months;
    }

    @Override
    public void pay(double amount) {
        double monthlyPayment = amount / months;
        System.out.println("Paid with a loan in " + months + " monthly installments of $" + monthlyPayment);
    }
}