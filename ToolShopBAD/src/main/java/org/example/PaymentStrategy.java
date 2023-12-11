package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Strategy Pattern: PaymentStrategy interface
interface PaymentStrategy {
    void pay(double amount);
}