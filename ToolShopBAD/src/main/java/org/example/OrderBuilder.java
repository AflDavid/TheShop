package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Builder Pattern: Builder interface
interface OrderBuilder {
    void buildProductOrder(String productName, int quantity);
    void buildPaymentStrategy(PaymentStrategy paymentStrategy);
}