package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Builder Pattern: Director
class OrderDirector {
    private OrderBuilder orderBuilder;

    public OrderDirector(OrderBuilder orderBuilder) {
        this.orderBuilder = orderBuilder;
    }

    public void constructOrder() {
        orderBuilder.buildProductOrder("Hammer", 2);
        orderBuilder.buildProductOrder("Screwdriver", 1);
        orderBuilder.buildPaymentStrategy(new CardPayment());
    }
}
